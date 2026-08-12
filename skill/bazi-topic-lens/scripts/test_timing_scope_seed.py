#!/usr/bin/env python3
"""Self-test the pre-overlay Bazi timing scope seed firewall."""

from __future__ import annotations

from validate_timing_scope_seed import validate


def payload():
    return {
        "schema_version": "1.0",
        "seed_id": "TSS-2027",
        "seed_type": "timing",
        "report_scope_ref": "report-scope.yaml",
        "natal_structure_freeze_ref": "SF-1",
        "question_center": "2027 年事业中的协作、竞争与原局压力转方法路线怎样变化",
        "domain_scope": ["career-work"],
        "scope_atoms": [{
            "atom_id": "YEAR-2027",
            "atom_type": "timing-annual",
            "scope_start": "2027-01-01",
            "scope_end": "2027-12-31",
            "external_node_refs": ["timing.gui"],
            "activation_interface_refs": ["AI-GUI-1"],
            "question_slice_refs": ["career.peer-allocation"],
            "parent_atom_ref": "LUCK-2021-2030",
        }],
        "canonical_axes_forbidden": True,
        "finding_handoff_forbidden": True,
        "domain_carrier_verdict_forbidden": True,
        "overlay_status": "pending",
    }


def main() -> None:
    assert validate(payload())["verdict"] == "PASS"

    post_overlay_leak = payload()
    post_overlay_leak["primary_axes"] = [{"axis_id": "AX-ILLEGAL"}]
    assert validate(post_overlay_leak)["verdict"] == "FAIL"

    collapsed_years = payload()
    collapsed_years["scope_atoms"][0]["scope_start"] = "2021-01-01"
    collapsed_years["scope_atoms"][0]["scope_end"] = "2034-12-31"
    assert validate(collapsed_years)["verdict"] == "FAIL"

    person_verdict = payload()
    person_verdict["scope_atoms"][0]["candidate_carriers_ranked"] = ["colleague"]
    assert validate(person_verdict)["verdict"] == "FAIL"

    print("PASS: timing scope seed stays conclusion-free and keeps annual atoms independent")


if __name__ == "__main__":
    main()
