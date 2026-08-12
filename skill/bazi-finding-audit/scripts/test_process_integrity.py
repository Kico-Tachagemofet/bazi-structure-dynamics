#!/usr/bin/env python3
"""Self-test v4 process closure, life-effect separation, and timing propagation guardrails."""

from __future__ import annotations

import json
import tempfile
from pathlib import Path

from validate_process_integrity import validate_legacy_overlay, validate_natal, validate_timing


EDGE_TEXT = """edges:
  - edge_id: "QE01"
    source_node: "A"
    target_node: "B"
    action: "生"
    edge_layer: "direct-action"
  - edge_id: "QE02"
    source_node: "B"
    target_node: "C"
    action: "制"
    edge_layer: "direct-action"
"""

ROUTE_TEXT = """routes:
  - route_id: "R1"
    edge_refs: ["QE01", "QE02"]
    topology: "chain"
    net_effect_on_primary_problem: "therapeutic"
    therapeutic_priority: "1"
    outlet_eligible: true
"""


def process_payload():
    agency = {"can-start": "conditional", "can-carry": "conditional", "can-redirect": "conditional", "can-stop": "blocked"}
    return {
        "schema_version": "4.0",
        "process_units": [{
            "process_id": "PROC-1",
            "process_role": "therapeutic",
            "primary_problem_ref": "P1",
            "strength_context": {"ref": "system-state#1"},
            "ordered_edge_refs": ["QE01", "QE02"],
            "route_refs": ["R1"],
            "condition_refs": ["C1"],
            "route_closure_receipt": [{"route_ref": "R1", "edge_refs": ["QE01", "QE02"], "complete": True}],
            "elemental_actions": ["生", "制"],
            "ten_god_relations": ["食神", "制杀"],
            "ordered_phases": [
                {
                    "phase_id": "PH1", "sequence_index": 1, "edge_refs": ["QE01"],
                    "mode": "active-initiation", "controller_ref": "daymaster",
                    "source_capacity_requirement": "residual-positive", "start_gate": "conditional",
                    "throughput_band": "low", "allocation_target_refs": ["B"],
                    "competing_allocation_refs": [], "cost_to_daymaster": "low",
                    "effect_on_primary_problem": "none", "failure_state": "stalled",
                    "recovery_or_transition_trigger": "support", "agency_state": agency,
                },
                {
                    "phase_id": "PH2", "sequence_index": 2, "edge_refs": ["QE02"],
                    "mode": "active-redirection", "controller_ref": "B",
                    "source_capacity_requirement": "PH1-complete", "start_gate": "conditional",
                    "throughput_band": "low", "allocation_target_refs": ["C"],
                    "competing_allocation_refs": [], "cost_to_daymaster": "indirect",
                    "effect_on_primary_problem": "therapeutic", "failure_state": "stalled",
                    "recovery_or_transition_trigger": "PH1-reopens", "agency_state": agency,
                },
            ],
            "daymaster_cost": "low",
            "therapeutic_effect": "conditional",
            "residual_problem": "pressure-remains",
            "bypass_and_rebound": "none",
            "life_effect_matrix": {
                "effect_on_daymaster_capacity": "conditional",
                "objective_output_capacity": "problem-solving-output",
                "social_realization_channels": ["career/technical-output"],
                "sustainability_and_cost": "support-required",
                "valence_separation_receipt": "cost and external output separated",
            },
            "competing_process_refs": [],
            "switch_and_reversal_conditions": ["support"],
            "scope": "natal",
            "evidence_refs": ["R1"],
            "counterevidence": [],
        }],
    }


def timing_payload():
    state = {
        "start_gate": "conditional", "phase_states": ["conditional", "conditional"],
        "throughput_band": "low", "allocation_state": "shared", "daymaster_cost": "low",
        "therapeutic_effect": "conditional", "residual_problem": "pressure-remains",
        "bypass_and_rebound": "none", "agency_state": "conditional",
        "life_effect_matrix": {
            "effect_on_daymaster_capacity": "conditional",
            "objective_output_capacity": "problem-solving-output",
            "social_realization_channels": ["career/technical-output"],
            "sustainability_and_cost": "support-required",
            "valence_separation_receipt": "cost and external output separated",
        },
    }
    return {
        "schema_version": "4.0",
        "process_state_diffs": [{
            "process_id": "PROC-1",
            "requalified_or_inherited_edge_receipts": [
                {"edge_ref": "QE01", "disposition": "requalified", "evidence_refs": ["diff#QE01"]},
                {"edge_ref": "QE02", "disposition": "explicitly-inherited-with-no-impact", "evidence_refs": ["diff#no-impact"]},
            ],
            "before": state,
            "after": dict(state, throughput_band="medium"),
        }],
        "propagation_closure": [{"visited_process_refs": ["PROC-1"], "closure_complete": True}],
        "natal_route_retentions": [{
            "retention_id": "NRR-1",
            "natal_process_ref": "PROC-1",
            "affected_phase_refs": ["PH1"],
            "affected_centrality": "upstream",
            "before_throughput": "low",
            "after_throughput": "medium",
            "retention_state": "enhanced",
            "shared_node_allocation_refs": ["ALLOC-WU-1"],
            "unchanged_natal_phase_refs": ["PH2"],
            "backup_route_refs": [],
            "overlay_layer_stack": ["natal", "luck"],
            "structural_impact_band": "noticeable",
            "expiry_rule": "luck-window-end",
        }],
        "overlay_function_transitions": [{
            "natal_node_ref": "hidden.gui",
            "natal_visibility": "hidden",
            "natal_participation_scope": "root-support",
            "natal_direct_action_gate": "closed",
            "external_trigger_refs": ["luck.gui"],
            "activation_interface_ref": "AI-GUI-1",
            "overlay_visibility": "visible-interface",
            "overlay_participation_scope": "relation-function",
            "overlay_direct_action_gate": "conditional",
            "qualified_overlay_functions": ["direct-function", "visible-interface"],
            "blocked_functions": [],
            "requalification_refs": ["diff#gui"],
            "natal_route_retention_ref": "NRR-1",
            "topic_handoff_ceiling": "relation-function-candidate",
            "persistence_mode": "overlay-only",
            "expiry_rule": "luck-window-end",
        }],
    }


def main() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        edge = root / "edges.yaml"
        routes = root / "routes.yaml"
        process = root / "process.json"
        timing = root / "timing.json"
        legacy = root / "legacy.json"
        edge.write_text(EDGE_TEXT, encoding="utf-8")
        routes.write_text(ROUTE_TEXT, encoding="utf-8")
        process.write_text(json.dumps(process_payload(), ensure_ascii=False), encoding="utf-8")
        timing.write_text(json.dumps(timing_payload(), ensure_ascii=False), encoding="utf-8")
        legacy.write_text(json.dumps({"edge_requalification_diff": [{"edge_ref": "QE01"}]}), encoding="utf-8")

        assert validate_natal(edge, routes, process)["verdict"] == "PASS"
        assert validate_timing(process, timing)["verdict"] == "PASS"
        legacy_result = validate_legacy_overlay(edge, routes, legacy)
        assert legacy_result["verdict"] == "FAIL"
        assert "QE02" in legacy_result["blockers"][0]

        broken = process_payload()
        broken["process_units"][0]["ordered_edge_refs"] = ["QE02"]
        process.write_text(json.dumps(broken, ensure_ascii=False), encoding="utf-8")
        assert validate_natal(edge, routes, process)["verdict"] == "FAIL"

        broken_timing = timing_payload()
        broken_timing["process_state_diffs"][0]["requalified_or_inherited_edge_receipts"] = [
            {"edge_ref": "QE01", "disposition": "requalified", "evidence_refs": ["diff#QE01"]}
        ]
        timing.write_text(json.dumps(broken_timing, ensure_ascii=False), encoding="utf-8")
        process.write_text(json.dumps(process_payload(), ensure_ascii=False), encoding="utf-8")
        assert validate_timing(process, timing)["verdict"] == "FAIL"

        missing_retention = timing_payload()
        missing_retention["natal_route_retentions"] = []
        timing.write_text(json.dumps(missing_retention, ensure_ascii=False), encoding="utf-8")
        assert validate_timing(process, timing)["verdict"] == "FAIL"

        bad_transition = timing_payload()
        bad_transition["overlay_function_transitions"][0]["natal_route_retention_ref"] = "NRR-MISSING"
        timing.write_text(json.dumps(bad_transition, ensure_ascii=False), encoding="utf-8")
        assert validate_timing(process, timing)["verdict"] == "FAIL"

    print("PASS: v4 timing guardrails preserve life-effect separation, downstream propagation, natal routes, and temporary functions")


if __name__ == "__main__":
    main()
