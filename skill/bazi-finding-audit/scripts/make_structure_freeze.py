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


REQUIRED = [
    "case-manifest.yaml",
    "chart-stage1.yaml",
    "chart-stage1-audit.md",
    "source-packet.md",
    "node-ledger.yaml",
    "interaction-census.yaml",
    "branch-relation-census.yaml",
    "branch-state.md",
    "post-branch-node-ledger.yaml",
    "qualified-edge-map.yaml",
    "system-state.md",
    "problem-state.yaml",
    "pattern-candidates.md",
    "route-candidates.yaml",
    "route-edge-endpoint-map.yaml",
    "conditions-matrix.md",
    "structure-kernel.md",
]


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def declared_schema_version(path: Path) -> str | None:
    text = path.read_text(encoding="utf-8", errors="replace")[:4096]
    match = re.search(r'^schema_version:\s*["\']?([^"\'\r\n]+)', text, re.MULTILINE)
    return match.group(1).strip() if match else None


def main() -> int:
    parser = argparse.ArgumentParser(description="Freeze audited Bazi structure artifacts.")
    parser.add_argument("case_dir")
    parser.add_argument("--audit-report", required=True)
    parser.add_argument("--freeze-id", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--audit-verdict", choices=("PASS", "PASS_WITH_WARNINGS"), required=True)
    args = parser.parse_args()

    case_dir = Path(args.case_dir).resolve()
    audit = Path(args.audit_report).resolve()
    missing = [name for name in REQUIRED if not (case_dir / name).is_file()]
    if not audit.is_file():
        missing.append(str(audit))
    if missing:
        print(json.dumps({"verdict": "FAIL", "missing": missing}, ensure_ascii=False, indent=2))
        return 1

    files = []
    for name in REQUIRED:
        path = case_dir / name
        files.append(
            {
                "path": name,
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
    receipt = {
        "freeze_id": args.freeze_id,
        "case_id": case_dir.name,
        "audit_report_id": audit.name,
        "audit_verdict": args.audit_verdict,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "commander_fact_ref": "chart-stage1.yaml#chart.month_command",
        "problem_state_ref": "problem-state.yaml",
        "edge_map_ref": "qualified-edge-map.yaml",
        "route_map_ref": "route-candidates.yaml",
        "files": files,
        "invalidates_when": "Any listed file hash changes.",
    }
    output = Path(args.output)
    output.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"verdict": "PASS", "output": str(output), "file_count": len(files)}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
