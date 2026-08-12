#!/usr/bin/env python3
"""Validate Bazi Taiji-field Topic Lens v4.1 without interpreting the chart."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Iterable


PROHIBITED_CONCLUSION_KEYS = {
    "external_result_target",
    "direct_answer",
    "direct_answer_summary",
    "final_verdict",
    "preferred_carrier",
    "role_ranking",
    "career_preference",
    "event_prediction",
}
QUESTION_SOURCES = {"user-verbatim", "scope-confirmed", "faithful-restatement"}
FACET_DISPOSITIONS = {"primary", "supporting", "cross-ref", "not-applicable", "source-gap", "pending-finding"}
SPECIFICITY_FLOORS = {"L1-outcome-level", "L2-domain-nature", "L3-action-material", "L4-carrier-family", "L5-exact-identity-event"}
PALETTE_LEVELS = {"L2-domain-nature", "L3-action-material", "L4-carrier-family"}


def _need(obj: Any, fields: Iterable[str], label: str, errors: list[str]) -> None:
    if not isinstance(obj, dict):
        errors.append(f"{label}: must be an object")
        return
    missing = [field for field in fields if field not in obj]
    if missing:
        errors.append(f"{label}: missing {', '.join(missing)}")


def _walk(value: Any, path: str = "$"):
    if isinstance(value, dict):
        for key, child in value.items():
            child_path = f"{path}.{key}"
            yield child_path, key, child
            yield from _walk(child, child_path)
    elif isinstance(value, list):
        for index, child in enumerate(value):
            yield from _walk(child, f"{path}[{index}]")


def _nonempty_list(value: Any) -> bool:
    return isinstance(value, list) and bool(value)


def validate_lens(payload: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    _need(
        payload,
        {
            "schema_version", "case_id", "topic_id", "structure_freeze_id",
            "report_scope_ref", "taiji_field", "coverage_facets", "mandatory_judgment_dimensions",
            "explicit_reader_questions", "topic_process_axes", "deep_card_queries",
            "domain_carrier_requests", "candidate_palette_requests", "source_and_kernel_handoff",
        },
        "lens",
        errors,
    )
    if errors:
        return errors
    if str(payload.get("schema_version")) != "4.1":
        errors.append("lens.schema_version: new lenses must use 4.1")

    for path, key, value in _walk(payload):
        if key in PROHIBITED_CONCLUSION_KEYS:
            errors.append(f"{path}: conclusion field is prohibited in Topic Lens")
        if key == "answer_status" and value not in (None, "pending"):
            errors.append(f"{path}: Lens cannot declare a completed or conditional answer")

    field = payload.get("taiji_field")
    _need(
        field,
        {
            "user_language_center", "field_type", "people_or_roles_in_scope",
            "matters_or_objects_in_scope", "result_dimensions_to_determine", "boundaries",
        },
        "taiji_field",
        errors,
    )
    if isinstance(field, dict) and not str(field.get("user_language_center", "")).strip():
        errors.append("taiji_field.user_language_center: cannot be empty")

    facets = payload.get("coverage_facets")
    if not isinstance(facets, list) or not facets:
        errors.append("coverage_facets: must be a non-empty list")
        facets = []
    facet_ids: set[str] = set()
    for index, facet in enumerate(facets):
        label = f"coverage_facets[{index}]"
        _need(
            facet,
            {"facet_id", "coverage_status", "reader_relevance", "attached_axis_ids", "final_disposition"},
            label,
            errors,
        )
        if not isinstance(facet, dict):
            continue
        facet_id = str(facet.get("facet_id", "")).strip()
        if not facet_id or facet_id in facet_ids:
            errors.append(f"{label}.facet_id: must be non-empty and unique")
        facet_ids.add(facet_id)
        if facet.get("final_disposition") not in FACET_DISPOSITIONS:
            errors.append(f"{label}.final_disposition: invalid disposition")

    dimensions = payload.get("mandatory_judgment_dimensions")
    if not isinstance(dimensions, list) or not dimensions:
        errors.append("mandatory_judgment_dimensions: must be a non-empty list")
        dimensions = []
    dimension_ids: set[str] = set()
    endpoint_ids: set[str] = set()
    for index, dimension in enumerate(dimensions):
        label = f"mandatory_judgment_dimensions[{index}]"
        _need(
            dimension,
            {
                "dimension_id", "required_disposition", "specificity_floor",
                "supporting_process_refs", "candidate_axis_refs",
                "downstream_claim_endpoint", "no_silent_merge",
            },
            label,
            errors,
        )
        if not isinstance(dimension, dict):
            continue
        dimension_id = str(dimension.get("dimension_id", "")).strip()
        endpoint_id = str(dimension.get("downstream_claim_endpoint", "")).strip()
        if not dimension_id or dimension_id in dimension_ids:
            errors.append(f"{label}.dimension_id: must be non-empty and unique")
        dimension_ids.add(dimension_id)
        if not endpoint_id or endpoint_id in endpoint_ids:
            errors.append(f"{label}.downstream_claim_endpoint: must be non-empty and unique")
        endpoint_ids.add(endpoint_id)
        if dimension.get("specificity_floor") not in SPECIFICITY_FLOORS:
            errors.append(f"{label}.specificity_floor: invalid specificity level")
        if dimension.get("no_silent_merge") is not True:
            errors.append(f"{label}.no_silent_merge: must be true")
        if not isinstance(dimension.get("supporting_process_refs"), list):
            errors.append(f"{label}.supporting_process_refs: must be a list")
        if not isinstance(dimension.get("candidate_axis_refs"), list):
            errors.append(f"{label}.candidate_axis_refs: must be a list")

    questions = payload.get("explicit_reader_questions")
    if not isinstance(questions, list):
        errors.append("explicit_reader_questions: must be a list")
        questions = []
    question_ids: set[str] = set()
    for index, question in enumerate(questions):
        label = f"explicit_reader_questions[{index}]"
        _need(
            question,
            {
                "question_id", "exact_reader_question", "source_kind", "source_ref",
                "answer_target", "allowed_answer_statuses", "closure_key",
            },
            label,
            errors,
        )
        if not isinstance(question, dict):
            continue
        question_id = str(question.get("question_id", "")).strip()
        if not question_id or question_id in question_ids:
            errors.append(f"{label}.question_id: must be non-empty and unique")
        question_ids.add(question_id)
        if question.get("source_kind") not in QUESTION_SOURCES:
            errors.append(f"{label}.source_kind: must prove real user/scope provenance")
        if not str(question.get("source_ref", "")).strip():
            errors.append(f"{label}.source_ref: cannot be empty")
        exact = str(question.get("exact_reader_question", "")).strip()
        if len(exact) < 6:
            errors.append(f"{label}.exact_reader_question: too short to be a real question")
        if question.get("facet_id") in facet_ids and question.get("source_kind") != "user-verbatim":
            errors.append(f"{label}: coverage facet cannot be promoted to a synthetic question")

    axes = payload.get("topic_process_axes")
    if not isinstance(axes, list) or not axes:
        errors.append("topic_process_axes: must be a non-empty list")
        axes = []
    axis_ids: set[str] = set()
    stem_refs: set[str] = set()
    branch_refs: set[str] = set()
    for index, axis in enumerate(axes):
        label = f"topic_process_axes[{index}]"
        _need(
            axis,
            {
                "axis_id", "axis_formation_basis", "process_ref", "route_closure_receipt_ref",
                "phase_focus_refs", "ten_god_chain_plan", "stem_branch_anchor_plan",
                "scene_kernel_required", "attached_facet_ids", "attached_explicit_question_ids",
            },
            label,
            errors,
        )
        if not isinstance(axis, dict):
            continue
        axis_id = str(axis.get("axis_id", "")).strip()
        if not axis_id or axis_id in axis_ids:
            errors.append(f"{label}.axis_id: must be non-empty and unique")
        axis_ids.add(axis_id)
        for key in ("process_ref", "route_closure_receipt_ref"):
            if not str(axis.get(key, "")).strip():
                errors.append(f"{label}.{key}: cannot be empty")
        if not _nonempty_list(axis.get("phase_focus_refs")):
            errors.append(f"{label}.phase_focus_refs: cannot be empty")
        if axis.get("scene_kernel_required") is not True:
            errors.append(f"{label}.scene_kernel_required: must be true")

        chain = axis.get("ten_god_chain_plan")
        _need(
            chain,
            {
                "domain_body", "required_relation_functions", "result_dimension_to_determine",
                "feedback_and_competition_to_check", "forbidden_shortcuts",
            },
            f"{label}.ten_god_chain_plan",
            errors,
        )
        if isinstance(chain, dict):
            if not str(chain.get("domain_body", "")).strip():
                errors.append(f"{label}.ten_god_chain_plan.domain_body: cannot be empty")
            if not _nonempty_list(chain.get("required_relation_functions")):
                errors.append(f"{label}.ten_god_chain_plan.required_relation_functions: cannot be empty")

        anchors = axis.get("stem_branch_anchor_plan")
        _need(
            anchors,
            {
                "visible_stem_refs", "branch_position_refs", "hidden_stem_refs",
                "pillar_role_refs", "relation_after_state_refs",
            },
            f"{label}.stem_branch_anchor_plan",
            errors,
        )
        if isinstance(anchors, dict):
            local_stems = anchors.get("visible_stem_refs", []) + anchors.get("hidden_stem_refs", [])
            local_branches = anchors.get("branch_position_refs", [])
            if not local_stems:
                errors.append(f"{label}.stem_branch_anchor_plan: needs a visible or hidden stem anchor")
            if not local_branches:
                errors.append(f"{label}.stem_branch_anchor_plan.branch_position_refs: cannot be empty")
            stem_refs.update(str(item) for item in local_stems)
            branch_refs.update(str(item) for item in local_branches)
        for facet_id in axis.get("attached_facet_ids", []):
            if facet_id not in facet_ids:
                errors.append(f"{label}.attached_facet_ids: unknown facet {facet_id}")
        for question_id in axis.get("attached_explicit_question_ids", []):
            if question_id not in question_ids:
                errors.append(f"{label}.attached_explicit_question_ids: unknown question {question_id}")

    for index, facet in enumerate(facets):
        for axis_id in facet.get("attached_axis_ids", []) if isinstance(facet, dict) else []:
            if axis_id not in axis_ids:
                errors.append(f"coverage_facets[{index}].attached_axis_ids: unknown axis {axis_id}")

    queries = payload.get("deep_card_queries")
    if not isinstance(queries, list):
        errors.append("deep_card_queries: must be a list")
        queries = []
    query_text = json.dumps(queries, ensure_ascii=False)
    if axes and "TEN-GODS" not in query_text.upper() and "十神" not in query_text:
        errors.append("deep_card_queries: ten-gods core request is required")
    for stem_ref in stem_refs:
        if stem_ref and stem_ref not in query_text:
            errors.append(f"deep_card_queries: missing stem/hidden-stem anchor {stem_ref}")
    for branch_ref in branch_refs:
        if branch_ref and branch_ref not in query_text:
            errors.append(f"deep_card_queries: missing branch anchor {branch_ref}")

    requests = payload.get("domain_carrier_requests")
    if not isinstance(requests, list):
        errors.append("domain_carrier_requests: must be a list")

    palettes = payload.get("candidate_palette_requests")
    if not isinstance(palettes, list) or not palettes:
        errors.append("candidate_palette_requests: must be a non-empty list")
        palettes = []
    for index, palette in enumerate(palettes):
        label = f"candidate_palette_requests[{index}]"
        _need(
            palette,
            {
                "palette_id", "judgment_dimension_refs", "requested_specificity_levels",
                "activation_anchor_refs", "excluded_preselection",
            },
            label,
            errors,
        )
        if not isinstance(palette, dict):
            continue
        unknown_dimensions = sorted(set(palette.get("judgment_dimension_refs", [])) - dimension_ids)
        if unknown_dimensions:
            errors.append(f"{label}.judgment_dimension_refs: unknown dimensions {unknown_dimensions}")
        levels = set(palette.get("requested_specificity_levels", []))
        if not levels or not levels <= PALETTE_LEVELS:
            errors.append(f"{label}.requested_specificity_levels: must use L2-L4 palette levels")
        if not _nonempty_list(palette.get("activation_anchor_refs")):
            errors.append(f"{label}.activation_anchor_refs: cannot be empty")

    handoff = payload.get("source_and_kernel_handoff")
    _need(
        handoff,
        {
            "required_claim_endpoint_refs", "endpoint_differentiation_required",
            "scene_synthesis_count_policy", "required_material_spread",
            "required_ten_god_stem_branch_synthesis",
        },
        "source_and_kernel_handoff",
        errors,
    )
    if isinstance(handoff, dict):
        if handoff.get("required_material_spread") is not True:
            errors.append("source_and_kernel_handoff.required_material_spread: must be true")
        if handoff.get("required_ten_god_stem_branch_synthesis") is not True:
            errors.append("source_and_kernel_handoff.required_ten_god_stem_branch_synthesis: must be true")
        if handoff.get("endpoint_differentiation_required") is not True:
            errors.append("source_and_kernel_handoff.endpoint_differentiation_required: must be true")
        if handoff.get("scene_synthesis_count_policy") != "chart-derived-after-differentiation":
            errors.append("source_and_kernel_handoff.scene_synthesis_count_policy: invalid policy")
        endpoint_refs = handoff.get("required_claim_endpoint_refs")
        if not isinstance(endpoint_refs, list) or set(endpoint_refs) != endpoint_ids:
            errors.append("source_and_kernel_handoff.required_claim_endpoint_refs: must exactly cover judgment endpoints")

    return errors


def _load(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    if path.suffix.lower() == ".json":
        value = json.loads(text)
    else:
        try:
            import yaml  # type: ignore
        except ImportError as exc:
            raise ValueError("YAML input requires PyYAML; use JSON or install PyYAML") from exc
        value = yaml.safe_load(text)
    if not isinstance(value, dict):
        raise ValueError("lens root must be an object")
    return value


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path)
    args = parser.parse_args()
    try:
        payload = _load(args.path)
        errors = validate_lens(payload)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(json.dumps({"status": "FAIL", "errors": [str(exc)]}, ensure_ascii=False, indent=2))
        return 2
    status = "PASS" if not errors else "FAIL"
    print(json.dumps({"status": status, "errors": errors}, ensure_ascii=False, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
