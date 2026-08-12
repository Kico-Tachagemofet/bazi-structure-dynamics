#!/usr/bin/env python3
"""Validate Topic Lens typed state without interpreting a chart."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


INTENTS = {"descriptive", "capability", "outcome", "therapeutic", "timing", "synastry"}
ELIGIBILITY = {"qualified", "diverted", "absorbed-by", "suppressed-by", "not-applicable", "undetermined"}
GATE_STATUS = {"supported", "conditional", "blocked", "not-applicable", "undetermined"}
CLAIM_LEVELS = {"internal_potential", "callable_capability", "sustainable_output", "external_result", "not-claimed"}
CLAIM_STRENGTH = {"strong", "conditional", "not-claimed"}
ALL_GATES = {"potential", "daymaster_access", "visibility", "sustainability", "destination", "external_result"}
DEFAULT_REQUIRED = {
    "internal_potential": {"potential"},
    "callable_capability": {"potential", "daymaster_access"},
    "sustainable_output": {"potential", "daymaster_access", "sustainability", "destination"},
    "external_result": ALL_GATES,
    "not-claimed": set(),
}
SNAPSHOT_KEYS = {
    "commander",
    "exposed_stems",
    "dominant_branch_field",
    "daymaster_roots_and_access",
    "conventional_symbol_post_state_and_destination",
}
SCHEMA_VERSIONS = {"2.0", "2.1", "2.2", "2.3", "3.0", "3.1", "3.2"}
DEEP_CARD_FAMILIES = {"foundation", "heavenly_stem", "earthly_branch", "ten_god"}
DEEP_CARD_QUERY_STATUS = {"requested", "deferred"}
DEEP_CARD_UNIT_CLASSES = {
    "semantic_core", "state_modifier", "symbol_carrier", "relational_carrier",
    "composite_domain_carrier", "cross_system_context",
}
DEEP_CARD_CARRIER_SCOPES = {"none", "symbol", "relational", "composite"}
DEEP_CARD_CLAIM_CEILINGS = {"mechanism", "candidate"}
DOMAIN_CARRIER_FAMILIES = {
    "career", "identity_role", "kinship", "object_place", "health_condition", "event_scenario",
}
FACET_DISPOSITIONS = {"primary", "supporting", "cross-ref", "not-applicable", "source-gap"}
EXPLANATORY_ROLES = {"formation", "advantage", "cost", "result-gate", "switch", "verification"}
CONTEXT_STATUSES = {"known-from-question", "unknown", "withheld-for-blindness"}
ROLE_MAPPING_DISPOSITIONS = {"not-requested", "candidate-requested", "source-gap"}
ANSWER_STATUSES = {"complete", "conditional", "not-applicable", "source-gap"}
PROHIBITED_ANSWER_SUBSTITUTES = {
    "personality-only", "advice-only", "generic-cross-topic-summary", "technical-label-only",
}
QUESTION_PLACEHOLDER_PREFIXES = ("完整回答", "完整交付")


def _is_natural_reader_question(value: Any, facet_id: Any) -> bool:
    if not isinstance(value, str):
        return False
    question = value.strip()
    if len(question) < 8 or not re.search(r"[\u3400-\u9fff]", question):
        return False
    if question.startswith(QUESTION_PLACEHOLDER_PREFIXES) or question == str(facet_id or "").strip():
        return False
    return question.endswith(("？", "?"))


def _need(obj: dict[str, Any], fields: set[str], label: str, errors: list[str]) -> None:
    missing = sorted(fields - set(obj))
    if missing:
        errors.append(f"{label}: missing {', '.join(missing)}")


def validate_state(payload: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    header = {
        "schema_version", "case_id", "topic_id", "topic_intent", "exact_question", "scope",
        "framework_lock", "structure_freeze_id", "structure_freeze_ref", "use_kernel_ref",
        "report_scope_ref", "delivery_mode", "subject_context_available_to_finding",
        "facts_snapshot", "question_slices", "centers", "star_eligibility",
        "capability_bridge", "topic_process_axes", "finding_handoff",
    }
    if payload.get("schema_version") in {"2.1", "2.2", "2.3", "3.0", "3.1", "3.2"}:
        header.add("deep_card_queries")
    if payload.get("schema_version") in {"2.3", "3.0", "3.1", "3.2"}:
        header |= {"coverage_profile", "scope_atoms"}
    if payload.get("schema_version") in {"3.0", "3.1", "3.2"}:
        header |= {"structure_process_handoff_ref", "domain_carrier_requests"}
    if payload.get("schema_version") in {"3.1", "3.2"}:
        header.add("reader_question_profile")
        if payload.get("topic_intent") in {"timing", "synastry"}:
            header.add("runtime_context_policy")
    _need(payload, header, "state", errors)
    if errors:
        return errors
    if payload["schema_version"] not in SCHEMA_VERSIONS:
        errors.append("state: schema_version must be 2.0, 2.1, 2.2, 2.3, 3.0, 3.1, or 3.2")
    if payload["topic_intent"] not in INTENTS:
        errors.append("state: invalid topic_intent")
    if payload["subject_context_available_to_finding"] is not False:
        errors.append("state: subject context must remain unavailable to blind finding")

    snapshot = payload["facts_snapshot"]
    if not isinstance(snapshot, dict) or set(snapshot) != SNAPSHOT_KEYS:
        errors.append("facts_snapshot: must contain exactly the five frozen fact groups")
    else:
        for key, item in snapshot.items():
            if not isinstance(item, dict):
                errors.append(f"facts_snapshot.{key}: must be an object")
                continue
            _need(item, {"status", "value", "refs", "conflicts_or_limits"}, f"facts_snapshot.{key}", errors)
            if not item.get("refs"):
                errors.append(f"facts_snapshot.{key}: refs cannot be empty")
        commander_value = snapshot["commander"].get("value", {})
        if not isinstance(commander_value, dict) or not {"month_branch_main_qi", "commander", "seasonal_phase"}.issubset(commander_value):
            errors.append("facts_snapshot.commander: main qi, commander, and seasonal phase must be separate")

    slice_ids: set[str] = set()
    slice_facets: dict[str, str] = {}
    slice_contracts: dict[str, str] = {}
    contract_ids: set[str] = set()
    closure_keys: set[str] = set()
    question_slices = payload.get("question_slices")
    if not isinstance(question_slices, list) or not question_slices:
        errors.append("question_slices: must be a non-empty list")
    else:
        base_slice_fields = {
            "question_slice_id", "user_language_center", "center_type", "relation_to_chart_subject",
            "body_anchor_refs", "internal_mechanism_target", "domain_carrier_target",
            "external_result_target", "strongest_alternative_body",
        }
        for item in question_slices:
            if not isinstance(item, dict):
                errors.append("question_slices: each slice must be an object")
                continue
            required_fields = set(base_slice_fields)
            if payload["schema_version"] in {"3.1", "3.2"}:
                required_fields |= {"facet_id", "reader_need", "explanatory_obligations"}
            if payload["schema_version"] == "3.2":
                required_fields |= {"exact_reader_question", "reader_answer_contract"}
            _need(item, required_fields, "question_slice", errors)
            slice_id = item.get("question_slice_id")
            if not isinstance(slice_id, str) or not slice_id:
                errors.append("question_slice: question_slice_id must be a non-empty string")
                continue
            if slice_id in slice_ids:
                errors.append(f"question_slices: duplicate question_slice_id {slice_id}")
            slice_ids.add(slice_id)
            if payload["schema_version"] in {"3.1", "3.2"}:
                facet_id = item.get("facet_id")
                if not isinstance(facet_id, str) or not facet_id:
                    errors.append(f"question_slice {slice_id}: facet_id must be a non-empty string")
                else:
                    slice_facets[slice_id] = facet_id
                obligations = item.get("explanatory_obligations")
                if not isinstance(obligations, list) or set(obligations) != EXPLANATORY_ROLES:
                    errors.append(
                        f"question_slice {slice_id}: explanatory_obligations must contain exactly the six reader roles"
                    )
                if not item.get("reader_need"):
                    errors.append(f"question_slice {slice_id}: reader_need cannot be empty")
            if payload["schema_version"] == "3.2":
                exact_reader_question = item.get("exact_reader_question")
                if not _is_natural_reader_question(exact_reader_question, item.get("facet_id")):
                    errors.append(
                        f"question_slice {slice_id}: exact_reader_question must be a concrete natural-Chinese question, not a facet label or placeholder"
                    )
                contract = item.get("reader_answer_contract")
                contract_fields = {
                    "contract_id", "closure_key", "answer_target", "direct_answer_required",
                    "allowed_answer_statuses", "prohibited_substitutes", "topic_specificity_required",
                }
                if not isinstance(contract, dict):
                    errors.append(f"question_slice {slice_id}: reader_answer_contract must be an object")
                else:
                    _need(contract, contract_fields, f"question_slice {slice_id} reader_answer_contract", errors)
                    contract_id = contract.get("contract_id")
                    closure_key = contract.get("closure_key")
                    if not isinstance(contract_id, str) or not contract_id:
                        errors.append(f"question_slice {slice_id}: contract_id must be a non-empty string")
                    elif contract_id in contract_ids:
                        errors.append(f"question_slices: duplicate contract_id {contract_id}")
                    else:
                        contract_ids.add(contract_id)
                        slice_contracts[slice_id] = contract_id
                    if not isinstance(closure_key, str) or not closure_key:
                        errors.append(f"question_slice {slice_id}: closure_key must be a non-empty string")
                    elif closure_key in closure_keys:
                        errors.append(f"question_slices: duplicate closure_key {closure_key}")
                    else:
                        closure_keys.add(closure_key)
                    answer_target = contract.get("answer_target")
                    target_fields = {"subject_or_role", "matter_or_domain_object", "result_or_outcome"}
                    if not isinstance(answer_target, dict) or set(answer_target) != target_fields:
                        errors.append(
                            f"question_slice {slice_id}: answer_target must contain exactly subject_or_role, matter_or_domain_object, and result_or_outcome"
                        )
                    elif any(not isinstance(answer_target.get(field), str) or not answer_target.get(field).strip() for field in target_fields):
                        errors.append(f"question_slice {slice_id}: every answer_target field must be non-empty")
                    if contract.get("direct_answer_required") is not True:
                        errors.append(f"question_slice {slice_id}: direct_answer_required must be true")
                    allowed_statuses = contract.get("allowed_answer_statuses")
                    if not isinstance(allowed_statuses, list) or set(allowed_statuses) != ANSWER_STATUSES:
                        errors.append(f"question_slice {slice_id}: allowed_answer_statuses must contain exactly the four closure statuses")
                    prohibited_substitutes = contract.get("prohibited_substitutes")
                    if not isinstance(prohibited_substitutes, list) or set(prohibited_substitutes) != PROHIBITED_ANSWER_SUBSTITUTES:
                        errors.append(f"question_slice {slice_id}: prohibited_substitutes must contain exactly the four forbidden answer substitutes")
                    if contract.get("topic_specificity_required") is not True:
                        errors.append(f"question_slice {slice_id}: topic_specificity_required must be true")

    reader_profile = payload.get("reader_question_profile")
    profile_dispositions: list[dict[str, Any]] = []
    if payload["schema_version"] in {"3.1", "3.2"}:
        if not isinstance(reader_profile, dict):
            errors.append("reader_question_profile: must be an object")
        else:
            _need(
                reader_profile,
                {"profile_id", "profile_ref", "profile_type", "required_facet_ids", "facet_dispositions"},
                "reader_question_profile",
                errors,
            )
            required_facets = reader_profile.get("required_facet_ids", [])
            profile_dispositions = reader_profile.get("facet_dispositions", [])
            if not isinstance(required_facets, list) or not required_facets:
                errors.append("reader_question_profile.required_facet_ids: must be a non-empty list")
                required_facets = []
            if not isinstance(profile_dispositions, list):
                errors.append("reader_question_profile.facet_dispositions: must be a list")
                profile_dispositions = []
            seen_facets: set[str] = set()
            for disposition in profile_dispositions:
                if not isinstance(disposition, dict):
                    errors.append("reader_question_profile: each facet disposition must be an object")
                    continue
                disposition_fields = {"facet_id", "disposition", "question_slice_ids", "axis_ids", "reason"}
                if payload["schema_version"] == "3.2":
                    disposition_fields |= {"answer_contract_ids", "domain_specific_delta", "shared_answer_ref"}
                _need(disposition, disposition_fields, "facet_disposition", errors)
                facet_id = disposition.get("facet_id")
                if facet_id in seen_facets:
                    errors.append(f"reader_question_profile: duplicate facet disposition {facet_id}")
                seen_facets.add(facet_id)
                if disposition.get("disposition") not in FACET_DISPOSITIONS:
                    errors.append(f"facet {facet_id}: invalid disposition")
                for field in {"question_slice_ids", "axis_ids"}:
                    if not isinstance(disposition.get(field), list):
                        errors.append(f"facet {facet_id}: {field} must be a list")
                if not disposition.get("reason"):
                    errors.append(f"facet {facet_id}: reason cannot be empty")
                unknown_slices = set(disposition.get("question_slice_ids", [])) - slice_ids
                if unknown_slices:
                    errors.append(f"facet {facet_id}: unknown question slices {sorted(unknown_slices)}")
                mismatched = [
                    item for item in disposition.get("question_slice_ids", [])
                    if slice_facets.get(item) != facet_id
                ]
                if mismatched:
                    errors.append(f"facet {facet_id}: question slices use a different facet {mismatched}")
                if disposition.get("disposition") in {"primary", "supporting"} and not disposition.get("question_slice_ids"):
                    errors.append(f"facet {facet_id}: {disposition.get('disposition')} disposition needs a question slice")
                if payload["schema_version"] == "3.2":
                    answer_contract_ids = disposition.get("answer_contract_ids")
                    if not isinstance(answer_contract_ids, list):
                        errors.append(f"facet {facet_id}: answer_contract_ids must be a list")
                        answer_contract_ids = []
                    unknown_contracts = set(answer_contract_ids) - contract_ids
                    if unknown_contracts:
                        errors.append(f"facet {facet_id}: unknown answer contracts {sorted(unknown_contracts)}")
                    expected_contracts = {
                        slice_contracts[slice_id]
                        for slice_id in disposition.get("question_slice_ids", [])
                        if slice_id in slice_contracts
                    }
                    if set(answer_contract_ids) != expected_contracts:
                        errors.append(f"facet {facet_id}: answer_contract_ids must exactly match its question slices")
                    if disposition.get("disposition") in {"primary", "supporting", "cross-ref"}:
                        if not answer_contract_ids:
                            errors.append(f"facet {facet_id}: substantive disposition needs an answer contract")
                        if not isinstance(disposition.get("domain_specific_delta"), str) or not disposition.get("domain_specific_delta", "").strip():
                            errors.append(f"facet {facet_id}: substantive disposition needs a domain_specific_delta")
                    if disposition.get("disposition") == "cross-ref" and not disposition.get("shared_answer_ref"):
                        errors.append(f"facet {facet_id}: cross-ref needs shared_answer_ref")
            if set(required_facets) != seen_facets:
                errors.append("reader_question_profile: every required facet must have exactly one disposition")
            if payload["schema_version"] == "3.2":
                owned_contracts = [
                    contract_id
                    for disposition in profile_dispositions
                    if isinstance(disposition, dict)
                    for contract_id in disposition.get("answer_contract_ids", [])
                ]
                if set(owned_contracts) != contract_ids or len(owned_contracts) != len(set(owned_contracts)):
                    errors.append("reader_question_profile: every Reader Answer Contract must belong to exactly one facet disposition")

        if payload.get("topic_intent") in {"timing", "synastry"}:
            context = payload.get("runtime_context_policy")
            required_context = {
                "context_status", "context_refs", "allowed_use", "structural_inference_forbidden",
                "confidence_uplift_forbidden", "unknown_context_action",
            }
            if not isinstance(context, dict):
                errors.append("runtime_context_policy: timing/synastry v3.1+ requires an object")
            else:
                _need(context, required_context, "runtime_context_policy", errors)
                if context.get("context_status") not in CONTEXT_STATUSES:
                    errors.append("runtime_context_policy: invalid context_status")
                if not isinstance(context.get("context_refs"), list):
                    errors.append("runtime_context_policy.context_refs: must be a list")
                if context.get("allowed_use") != "carrier-branching-and-agency-only":
                    errors.append("runtime_context_policy.allowed_use: must be carrier-branching-and-agency-only")
                if context.get("structural_inference_forbidden") is not True:
                    errors.append("runtime_context_policy: structural inference must remain forbidden")
                if context.get("confidence_uplift_forbidden") is not True:
                    errors.append("runtime_context_policy: confidence uplift must remain forbidden")
                if context.get("unknown_context_action") != "keep-conditional-branches":
                    errors.append("runtime_context_policy: unknown context must keep conditional branches")

    centers = payload["centers"]
    if not isinstance(centers, dict):
        errors.append("centers: must be an object")
        return errors
    _need(centers, {"conventional_symbol_candidates", "actual_controller_or_carrier", "therapeutic_pivots"}, "centers", errors)
    candidates = centers.get("conventional_symbol_candidates", [])
    actual = centers.get("actual_controller_or_carrier", [])
    pivots = centers.get("therapeutic_pivots", [])
    if not actual:
        errors.append("centers: actual controller or carrier cannot be empty")
    if payload["topic_intent"] == "therapeutic" and not pivots:
        errors.append("centers: therapeutic intent requires a frozen therapeutic pivot")
    candidate_ids = {item.get("candidate_id") for item in candidates if isinstance(item, dict)}
    actual_ids = {item.get("center_id") for item in actual if isinstance(item, dict)}
    pivot_ids = {item.get("pivot_id") for item in pivots if isinstance(item, dict)}
    for item in actual:
        if isinstance(item, dict) and (not item.get("refs") or not item.get("comparison_against_alternatives")):
            errors.append(f"center {item.get('center_id')}: refs and alternative comparison are required")

    eligibility_by_id: dict[str, str] = {}
    for item in payload["star_eligibility"]:
        if not isinstance(item, dict):
            errors.append("star_eligibility: each item must be an object")
            continue
        _need(item, {"candidate_id", "status", "evidence_refs", "post_state_refs", "destination", "comparison_against_alternatives", "disposition_target"}, "star_eligibility item", errors)
        candidate_id = item.get("candidate_id")
        status = item.get("status")
        eligibility_by_id[candidate_id] = status
        if candidate_id not in candidate_ids:
            errors.append(f"star_eligibility {candidate_id}: unknown conventional candidate")
        if status not in ELIGIBILITY:
            errors.append(f"star_eligibility {candidate_id}: invalid status")
        if not item.get("evidence_refs") or not item.get("post_state_refs") or not item.get("comparison_against_alternatives"):
            errors.append(f"star_eligibility {candidate_id}: evidence, post-state, and comparison are required")
        if status in {"diverted", "absorbed-by", "suppressed-by"} and not item.get("disposition_target"):
            errors.append(f"star_eligibility {candidate_id}: disposition target is required for {status}")
    if set(eligibility_by_id) != candidate_ids:
        errors.append("star_eligibility: must cover every conventional candidate exactly once")

    bridge = payload["capability_bridge"]
    if not isinstance(bridge, dict):
        errors.append("capability_bridge: must be an object")
    else:
        _need(bridge, {"claim_target", "claim_level", "claim_strength", "required_gates", "gates", "claim_disposition"}, "capability_bridge", errors)
        level = bridge.get("claim_level")
        strength = bridge.get("claim_strength")
        if level not in CLAIM_LEVELS:
            errors.append("capability_bridge: invalid claim_level")
        if strength not in CLAIM_STRENGTH:
            errors.append("capability_bridge: invalid claim_strength")
        gates = bridge.get("gates", {})
        if not isinstance(gates, dict) or set(gates) != ALL_GATES:
            errors.append("capability_bridge: all six gates are required")
        else:
            for gate, item in gates.items():
                if not isinstance(item, dict):
                    errors.append(f"capability_bridge.{gate}: must be an object")
                    continue
                _need(item, {"status", "evidence_refs", "counterevidence"}, f"capability_bridge.{gate}", errors)
                if item.get("status") not in GATE_STATUS:
                    errors.append(f"capability_bridge.{gate}: invalid status")
            required = set(bridge.get("required_gates", []))
            if not required.issubset(ALL_GATES):
                errors.append("capability_bridge: unknown required gate")
            if level in DEFAULT_REQUIRED and not DEFAULT_REQUIRED[level].issubset(required):
                errors.append(f"capability_bridge: {level} omitted a default required gate")
            if level == "not-claimed" and strength != "not-claimed":
                errors.append("capability_bridge: not-claimed level needs not-claimed strength")
            if strength == "strong":
                failed = sorted(gate for gate in required if gates[gate].get("status") != "supported")
                if failed:
                    errors.append(f"capability_bridge: strong claim has unsupported gates {', '.join(failed)}")
            if strength == "conditional":
                failed = sorted(gate for gate in required if gates[gate].get("status") in {"blocked", "undetermined"})
                if failed:
                    errors.append(f"capability_bridge: conditional claim still has blocked/undetermined gates {', '.join(failed)}")

    axes_by_id: dict[str, dict[str, Any]] = {}
    for axis in payload["topic_process_axes"]:
        if not isinstance(axis, dict):
            errors.append("topic_process_axes: each axis must be an object")
            continue
        required_axis = {
            "axis_id", "question_slice_id", "axis_role", "focal_question", "conventional_symbol_refs",
            "controller_or_carrier_refs", "therapeutic_pivot_ref", "source_endpoint", "target_endpoint",
            "node_refs", "edge_refs", "route_refs", "mechanism", "base_state", "supporting_factors",
            "damage_diversion_or_occupation", "destination_and_feedback", "daymaster_agency_relation",
            "competing_allocation", "switch_conditions", "failure_or_reversal", "strongest_alternative",
            "finding_disposition",
        }
        if payload["schema_version"] in {"3.0", "3.1", "3.2"}:
            required_axis |= {
                "process_ref", "process_freeze_or_hash_ref", "route_closure_receipt_ref",
                "phase_focus_refs", "strength_and_bearing_snapshot_ref", "complete_edge_closure",
                "daymaster_cost_ref", "therapeutic_effect_ref", "residual_problem_ref",
                "bypass_and_rebound_ref", "agency_phase_refs",
            }
            if payload["topic_intent"] in {"timing", "synastry"}:
                required_axis |= {
                    "timing_process_diff_ref", "propagation_closure_ref",
                    "process_before_after_ref", "agency_transition_ref", "expiry_rule",
                }
                if payload["schema_version"] in {"3.1", "3.2"}:
                    required_axis.add("timing_manifestation_adjudication")
        _need(axis, required_axis, f"axis {axis.get('axis_id')}", errors)
        axis_id = axis.get("axis_id")
        axes_by_id[axis_id] = axis
        unknown_centers = set(axis.get("controller_or_carrier_refs", [])) - actual_ids
        if unknown_centers:
            errors.append(f"axis {axis_id}: unknown controller/carrier refs {sorted(unknown_centers)}")
        if axis.get("axis_role") == "primary" and not axis.get("controller_or_carrier_refs"):
            errors.append(f"axis {axis_id}: primary axis needs an actual controller/carrier")
        unknown_candidates = set(axis.get("conventional_symbol_refs", [])) - candidate_ids
        if unknown_candidates:
            errors.append(f"axis {axis_id}: unknown conventional symbol refs {sorted(unknown_candidates)}")
        pivot_ref = axis.get("therapeutic_pivot_ref")
        if pivot_ref is not None and pivot_ref not in pivot_ids:
            errors.append(f"axis {axis_id}: unknown therapeutic pivot {pivot_ref}")
        if payload["schema_version"] in {"3.0", "3.1", "3.2"}:
            for field in {
                "process_ref", "process_freeze_or_hash_ref", "route_closure_receipt_ref",
                "strength_and_bearing_snapshot_ref", "daymaster_cost_ref", "therapeutic_effect_ref",
                "residual_problem_ref", "bypass_and_rebound_ref",
            }:
                if not axis.get(field):
                    errors.append(f"axis {axis_id}: {field} cannot be empty in v3")
            for field in {"phase_focus_refs", "agency_phase_refs"}:
                value = axis.get(field)
                if not isinstance(value, list) or not value:
                    errors.append(f"axis {axis_id}: {field} must be a non-empty list in v3")
            closure = axis.get("complete_edge_closure")
            edge_refs = axis.get("edge_refs")
            if not isinstance(closure, list) or not closure:
                errors.append(f"axis {axis_id}: complete_edge_closure must be a non-empty list in v3")
            elif closure != edge_refs:
                errors.append(f"axis {axis_id}: edge_refs must exactly equal complete_edge_closure")
            if payload["topic_intent"] in {"timing", "synastry"}:
                for field in {
                    "timing_process_diff_ref", "propagation_closure_ref", "process_before_after_ref",
                    "agency_transition_ref", "expiry_rule",
                }:
                    if not axis.get(field):
                        errors.append(f"axis {axis_id}: {field} is required for v3 timing/synastry")
                if payload["schema_version"] in {"3.1", "3.2"}:
                    adjudication = axis.get("timing_manifestation_adjudication")
                    required_adjudication = {
                        "natal_node_state_refs", "activation_interface_refs", "matched_trigger_refs",
                        "overlay_function_transition", "relation_requalification_refs",
                        "shared_node_competition_ref", "retained_natal_route_ref",
                        "temporary_relation_function", "role_mapping_disposition", "role_candidate_refs",
                        "impact_bounds_ref", "runtime_context_refs", "expiry_rule",
                    }
                    if not isinstance(adjudication, dict):
                        errors.append(f"axis {axis_id}: timing_manifestation_adjudication must be an object")
                    else:
                        _need(adjudication, required_adjudication, f"axis {axis_id} adjudication", errors)
                        for field in {
                            "natal_node_state_refs", "activation_interface_refs", "matched_trigger_refs",
                            "relation_requalification_refs", "role_candidate_refs", "runtime_context_refs",
                        }:
                            if not isinstance(adjudication.get(field), list):
                                errors.append(f"axis {axis_id} adjudication: {field} must be a list")
                        if adjudication.get("role_mapping_disposition") not in ROLE_MAPPING_DISPOSITIONS:
                            errors.append(f"axis {axis_id} adjudication: invalid role_mapping_disposition")
                        if (
                            adjudication.get("role_mapping_disposition") == "candidate-requested"
                            and not adjudication.get("role_candidate_refs")
                        ):
                            errors.append(f"axis {axis_id} adjudication: candidate-requested needs role_candidate_refs")
                        for field in {
                            "overlay_function_transition", "shared_node_competition_ref",
                            "retained_natal_route_ref", "temporary_relation_function",
                            "impact_bounds_ref", "expiry_rule",
                        }:
                            if not adjudication.get(field):
                                errors.append(f"axis {axis_id} adjudication: {field} cannot be empty")

    if payload["schema_version"] in {"3.1", "3.2"}:
        for disposition in profile_dispositions:
            if not isinstance(disposition, dict):
                continue
            unknown_axes = set(disposition.get("axis_ids", [])) - set(axes_by_id)
            if unknown_axes:
                errors.append(f"facet {disposition.get('facet_id')}: unknown axis_ids {sorted(unknown_axes)}")
            if disposition.get("disposition") == "primary":
                primary_refs = [
                    axis_id for axis_id in disposition.get("axis_ids", [])
                    if axes_by_id.get(axis_id, {}).get("axis_role") == "primary"
                ]
                if not primary_refs:
                    errors.append(f"facet {disposition.get('facet_id')}: primary disposition needs a primary axis")

    if payload["schema_version"] in {"2.1", "2.2", "2.3", "3.0", "3.1", "3.2"}:
        deep_queries = payload.get("deep_card_queries")
        if not isinstance(deep_queries, list) or not deep_queries:
            errors.append("deep_card_queries: schema v2.1+ requires a non-empty list")
        else:
            query_ids: set[str] = set()
            foundation_count = 0
            required_query_fields = {
                "query_id", "axis_id", "symbol_family", "symbol", "card_id", "reason_needed",
                "topic_axis", "required_source_layers", "query_status",
            }
            if payload["schema_version"] in {"2.2", "2.3", "3.0", "3.1", "3.2"}:
                required_query_fields |= {
                    "requested_unit_classes", "activation_basis_refs", "requested_carrier_scope",
                    "claim_ceiling", "excluded_uses",
                }
            if payload["schema_version"] in {"3.0", "3.1", "3.2"}:
                required_query_fields |= {
                    "selection_purpose", "excluded_unit_classes", "raw_card_access_requested",
                }
            for item in deep_queries:
                if not isinstance(item, dict):
                    errors.append("deep_card_queries: each query must be an object")
                    continue
                _need(item, required_query_fields, "deep_card_query", errors)
                query_id = item.get("query_id")
                if query_id in query_ids:
                    errors.append(f"deep_card_queries: duplicate query_id {query_id}")
                query_ids.add(query_id)
                family = item.get("symbol_family")
                if family not in DEEP_CARD_FAMILIES:
                    errors.append(f"deep_card_query {query_id}: invalid symbol_family")
                if item.get("query_status") not in DEEP_CARD_QUERY_STATUS:
                    errors.append(f"deep_card_query {query_id}: invalid query_status")
                axis_ref = item.get("axis_id")
                if family == "foundation":
                    if item.get("card_id") == "DC-FIVE-ELEMENTS-CORE":
                        foundation_count += 1
                    if axis_ref is not None:
                        errors.append(f"deep_card_query {query_id}: foundation axis_id must be null")
                elif axis_ref not in axes_by_id:
                    errors.append(f"deep_card_query {query_id}: unknown axis_id {axis_ref}")
                if not item.get("reason_needed") or not item.get("topic_axis"):
                    errors.append(f"deep_card_query {query_id}: reason_needed and topic_axis are required")
                if not item.get("required_source_layers"):
                    errors.append(f"deep_card_query {query_id}: required_source_layers cannot be empty")
                if payload["schema_version"] in {"2.2", "2.3", "3.0", "3.1", "3.2"}:
                    unit_classes = item.get("requested_unit_classes", [])
                    if not isinstance(unit_classes, list) or not unit_classes:
                        errors.append(f"deep_card_query {query_id}: requested_unit_classes cannot be empty")
                    else:
                        unknown_units = sorted(set(unit_classes) - DEEP_CARD_UNIT_CLASSES)
                        if unknown_units:
                            errors.append(f"deep_card_query {query_id}: unknown unit classes {unknown_units}")
                    carrier_scope = item.get("requested_carrier_scope")
                    if carrier_scope not in DEEP_CARD_CARRIER_SCOPES:
                        errors.append(f"deep_card_query {query_id}: invalid requested_carrier_scope")
                    if item.get("claim_ceiling") not in DEEP_CARD_CLAIM_CEILINGS:
                        errors.append(f"deep_card_query {query_id}: Topic claim_ceiling must be mechanism or candidate")
                    basis_refs = item.get("activation_basis_refs", [])
                    if not isinstance(basis_refs, list) or not basis_refs:
                        errors.append(f"deep_card_query {query_id}: activation_basis_refs cannot be empty")
                    excluded = item.get("excluded_uses")
                    if not isinstance(excluded, list):
                        errors.append(f"deep_card_query {query_id}: excluded_uses must be a list")
                    if payload["schema_version"] in {"3.0", "3.1", "3.2"}:
                        excluded_classes = item.get("excluded_unit_classes")
                        if not isinstance(excluded_classes, list):
                            errors.append(f"deep_card_query {query_id}: excluded_unit_classes must be a list")
                        else:
                            unknown_excluded = sorted(set(excluded_classes) - DEEP_CARD_UNIT_CLASSES)
                            if unknown_excluded:
                                errors.append(f"deep_card_query {query_id}: unknown excluded unit classes {unknown_excluded}")
                            overlap = sorted(set(unit_classes) & set(excluded_classes))
                            if overlap:
                                errors.append(f"deep_card_query {query_id}: requested and excluded unit classes overlap {overlap}")
                        if not item.get("selection_purpose"):
                            errors.append(f"deep_card_query {query_id}: selection_purpose cannot be empty")
                        if item.get("raw_card_access_requested") is not False:
                            errors.append(f"deep_card_query {query_id}: raw_card_access_requested must be false")
                        if "composite_domain_carrier" in unit_classes:
                            errors.append(
                                f"deep_card_query {query_id}: composite_domain_carrier must use domain_carrier_requests"
                            )
            if foundation_count != 1:
                errors.append("deep_card_queries: exactly one DC-FIVE-ELEMENTS-CORE query is required")

    if payload["schema_version"] in {"3.0", "3.1", "3.2"}:
        domain_requests = payload.get("domain_carrier_requests")
        if not isinstance(domain_requests, list):
            errors.append("domain_carrier_requests: v3 requires a list")
        else:
            request_ids: set[str] = set()
            required_fields = {
                "request_id", "axis_id", "topic_axis", "carrier_family", "question_target",
                "process_ref", "controller_or_carrier_refs", "relation_function_refs",
                "position_visibility_refs", "capability_gate_refs", "required_contribution_types",
                "excluded_shortcuts", "claim_ceiling", "request_status",
            }
            if payload["schema_version"] in {"3.1", "3.2"} and payload["topic_intent"] in {"timing", "synastry"}:
                required_fields |= {
                    "relation_function_transition_ref", "retained_natal_route_ref",
                    "runtime_context_refs", "role_candidate_scope", "impact_assessment_refs",
                }
            for item in domain_requests:
                if not isinstance(item, dict):
                    errors.append("domain_carrier_requests: each request must be an object")
                    continue
                _need(item, required_fields, "domain_carrier_request", errors)
                request_id = item.get("request_id")
                if not isinstance(request_id, str) or not request_id:
                    errors.append("domain_carrier_request: request_id must be a non-empty string")
                    continue
                if request_id in request_ids:
                    errors.append(f"domain_carrier_requests: duplicate request_id {request_id}")
                request_ids.add(request_id)
                if item.get("axis_id") not in axes_by_id:
                    errors.append(f"domain_carrier_request {request_id}: unknown axis_id {item.get('axis_id')}")
                if item.get("carrier_family") not in DOMAIN_CARRIER_FAMILIES:
                    errors.append(f"domain_carrier_request {request_id}: invalid carrier_family")
                if item.get("claim_ceiling") != "candidate":
                    errors.append(f"domain_carrier_request {request_id}: Topic claim_ceiling must be candidate")
                if item.get("request_status") not in DEEP_CARD_QUERY_STATUS:
                    errors.append(f"domain_carrier_request {request_id}: invalid request_status")
                for field in {
                    "controller_or_carrier_refs", "position_visibility_refs", "capability_gate_refs",
                    "required_contribution_types", "excluded_shortcuts",
                }:
                    value = item.get(field)
                    if not isinstance(value, list) or not value:
                        errors.append(f"domain_carrier_request {request_id}: {field} must be a non-empty list")
                relation_refs = item.get("relation_function_refs")
                if not isinstance(relation_refs, list):
                    errors.append(f"domain_carrier_request {request_id}: relation_function_refs must be a list")
                if not item.get("question_target") or not item.get("process_ref"):
                    errors.append(f"domain_carrier_request {request_id}: question_target and process_ref are required")
                if payload["schema_version"] in {"3.1", "3.2"} and payload["topic_intent"] in {"timing", "synastry"}:
                    for field in {"runtime_context_refs", "role_candidate_scope", "impact_assessment_refs"}:
                        value = item.get(field)
                        if not isinstance(value, list) or not value:
                            errors.append(f"domain_carrier_request {request_id}: {field} must be a non-empty list")
                    for field in {"relation_function_transition_ref", "retained_natal_route_ref"}:
                        if not item.get(field):
                            errors.append(f"domain_carrier_request {request_id}: {field} cannot be empty")
                    if (
                        payload.get("runtime_context_policy", {}).get("context_status") != "known-from-question"
                        and len(item.get("role_candidate_scope", [])) < 2
                    ):
                        errors.append(
                            f"domain_carrier_request {request_id}: unknown/withheld context needs at least two role candidates"
                        )

    if payload["schema_version"] in {"2.3", "3.0", "3.1", "3.2"}:
        coverage = payload.get("coverage_profile")
        required_coverage = {
            "profile_id", "scope_type", "required_question_slices", "covered_question_slice_ids",
            "not_applicable_receipts", "deferred_or_source_gap_receipts", "primary_axis_count",
            "required_primary_axis_count", "expected_primary_finding_count", "coverage_verdict",
        }
        if not isinstance(coverage, dict):
            errors.append("coverage_profile: must be an object")
        else:
            _need(coverage, required_coverage, "coverage_profile", errors)
            list_fields = {
                "required_question_slices", "covered_question_slice_ids", "not_applicable_receipts",
                "deferred_or_source_gap_receipts",
            }
            for field in list_fields:
                if not isinstance(coverage.get(field), list):
                    errors.append(f"coverage_profile.{field}: must be a list")
            count_fields = {"primary_axis_count", "required_primary_axis_count", "expected_primary_finding_count"}
            for field in count_fields:
                value = coverage.get(field)
                if not isinstance(value, int) or isinstance(value, bool) or value < 0:
                    errors.append(f"coverage_profile.{field}: must be a non-negative integer")

            required_slices = set(coverage.get("required_question_slices", []))
            disposed_slices = (
                set(coverage.get("covered_question_slice_ids", []))
                | set(coverage.get("not_applicable_receipts", []))
                | set(coverage.get("deferred_or_source_gap_receipts", []))
            )
            missing_slices = sorted(required_slices - disposed_slices)
            if missing_slices:
                errors.append(f"coverage_profile: required question slices lack disposition {missing_slices}")

            primary_required = [
                axis for axis in axes_by_id.values()
                if axis.get("axis_role") == "primary" and axis.get("finding_disposition") == "required"
            ]
            if coverage.get("primary_axis_count") != sum(
                axis.get("axis_role") == "primary" for axis in axes_by_id.values()
            ):
                errors.append("coverage_profile: primary_axis_count must equal actual primary axes")
            if coverage.get("required_primary_axis_count") != len(primary_required):
                errors.append("coverage_profile: required_primary_axis_count must equal required primary axes")
            if coverage.get("expected_primary_finding_count") != len(primary_required):
                errors.append("coverage_profile: expected_primary_finding_count must equal required primary axes")

        atoms = payload.get("scope_atoms")
        if not isinstance(atoms, list) or not atoms:
            errors.append("scope_atoms: schema v2.3 requires a non-empty list")
        else:
            atom_ids: set[str] = set()
            annual_axis_owners: dict[str, str] = {}
            required_finding_atom_count = 0
            for atom in atoms:
                if not isinstance(atom, dict):
                    errors.append("scope_atoms: each atom must be an object")
                    continue
                _need(
                    atom,
                    {"atom_id", "atom_type", "label", "required", "axis_ids", "finding_disposition", "not_applicable_reason"},
                    "scope_atom",
                    errors,
                )
                atom_id = atom.get("atom_id")
                if not isinstance(atom_id, str) or not atom_id:
                    errors.append("scope_atom: atom_id must be a non-empty string")
                    continue
                if atom_id in atom_ids:
                    errors.append(f"scope_atoms: duplicate atom_id {atom_id}")
                atom_ids.add(atom_id)
                axis_ids = atom.get("axis_ids", [])
                if not isinstance(axis_ids, list):
                    errors.append(f"scope_atom {atom_id}: axis_ids must be a list")
                    continue
                unknown_axes = set(axis_ids) - set(axes_by_id)
                if unknown_axes:
                    errors.append(f"scope_atom {atom_id}: unknown axis_ids {sorted(unknown_axes)}")
                if atom.get("required") is True:
                    if atom.get("finding_disposition") == "required":
                        required_finding_atom_count += 1
                        primary_refs = [
                            axis_id for axis_id in axis_ids
                            if axes_by_id.get(axis_id, {}).get("axis_role") == "primary"
                            and axes_by_id.get(axis_id, {}).get("finding_disposition") == "required"
                        ]
                        if not primary_refs:
                            errors.append(f"scope_atom {atom_id}: required atom needs a required primary axis")
                    elif atom.get("finding_disposition") not in {"not-applicable", "deferred", "source-gap"}:
                        errors.append(f"scope_atom {atom_id}: required atom needs an explicit disposition")
                    if atom.get("finding_disposition") == "not-applicable" and not atom.get("not_applicable_reason"):
                        errors.append(f"scope_atom {atom_id}: not-applicable needs a reason")
                if atom.get("atom_type") == "timing-annual" and atom.get("required") is True:
                    for axis_id in axis_ids:
                        axis = axes_by_id.get(axis_id, {})
                        if axis.get("axis_role") != "primary" or axis.get("finding_disposition") != "required":
                            continue
                        previous = annual_axis_owners.get(axis_id)
                        if previous and previous != atom_id:
                            errors.append(
                                f"scope_atoms: annual atoms {previous} and {atom_id} share primary axis {axis_id}; "
                                "each requested year needs its own axis"
                            )
                        annual_axis_owners[axis_id] = atom_id
            if coverage and isinstance(coverage, dict):
                expected_count = coverage.get("expected_primary_finding_count")
                if isinstance(expected_count, int) and expected_count < required_finding_atom_count:
                    errors.append(
                        "coverage_profile: expected_primary_finding_count is below required scope-atom minimum"
                    )

    handoff = payload["finding_handoff"]
    if isinstance(handoff, dict):
        _need(handoff, {"primary_axis_ids", "supporting_axis_ids", "expected_primary_findings", "cross_topic_refs", "unresolved_source_gaps"}, "finding_handoff", errors)
        expected_primary = {axis_id for axis_id, axis in axes_by_id.items() if axis.get("axis_role") == "primary"}
        if set(handoff.get("primary_axis_ids", [])) != expected_primary:
            errors.append("finding_handoff: primary_axis_ids must match primary axes")
        if payload["schema_version"] in {"2.3", "3.0", "3.1", "3.2"}:
            expected_required = sum(
                axis.get("axis_role") == "primary" and axis.get("finding_disposition") == "required"
                for axis in axes_by_id.values()
            )
            expected_findings = handoff.get("expected_primary_findings")
            if not isinstance(expected_findings, int) or isinstance(expected_findings, bool):
                errors.append("finding_handoff: v2.3+ expected_primary_findings must be an integer")
            elif expected_findings != expected_required:
                errors.append("finding_handoff: expected_primary_findings must equal required primary axes")
            coverage = payload.get("coverage_profile", {})
            if isinstance(coverage, dict) and expected_findings != coverage.get("expected_primary_finding_count"):
                errors.append("finding_handoff: expected_primary_findings must equal coverage profile count")
    else:
        errors.append("finding_handoff: must be an object")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate Topic Lens typed state.")
    parser.add_argument("state")
    args = parser.parse_args()
    path = Path(args.state)
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
        errors = validate_state(payload)
    except (OSError, json.JSONDecodeError) as exc:
        errors = [f"state unreadable: {exc}"]
    result = {
        "verdict": "PASS" if not errors else "FAIL",
        "state": str(path),
        "errors": errors,
        "boundary": "Contract validation only; controller and eligibility remain analytical judgments.",
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
