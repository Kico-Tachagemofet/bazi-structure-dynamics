#!/usr/bin/env python3
"""Validate the conclusion-free Bazi timing/synastry scope seed."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


TOP_REQUIRED = {
    "schema_version", "seed_id", "seed_type", "report_scope_ref",
    "natal_structure_freeze_ref", "question_center", "domain_scope", "scope_atoms",
    "canonical_axes_forbidden", "finding_handoff_forbidden",
    "domain_carrier_verdict_forbidden", "overlay_status",
}
ATOM_REQUIRED = {
    "atom_id", "atom_type", "scope_start", "scope_end", "external_node_refs",
    "activation_interface_refs", "question_slice_refs", "parent_atom_ref",
}
ATOM_TYPES = {"timing-luck-cycle", "timing-annual", "timing-monthly", "synastry-field"}
FORBIDDEN_FIELDS = {
    "topic_process_axes", "primary_axes", "expected_primary_findings", "finding_handoff",
    "deep_card_queries", "domain_carrier_resolution", "candidate_carriers_ranked",
    "canonical_topic_lens_ref",
}


def load_structured(path: Path) -> Any:
    text = path.read_text(encoding="utf-8")
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        try:
            import yaml  # type: ignore
        except ImportError as exc:
            raise ValueError(f"{path}: not JSON and PyYAML is unavailable") from exc
        return yaml.safe_load(text)


def validate(payload: Any) -> dict[str, Any]:
    errors: list[str] = []
    if not isinstance(payload, dict):
        return {"verdict": "FAIL", "errors": ["scope seed must be an object"]}
    missing = sorted(TOP_REQUIRED - set(payload))
    if missing:
        errors.append(f"scope seed missing {', '.join(missing)}")
    forbidden = sorted(FORBIDDEN_FIELDS & set(payload))
    if forbidden:
        errors.append(f"scope seed contains post-overlay fields {forbidden}")
    if payload.get("schema_version") != "1.0":
        errors.append("schema_version must be 1.0")
    if payload.get("seed_type") not in {"timing", "synastry"}:
        errors.append("seed_type must be timing or synastry")
    if payload.get("canonical_axes_forbidden") is not True:
        errors.append("canonical_axes_forbidden must be true")
    if payload.get("finding_handoff_forbidden") is not True:
        errors.append("finding_handoff_forbidden must be true")
    if payload.get("domain_carrier_verdict_forbidden") is not True:
        errors.append("domain_carrier_verdict_forbidden must be true")
    if payload.get("overlay_status") != "pending":
        errors.append("overlay_status must be pending")
    if not isinstance(payload.get("domain_scope"), list) or not payload.get("domain_scope"):
        errors.append("domain_scope must be a non-empty list")

    atoms = payload.get("scope_atoms")
    if not isinstance(atoms, list) or not atoms:
        errors.append("scope_atoms must be a non-empty list")
        atoms = []
    seen_ids: set[str] = set()
    annual_years: set[str] = set()
    for atom in atoms:
        if not isinstance(atom, dict):
            errors.append("scope atom must be an object")
            continue
        atom_id = str(atom.get("atom_id", "<missing>"))
        missing = sorted(ATOM_REQUIRED - set(atom))
        if missing:
            errors.append(f"{atom_id}: missing {', '.join(missing)}")
        if atom_id in seen_ids:
            errors.append(f"{atom_id}: duplicate atom_id")
        seen_ids.add(atom_id)
        atom_type = atom.get("atom_type")
        if atom_type not in ATOM_TYPES:
            errors.append(f"{atom_id}: invalid atom_type")
        if not isinstance(atom.get("external_node_refs"), list) or not atom.get("external_node_refs"):
            errors.append(f"{atom_id}: external_node_refs must be non-empty")
        if not isinstance(atom.get("activation_interface_refs"), list) or not atom.get("activation_interface_refs"):
            errors.append(f"{atom_id}: activation_interface_refs must be non-empty")
        if not isinstance(atom.get("question_slice_refs"), list) or not atom.get("question_slice_refs"):
            errors.append(f"{atom_id}: question_slice_refs must be non-empty")
        nested_forbidden = sorted(FORBIDDEN_FIELDS & set(atom))
        if nested_forbidden:
            errors.append(f"{atom_id}: contains post-overlay fields {nested_forbidden}")
        if atom_type == "timing-annual":
            start = str(atom.get("scope_start", ""))
            end = str(atom.get("scope_end", ""))
            year = start[:4]
            if len(year) != 4 or not year.isdigit() or end[:4] != year:
                errors.append(f"{atom_id}: annual atom must stay within one calendar year")
            elif year in annual_years:
                errors.append(f"{atom_id}: duplicate annual atom for {year}")
            annual_years.add(year)

    return {"verdict": "FAIL" if errors else "PASS", "errors": errors}


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate Bazi timing/synastry scope seed.")
    parser.add_argument("seed")
    args = parser.parse_args()
    try:
        result = validate(load_structured(Path(args.seed)))
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        result = {"verdict": "FAIL", "errors": [str(exc)]}
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["verdict"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
