#!/usr/bin/env python3
from __future__ import annotations

import copy
import importlib.util
import unittest
from pathlib import Path


PATH = Path(__file__).with_name("validate_taiji_field_lens.py")
SPEC = importlib.util.spec_from_file_location("lens_validator", PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(MODULE)


def valid_payload():
    return {
        "schema_version": "4.1",
        "case_id": "CASE",
        "topic_id": "career-work",
        "structure_freeze_id": "FREEZE",
        "report_scope_ref": "report-scope.yaml",
        "taiji_field": {
            "user_language_center": "命主本人在职业中的任务、位置与发展",
            "field_type": "person-domain",
            "people_or_roles_in_scope": ["命主", "组织角色"],
            "matters_or_objects_in_scope": ["任务", "权限", "成果"],
            "result_dimensions_to_determine": ["成事方式", "结果去向"],
            "boundaries": [],
        },
        "coverage_facets": [{
            "facet_id": "task",
            "coverage_status": "required",
            "reader_relevance": "判断实际处理哪类任务",
            "attached_axis_ids": ["AX-01"],
            "final_disposition": "primary",
        }],
        "mandatory_judgment_dimensions": [{
            "dimension_id": "occupational-nature",
            "required_disposition": "directional-verdict|not-applicable|source-gap",
            "specificity_floor": "L2-domain-nature",
            "supporting_process_refs": ["P-01"],
            "candidate_axis_refs": ["AX-01"],
            "downstream_claim_endpoint": "career-nature",
            "no_silent_merge": True,
        }],
        "explicit_reader_questions": [],
        "topic_process_axes": [{
            "axis_id": "AX-01",
            "axis_formation_basis": "distinct-process-ten-god-pillar-scene",
            "process_ref": "P-01",
            "route_closure_receipt_ref": "handoff#P-01",
            "phase_focus_refs": ["P-01-A"],
            "ten_god_chain_plan": {
                "domain_body": "职业任务与结果",
                "required_relation_functions": ["权责如何承接", "输出怎样进入成果端"],
                "result_dimension_to_determine": "成果转权限还是新增责任",
                "feedback_and_competition_to_check": ["成果回流是否增加任务"],
                "forbidden_shortcuts": ["官杀不直断上司"],
            },
            "stem_branch_anchor_plan": {
                "visible_stem_refs": ["year.stem.wu"],
                "branch_position_refs": ["month.branch.yin"],
                "hidden_stem_refs": ["month.branch.yin.hidden.jia"],
                "pillar_role_refs": ["year", "month"],
                "relation_after_state_refs": ["post-node-01"],
            },
            "scene_kernel_required": True,
            "attached_facet_ids": ["task"],
            "attached_explicit_question_ids": [],
        }],
        "deep_card_queries": [{
            "card_id": "DC-TEN-GODS-CORE",
            "anchor_refs": ["year.stem.wu", "month.branch.yin", "month.branch.yin.hidden.jia"],
        }],
        "domain_carrier_requests": [{"carrier_family": "career"}],
        "candidate_palette_requests": [{
            "palette_id": "PAL-01",
            "judgment_dimension_refs": ["occupational-nature"],
            "requested_specificity_levels": ["L2-domain-nature", "L3-action-material", "L4-carrier-family"],
            "activation_anchor_refs": ["year.stem.wu", "month.branch.yin"],
            "excluded_preselection": ["exact-career"],
        }],
        "source_and_kernel_handoff": {
            "required_claim_endpoint_refs": ["career-nature"],
            "endpoint_differentiation_required": True,
            "scene_synthesis_count_policy": "chart-derived-after-differentiation",
            "required_material_spread": True,
            "required_ten_god_stem_branch_synthesis": True,
        },
    }


class LensValidatorTests(unittest.TestCase):
    def test_valid_chart_driven_lens_passes(self):
        self.assertEqual(MODULE.validate_lens(valid_payload()), [])

    def test_prefilled_answer_is_blocked(self):
        payload = copy.deepcopy(valid_payload())
        payload["external_result_target"] = "更适合流程管理"
        errors = MODULE.validate_lens(payload)
        self.assertTrue(any("conclusion field" in error for error in errors))

    def test_missing_ten_god_chain_is_blocked(self):
        payload = copy.deepcopy(valid_payload())
        payload["topic_process_axes"][0]["ten_god_chain_plan"]["required_relation_functions"] = []
        errors = MODULE.validate_lens(payload)
        self.assertTrue(any("required_relation_functions" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
