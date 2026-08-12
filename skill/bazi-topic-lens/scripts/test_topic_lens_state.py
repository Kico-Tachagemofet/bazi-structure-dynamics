#!/usr/bin/env python3
"""Self-test Topic Lens typed-state guardrails."""

from __future__ import annotations

from copy import deepcopy

from validate_topic_lens_state import validate_state


def fact(value):
    return {"status": "resolved", "value": value, "refs": ["frozen#ref"], "conflicts_or_limits": []}


def gate(status="supported"):
    return {"status": status, "evidence_refs": ["frozen#ref"], "counterevidence": []}


def valid_state():
    return {
        "schema_version": "2.0",
        "case_id": "fixture",
        "topic_id": "creation-expression",
        "topic_intent": "capability",
        "exact_question": "表达能否形成可持续输出？",
        "scope": "natal",
        "framework_lock": "fixture",
        "structure_freeze_id": "FRZ-1",
        "structure_freeze_ref": "structure-freeze-receipt.yaml",
        "use_kernel_ref": "use-kernel.md",
        "report_scope_ref": "report-scope.yaml",
        "delivery_mode": "limited-topic",
        "subject_context_available_to_finding": False,
        "facts_snapshot": {
            "commander": fact({"month_branch_main_qi": "丙", "commander": "戊", "seasonal_phase": "巳月土司令阶段"}),
            "exposed_stems": fact(["己", "甲"]),
            "dominant_branch_field": fact("金场候选"),
            "daymaster_roots_and_access": fact("无本根；调用有条件"),
            "conventional_symbol_post_state_and_destination": fact("伤官受占用并流向财")
        },
        "question_slices": [{
            "question_slice_id": "QS-1",
            "user_language_center": "可持续表达",
            "center_type": "capability",
            "relation_to_chart_subject": "self",
            "body_anchor_refs": ["route#R1"],
            "internal_mechanism_target": "输出形成",
            "domain_carrier_target": "表达任务",
            "external_result_target": "持续成果",
            "strongest_alternative_body": "资源承接"
        }],
        "centers": {
            "conventional_symbol_candidates": [{"candidate_id": "CS-1", "symbol_refs": ["node#伤官"], "reason_conventional": "表达常规取食伤"}],
            "actual_controller_or_carrier": [{"center_id": "AC-1", "refs": ["route#财承接"], "mechanism": "输出被财承接", "comparison_against_alternatives": "比伤官原始强度更能解释最终去处"}],
            "therapeutic_pivots": []
        },
        "star_eligibility": [{
            "candidate_id": "CS-1",
            "status": "diverted",
            "evidence_refs": ["edge#E1"],
            "post_state_refs": ["post#P1"],
            "destination": "财",
            "comparison_against_alternatives": "财承接更主导",
            "disposition_target": "AC-1"
        }],
        "capability_bridge": {
            "claim_target": "可持续表达",
            "claim_level": "sustainable_output",
            "claim_strength": "conditional",
            "required_gates": ["potential", "daymaster_access", "sustainability", "destination"],
            "gates": {
                "potential": gate(),
                "daymaster_access": gate("conditional"),
                "visibility": gate("conditional"),
                "sustainability": gate("conditional"),
                "destination": gate(),
                "external_result": gate("conditional")
            },
            "claim_disposition": "只能写成条件性输出，不称稳定强项"
        },
        "topic_process_axes": [{
            "axis_id": "TPA-1",
            "question_slice_id": "QS-1",
            "axis_role": "primary",
            "focal_question": "输出最后由谁承接？",
            "conventional_symbol_refs": ["CS-1"],
            "controller_or_carrier_refs": ["AC-1"],
            "therapeutic_pivot_ref": None,
            "source_endpoint": "伤官",
            "target_endpoint": "财",
            "node_refs": ["node#1"],
            "edge_refs": ["edge#1"],
            "route_refs": ["route#1"],
            "mechanism": "输出转财",
            "base_state": "conditional",
            "supporting_factors": [],
            "damage_diversion_or_occupation": "伤官不独立主导",
            "destination_and_feedback": "财再接管",
            "daymaster_agency_relation": "调用有条件",
            "competing_allocation": "财与其他路线竞争",
            "switch_conditions": ["补调用条件"],
            "failure_or_reversal": ["被再次占用"],
            "strongest_alternative": "财主导",
            "finding_disposition": "required"
        }],
        "finding_handoff": {
            "primary_axis_ids": ["TPA-1"],
            "supporting_axis_ids": [],
            "expected_primary_findings": ["F-1"],
            "cross_topic_refs": [],
            "unresolved_source_gaps": []
        }
    }


def valid_v23_state():
    state = deepcopy(valid_state())
    state["schema_version"] = "2.3"
    state["deep_card_queries"] = [{
        "query_id": "DCQ-FOUNDATION",
        "axis_id": None,
        "symbol_family": "foundation",
        "symbol": "five-elements",
        "card_id": "DC-FIVE-ELEMENTS-CORE",
        "reason_needed": "shared semantic foundation",
        "topic_axis": "whole topic",
        "required_source_layers": ["semantic_core"],
        "query_status": "requested",
        "requested_unit_classes": ["semantic_core"],
        "activation_basis_refs": ["freeze#FRZ-1"],
        "requested_carrier_scope": "none",
        "claim_ceiling": "mechanism",
        "selection_purpose": "explain frozen five-element process",
        "excluded_unit_classes": ["composite_domain_carrier"],
        "excluded_uses": [],
        "raw_card_access_requested": False,
    }]
    state["coverage_profile"] = {
        "profile_id": "CP-1",
        "scope_type": "timing-annual",
        "required_question_slices": ["QS-1"],
        "covered_question_slice_ids": ["QS-1"],
        "not_applicable_receipts": [],
        "deferred_or_source_gap_receipts": [],
        "primary_axis_count": 1,
        "required_primary_axis_count": 1,
        "expected_primary_finding_count": 1,
        "coverage_verdict": "complete",
    }
    state["scope_atoms"] = [{
        "atom_id": "YEAR-2027",
        "atom_type": "timing-annual",
        "label": "2027 丁未",
        "required": True,
        "axis_ids": ["TPA-1"],
        "finding_disposition": "required",
        "not_applicable_reason": None,
    }]
    state["finding_handoff"]["expected_primary_findings"] = 1
    return state


def valid_v30_state():
    state = deepcopy(valid_v23_state())
    state["schema_version"] = "3.0"
    state["structure_process_handoff_ref"] = "structure-process-handoff.yaml#PROC-1"
    state["domain_carrier_requests"] = []
    axis = state["topic_process_axes"][0]
    axis.update({
        "process_ref": "structure-process-handoff.yaml#PROC-1",
        "process_freeze_or_hash_ref": "freeze#PROC-1",
        "route_closure_receipt_ref": "structure-process-handoff.yaml#PROC-1.route_closure_receipt",
        "phase_focus_refs": ["PROC-1#PH-1"],
        "strength_and_bearing_snapshot_ref": "structure-process-handoff.yaml#PROC-1.strength_context",
        "complete_edge_closure": ["edge#1"],
        "daymaster_cost_ref": "structure-process-handoff.yaml#PROC-1.daymaster_cost",
        "therapeutic_effect_ref": "structure-process-handoff.yaml#PROC-1.therapeutic_effect",
        "residual_problem_ref": "structure-process-handoff.yaml#PROC-1.residual_problem",
        "bypass_and_rebound_ref": "structure-process-handoff.yaml#PROC-1.bypass_and_rebound",
        "agency_phase_refs": ["PROC-1#PH-1.agency_state"],
    })
    return state


def valid_v31_timing_state():
    state = deepcopy(valid_v30_state())
    state["schema_version"] = "3.1"
    state["topic_id"] = "career-work-2027"
    state["topic_intent"] = "timing"
    state["scope"] = "timing-annual"
    state["question_slices"][0].update({
        "facet_id": "domain-manifestation-candidates",
        "reader_need": "癸运引动的关系功能在职场可能落成什么，以及影响为何轻重有别",
        "explanatory_obligations": [
            "formation", "advantage", "cost", "result-gate", "switch", "verification",
        ],
    })
    state["reader_question_profile"] = {
        "profile_id": "RQP-TIMING-2027",
        "profile_ref": "reader-question-profiles.md#岁运剖面",
        "profile_type": "timing",
        "required_facet_ids": ["domain-manifestation-candidates"],
        "facet_dispositions": [{
            "facet_id": "domain-manifestation-candidates",
            "disposition": "primary",
            "question_slice_ids": ["QS-1"],
            "axis_ids": ["TPA-1"],
            "reason": "本年有受审计的临时关系功能变化，需要进入职场载体比较。",
        }],
    }
    state["runtime_context_policy"] = {
        "context_status": "unknown",
        "context_refs": [],
        "allowed_use": "carrier-branching-and-agency-only",
        "structural_inference_forbidden": True,
        "confidence_uplift_forbidden": True,
        "unknown_context_action": "keep-conditional-branches",
    }
    axis = state["topic_process_axes"][0]
    axis.update({
        "timing_process_diff_ref": "timing/year-2027-process-state-diff.yaml#PROC-1",
        "propagation_closure_ref": "timing/year-2027-process-state-diff.yaml#CLOSURE-1",
        "process_before_after_ref": "timing/year-2027-process-state-diff.yaml#BEFORE-AFTER-1",
        "agency_transition_ref": "timing/year-2027-process-state-diff.yaml#AGENCY-1",
        "expiry_rule": "2027 annual overlay expiry",
        "timing_manifestation_adjudication": {
            "natal_node_state_refs": ["post#hidden-gui"],
            "activation_interface_refs": ["post#AI-GUI-EXPOSURE"],
            "matched_trigger_refs": ["timing#GUI"],
            "overlay_function_transition": "root-support-only -> conditional direct-function in annual window",
            "relation_requalification_refs": ["overlay#WU-GUI", "overlay#QE-KILL-PRINT"],
            "shared_node_competition_ref": "overlay#ALLOCATION-WU",
            "retained_natal_route_ref": "timing/year-2027-process-state-diff.yaml#RETAINED-KILL-PRINT",
            "temporary_relation_function": "peer allocation and shared-resource relation",
            "role_mapping_disposition": "candidate-requested",
            "role_candidate_refs": ["DCR-1"],
            "impact_bounds_ref": "timing/year-2027-process-state-diff.yaml#IMPACT-BOUNDS",
            "runtime_context_refs": ["runtime_context_policy"],
            "expiry_rule": "2027 annual overlay expiry",
        },
    })
    state["domain_carrier_requests"] = [{
        "request_id": "DCR-1",
        "axis_id": "TPA-1",
        "topic_axis": "career_work_timing",
        "carrier_family": "career",
        "question_target": "临时增强的同侪／分配功能在职场落成何种关系角色",
        "process_ref": "structure-process-handoff.yaml#PROC-1",
        "controller_or_carrier_refs": ["AC-1"],
        "relation_function_refs": ["overlay#temporary-peer-allocation"],
        "position_visibility_refs": ["overlay#visible-gui"],
        "capability_gate_refs": ["capability_bridge#visibility"],
        "required_contribution_types": [
            "process_or_work_property", "relation_function", "position_visibility_or_route",
        ],
        "excluded_shortcuts": ["gui_to_colleague", "rob_wealth_to_villain", "single_ten_god_to_person"],
        "claim_ceiling": "candidate",
        "request_status": "requested",
        "relation_function_transition_ref": "overlay#temporary-peer-allocation",
        "retained_natal_route_ref": "timing/year-2027-process-state-diff.yaml#RETAINED-KILL-PRINT",
        "runtime_context_refs": ["runtime_context_policy"],
        "role_candidate_scope": ["lateral-colleague-or-collaborator", "competitor-or-resource-sharing-party"],
        "impact_assessment_refs": ["timing/year-2027-process-state-diff.yaml#IMPACT-BOUNDS"],
    }]
    return state


def valid_v32_timing_state():
    state = deepcopy(valid_v31_timing_state())
    state["schema_version"] = "3.2"
    state["question_slices"][0].update({
        "exact_reader_question": "2027 年职场中可能出现哪些同层协作或资源竞争，结果轻重如何？",
        "reader_answer_contract": {
            "contract_id": "RAC-CAREER-2027-01",
            "closure_key": "QA-CAREER-2027-01",
            "answer_target": {
                "subject_or_role": "命主与同层协作、竞争角色",
                "matter_or_domain_object": "职场任务、资源与责任分配",
                "result_or_outcome": "可能发生的协作或竞争形态及影响轻重",
            },
            "direct_answer_required": True,
            "allowed_answer_statuses": ["complete", "conditional", "not-applicable", "source-gap"],
            "prohibited_substitutes": [
                "personality-only", "advice-only", "generic-cross-topic-summary", "technical-label-only",
            ],
            "topic_specificity_required": True,
        },
    })
    state["reader_question_profile"]["facet_dispositions"][0].update({
        "answer_contract_ids": ["RAC-CAREER-2027-01"],
        "domain_specific_delta": "限定为 2027 年职场横向角色、任务资源分配和影响边界，不以泛化劫财性格替代。",
        "shared_answer_ref": None,
    })
    return state


def main() -> None:
    state = valid_state()
    assert validate_state(state) == []

    broken = deepcopy(state)
    broken["capability_bridge"]["claim_strength"] = "strong"
    broken["capability_bridge"]["gates"]["daymaster_access"]["status"] = "blocked"
    assert any("strong claim has unsupported gates" in error for error in validate_state(broken))

    broken = deepcopy(state)
    broken["topic_process_axes"][0]["controller_or_carrier_refs"] = ["CS-1"]
    assert any("unknown controller/carrier refs" in error for error in validate_state(broken))

    broken = deepcopy(state)
    broken["star_eligibility"][0]["comparison_against_alternatives"] = ""
    assert any("comparison are required" in error for error in validate_state(broken))

    v23 = valid_v23_state()
    assert validate_state(v23) == []

    broken = deepcopy(v23)
    broken["scope_atoms"].append({
        "atom_id": "YEAR-2028",
        "atom_type": "timing-annual",
        "label": "2028 戊申",
        "required": True,
        "axis_ids": ["TPA-1"],
        "finding_disposition": "required",
        "not_applicable_reason": None,
    })
    assert any("each requested year needs its own axis" in error for error in validate_state(broken))

    broken = deepcopy(v23)
    broken["finding_handoff"]["expected_primary_findings"] = ["F-1"]
    assert any("must be an integer" in error for error in validate_state(broken))

    v30 = valid_v30_state()
    assert validate_state(v30) == []

    broken = deepcopy(v30)
    broken["topic_process_axes"][0]["complete_edge_closure"] = ["edge#1", "edge#2"]
    assert any("must exactly equal complete_edge_closure" in error for error in validate_state(broken))

    broken = deepcopy(v30)
    broken["topic_intent"] = "timing"
    assert any("required for v3 timing" in error for error in validate_state(broken))

    broken = deepcopy(v30)
    broken["deep_card_queries"][0]["raw_card_access_requested"] = True
    assert any("raw_card_access_requested must be false" in error for error in validate_state(broken))

    broken = deepcopy(v30)
    broken["deep_card_queries"][0]["requested_unit_classes"] = ["semantic_core", "composite_domain_carrier"]
    assert any("must use domain_carrier_requests" in error for error in validate_state(broken))

    with_carrier = deepcopy(v30)
    with_carrier["domain_carrier_requests"] = [{
        "request_id": "DCR-1",
        "axis_id": "TPA-1",
        "topic_axis": "career_work",
        "carrier_family": "career",
        "question_target": "现实岗位与任务性质",
        "process_ref": "structure-process-handoff.yaml#PROC-1",
        "controller_or_carrier_refs": ["AC-1"],
        "relation_function_refs": ["node#伤官", "node#财"],
        "position_visibility_refs": ["post#P1"],
        "capability_gate_refs": ["capability_bridge#sustainability", "capability_bridge#external_result"],
        "required_contribution_types": ["process_or_work_property", "relation_function", "position_visibility_or_route"],
        "excluded_shortcuts": ["single_stem_to_job", "single_ten_god_to_job", "industry_name_backsolve"],
        "claim_ceiling": "candidate",
        "request_status": "requested",
    }]
    assert validate_state(with_carrier) == []

    v31 = valid_v31_timing_state()
    assert validate_state(v31) == []

    broken = deepcopy(v31)
    broken["reader_question_profile"]["facet_dispositions"] = []
    assert any("every required facet" in error for error in validate_state(broken))

    broken = deepcopy(v31)
    broken["topic_process_axes"][0]["timing_manifestation_adjudication"]["retained_natal_route_ref"] = ""
    assert any("retained_natal_route_ref cannot be empty" in error for error in validate_state(broken))

    broken = deepcopy(v31)
    broken["domain_carrier_requests"][0]["role_candidate_scope"] = ["colleague"]
    assert any("needs at least two role candidates" in error for error in validate_state(broken))

    broken = deepcopy(v31)
    broken["runtime_context_policy"]["structural_inference_forbidden"] = False
    assert any("structural inference must remain forbidden" in error for error in validate_state(broken))

    v32 = valid_v32_timing_state()
    assert validate_state(v32) == []

    broken = deepcopy(v32)
    broken["question_slices"][0]["exact_reader_question"] = "完整回答domain-manifestation-candidates"
    assert any("concrete natural-Chinese question" in error for error in validate_state(broken))

    broken = deepcopy(v32)
    broken["question_slices"][0]["exact_reader_question"] = "What happens in career?"
    assert any("concrete natural-Chinese question" in error for error in validate_state(broken))

    broken = deepcopy(v32)
    broken["question_slices"][0]["reader_answer_contract"]["answer_target"]["result_or_outcome"] = ""
    assert any("every answer_target field must be non-empty" in error for error in validate_state(broken))

    broken = deepcopy(v32)
    broken["question_slices"][0]["reader_answer_contract"]["prohibited_substitutes"].remove("advice-only")
    assert any("four forbidden answer substitutes" in error for error in validate_state(broken))

    broken = deepcopy(v32)
    broken["reader_question_profile"]["facet_dispositions"][0]["disposition"] = "supporting"
    broken["reader_question_profile"]["facet_dispositions"][0]["domain_specific_delta"] = ""
    assert any("needs a domain_specific_delta" in error for error in validate_state(broken))

    broken = deepcopy(v32)
    broken["reader_question_profile"]["facet_dispositions"][0]["disposition"] = "cross-ref"
    broken["reader_question_profile"]["facet_dispositions"][0]["shared_answer_ref"] = None
    assert any("cross-ref needs shared_answer_ref" in error for error in validate_state(broken))

    broken = deepcopy(v32)
    second_slice = deepcopy(broken["question_slices"][0])
    second_slice["question_slice_id"] = "QS-2"
    second_slice["reader_answer_contract"]["contract_id"] = "RAC-CAREER-2027-02"
    broken["question_slices"].append(second_slice)
    disposition = broken["reader_question_profile"]["facet_dispositions"][0]
    disposition["question_slice_ids"].append("QS-2")
    disposition["answer_contract_ids"].append("RAC-CAREER-2027-02")
    assert any("duplicate closure_key" in error for error in validate_state(broken))

    print("PASS: Topic Lens v3.2 preserves process closure, reader answer contracts, and timing manifestation boundaries")


if __name__ == "__main__":
    main()
