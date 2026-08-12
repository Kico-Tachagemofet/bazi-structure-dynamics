#!/usr/bin/env python3
"""Validate Bazi coverage receipts and invisible report markers."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


STATUSES = {"primary", "supporting", "cross-ref", "not-applicable", "source-gap"}
ROLES = {"formation", "advantage", "cost", "result-gate", "switch", "verification"}
MARKER = re.compile(r"<!--\s*coverage_id:\s*([^\s>]+)\s*-->")


def _nonempty(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _list(value: Any) -> bool:
    return isinstance(value, list) and bool(value) and all(_nonempty(item) for item in value)


def validate(coverage: dict[str, Any], report: str, receipt: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    for label, payload, list_key in (
        ("coverage-receipt", coverage, "coverage_items"),
        ("coverage-render-receipt", receipt, "coverage_render_receipts"),
    ):
        if str(payload.get("schema_version")) != "1.0":
            errors.append(f"{label}: schema_version must be 1.0")
        if not _nonempty(payload.get("case_id")):
            errors.append(f"{label}: case_id is required")
        if not isinstance(payload.get(list_key), list) or not payload.get(list_key):
            errors.append(f"{label}: {list_key} must be a non-empty list")
    if errors:
        return errors

    item_by_id: dict[str, dict[str, Any]] = {}
    for index, item in enumerate(coverage["coverage_items"]):
        label = f"coverage_items[{index}]"
        if not isinstance(item, dict):
            errors.append(f"{label}: must be an object")
            continue
        required = {"coverage_id", "topic_id", "facet_id", "coverage_status", "render_obligation_id"}
        missing = required - set(item)
        if missing:
            errors.append(f"{label}: missing {', '.join(sorted(missing))}")
            continue
        coverage_id = item.get("coverage_id")
        if not _nonempty(coverage_id) or coverage_id in item_by_id:
            errors.append(f"{label}.coverage_id: must be non-empty and unique")
            continue
        item_by_id[coverage_id] = item
        status = item.get("coverage_status")
        if status not in STATUSES:
            errors.append(f"{label}.coverage_status: invalid")
        if status in {"primary", "supporting", "cross-ref"}:
            for key in ("scene_kernel_refs", "finding_refs", "claim_refs"):
                if not _list(item.get(key)):
                    errors.append(f"{label}.{key}: cannot be empty for {status}")
            if not _nonempty(item.get("domain_specific_delta")):
                errors.append(f"{label}.domain_specific_delta: required for {status}")
            roles = item.get("explanatory_roles")
            if not isinstance(roles, dict) or set(roles) != ROLES or any(roles.get(role) is not True for role in ROLES):
                errors.append(f"{label}.explanatory_roles: all six roles must be true")
        elif not _nonempty(item.get("gap_or_na_reason")):
            errors.append(f"{label}.gap_or_na_reason: required for {status}")

    marker_counts: dict[str, int] = {}
    for match in MARKER.finditer(report):
        marker_counts[match.group(1)] = marker_counts.get(match.group(1), 0) + 1
    unknown_markers = set(marker_counts) - set(item_by_id)
    if unknown_markers:
        errors.append(f"report: unknown coverage markers {sorted(unknown_markers)}")

    receipt_by_id: dict[str, dict[str, Any]] = {}
    for index, item in enumerate(receipt["coverage_render_receipts"]):
        label = f"coverage_render_receipts[{index}]"
        if not isinstance(item, dict):
            errors.append(f"{label}: must be an object")
            continue
        required = {"coverage_id", "render_obligation_id", "marker_count", "body_ref", "coverage_present", "audit_status"}
        missing = required - set(item)
        if missing:
            errors.append(f"{label}: missing {', '.join(sorted(missing))}")
            continue
        coverage_id = item.get("coverage_id")
        if not _nonempty(coverage_id) or coverage_id in receipt_by_id:
            errors.append(f"{label}.coverage_id: must be non-empty and unique")
            continue
        receipt_by_id[coverage_id] = item
        if item.get("audit_status") != "pending-independent-audit":
            errors.append(f"{label}.audit_status: producer cannot self-pass")
        if item.get("coverage_present") is not True:
            errors.append(f"{label}.coverage_present: must be true before audit")

    if set(item_by_id) != set(receipt_by_id):
        errors.append("coverage IDs in composition and render receipts must match exactly")
    for coverage_id, source in item_by_id.items():
        rendered = receipt_by_id.get(coverage_id)
        if not rendered:
            continue
        count = marker_counts.get(coverage_id, 0)
        if count != 1 or rendered.get("marker_count") != 1:
            errors.append(f"{coverage_id}: report and receipt marker_count must both equal 1")
        if rendered.get("render_obligation_id") != source.get("render_obligation_id"):
            errors.append(f"{coverage_id}: render obligation drift")
        if not _nonempty(rendered.get("body_ref")):
            errors.append(f"{coverage_id}: body_ref cannot be empty")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("coverage", type=Path)
    parser.add_argument("report", type=Path)
    parser.add_argument("render_receipt", type=Path)
    args = parser.parse_args()
    try:
        coverage = json.loads(args.coverage.read_text(encoding="utf-8"))
        report = args.report.read_text(encoding="utf-8")
        receipt = json.loads(args.render_receipt.read_text(encoding="utf-8"))
        errors = validate(coverage, report, receipt)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(json.dumps({"status": "FAIL", "errors": [str(exc)]}, ensure_ascii=False, indent=2))
        return 2
    print(json.dumps({"status": "PASS" if not errors else "FAIL", "errors": errors}, ensure_ascii=False, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
