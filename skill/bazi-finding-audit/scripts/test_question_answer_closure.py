#!/usr/bin/env python3
"""Self-test the Reader Answer Contract closure validator."""

from __future__ import annotations

from copy import deepcopy

from validate_question_answer_closure import validate_closure


def answer(topic_id="career-work", closure_key="QA-CAREER-01", contract_id="RAC-CAREER-01"):
    return {
        "closure_key": closure_key,
        "contract_id": contract_id,
        "topic_id": topic_id,
        "question_slice_id": f"QS-{topic_id}",
        "facet_id": "role-result",
        "exact_reader_question": "命主在职场更可能承担什么角色，怎样形成成果，又会付出什么代价？",
        "answer_status": "conditional",
        "answer_target": {
            "subject_or_role": "命主在组织中的岗位与责任角色",
            "matter_or_domain_object": "任务承接、专业输出和组织资源",
            "result_or_outcome": "主要成事方式、可见成果与责任代价",
        },
        "direct_answer_summary": "更容易靠承接高要求任务并整理复杂问题建立职位信用，但成果常连带新增责任，能否升级为授权仍取决于组织结果门。",
        "direct_answer_claim_ids": [f"AC-{topic_id}"],
        "finding_refs": [f"F-{topic_id}"],
        "source_coverage_refs": [f"source#{topic_id}"],
        "process_refs": ["PROC-01"],
        "obligation_refs": {
            "formation": [f"F-{topic_id}#formation"],
            "advantage": [f"F-{topic_id}#advantage"],
            "cost": [f"F-{topic_id}#cost"],
            "result-gate": [f"F-{topic_id}#result-gate"],
            "switch": [f"F-{topic_id}#switch"],
            "verification": [f"J-{topic_id}-01"],
        },
        "domain_specific_delta": "限定到职场岗位责任、专业交付、组织授权和职位信用，不泛说责任感。",
        "shared_mechanism_refs": ["PROC-01"],
        "shared_answer_ref": None,
        "strongest_alternative": "若岗位没有授权和成果归属，同一结构更可能只表现为临时救火与责任增加。",
        "personality_role": "explanatory-only",
        "advice_role": "after-answer",
        "advice_substitutes_answer": False,
        "render_obligation_id": f"RO-{topic_id}",
        "gap_or_na_reason": None,
    }


def payload():
    return {
        "schema_version": "1.0",
        "case_id": "fixture",
        "structure_freeze_id": "FRZ-1",
        "report_scope_ref": "report-scope.yaml",
        "topic_lens_index_ref": "topic-lens-index.yaml",
        "question_answers": [answer()],
    }


def receipt():
    return {
        "schema_version": "1.0",
        "case_id": "fixture",
        "report_ref": "full-reading.md",
        "question_answer_receipts": [{
            "closure_key": "QA-CAREER-01",
            "contract_id": "RAC-CAREER-01",
            "render_obligation_id": "RO-career-work",
            "marker_count": 1,
            "direct_answer_present": True,
            "answer_before_advice": True,
            "body_ref": "full-reading.md#career",
            "audit_status": "pending-independent-audit",
        }],
    }


REPORT = """# 报告

<!-- question_id: QA-CAREER-01 -->
职场上更容易以承接高要求任务、梳理复杂问题并交付成果建立信用；代价是成果出现后常继续增加责任，能否转成正式授权取决于组织是否给出权限和成果归属。

形成这一路径的结构、优势和切换条件随后完整展开。建议只放在答案之后。
"""


def main() -> None:
    valid = payload()
    assert validate_closure(valid) == []
    assert validate_closure(valid, REPORT, receipt()) == []

    broken = deepcopy(valid)
    broken["question_answers"][0]["exact_reader_question"] = "完整回答role-result"
    assert any("natural-Chinese question" in error for error in validate_closure(broken))

    broken = deepcopy(valid)
    broken["question_answers"][0]["answer_target"]["result_or_outcome"] = ""
    assert any("answer_target field" in error for error in validate_closure(broken))

    broken = deepcopy(valid)
    broken["question_answers"][0]["direct_answer_summary"] = "建议先建立清晰边界并控制工作量。"
    assert any("advice-first" in error for error in validate_closure(broken))

    broken = deepcopy(valid)
    broken["question_answers"][0]["obligation_refs"]["result-gate"] = []
    assert any("result-gate cannot be empty" in error for error in validate_closure(broken))

    broken = deepcopy(valid)
    second = answer("wealth-resource", "QA-WEALTH-01", "RAC-WEALTH-01")
    second["exact_reader_question"] = "命主的资源与收入主要怎样形成，什么会妨碍积累，结果边界在哪里？"
    second["render_obligation_id"] = "RO-wealth-resource"
    second["domain_specific_delta"] = "限定到收入、流动性与积累。"
    broken["question_answers"].append(second)
    assert any("identical direct answers across topics" in error for error in validate_closure(broken))

    shared = deepcopy(broken)
    shared["question_answers"][0]["shared_answer_ref"] = "SHARED-01"
    shared["question_answers"][1]["shared_answer_ref"] = "SHARED-01"
    assert validate_closure(shared) == []

    assert any("must appear exactly once" in error for error in validate_closure(valid, "# 空报告", receipt()))

    advice_report = """<!-- question_id: QA-CAREER-01 -->
建议你先建立边界并控制任务量，之后再观察组织是否给出授权和成果归属。
"""
    assert any("starts with advice" in error for error in validate_closure(valid, advice_report, receipt()))

    broken_receipt = receipt()
    broken_receipt["question_answer_receipts"][0]["audit_status"] = "PASS"
    assert any("Render cannot self-pass" in error for error in validate_closure(valid, REPORT, broken_receipt))

    v2_empty = deepcopy(valid)
    v2_empty["schema_version"] = "2.0"
    v2_empty["question_answers"] = []
    assert validate_closure(v2_empty, "# 没有显式问题的完整报告") == []

    v2 = deepcopy(valid)
    v2["schema_version"] = "2.0"
    v2_item = v2["question_answers"][0]
    v2_item.pop("question_slice_id")
    v2_item.pop("facet_id")
    v2_item.update({
        "explicit_question_id": "UQ-CAREER-01",
        "source_kind": "user-verbatim",
        "source_ref": "report-scope.yaml#explicit_questions[0]",
    })
    assert validate_closure(v2) == []
    v2_item["source_ref"] = ""
    assert any("source_ref" in error for error in validate_closure(v2))

    print("PASS: question-answer closure supports genuine-question v2, rejects synthetic substitutes, and permits empty maps when no real question exists")


if __name__ == "__main__":
    main()
