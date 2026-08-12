#!/usr/bin/env python3
"""Validate Bazi v4 process closure, life-effect separation, and timing propagation.

Structured handoff files may be JSON or YAML when PyYAML is available. Edge and
route files use the narrow deterministic parser from validate_route_integrity.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from validate_route_integrity import records


PROCESS_REQUIRED = {
    "process_id", "process_role", "primary_problem_ref", "strength_context",
    "ordered_edge_refs", "route_refs", "condition_refs", "route_closure_receipt",
    "elemental_actions", "ten_god_relations", "ordered_phases", "daymaster_cost",
    "therapeutic_effect", "residual_problem", "bypass_and_rebound", "life_effect_matrix",
    "competing_process_refs", "switch_and_reversal_conditions", "scope",
    "evidence_refs", "counterevidence",
}
PHASE_REQUIRED = {
    "phase_id", "sequence_index", "edge_refs", "mode", "controller_ref",
    "source_capacity_requirement", "start_gate", "throughput_band",
    "allocation_target_refs", "competing_allocation_refs", "cost_to_daymaster",
    "effect_on_primary_problem", "failure_state", "recovery_or_transition_trigger",
    "agency_state",
}
AGENCY_KEYS = {"can-start", "can-carry", "can-redirect", "can-stop"}
STATE_FIELDS = {
    "start_gate", "phase_states", "throughput_band", "allocation_state",
    "daymaster_cost", "therapeutic_effect", "residual_problem",
    "bypass_and_rebound", "agency_state", "life_effect_matrix",
}
LIFE_EFFECT_REQUIRED = {
    "effect_on_daymaster_capacity", "objective_output_capacity",
    "social_realization_channels", "sustainability_and_cost",
    "valence_separation_receipt",
}
RETENTION_REQUIRED = {
    "retention_id", "natal_process_ref", "affected_phase_refs", "affected_centrality",
    "before_throughput", "after_throughput", "retention_state",
    "shared_node_allocation_refs", "unchanged_natal_phase_refs", "backup_route_refs",
    "overlay_layer_stack", "structural_impact_band", "expiry_rule",
}
RETENTION_STATES = {"retained", "reduced", "redirected", "blocked", "enhanced", "undetermined"}
IMPACT_BANDS = {"background", "noticeable", "material", "dominant", "undetermined"}
FUNCTION_TRANSITION_REQUIRED = {
    "natal_node_ref", "natal_visibility", "natal_participation_scope",
    "natal_direct_action_gate", "external_trigger_refs", "activation_interface_ref",
    "overlay_visibility", "overlay_participation_scope", "overlay_direct_action_gate",
    "qualified_overlay_functions", "blocked_functions", "requalification_refs",
    "natal_route_retention_ref", "topic_handoff_ceiling", "persistence_mode", "expiry_rule",
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


def edge_and_route_maps(edge_path: Path, route_path: Path) -> tuple[dict[str, dict], dict[str, dict]]:
    edges = {
        item["edge_id"]: item
        for item in records(edge_path.read_text(encoding="utf-8"), "edge_id")
        if item.get("edge_id")
    }
    routes = {
        item["route_id"]: item
        for item in records(route_path.read_text(encoding="utf-8"), "route_id")
        if item.get("route_id")
    }
    return edges, routes


def validate_natal(edge_path: Path, route_path: Path, process_path: Path) -> dict[str, Any]:
    edges, routes = edge_and_route_maps(edge_path, route_path)
    payload = load_structured(process_path)
    blockers: list[str] = []
    warnings: list[str] = []
    process_map: dict[str, dict] = {}

    if not isinstance(payload, dict) or payload.get("schema_version") != "4.0":
        blockers.append("process handoff must be a schema_version 4.0 object")
        units = []
    else:
        units = payload.get("process_units", [])
    if not isinstance(units, list) or not units:
        blockers.append("process_units must be a non-empty list")
        units = []

    for process in units:
        if not isinstance(process, dict):
            blockers.append("process unit must be an object")
            continue
        process_id = process.get("process_id", "<missing>")
        if process_id in process_map:
            blockers.append(f"{process_id}: duplicate process_id")
        process_map[str(process_id)] = process
        missing = sorted(PROCESS_REQUIRED - set(process))
        if missing:
            blockers.append(f"{process_id}: missing {', '.join(missing)}")
        life_effect = process.get("life_effect_matrix")
        if not isinstance(life_effect, dict):
            blockers.append(f"{process_id}: life_effect_matrix must be an object")
        else:
            missing_life = sorted(LIFE_EFFECT_REQUIRED - set(life_effect))
            if missing_life:
                blockers.append(f"{process_id}: life_effect_matrix missing {', '.join(missing_life)}")
            if not isinstance(life_effect.get("social_realization_channels"), list):
                blockers.append(f"{process_id}: social_realization_channels must be a list")

        ordered = process.get("ordered_edge_refs", [])
        if not isinstance(ordered, list) or not ordered:
            blockers.append(f"{process_id}: ordered_edge_refs must be non-empty")
            continue
        if len(ordered) != len(set(ordered)):
            blockers.append(f"{process_id}: ordered_edge_refs contains duplicates")
        unknown_edges = sorted(set(ordered) - set(edges))
        if unknown_edges:
            blockers.append(f"{process_id}: unknown edges {unknown_edges}")

        route_refs = process.get("route_refs", [])
        receipts = process.get("route_closure_receipt", [])
        if not isinstance(route_refs, list) or not route_refs:
            blockers.append(f"{process_id}: route_refs must be non-empty")
            route_refs = []
        if not isinstance(receipts, list):
            blockers.append(f"{process_id}: route_closure_receipt must be a list")
            receipts = []
        receipt_map = {
            item.get("route_ref"): item
            for item in receipts
            if isinstance(item, dict) and item.get("route_ref")
        }
        for route_ref in route_refs:
            route = routes.get(route_ref)
            receipt = receipt_map.get(route_ref)
            if route is None:
                blockers.append(f"{process_id}: unknown route {route_ref}")
                continue
            route_edges = route.get("edge_refs", [])
            if not isinstance(route_edges, list) or not route_edges:
                blockers.append(f"{process_id}: route {route_ref} has no edge_refs")
                continue
            if receipt is None:
                blockers.append(f"{process_id}: route {route_ref} lacks closure receipt")
            else:
                if receipt.get("edge_refs") != route_edges or receipt.get("complete") is not True:
                    blockers.append(f"{process_id}: route {route_ref} closure does not exactly match route edges")
            missing_edges = [edge for edge in route_edges if edge not in ordered]
            if missing_edges:
                blockers.append(f"{process_id}: route {route_ref} omitted edges {missing_edges}")

        phases = process.get("ordered_phases", [])
        if not isinstance(phases, list) or not phases:
            blockers.append(f"{process_id}: ordered_phases must be non-empty")
            phases = []
        covered: list[str] = []
        indices: list[int] = []
        for phase in phases:
            if not isinstance(phase, dict):
                blockers.append(f"{process_id}: phase must be an object")
                continue
            phase_id = phase.get("phase_id", "<missing>")
            missing = sorted(PHASE_REQUIRED - set(phase))
            if missing:
                blockers.append(f"{process_id}/{phase_id}: missing {', '.join(missing)}")
            phase_edges = phase.get("edge_refs", [])
            if not isinstance(phase_edges, list):
                blockers.append(f"{process_id}/{phase_id}: edge_refs must be a list")
            else:
                covered.extend(phase_edges)
                extra = sorted(set(phase_edges) - set(ordered))
                if extra:
                    blockers.append(f"{process_id}/{phase_id}: edges outside process {extra}")
            if isinstance(phase.get("sequence_index"), int):
                indices.append(phase["sequence_index"])
            agency = phase.get("agency_state")
            if not isinstance(agency, dict) or set(agency) != AGENCY_KEYS:
                blockers.append(f"{process_id}/{phase_id}: agency_state must contain exactly {sorted(AGENCY_KEYS)}")
        uncovered = [edge for edge in ordered if edge not in covered]
        if uncovered:
            blockers.append(f"{process_id}: edges not assigned to any phase {uncovered}")
        if indices and sorted(indices) != list(range(1, len(indices) + 1)):
            blockers.append(f"{process_id}: phase sequence_index must be contiguous from 1")

    verdict = "FAIL" if blockers else ("PASS_WITH_WARNINGS" if warnings else "PASS")
    return {
        "verdict": verdict,
        "process_count": len(process_map),
        "blockers": blockers,
        "warnings": warnings,
    }


def validate_timing(process_path: Path, timing_path: Path) -> dict[str, Any]:
    natal = load_structured(process_path)
    timing = load_structured(timing_path)
    blockers: list[str] = []
    process_map = {
        item.get("process_id"): item
        for item in natal.get("process_units", [])
        if isinstance(item, dict) and item.get("process_id")
    }
    timing_version = timing.get("schema_version") if isinstance(timing, dict) else None
    if not isinstance(timing, dict) or timing_version != "4.0":
        blockers.append("timing process diff must be schema_version 4.0")
        diffs = []
    else:
        diffs = timing.get("process_state_diffs", [])
    if not isinstance(diffs, list) or not diffs:
        blockers.append("process_state_diffs must be a non-empty list")
        diffs = []

    for item in diffs:
        if not isinstance(item, dict):
            blockers.append("process_state_diff must be an object")
            continue
        process_id = item.get("process_id", "<missing>")
        process = process_map.get(process_id)
        if process is None:
            blockers.append(f"{process_id}: unknown natal process")
            continue
        receipts = item.get("requalified_or_inherited_edge_receipts", [])
        if not isinstance(receipts, list):
            blockers.append(f"{process_id}: edge receipts must be a list")
            receipts = []
        receipt_map = {
            receipt.get("edge_ref"): receipt
            for receipt in receipts
            if isinstance(receipt, dict) and receipt.get("edge_ref")
        }
        for edge_ref in process.get("ordered_edge_refs", []):
            receipt = receipt_map.get(edge_ref)
            if receipt is None:
                blockers.append(f"{process_id}: process edge {edge_ref} lacks timing disposition")
                continue
            if receipt.get("disposition") not in {"requalified", "explicitly-inherited-with-no-impact"}:
                blockers.append(f"{process_id}/{edge_ref}: invalid timing disposition")
            if receipt.get("disposition") == "explicitly-inherited-with-no-impact" and not receipt.get("evidence_refs"):
                blockers.append(f"{process_id}/{edge_ref}: inherited edge needs no-impact evidence")
        for state_name in ("before", "after"):
            state = item.get(state_name)
            if not isinstance(state, dict):
                blockers.append(f"{process_id}: {state_name} must be an object")
                continue
            missing = sorted(STATE_FIELDS - set(state))
            if missing:
                blockers.append(f"{process_id}: {state_name} missing {', '.join(missing)}")

    closures = timing.get("propagation_closure", []) if isinstance(timing, dict) else []
    if not isinstance(closures, list) or not closures:
        blockers.append("propagation_closure must be a non-empty list")
    else:
        for closure in closures:
            if not isinstance(closure, dict) or closure.get("closure_complete") is not True:
                blockers.append("every propagation closure must declare closure_complete: true")
            elif not closure.get("visited_process_refs"):
                blockers.append("propagation closure must visit at least one process")

    if timing_version == "4.0":
        retentions = timing.get("natal_route_retentions", [])
        if not isinstance(retentions, list) or not retentions:
            blockers.append("v4.0 timing diff requires natal_route_retentions")
            retentions = []
        retention_map: dict[str, dict] = {}
        for retention in retentions:
            if not isinstance(retention, dict):
                blockers.append("natal_route_retention must be an object")
                continue
            retention_id = retention.get("retention_id", "<missing>")
            missing = sorted(RETENTION_REQUIRED - set(retention))
            if missing:
                blockers.append(f"{retention_id}: natal route retention missing {', '.join(missing)}")
            if retention.get("retention_state") not in RETENTION_STATES:
                blockers.append(f"{retention_id}: invalid retention_state")
            if retention.get("structural_impact_band") not in IMPACT_BANDS:
                blockers.append(f"{retention_id}: invalid structural_impact_band")
            process_ref = retention.get("natal_process_ref")
            if process_ref not in process_map:
                blockers.append(f"{retention_id}: unknown natal_process_ref {process_ref}")
            if not retention.get("shared_node_allocation_refs"):
                blockers.append(f"{retention_id}: shared node allocation refs must be explicit")
            if not retention.get("overlay_layer_stack"):
                blockers.append(f"{retention_id}: overlay layer stack must be explicit")
            if retention_id in retention_map:
                blockers.append(f"{retention_id}: duplicate retention_id")
            retention_map[str(retention_id)] = retention
        for process_diff in diffs:
            if not isinstance(process_diff, dict):
                continue
            process_id = process_diff.get("process_id")
            if process_id and not any(
                item.get("natal_process_ref") == process_id for item in retention_map.values()
            ):
                blockers.append(f"{process_id}: v4.0 timing diff lacks natal route retention")

        transitions = timing.get("overlay_function_transitions", [])
        if not isinstance(transitions, list) or not transitions:
            blockers.append("v4.0 timing diff requires overlay_function_transitions")
            transitions = []
        for transition in transitions:
            if not isinstance(transition, dict):
                blockers.append("overlay_function_transition must be an object")
                continue
            node_ref = transition.get("natal_node_ref", "<missing>")
            missing = sorted(FUNCTION_TRANSITION_REQUIRED - set(transition))
            if missing:
                blockers.append(f"{node_ref}: overlay function transition missing {', '.join(missing)}")
            if transition.get("natal_route_retention_ref") not in retention_map:
                blockers.append(f"{node_ref}: overlay function transition has unknown natal_route_retention_ref")
            if transition.get("topic_handoff_ceiling") not in {
                "mechanism-only", "relation-function-candidate", "domain-carrier-candidate"
            }:
                blockers.append(f"{node_ref}: invalid topic_handoff_ceiling")

    return {"verdict": "FAIL" if blockers else "PASS", "blockers": blockers, "warnings": []}


def validate_legacy_overlay(edge_path: Path, route_path: Path, overlay_path: Path) -> dict[str, Any]:
    """Expose missing downstream propagation in pre-v3 annual overlays."""
    _, routes = edge_and_route_maps(edge_path, route_path)
    overlay = load_structured(overlay_path)
    changed = {
        item.get("edge_ref")
        for item in overlay.get("edge_requalification_diff", [])
        if isinstance(item, dict) and item.get("edge_ref")
    }
    blockers: list[str] = []
    for route_id, route in routes.items():
        refs = route.get("edge_refs", [])
        if not isinstance(refs, list) or not refs:
            continue
        changed_positions = [index for index, edge in enumerate(refs) if edge in changed]
        if not changed_positions:
            continue
        first = min(changed_positions)
        missing_downstream = [edge for edge in refs[first + 1 :] if edge not in changed]
        if missing_downstream:
            blockers.append(
                f"{route_id}: changed upstream edge {refs[first]} has unqualified downstream edges "
                f"{missing_downstream}; legacy overlay has no explicit no-impact receipts"
            )
    return {
        "verdict": "FAIL" if blockers else "PASS",
        "changed_edge_refs": sorted(changed),
        "blockers": blockers,
        "warnings": [],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate Bazi process closure and timing propagation.")
    sub = parser.add_subparsers(dest="mode", required=True)
    natal = sub.add_parser("natal")
    natal.add_argument("edge_map")
    natal.add_argument("routes")
    natal.add_argument("process_handoff")
    timing = sub.add_parser("timing")
    timing.add_argument("process_handoff")
    timing.add_argument("timing_process_diff")
    legacy = sub.add_parser("legacy-overlay")
    legacy.add_argument("edge_map")
    legacy.add_argument("routes")
    legacy.add_argument("overlay_diff")
    args = parser.parse_args()

    try:
        if args.mode == "natal":
            result = validate_natal(Path(args.edge_map), Path(args.routes), Path(args.process_handoff))
        elif args.mode == "timing":
            result = validate_timing(Path(args.process_handoff), Path(args.timing_process_diff))
        else:
            result = validate_legacy_overlay(Path(args.edge_map), Path(args.routes), Path(args.overlay_diff))
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        result = {"verdict": "FAIL", "blockers": [str(exc)], "warnings": []}
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 1 if result["verdict"] == "FAIL" else 0


if __name__ == "__main__":
    sys.exit(main())
