#!/usr/bin/env python3
"""Self-test the mechanical Bazi render coverage checker."""

from check_render_coverage import NATAL_CORE_SECTIONS, check, scope_values


FINDINGS = """
## F-TEST-001
judgment_id: J-F-TEST-001-01
judgment_id: J-F-TEST-001-02
judgment_id: J-F-TEST-001-03
body
## F-TEST-002
judgment_id: J-F-TEST-002-01
judgment_id: J-F-TEST-002-02
judgment_id: J-F-TEST-002-03
body
"""

GOOD = """
## Two connected life lines
<!-- topic_id: family-home -->
<!-- finding_id: F-TEST-001 -->
家庭中的责任怎样转成学习方法，并在现实选择里留下可以核对的结果。
<!-- topic_id: education-learning -->
<!-- finding_id: F-TEST-002 -->
同一条结构进入学习后，会改变吸收资料、应对考核与安排长期任务的方式。
<!-- topic_id: wealth-resource -->
它进入财务时，重点转为怎样取得、保存并分配能够长期承载的资源。
<!-- topic_id: career-work -->
到了事业场景，这条主线落实为任务责任、方法权限与最终交付之间的关系。
"""

BAD = """
### Compressed
<!-- finding_id: F-TEST-001 -->
A
"""

SCOPE = """
delivery_mode: full-reading
report_depth: summary
mandatory_sections:
  - family-home
  - education-learning
  - wealth-resource
  - career-work
selected_optional_sections: []
manifestation_mapping_state: none
validation_state: none
"""

BAD_SCOPE = """
delivery_mode: full-reading
report_depth: summary
mandatory_sections:
  - family-home
  - education-learning
selected_optional_sections:
  - love-relationship
manifestation_mapping_state: none
validation_state: none
"""

CORE = "\n".join(
    f"<!-- core_section_id: {item} -->\n原局章节具体说明 {item} 的结构过程。"
    for item in NATAL_CORE_SECTIONS
)

DETAILED_GOOD = f"""
{CORE}
## Family
<!-- topic_id: family-home -->
<!-- finding_id: F-TEST-001 -->
<!-- judgment_id: J-F-TEST-001-01 -->
第一段说明盘面结构如何形成，而且给出可核验体验。

<!-- judgment_id: J-F-TEST-001-02 -->
第二段说明条件、动作主体、去向与现实承载方式。

<!-- judgment_id: J-F-TEST-001-03 -->
第三段说明反向表现、边界以及最强替代解释。
## Education
<!-- topic_id: education-learning -->
<!-- finding_id: F-TEST-002 -->
<!-- judgment_id: J-F-TEST-002-01 -->
第一段说明第二条判断的结构形成与可核验表现。

<!-- judgment_id: J-F-TEST-002-02 -->
第二段说明谁推动、谁承接以及资源最后去向哪里。

<!-- judgment_id: J-F-TEST-002-03 -->
第三段说明失败条件、反向表现和不能推出的事情。
## Wealth
<!-- topic_id: wealth-resource -->
财务部分说明资源怎样进入、被占用，以及什么条件下才能真正留下。
## Career
<!-- topic_id: career-work -->
事业部分说明外部要求、本人能动和现实结果怎样沿同一主线分开落下。
## Love
<!-- topic_id: love-relationship -->
关系部分说明互动怎样开始、由谁承接，以及条件变化时会怎样转向。
<!-- topic_id: formative-major-luck -->
<!-- luck_period_id: LP-TEST-01 -->
第一步大运说明原局主线如何被临时增量改变，以及到期后哪些关系退出。
<!-- timing_year: 2027 -->
2027 年保留独立年度判断，说明旧结构、本人的选择和外部结果如何变化。
"""

NATAL_CORE_SCOPE_LINES = "".join(f"  - {item}\n" for item in NATAL_CORE_SECTIONS)

DETAILED_SCOPE = f"""
schema_version: "1.1"
delivery_mode: full-reading
report_depth: detailed-natal
feedback_offer_state: offered
natal_core_sections:
{NATAL_CORE_SCOPE_LINES}mandatory_sections:
  - family-home
  - education-learning
  - wealth-resource
  - career-work
selected_optional_sections:
  - topic_slug: love-relationship
    exact_question: 关系怎样运作
    scope: timing
timing_scope:
  requested: true
  luck_periods: [LP-TEST-01]
  annual_years: [2027]
manifestation_mapping_state: none
validation_state: none
"""

RECEIPT = "\n".join([
    "raw_card_access: forbidden",
    "render_input_mode: audited-envelopes-only",
    "raw_card_read: false",
    "F-TEST-001", "J-F-TEST-001-01", "J-F-TEST-001-02", "J-F-TEST-001-03",
    "F-TEST-002", "J-F-TEST-002-01", "J-F-TEST-002-02", "J-F-TEST-002-03",
])

FIELD_FINDING = """
- finding_id: F-CORE-001
- judgment_ids:
  - J-F-CORE-001-01
  - J-F-CORE-001-02
"""

FIELD_RENDER = """
<!-- finding_id: F-CORE-001 -->
<!-- judgment_id: J-F-CORE-001-01 -->
第一条原局判断有完整的现实结果、作用条件和可供核对的落点。
<!-- judgment_id: J-F-CORE-001-02 -->
第二条判断补足相反条件与替代解释，不把句数当成质量本身。
"""


def main() -> None:
    good = check(FINDINGS, GOOD, "report", [], SCOPE)
    bad = check(FINDINGS, BAD, "report", [])
    bad_scope = check(FINDINGS, GOOD, "report", [], BAD_SCOPE)
    assert good["verdict"] == "PASS", good
    assert bad["verdict"] == "FAIL", bad
    assert bad_scope["verdict"] == "FAIL", bad_scope
    assert any("F-TEST-002" in item for item in bad["blockers"]), bad
    assert any("reader-facing prose" in item for item in bad["blockers"]), bad
    assert any("baseline" in item.lower() for item in bad_scope["blockers"]), bad_scope
    assert any("love-relationship" in item for item in bad_scope["blockers"]), bad_scope

    parsed = scope_values(DETAILED_SCOPE)
    assert parsed["selected_optional_sections"] == ["love-relationship"], parsed
    assert parsed["annual_years"] == [2027], parsed
    assert parsed["luck_periods"] == ["LP-TEST-01"], parsed
    field_based = check(FIELD_FINDING, FIELD_RENDER, "qa", ["F-CORE-001"])
    assert field_based["verdict"] == "PASS", field_based
    detailed = check(FINDINGS, DETAILED_GOOD, "report", [], DETAILED_SCOPE, RECEIPT)
    assert detailed["verdict"] == "PASS", detailed
    missing_judgment = check(
        FINDINGS,
        DETAILED_GOOD.replace("<!-- judgment_id: J-F-TEST-001-02 -->", ""),
        "report",
        [],
        DETAILED_SCOPE,
        RECEIPT,
    )
    assert missing_judgment["verdict"] == "FAIL", missing_judgment
    assert any("J-F-TEST-001-02" in item for item in missing_judgment["blockers"]), missing_judgment
    empty_judgment = check(
        FINDINGS,
        DETAILED_GOOD.replace("第二段说明条件、动作主体、去向与现实承载方式。", ""),
        "report",
        [],
        DETAILED_SCOPE,
        RECEIPT,
    )
    assert empty_judgment["verdict"] == "FAIL", empty_judgment
    assert any("J-F-TEST-001-02" in item for item in empty_judgment["blockers"]), empty_judgment
    empty_topic = check(
        FINDINGS,
        DETAILED_GOOD.replace("事业部分说明外部要求、本人能动和现实结果怎样沿同一主线分开落下。", ""),
        "report",
        [],
        DETAILED_SCOPE,
        RECEIPT,
    )
    assert any("career-work" in item for item in empty_topic["blockers"]), empty_topic
    empty_core = check(
        FINDINGS,
        DETAILED_GOOD.replace("原局章节具体说明 natal-system-engine 的结构过程。", ""),
        "report",
        [],
        DETAILED_SCOPE,
        RECEIPT,
    )
    assert any("natal-system-engine" in item for item in empty_core["blockers"]), empty_core
    empty_year = check(
        FINDINGS,
        DETAILED_GOOD.replace("2027 年保留独立年度判断，说明旧结构、本人的选择和外部结果如何变化。", ""),
        "report",
        [],
        DETAILED_SCOPE,
        RECEIPT,
    )
    assert any("Timing year 2027" in item for item in empty_year["blockers"]), empty_year
    no_receipt = check(FINDINGS, DETAILED_GOOD, "report", [], DETAILED_SCOPE)
    assert any("render-card-receipt" in item for item in no_receipt["blockers"]), no_receipt
    unsafe_receipt = check(
        FINDINGS,
        DETAILED_GOOD,
        "report",
        [],
        DETAILED_SCOPE,
        RECEIPT.replace("raw_card_read: false", "raw_card_read: true"),
    )
    assert any("raw-card firewall guards" in item for item in unsafe_receipt["blockers"]), unsafe_receipt
    pending_feedback = check(
        FINDINGS,
        DETAILED_GOOD,
        "report",
        [],
        DETAILED_SCOPE.replace("feedback_offer_state: offered", "feedback_offer_state: pending"),
        RECEIPT,
    )
    assert any("feedback_offer_state" in item for item in pending_feedback["blockers"]), pending_feedback
    print("PASS: render coverage enforces semantic bodies and scope markers without fixed headings, labels, or paragraph quotas")


if __name__ == "__main__":
    main()
