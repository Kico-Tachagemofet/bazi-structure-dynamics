#!/usr/bin/env python3
"""Self-test the structure freeze receipt generator."""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from pathlib import Path

from make_structure_freeze import REQUIRED


def main() -> None:
    script = Path(__file__).with_name("make_structure_freeze.py")
    with tempfile.TemporaryDirectory() as temp:
        root = Path(temp)
        for logical_name, candidates in REQUIRED.items():
            fixture = root / candidates[-1]
            fixture.parent.mkdir(parents=True, exist_ok=True)
            fixture.write_text(f"fixture: {logical_name}\n", encoding="utf-8")
        audit = root / "audit-report.md"
        audit.write_text("# PASS\n", encoding="utf-8")
        audit_state = root / "audit-state.json"
        audit_state.write_text(
            json.dumps(
                {
                    "schema_version": "2.0",
                    "audit_id": "AUD-TEST",
                    "audit_report_ref": audit.name,
                    "stage": "structure",
                    "verdict": "PASS",
                    "findings": [],
                    "repair_propagations": [],
                    "summary": {"blocker_total": 0, "blocker_open": 0, "warning_total": 0, "warning_open": 0},
                },
                ensure_ascii=False,
            ),
            encoding="utf-8",
        )
        output = root / "structure-freeze-receipt.yaml"
        subprocess.run(
            [
                sys.executable,
                str(script),
                str(root),
                "--audit-report",
                str(audit),
                "--audit-state",
                str(audit_state),
                "--freeze-id",
                "TEST-FREEZE",
                "--output",
                str(output),
            ],
            check=True,
            capture_output=True,
            text=True,
        )
        receipt = json.loads(output.read_text(encoding="utf-8"))
        assert receipt["freeze_id"] == "TEST-FREEZE"
        assert len(receipt["files"]) == len(REQUIRED) + 2
        assert all(len(item["sha256"]) == 64 for item in receipt["files"])
        assert all("schema_version" in item for item in receipt["files"])
        assert receipt["commander_fact_ref"] == "chart-stage1.yaml#chart.month_command"
        assert receipt["use_kernel_ref"] == "use-kernel.md"
        assert receipt["process_handoff_ref"].endswith("structure-process-handoff.yaml")
        assert receipt["audit_state_id"] == "AUD-TEST"
        audit_state_entry = next(item for item in receipt["files"] if Path(item["path"]).name == audit_state.name)
        assert audit_state_entry["schema_version"] == "2.0"

        broken_state = json.loads(audit_state.read_text(encoding="utf-8"))
        broken_state["findings"] = [{
            "audit_id": "AUD-BLOCK",
            "severity": "BLOCKER",
            "pattern_id": "TOPIC_STAR_FORCED",
            "status": "open",
            "affected_artifacts": ["topic-lens.json"],
            "evidence_refs": ["topic-lens.json#centers"],
            "repair_stage": "topic",
            "repair_type": "patch",
            "verdict_direction_changed": True,
            "discovered_by": "user",
            "downstream_impacted": [],
            "propagation_id": None,
        }]
        broken_state["verdict"] = "PASS"
        broken_state["summary"] = {"blocker_total": 0, "blocker_open": 0, "warning_total": 0, "warning_open": 0}
        audit_state.write_text(json.dumps(broken_state, ensure_ascii=False), encoding="utf-8")
        failed = subprocess.run(
            [
                sys.executable,
                str(script),
                str(root),
                "--audit-report",
                str(audit),
                "--audit-state",
                str(audit_state),
                "--freeze-id",
                "TEST-BROKEN",
                "--output",
                str(output),
            ],
            check=False,
            capture_output=True,
            text=True,
        )
        assert failed.returncode == 1
        assert "direction-changing repair must be re-derive" in failed.stdout
        assert "audit summary mismatch" in failed.stdout
    print("PASS: structure freeze derives verdict from validated audit state and rejects stale summaries/patches")


if __name__ == "__main__":
    main()
