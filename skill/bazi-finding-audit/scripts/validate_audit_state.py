#!/usr/bin/env python3
"""Validate canonical Bazi audit state and repair propagation."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


STAGES = {"structure", "topic", "finding", "composition", "render", "timing", "synastry", "validation"}
SEVERITIES = {"BLOCKER", "WARNING"}
STATUSES = {"open", "resolved"}
REPAIR_TYPES = {"patch", "re-derive"}
DISCOVERED_BY = {"self-audit", "user", "downstream-stage"}


def computed_summary(findings: list[dict[str, Any]]) -> dict[str, int]:
    return {
        "blocker_total": sum(item.get("severity") == "BLOCKER" for item in findings),
        "blocker_open": sum(item.get("severity") == "BLOCKER" and item.get("status") == "open" for item in findings),
        "warning_total": sum(item.get("severity") == "WARNING" for item in findings),
        "warning_open": sum(item.get("severity") == "WARNING" and item.get("status") == "open" for item in findings),
    }


def computed_verdict(summary: dict[str, int]) -> str:
    if summary["blocker_open"]:
        return "FAIL"
    if summary["warning_open"]:
        return "PASS_WITH_WARNINGS"
    return "PASS"


def validate_state(
    payload: dict[str, Any],
    audit_report: Path | None = None,
    evidence_scan: dict[str, Any] | None = None,
    evidence_scan_path: Path | None = None,
) -> list[str]:
    errors: list[str] = []
    required = {"schema_version", "audit_id", "audit_report_ref", "stage", "verdict", "findings", "repair_propagations", "summary"}
    missing = sorted(required - set(payload))
    if missing:
        return [f"audit state missing {', '.join(missing)}"]
    if payload["schema_version"] not in {"2.0", "2.1"}:
        errors.append("audit state schema_version must be 2.0 or 2.1")
    if payload["stage"] not in STAGES:
        errors.append("audit state has invalid stage")
    if audit_report is not None and Path(payload["audit_report_ref"]).name != audit_report.name:
        errors.append("audit_report_ref does not match the supplied audit report")
    evidence_required = payload["schema_version"] == "2.1" and payload["stage"] in {"finding", "composition", "render"}
    if evidence_required and not payload.get("evidence_scan_ref"):
        errors.append("audit state v2.1 finding/composition/render stage requires evidence_scan_ref")
    if evidence_scan_path is not None:
        if Path(payload.get("evidence_scan_ref", "")).name != evidence_scan_path.name:
            errors.append("evidence_scan_ref does not match the supplied evidence scan")
    if evidence_scan is not None:
        scan_verdict = evidence_scan.get("verdict")
        if scan_verdict not in {"PASS", "PASS_WITH_WARNINGS", "FAIL"}:
            errors.append("evidence scan has invalid verdict")
        elif scan_verdict == "FAIL" and payload.get("verdict") != "FAIL":
            errors.append("audit state cannot pass while independent evidence scan fails")

    findings = payload["findings"]
    if not isinstance(findings, list):
        return errors + ["findings must be a list"]
    finding_ids: set[str] = set()
    propagation_by_id: dict[str, dict[str, Any]] = {}
    for propagation in payload["repair_propagations"]:
        if not isinstance(propagation, dict):
            errors.append("repair propagation must be an object")
            continue
        needed = {"propagation_id", "trigger_audit_id", "status", "rerun_from_stage", "required_artifacts", "rerun_artifacts", "recheck_refs"}
        if not needed.issubset(propagation):
            errors.append("repair propagation is incomplete")
            continue
        propagation_id = propagation["propagation_id"]
        if propagation_id in propagation_by_id:
            errors.append(f"duplicate propagation_id {propagation_id}")
        propagation_by_id[propagation_id] = propagation
        if propagation["status"] not in {"pending", "complete"}:
            errors.append(f"{propagation_id}: invalid propagation status")
        if propagation["status"] == "complete":
            missing_reruns = set(propagation["required_artifacts"]) - set(propagation["rerun_artifacts"])
            if missing_reruns:
                errors.append(f"{propagation_id}: complete propagation missing reruns {sorted(missing_reruns)}")

    finding_required = {
        "audit_id", "severity", "pattern_id", "status", "affected_artifacts", "evidence_refs",
        "repair_stage", "repair_type", "verdict_direction_changed", "discovered_by",
        "downstream_impacted", "propagation_id",
    }
    for finding in findings:
        if not isinstance(finding, dict):
            errors.append("finding must be an object")
            continue
        missing = sorted(finding_required - set(finding))
        if missing:
            errors.append(f"finding missing {', '.join(missing)}")
            continue
        audit_id = finding["audit_id"]
        if audit_id in finding_ids:
            errors.append(f"duplicate audit_id {audit_id}")
        finding_ids.add(audit_id)
        if finding["severity"] not in SEVERITIES:
            errors.append(f"{audit_id}: invalid severity")
        if finding["status"] not in STATUSES:
            errors.append(f"{audit_id}: invalid status")
        if finding["repair_type"] not in REPAIR_TYPES:
            errors.append(f"{audit_id}: invalid repair_type")
        if finding["discovered_by"] not in DISCOVERED_BY:
            errors.append(f"{audit_id}: invalid discovered_by")
        if finding["verdict_direction_changed"] and finding["repair_type"] != "re-derive":
            errors.append(f"{audit_id}: direction-changing repair must be re-derive, not patch")
        if finding["status"] == "resolved" and finding["verdict_direction_changed"]:
            propagation_id = finding["propagation_id"]
            propagation = propagation_by_id.get(propagation_id)
            if not propagation or propagation.get("status") != "complete":
                errors.append(f"{audit_id}: resolved direction change needs complete propagation")
            else:
                impacted = set(finding["downstream_impacted"])
                rerun = set(propagation["rerun_artifacts"])
                if not impacted.issubset(rerun):
                    errors.append(f"{audit_id}: propagation did not rerun all downstream impacted artifacts")
        if finding["status"] == "open" and finding["propagation_id"] is not None:
            errors.append(f"{audit_id}: open finding cannot claim completed propagation")

    summary = computed_summary(findings)
    if payload["summary"] != summary:
        errors.append(f"audit summary mismatch; computed={summary}")
    verdict = computed_verdict(summary)
    if payload["verdict"] != verdict:
        errors.append(f"audit verdict mismatch; computed={verdict}")
    return errors


def load_and_validate(
    path: Path,
    audit_report: Path | None = None,
    evidence_scan_path: Path | None = None,
) -> tuple[dict[str, Any] | None, list[str]]:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return None, [f"audit state unreadable: {exc}"]
    evidence_scan: dict[str, Any] | None = None
    if evidence_scan_path is not None:
        try:
            evidence_scan = json.loads(evidence_scan_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            return payload, [f"evidence scan unreadable: {exc}"]
    return payload, validate_state(payload, audit_report, evidence_scan, evidence_scan_path)


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate canonical Bazi audit state.")
    parser.add_argument("audit_state")
    parser.add_argument("--audit-report")
    parser.add_argument("--evidence-scan")
    args = parser.parse_args()
    report = Path(args.audit_report).resolve() if args.audit_report else None
    evidence = Path(args.evidence_scan).resolve() if args.evidence_scan else None
    _, errors = load_and_validate(Path(args.audit_state), report, evidence)
    result = {"verdict": "PASS" if not errors else "FAIL", "errors": errors}
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
