#!/usr/bin/env python3
"""Create a SHA-256 receipt for an audited Bazi structure stage."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

from validate_audit_state import load_and_validate


REQUIRED = {
    "case-manifest": ("reader/case-manifest.yaml", "case-manifest.yaml"),
    "chart-stage1": ("reader/chart-stage1.yaml", "chart-stage1.yaml"),
    "chart-stage1-audit": ("reader/chart-stage1-audit.md", "chart-stage1-audit.md"),
    "source-packet": ("source/structure/source-packet-structure.md", "source-packet.md"),
    "node-ledger": ("structure/node-ledger.yaml", "node-ledger.yaml"),
    "interaction-census": ("structure/interaction-census.yaml", "interaction-census.yaml"),
    "branch-relation-census": ("structure/branch-relation-census.yaml", "branch-relation-census.yaml"),
    "branch-state": ("structure/branch-state.md", "branch-state.md"),
    "post-branch-node-ledger": ("structure/post-branch-node-ledger.yaml", "post-branch-node-ledger.yaml"),
    "qualified-edge-map": ("structure/qualified-edge-map.yaml", "qualified-edge-map.yaml"),
    "system-state": ("structure/system-state.md", "system-state.md"),
    "problem-state": ("structure/problem-state.yaml", "problem-state.yaml"),
    "pattern-candidates": ("structure/pattern-candidates.md", "pattern-candidates.md"),
    "route-candidates": ("structure/route-candidates.yaml", "route-candidates.yaml"),
    "route-edge-endpoint-map": ("structure/route-edge-endpoint-map.yaml", "route-edge-endpoint-map.yaml"),
    "conditions-matrix": ("structure/conditions-matrix.md", "conditions-matrix.md"),
    "structure-kernel": ("structure/structure-kernel.md", "structure-kernel.md"),
    "use-kernel": ("structure/use-kernel.md", "use-kernel.md"),
    "structure-process-handoff": ("structure/structure-process-handoff.yaml",),
}


def resolve_required(case_dir: Path) -> tuple[dict[str, Path], list[str]]:
    """Resolve the current staged layout first, then the legacy flat layout."""
    resolved: dict[str, Path] = {}
    missing: list[str] = []
    for logical_name, candidates in REQUIRED.items():
        match = next((case_dir / rel for rel in candidates if (case_dir / rel).is_file()), None)
        if match is None:
            missing.append(f"{logical_name}: one of {list(candidates)}")
        else:
            resolved[logical_name] = match
    return resolved, missing


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def declared_schema_version(path: Path) -> str | None:
    text = path.read_text(encoding="utf-8", errors="replace")[:4096]
    if path.suffix.lower() == ".json":
        try:
            payload = json.loads(path.read_text(encoding="utf-8"))
            version = payload.get("schema_version") if isinstance(payload, dict) else None
            return str(version) if version is not None else None
        except json.JSONDecodeError:
            return None
    match = re.search(r'^schema_version:\s*["\']?([^"\'\r\n]+)', text, re.MULTILINE)
    return match.group(1).strip() if match else None


def declared_case_id(path: Path, fallback: str) -> str:
    text = path.read_text(encoding="utf-8", errors="replace")[:4096]
    match = re.search(r'^case_id:\s*["\']?([^"\'\r\n]+)', text, re.MULTILINE)
    return match.group(1).strip() if match else fallback


def main() -> int:
    parser = argparse.ArgumentParser(description="Freeze audited Bazi structure artifacts.")
    parser.add_argument("case_dir")
    parser.add_argument("--audit-report", required=True)
    parser.add_argument("--audit-state", required=True)
    parser.add_argument("--freeze-id", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    case_dir = Path(args.case_dir).resolve()
    audit = Path(args.audit_report).resolve()
    audit_state = Path(args.audit_state).resolve()
    resolved, missing = resolve_required(case_dir)
    if not audit.is_file():
        missing.append(str(audit))
    if not audit_state.is_file():
        missing.append(str(audit_state))
    if missing:
        print(json.dumps({"verdict": "FAIL", "missing": missing}, ensure_ascii=False, indent=2))
        return 1

    audit_payload, audit_errors = load_and_validate(audit_state, audit)
    if audit_errors:
        print(json.dumps({"verdict": "FAIL", "audit_state_errors": audit_errors}, ensure_ascii=False, indent=2))
        return 1
    assert audit_payload is not None
    if audit_payload["stage"] != "structure":
        print(json.dumps({"verdict": "FAIL", "audit_state_errors": ["freeze requires stage=structure"]}, ensure_ascii=False, indent=2))
        return 1
    if audit_payload["verdict"] not in {"PASS", "PASS_WITH_WARNINGS"}:
        print(json.dumps({"verdict": "FAIL", "audit_state_errors": ["audit state is not freeze-eligible"]}, ensure_ascii=False, indent=2))
        return 1

    files = []
    for logical_name, path in resolved.items():
        files.append(
            {
                "logical_name": logical_name,
                "path": path.relative_to(case_dir).as_posix(),
                "sha256": digest(path),
                "schema_version": declared_schema_version(path),
                "modified_utc": datetime.fromtimestamp(path.stat().st_mtime, timezone.utc).isoformat(),
            }
        )
    files.append(
        {
            "path": str(audit),
            "sha256": digest(audit),
            "schema_version": declared_schema_version(audit),
            "modified_utc": datetime.fromtimestamp(audit.stat().st_mtime, timezone.utc).isoformat(),
        }
    )
    files.append(
        {
            "path": str(audit_state),
            "sha256": digest(audit_state),
            "schema_version": declared_schema_version(audit_state),
            "modified_utc": datetime.fromtimestamp(audit_state.stat().st_mtime, timezone.utc).isoformat(),
        }
    )
    receipt = {
        "schema_version": "2.0",
        "freeze_id": args.freeze_id,
        "case_id": declared_case_id(resolved["case-manifest"], case_dir.name),
        "audit_state_id": audit_payload["audit_id"],
        "audit_report_id": audit_payload["audit_report_ref"],
        "audit_verdict": audit_payload["verdict"],
        "created_at": datetime.now(timezone.utc).isoformat(),
        "commander_fact_ref": resolved["chart-stage1"].relative_to(case_dir).as_posix() + "#chart.month_command",
        "problem_state_ref": resolved["problem-state"].relative_to(case_dir).as_posix(),
        "edge_map_ref": resolved["qualified-edge-map"].relative_to(case_dir).as_posix(),
        "route_map_ref": resolved["route-candidates"].relative_to(case_dir).as_posix(),
        "use_kernel_ref": resolved["use-kernel"].relative_to(case_dir).as_posix(),
        "process_handoff_ref": resolved["structure-process-handoff"].relative_to(case_dir).as_posix(),
        "files": files,
        "invalidates_when": "Any listed file hash changes, audit state changes, or an active downstream artifact references another freeze.",
    }
    output = Path(args.output)
    output.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"verdict": "PASS", "output": str(output), "file_count": len(files)}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
