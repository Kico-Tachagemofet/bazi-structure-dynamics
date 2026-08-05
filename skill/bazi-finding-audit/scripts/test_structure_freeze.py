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
        for name in REQUIRED:
            (root / name).write_text(f"fixture: {name}\n", encoding="utf-8")
        audit = root / "audit-report.md"
        audit.write_text("# PASS\n", encoding="utf-8")
        output = root / "structure-freeze-receipt.yaml"
        subprocess.run(
            [
                sys.executable,
                str(script),
                str(root),
                "--audit-report",
                str(audit),
                "--freeze-id",
                "TEST-FREEZE",
                "--output",
                str(output),
                "--audit-verdict",
                "PASS",
            ],
            check=True,
            capture_output=True,
            text=True,
        )
        receipt = json.loads(output.read_text(encoding="utf-8"))
        assert receipt["freeze_id"] == "TEST-FREEZE"
        assert len(receipt["files"]) == len(REQUIRED) + 1
        assert all(len(item["sha256"]) == 64 for item in receipt["files"])
        assert all("schema_version" in item for item in receipt["files"])
        assert receipt["commander_fact_ref"] == "chart-stage1.yaml#chart.month_command"
        assert receipt["use_kernel_ref"] == "use-kernel.md"
    print("PASS: structure freeze hashes every required artifact and audit report")


if __name__ == "__main__":
    main()
