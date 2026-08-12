#!/usr/bin/env python3
from __future__ import annotations

import copy
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


PATH = Path(__file__).with_name("validate_ten_god_stem_branch_kernel.py")
SPEC = importlib.util.spec_from_file_location("kernel_validator", PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(MODULE)


def valid_payload():
    return {"kernels": [{
        "kernel_id": "BSK-CAREER-01",
        "topic_id": "career-work",
        "taiji_center": "命主本人在职业场中的任务、位置与结果",
        "process_refs": ["P-01"],
        "phase_focus_refs": ["P-01-A", "P-01-B"],
        "topic_process_axis_refs": ["AX-01", "AX-02"],
        "ten_god_chain": {
            "body_or_subject": "命主承担的职业任务与组织结果",
            "start_node_and_agency": "官杀先以外部标准发动，命主先承受后承接",
            "ordered_relation_functions": ["官杀提出标准", "印星转为方法", "食神形成方案", "财星承接成果"],
            "result_endpoint": "成果可能转成专业信用，也可能回流为新增责任",
            "feedback_to_daymaster": "项目扩张会继续占用命主承载与印星方法端",
            "competing_uses": ["印星同时承担学习与工作救火"],
            "agency": {"can_start": "conditional", "can_carry": "yes", "can_redirect": "conditional", "can_stop": "weak"},
            "reversal_gate": "授权、资料与交付终点先到位时，压力转成职位信用",
        },
        "stem_branch_composition": {
            "exposed_stems": ["戊杀公开标准", "庚印公开方法端"],
            "branch_fields": ["寅支提供持续输出与项目场"],
            "hidden_stem_layers": ["甲食神以内在拆题供给参与"],
            "pillar_roles": ["年柱外部标准", "月柱组织运行", "时柱后续方法"],
            "same_pillar_coloring": ["庚的可见方法受坐支场景承载"],
            "cross_pillar_transfer": ["外部要求传到后续方法与成果端"],
        },
        "material_spread_receipt": {
            "runtime_packet_ref": "runtime-career.json",
            "selected_unit_ids": ["TG-KILL", "TG-PRINT", "ST-WU", "BR-YIN"],
            "unit_dispositions": [
                {"unit_id": "TG-KILL", "disposition": "used", "claim_kernel_refs": ["CK-CAREER-NATURE", "CK-CAREER-AUTHORITY"], "reason": "官杀提供标准与权责起点"},
                {"unit_id": "TG-PRINT", "disposition": "used", "claim_kernel_refs": ["CK-CAREER-NATURE", "CK-CAREER-AUTHORITY"], "reason": "印星提供方法与资格承接"},
                {"unit_id": "ST-WU", "disposition": "used", "claim_kernel_refs": ["CK-CAREER-NATURE"], "reason": "戊把标准具体化为显性压力动作"},
                {"unit_id": "BR-YIN", "disposition": "used", "claim_kernel_refs": ["CK-CAREER-NATURE"], "reason": "寅限定持续输出与项目场"},
            ],
            "source_refs": ["runtime-career.json", "process-compositions.yaml#P-01"],
            "excluded_unit_receipts": [],
            "coverage_validator_receipt_ref": "validator-receipt.json",
        },
        "composition_relations": [{
            "from_ref": "TG-KILL",
            "to_ref": "ST-WU",
            "interaction_type": "specifies",
            "chain_position": "start",
            "effect": "把抽象权责收窄为公开标准和后果",
        }],
        "mandatory_judgment_dimension_refs": ["occupational-nature", "authority-result"],
        "claim_kernels": [
            {
                "claim_kernel_id": "CK-CAREER-NATURE",
                "judgment_dimension_ref": "occupational-nature",
                "claim_endpoint_id": "career-nature",
                "specificity_level": "L2-domain-nature",
                "disposition": "directional-verdict",
                "directional_verdict": "职业以处理复杂标准和专业审查为主要性质",
                "claim_strength": "supported",
                "support_refs": ["P-01", "TG-KILL", "TG-PRINT"],
                "counterevidence_refs": [],
                "support_unit_refs": ["TG-KILL", "TG-PRINT", "ST-WU", "BR-YIN"],
                "counterevidence_unit_refs": [],
                "counterevidence_check": "已检查无权责结果门和无持续场时的替代解释",
                "result_gate": "方法和资格可以稳定使用",
                "reversal_condition": "只有责任没有方法时退为临时救火",
                "daymaster_cost_ref": "P-01#cost",
                "competing_claim_or_carrier_refs": ["complex-project", "professional-review"],
            },
            {
                "claim_kernel_id": "CK-CAREER-AUTHORITY",
                "judgment_dimension_ref": "authority-result",
                "claim_endpoint_id": "career-authority",
                "specificity_level": "L1-outcome-level",
                "disposition": "directional-verdict",
                "directional_verdict": "专业信用强于名义职位，授权到位后可转成正式权责",
                "claim_strength": "supported",
                "support_refs": ["P-01", "TG-KILL", "TG-PRINT"],
                "counterevidence_refs": [],
                "support_unit_refs": ["TG-KILL", "TG-PRINT"],
                "counterevidence_unit_refs": [],
                "counterevidence_check": "已检查只有责任而无授权的反向分支",
                "result_gate": "组织提供正式授权",
                "reversal_condition": "口头赏识而无授权时只增加责任",
                "daymaster_cost_ref": "P-01#cost",
                "competing_claim_or_carrier_refs": [],
            },
        ],
        "main_scene": "命主常因能处理高要求难题而被交付复杂任务，成果首先形成专业信用",
        "secondary_scene": "成果被看见后也容易带回更多项目与维护责任",
        "switch_scene": "授权、资料和人手同步增加时，新增责任才更容易转成正式位置",
        "nonmanifestation_scene": "没有公开接口时仍表现为内部拆题和临时救火，不自动形成职级",
        "distinctive_detail_palette": ["一次解决后同类任务持续归他", "口头赏识与正式授权分离"],
        "candidate_carriers_ranked": ["复杂项目交付", "专业审查"],
        "strongest_alternative": "若组织没有成果归属，同一结构只表现为幕后救火",
        "do_not_render": ["不直断唯一行业", "不把官杀固定为上司"],
        "confidence": "medium",
    }]}


def validate_payload(payload, runtime_ids=None):
    runtime_ids = runtime_ids or ["TG-KILL", "TG-PRINT", "ST-WU", "BR-YIN"]
    with tempfile.TemporaryDirectory() as temp_dir:
        root = Path(temp_dir)
        (root / "runtime-career.json").write_text(
            json.dumps({"selected_units": [{"runtime_unit_id": unit_id} for unit_id in runtime_ids]}),
            encoding="utf-8",
        )
        return MODULE.validate(payload, root / "kernels.json")[0]


class KernelValidatorTests(unittest.TestCase):
    def test_valid_composite_kernel_passes(self):
        self.assertEqual(validate_payload(valid_payload()), [])

    def test_missing_chain_is_blocked(self):
        payload = copy.deepcopy(valid_payload())
        payload["kernels"][0]["ten_god_chain"]["ordered_relation_functions"] = []
        errors = validate_payload(payload)
        self.assertTrue(any("ordered_relation_functions" in error for error in errors))

    def test_raw_card_payload_is_blocked(self):
        payload = copy.deepcopy(valid_payload())
        payload["kernels"][0]["raw_card_text"] = "forbidden"
        errors = validate_payload(payload)
        self.assertTrue(any("prohibited" in error for error in errors))

    def test_runtime_truncation_is_blocked(self):
        errors = validate_payload(valid_payload(), ["TG-KILL", "TG-PRINT", "ST-WU", "BR-YIN", "GENG-ACTION"])
        self.assertTrue(any("runtime set mismatch" in error for error in errors))

    def test_producer_self_attestation_is_blocked(self):
        payload = copy.deepcopy(valid_payload())
        payload["kernels"][0]["material_spread_receipt"]["all_chain_links_covered"] = True
        errors = validate_payload(payload)
        self.assertTrue(any("self-attestation is prohibited" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
