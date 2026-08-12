#!/usr/bin/env python3
"""Self-test audit verdict and propagation rules."""

from __future__ import annotations

from copy import deepcopy

from validate_audit_state import validate_state


def base_state():
    return {
        "schema_version": "2.0",
        "audit_id": "AUD-ROOT",
        "audit_report_ref": "audit-report.md",
        "stage": "structure",
        "verdict": "PASS",
        "findings": [],
        "repair_propagations": [],
        "summary": {"blocker_total": 0, "blocker_open": 0, "warning_total": 0, "warning_open": 0},
    }


def main() -> None:
    assert validate_state(base_state()) == []

    broken = base_state()
    broken["findings"] = [{
        "audit_id": "AUD-11",
        "severity": "BLOCKER",
        "pattern_id": "TOPIC_STAR_FORCED",
        "status": "resolved",
        "affected_artifacts": ["topic-lens.json"],
        "evidence_refs": ["topic-lens.json#centers"],
        "repair_stage": "topic",
        "repair_type": "patch",
        "verdict_direction_changed": True,
        "discovered_by": "user",
        "downstream_impacted": ["topic-findings/creation.md"],
        "propagation_id": None,
    }]
    broken["summary"] = {"blocker_total": 1, "blocker_open": 0, "warning_total": 0, "warning_open": 0}
    errors = validate_state(broken)
    assert any("direction-changing repair must be re-derive" in error for error in errors)
    assert any("needs complete propagation" in error for error in errors)

    repaired = deepcopy(broken)
    repaired["findings"][0]["repair_type"] = "re-derive"
    repaired["findings"][0]["propagation_id"] = "PROP-1"
    repaired["repair_propagations"] = [{
        "propagation_id": "PROP-1",
        "trigger_audit_id": "AUD-11",
        "status": "complete",
        "rerun_from_stage": "topic",
        "required_artifacts": ["topic-findings/creation.md"],
        "rerun_artifacts": ["topic-findings/creation.md"],
        "recheck_refs": ["finding-audit.md"],
    }]
    assert validate_state(repaired) == []

    render_state = base_state()
    render_state.update({
        "schema_version": "2.1",
        "stage": "render",
        "evidence_scan_ref": "delivery-evidence-scan.json",
    })
    assert validate_state(render_state, evidence_scan={"verdict": "PASS"}) == []
    errors = validate_state(render_state, evidence_scan={"verdict": "FAIL"})
    assert any("cannot pass" in error for error in errors)
    missing_ref = deepcopy(render_state)
    missing_ref.pop("evidence_scan_ref")
    assert any("requires evidence_scan_ref" in error for error in validate_state(missing_ref))
    print("PASS: audit state computes verdict, requires propagation, and cannot overrule failed evidence scan")


if __name__ == "__main__":
    main()
