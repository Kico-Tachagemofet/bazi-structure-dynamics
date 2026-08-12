#!/usr/bin/env python3
"""Validate domain-carrier promotion receipts without choosing carriers."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


RANKS = {"candidate", "supported", "preferred", "assertable"}
STATUSES = {"candidate-only", "resolved", "source-gap", "not-applicable"}
CONTEXT_BRANCH_STATUSES = {"known-from-question", "conditional", "not-applicable"}
SPECIFICITY_LEVELS = {
    "L1-outcome-level", "L2-domain-nature", "L3-action-material",
    "L4-carrier-family", "L5-exact-identity-event",
}
SPECIFICITY_DISPOSITIONS = {"directional-verdict", "not-applicable", "source-gap", "not-claimed"}
REQUIRED_GROUPS_FOR_SUPPORT = {
    "process_or_work_property", "relation_function", "position_visibility_or_route",
}
ALL_GROUPS = REQUIRED_GROUPS_FOR_SUPPORT | {
    "daymaster_access_and_sustainability", "destination_and_external_result",
}


def _need(obj: dict[str, Any], fields: set[str], label: str, errors: list[str]) -> None:
    missing = sorted(fields - set(obj))
    if missing:
        errors.append(f"{label}: missing {', '.join(missing)}")


def _nonempty_list(value: Any) -> bool:
    return isinstance(value, list) and bool(value)


def validate_resolution(payload: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    _need(
        payload,
        {
            "schema_version", "case_id", "topic_id", "structure_freeze_id",
            "topic_lens_ref", "runtime_packet_ref", "resolutions",
        },
        "resolution_packet",
        errors,
    )
    if errors:
        return errors
    if payload.get("schema_version") != "2.0":
        errors.append("resolution_packet: schema_version must be 2.0")
    _need(payload, {"runtime_context_policy_ref"}, "resolution_packet", errors)
    if not payload.get("runtime_context_policy_ref"):
        errors.append("resolution_packet: runtime_context_policy_ref cannot be empty in v2.0")
    resolutions = payload.get("resolutions")
    if not isinstance(resolutions, list):
        errors.append("resolutions: must be a list")
        return errors

    resolution_ids: set[str] = set()
    for resolution in resolutions:
        if not isinstance(resolution, dict):
            errors.append("resolutions: each item must be an object")
            continue
        _need(
            resolution,
            {
                "resolution_id", "domain_request_ref", "axis_id", "judgment_dimension_refs",
                "carrier_family", "specificity_verdicts", "resolution_status",
                "candidate_pool", "selected_carrier_ids",
            },
            "resolution",
            errors,
        )
        resolution_id = resolution.get("resolution_id")
        if not isinstance(resolution_id, str) or not resolution_id:
            errors.append("resolution: resolution_id must be a non-empty string")
            continue
        if resolution_id in resolution_ids:
            errors.append(f"resolutions: duplicate resolution_id {resolution_id}")
        resolution_ids.add(resolution_id)
        if not resolution.get("domain_request_ref") or not resolution.get("axis_id") or not resolution.get("carrier_family"):
            errors.append(f"resolution {resolution_id}: request, axis, and family are required")
        if not _nonempty_list(resolution.get("judgment_dimension_refs")):
            errors.append(f"resolution {resolution_id}: judgment_dimension_refs must be non-empty")
        specificity_verdicts = resolution.get("specificity_verdicts")
        if not isinstance(specificity_verdicts, list):
            errors.append(f"resolution {resolution_id}: specificity_verdicts must be a list")
            specificity_verdicts = []
        levels_seen: set[str] = set()
        for verdict in specificity_verdicts:
            if not isinstance(verdict, dict):
                errors.append(f"resolution {resolution_id}: each specificity verdict must be an object")
                continue
            _need(
                verdict,
                {"specificity_level", "disposition", "verdict", "rank", "support_or_gap_refs", "enters_finding"},
                f"resolution {resolution_id} specificity verdict",
                errors,
            )
            level = verdict.get("specificity_level")
            if level not in SPECIFICITY_LEVELS or level in levels_seen:
                errors.append(f"resolution {resolution_id}: specificity levels must be valid and unique")
            levels_seen.add(level)
            if verdict.get("disposition") not in SPECIFICITY_DISPOSITIONS:
                errors.append(f"resolution {resolution_id}/{level}: invalid disposition")
            if verdict.get("rank") not in RANKS:
                errors.append(f"resolution {resolution_id}/{level}: invalid rank")
            if not verdict.get("verdict") or not isinstance(verdict.get("support_or_gap_refs"), list):
                errors.append(f"resolution {resolution_id}/{level}: verdict and support_or_gap_refs are required")
            if not isinstance(verdict.get("enters_finding"), bool):
                errors.append(f"resolution {resolution_id}/{level}: enters_finding must be boolean")
        if levels_seen != SPECIFICITY_LEVELS:
            errors.append(f"resolution {resolution_id}: specificity_verdicts must cover L1-L5")
        status = resolution.get("resolution_status")
        if status not in STATUSES:
            errors.append(f"resolution {resolution_id}: invalid resolution_status")
        candidates = resolution.get("candidate_pool")
        if not isinstance(candidates, list):
            errors.append(f"resolution {resolution_id}: candidate_pool must be a list")
            continue
        selected = resolution.get("selected_carrier_ids")
        if not isinstance(selected, list):
            errors.append(f"resolution {resolution_id}: selected_carrier_ids must be a list")
            selected = []

        candidate_ids: set[str] = set()
        rank_by_id: dict[str, str] = {}
        for candidate in candidates:
            if not isinstance(candidate, dict):
                errors.append(f"resolution {resolution_id}: each candidate must be an object")
                continue
            required_candidate_fields = {
                    "candidate_id", "label", "specificity_level", "rank", "source_lead_refs", "contributing_card_ids",
                    "contribution_groups", "independent_anchor_refs", "passed_gates",
                    "blocked_or_missing_gates", "alternative_carrier_ids", "comparison_reason",
                    "single_symbol_card_sufficient", "lower_level_verdicts_preserved",
                    "assertable_fact_refs", "forbidden_direct_inferences",
                }
            required_candidate_fields |= {
                "relation_function_transition", "retained_natal_route_ref",
                "runtime_context_branches", "structural_impact_bounds_ref",
            }
            _need(
                candidate,
                required_candidate_fields,
                f"resolution {resolution_id} candidate",
                errors,
            )
            candidate_id = candidate.get("candidate_id")
            if not isinstance(candidate_id, str) or not candidate_id:
                errors.append(f"resolution {resolution_id}: candidate_id must be a non-empty string")
                continue
            if candidate_id in candidate_ids:
                errors.append(f"resolution {resolution_id}: duplicate candidate_id {candidate_id}")
            candidate_ids.add(candidate_id)
            rank = candidate.get("rank")
            rank_by_id[candidate_id] = rank
            if rank not in RANKS:
                errors.append(f"candidate {candidate_id}: invalid rank")
                continue
            if candidate.get("specificity_level") not in SPECIFICITY_LEVELS:
                errors.append(f"candidate {candidate_id}: invalid specificity_level")
            if candidate.get("single_symbol_card_sufficient") is not False:
                errors.append(f"candidate {candidate_id}: single_symbol_card_sufficient must be false")
            if candidate.get("lower_level_verdicts_preserved") is not True:
                errors.append(f"candidate {candidate_id}: lower_level_verdicts_preserved must be true")
            groups = candidate.get("contribution_groups")
            if not isinstance(groups, dict) or set(groups) != ALL_GROUPS:
                errors.append(f"candidate {candidate_id}: contribution_groups must contain exactly the five groups")
                groups = {}
            else:
                for group, refs in groups.items():
                    if not isinstance(refs, list):
                        errors.append(f"candidate {candidate_id}: contribution group {group} must be a list")
            for field in {
                "source_lead_refs", "contributing_card_ids", "independent_anchor_refs",
                "passed_gates", "blocked_or_missing_gates", "alternative_carrier_ids",
                "assertable_fact_refs", "forbidden_direct_inferences",
            }:
                if not isinstance(candidate.get(field), list):
                    errors.append(f"candidate {candidate_id}: {field} must be a list")

            if rank in {"supported", "preferred", "assertable"}:
                missing_groups = sorted(
                    group for group in REQUIRED_GROUPS_FOR_SUPPORT if not groups.get(group)
                )
                if missing_groups:
                    errors.append(f"candidate {candidate_id}: supported+ missing contribution groups {missing_groups}")
                anchors = candidate.get("independent_anchor_refs", [])
                if len(set(anchors)) < 2:
                    errors.append(f"candidate {candidate_id}: supported+ needs at least two independent anchors")
                if not _nonempty_list(candidate.get("passed_gates")):
                    errors.append(f"candidate {candidate_id}: supported+ needs passed_gates")
                if not _nonempty_list(candidate.get("source_lead_refs")):
                    errors.append(f"candidate {candidate_id}: supported+ needs source_lead_refs")
            if rank in {"preferred", "assertable"}:
                if not _nonempty_list(candidate.get("alternative_carrier_ids")):
                    errors.append(f"candidate {candidate_id}: preferred+ needs an alternative carrier")
                if not candidate.get("comparison_reason"):
                    errors.append(f"candidate {candidate_id}: preferred+ needs comparison_reason")
            if rank == "assertable" and not _nonempty_list(candidate.get("assertable_fact_refs")):
                errors.append(f"candidate {candidate_id}: assertable needs specific fact refs")
            if payload.get("schema_version") == "2.0":
                for field in {
                    "relation_function_transition", "retained_natal_route_ref",
                    "structural_impact_bounds_ref",
                }:
                    if not candidate.get(field):
                        errors.append(f"candidate {candidate_id}: {field} cannot be empty in v2.0")
                branches = candidate.get("runtime_context_branches")
                if not isinstance(branches, list) or not branches:
                    errors.append(f"candidate {candidate_id}: runtime_context_branches must be a non-empty list")
                else:
                    branch_ids: set[str] = set()
                    conditional_count = 0
                    for branch in branches:
                        if not isinstance(branch, dict):
                            errors.append(f"candidate {candidate_id}: each runtime context branch must be an object")
                            continue
                        _need(
                            branch,
                            {
                                "branch_id", "context_status", "position_or_role_condition",
                                "carrier_expression", "agency_difference", "structural_claim_unchanged",
                                "context_used_as_structure_evidence",
                            },
                            f"candidate {candidate_id} runtime branch",
                            errors,
                        )
                        branch_id = branch.get("branch_id")
                        if not isinstance(branch_id, str) or not branch_id:
                            errors.append(f"candidate {candidate_id}: runtime branch_id must be non-empty")
                        elif branch_id in branch_ids:
                            errors.append(f"candidate {candidate_id}: duplicate runtime branch_id {branch_id}")
                        else:
                            branch_ids.add(branch_id)
                        if branch.get("context_status") not in CONTEXT_BRANCH_STATUSES:
                            errors.append(f"candidate {candidate_id}: invalid runtime context_status")
                        if branch.get("context_status") == "conditional":
                            conditional_count += 1
                        if branch.get("structural_claim_unchanged") is not True:
                            errors.append(f"candidate {candidate_id}: runtime context cannot change structural claim")
                        if branch.get("context_used_as_structure_evidence") is not False:
                            errors.append(f"candidate {candidate_id}: runtime context cannot serve as structure evidence")
                        for field in {"position_or_role_condition", "carrier_expression", "agency_difference"}:
                            if not branch.get(field):
                                errors.append(f"candidate {candidate_id}: runtime branch {field} cannot be empty")
                    if conditional_count == 1:
                        errors.append(
                            f"candidate {candidate_id}: unresolved runtime context needs at least two conditional branches"
                        )

        unknown_selected = sorted(set(selected) - candidate_ids)
        if unknown_selected:
            errors.append(f"resolution {resolution_id}: selected unknown candidates {unknown_selected}")
        if status == "resolved":
            if not selected:
                errors.append(f"resolution {resolution_id}: resolved status needs selected carriers")
            elif any(rank_by_id.get(item) == "candidate" for item in selected):
                errors.append(f"resolution {resolution_id}: resolved selection cannot remain candidate-only")
        if status == "candidate-only" and any(rank_by_id.get(item) != "candidate" for item in selected):
            errors.append(f"resolution {resolution_id}: candidate-only status cannot select supported+ carriers")
        if status in {"source-gap", "not-applicable"} and selected:
            errors.append(f"resolution {resolution_id}: {status} cannot select carriers")

        for candidate in candidates:
            if not isinstance(candidate, dict):
                continue
            candidate_id = candidate.get("candidate_id")
            unknown_alternatives = sorted(set(candidate.get("alternative_carrier_ids", [])) - candidate_ids)
            if unknown_alternatives:
                errors.append(f"candidate {candidate_id}: unknown alternative carriers {unknown_alternatives}")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a domain carrier resolution packet.")
    parser.add_argument("resolution")
    args = parser.parse_args()
    path = Path(args.resolution)
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
        errors = validate_resolution(payload)
    except (OSError, json.JSONDecodeError) as exc:
        errors = [f"resolution unreadable: {exc}"]
    result = {
        "verdict": "PASS" if not errors else "FAIL",
        "resolution": str(path),
        "errors": errors,
        "boundary": "Carrier promotion and runtime-context receipt validation only; no carrier is selected by this script.",
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
