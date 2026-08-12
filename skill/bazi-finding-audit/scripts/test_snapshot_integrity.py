#!/usr/bin/env python3
"""Self-test freeze and active-artifact graph validation."""

from __future__ import annotations

import hashlib
import json
import tempfile
from pathlib import Path

from validate_snapshot_integrity import validate


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    with tempfile.TemporaryDirectory() as temp:
        case = Path(temp) / "fixture-case"
        case.mkdir()
        structure = case / "structure-kernel.md"
        structure.write_text("frozen\n", encoding="utf-8")
        receipt = case / "structure-freeze-receipt.yaml"
        receipt.write_text(json.dumps({
            "schema_version": "2.0",
            "freeze_id": "FRZ-1",
            "files": [{"path": structure.name, "sha256": sha(structure)}],
        }), encoding="utf-8")
        lens = case / "topic-lens-career.json"
        lens.write_text(json.dumps({"structure_freeze_id": "FRZ-1"}), encoding="utf-8")
        manifest = case / "active-artifact-manifest.json"
        payload = {
            "schema_version": "1.0",
            "case_id": case.name,
            "current_structure_freeze_id": "FRZ-1",
            "active_artifacts": [{
                "path": lens.name,
                "stage": "topic",
                "structure_freeze_id": "FRZ-1",
                "dependencies": [structure.name],
            }],
            "inactive_artifacts": [],
        }
        manifest.write_text(json.dumps(payload), encoding="utf-8")
        assert validate(case, receipt, manifest) == []

        lens.write_text(json.dumps({"structure_freeze_id": "FRZ-0"}), encoding="utf-8")
        errors = validate(case, receipt, manifest)
        assert any("stale or mixed freeze refs" in error for error in errors)

        lens.write_text(json.dumps({"structure_freeze_id": "FRZ-1"}), encoding="utf-8")
        stale_dir = case / "topic-findings"
        stale_dir.mkdir()
        stale = stale_dir / "old.md"
        stale.write_text("structure_freeze_id: FRZ-0\n", encoding="utf-8")
        errors = validate(case, receipt, manifest)
        assert any("unclassified" in error for error in errors)
        payload["inactive_artifacts"].append({"path": "topic-findings/old.md", "reason": "superseded", "superseded_by": lens.name})
        manifest.write_text(json.dumps(payload), encoding="utf-8")
        assert validate(case, receipt, manifest) == []

        root_finding = case / "topic-findings-career.md"
        root_finding.write_text("structure_freeze_id: FRZ-0\n", encoding="utf-8")
        errors = validate(case, receipt, manifest)
        assert any("topic-findings-career.md" in error and "unclassified" in error for error in errors)
        payload["inactive_artifacts"].append({
            "path": root_finding.name,
            "reason": "legacy",
            "superseded_by": lens.name,
        })
        manifest.write_text(json.dumps(payload), encoding="utf-8")
        assert validate(case, receipt, manifest) == []

        archived = case / "archive" / "old-delivery" / "full-reading.md"
        archived.parent.mkdir(parents=True)
        archived.write_text("rollback only\n", encoding="utf-8")
        assert validate(case, receipt, manifest) == []

    print("PASS: snapshot integrity rejects stale, mixed, and unclassified downstream artifacts")


if __name__ == "__main__":
    main()
