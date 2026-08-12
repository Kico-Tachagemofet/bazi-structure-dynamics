#!/usr/bin/env python3
"""Self-test composite carrier promotion guardrails."""

from __future__ import annotations

from copy import deepcopy

from validate_domain_carrier_resolution import validate_resolution


def candidate(candidate_id: str, label: str, rank: str):
    return {
        "candidate_id": candidate_id,
        "label": label,
        "specificity_level": "L4-carrier-family",
        "rank": rank,
        "source_lead_refs": [f"LEAD-{candidate_id}"],
        "contributing_card_ids": ["DC-STEM-JIA", "DC-TEN-GODS-CORE"],
        "contribution_groups": {
            "process_or_work_property": ["JIA-WORK-GROWTH"],
            "relation_function": ["TG-FUNC-INPUT", "TG-FUNC-OUTPUT"],
            "position_visibility_or_route": ["TPA-1", "PROC-1"],
            "daymaster_access_and_sustainability": ["CAP#access", "CAP#sustainability"],
            "destination_and_external_result": ["CAP#destination", "CAP#external_result"],
        },
        "independent_anchor_refs": ["PROC-1", "POST-1", "CAP-1"],
        "passed_gates": ["relation", "visibility", "route", "access", "sustainability"],
        "blocked_or_missing_gates": [],
        "alternative_carrier_ids": ["C-RESEARCH"] if candidate_id != "C-RESEARCH" else ["C-EDUCATION"],
        "comparison_reason": "培养输入与输出同时接入职业位置，较纯研究载体更完整。",
        "single_symbol_card_sufficient": False,
        "lower_level_verdicts_preserved": True,
        "assertable_fact_refs": [],
        "forbidden_direct_inferences": ["甲木直接等于教师", "印星直接等于教育行业"],
        "relation_function_transition": "timing relation function remains prior to person-role mapping",
        "retained_natal_route_ref": "not-applicable",
        "runtime_context_branches": [{
            "branch_id": f"RCB-{candidate_id}",
            "context_status": "not-applicable",
            "position_or_role_condition": "natal carrier resolution",
            "carrier_expression": label,
            "agency_difference": "not-applicable",
            "structural_claim_unchanged": True,
            "context_used_as_structure_evidence": False,
        }],
        "structural_impact_bounds_ref": "not-applicable",
    }


def valid_packet():
    education = candidate("C-EDUCATION", "教育／培养类岗位", "preferred")
    research = candidate("C-RESEARCH", "研究／专业资格类岗位", "supported")
    return {
        "schema_version": "2.0",
        "case_id": "fixture",
        "topic_id": "career-work",
        "structure_freeze_id": "FRZ-1",
        "topic_lens_ref": "topic-lens-career-work.json",
        "runtime_packet_ref": "deep-card-runtime-packet-career-work.json",
        "runtime_context_policy_ref": "not-applicable",
        "resolutions": [{
            "resolution_id": "DCRS-1",
            "domain_request_ref": "DCR-1",
            "axis_id": "TPA-1",
            "judgment_dimension_refs": ["occupational-nature", "career-carrier-family"],
            "carrier_family": "career",
            "specificity_verdicts": [
                {"specificity_level": "L1-outcome-level", "disposition": "directional-verdict", "verdict": "专业化程度较高", "rank": "supported", "support_or_gap_refs": ["PROC-1"], "enters_finding": True},
                {"specificity_level": "L2-domain-nature", "disposition": "directional-verdict", "verdict": "研究与培养性质较强", "rank": "preferred", "support_or_gap_refs": ["PROC-1", "TPA-1"], "enters_finding": True},
                {"specificity_level": "L3-action-material", "disposition": "directional-verdict", "verdict": "主要动作是研究、组织和培养", "rank": "supported", "support_or_gap_refs": ["LEAD-C-EDUCATION"], "enters_finding": True},
                {"specificity_level": "L4-carrier-family", "disposition": "directional-verdict", "verdict": "教育培养优先于纯研究", "rank": "preferred", "support_or_gap_refs": ["C-EDUCATION", "C-RESEARCH"], "enters_finding": True},
                {"specificity_level": "L5-exact-identity-event", "disposition": "not-claimed", "verdict": "不锁定具体岗位", "rank": "candidate", "support_or_gap_refs": [], "enters_finding": False},
            ],
            "resolution_status": "resolved",
            "candidate_pool": [education, research],
            "selected_carrier_ids": ["C-EDUCATION"],
        }],
    }


def main() -> None:
    packet = valid_packet()
    assert validate_resolution(packet) == []

    broken = deepcopy(packet)
    broken["resolutions"][0]["candidate_pool"][0]["single_symbol_card_sufficient"] = True
    assert any("single_symbol_card_sufficient must be false" in error for error in validate_resolution(broken))

    broken = deepcopy(packet)
    broken["resolutions"][0]["candidate_pool"][0]["contribution_groups"]["relation_function"] = []
    assert any("missing contribution groups" in error for error in validate_resolution(broken))

    broken = deepcopy(packet)
    broken["resolutions"][0]["candidate_pool"][0]["independent_anchor_refs"] = ["ONLY-ONE"]
    assert any("at least two independent anchors" in error for error in validate_resolution(broken))

    broken = deepcopy(packet)
    broken["resolutions"][0]["candidate_pool"][0]["alternative_carrier_ids"] = []
    assert any("preferred+ needs an alternative carrier" in error for error in validate_resolution(broken))

    broken = deepcopy(packet)
    broken["resolutions"][0]["candidate_pool"][0]["runtime_context_branches"][0]["structural_claim_unchanged"] = False
    assert any("cannot change structural claim" in error for error in validate_resolution(broken))

    timing = deepcopy(packet)
    timing_candidate = timing["resolutions"][0]["candidate_pool"][0]
    timing_candidate["retained_natal_route_ref"] = "timing#retained-route"
    timing_candidate["structural_impact_bounds_ref"] = "timing#impact-bounds"
    timing_candidate["runtime_context_branches"] = [{
        "branch_id": "RCB-LATERAL",
        "context_status": "conditional",
        "position_or_role_condition": "subject is in a lateral role",
        "carrier_expression": "peer colleague or collaborator",
        "agency_difference": "can negotiate work split but not final organization decision",
        "structural_claim_unchanged": True,
        "context_used_as_structure_evidence": False,
    }, {
        "branch_id": "RCB-LEAD",
        "context_status": "conditional",
        "position_or_role_condition": "subject has project or management authority",
        "carrier_expression": "team member, co-owner, or resource-allocation participant",
        "agency_difference": "can set part of the allocation rule",
        "structural_claim_unchanged": True,
        "context_used_as_structure_evidence": False,
    }]
    assert validate_resolution(timing) == []

    broken = deepcopy(timing)
    broken["resolutions"][0]["candidate_pool"][0]["runtime_context_branches"] = broken["resolutions"][0]["candidate_pool"][0]["runtime_context_branches"][:1]
    assert any("at least two conditional branches" in error for error in validate_resolution(broken))

    print("PASS: domain carrier resolver preserves L1-L4 while keeping exact identity and runtime context conditional")


if __name__ == "__main__":
    main()
