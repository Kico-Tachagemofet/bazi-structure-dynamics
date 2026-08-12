#!/usr/bin/env python3
"""Self-test the independent Bazi delivery evidence scan."""

from __future__ import annotations

import tempfile
from pathlib import Path

from validate_delivery_artifacts import load_render_checker, scan


def main() -> None:
    checker = load_render_checker()
    with tempfile.TemporaryDirectory() as temp:
        case = Path(temp) / "fixture-case"
        case.mkdir()
        core_lines = "".join(f"  - {item}\n" for item in checker.NATAL_CORE_SECTIONS)
        scope = case / "report-scope.yaml"
        scope.write_text(
            "schema_version: '1.1'\n"
            "delivery_mode: full-reading\n"
            "report_depth: detailed-natal\n"
            "feedback_offer_state: offered\n"
            "natal_core_sections:\n"
            f"{core_lines}"
            "mandatory_sections:\n"
            "  - family-home\n  - education-learning\n  - wealth-resource\n  - career-work\n"
            "selected_optional_sections: []\n"
            "timing_scope:\n"
            "  requested: true\n"
            "  luck_periods: [LP-01-TEST]\n"
            "  annual_years: [2027]\n",
            encoding="utf-8",
        )
        finding = case / "topic-findings-test.md"
        finding.write_text(
            "## F-TEST-001\n"
            "judgment_id: J-F-TEST-001-01\n"
            "judgment_id: J-F-TEST-001-02\n"
            "judgment_id: J-F-TEST-001-03\n",
            encoding="utf-8",
        )
        core_markers = "\n".join(
            f"<!-- core_section_id: {item} -->\n原局结构章节 {item} 的完整说明。"
            for item in checker.NATAL_CORE_SECTIONS
        )
        render = case / "full-reading.md"
        render.write_text(
            f"{core_markers}\n"
            "<!-- topic_id: family-home -->\n"
            "<!-- finding_id: F-TEST-001 -->\n"
            "<!-- judgment_id: J-F-TEST-001-01 -->\n第一段具体说明判断与可核验表现。\n\n"
            "<!-- judgment_id: J-F-TEST-001-02 -->\n第二段具体说明形成机制和现实载体。\n\n"
            "<!-- judgment_id: J-F-TEST-001-03 -->\n第三段具体说明条件、反证和边界。\n\n"
            "<!-- topic_id: education-learning -->\n学习范围有自己的完整正文，说明吸收、考核和方法怎样运作。\n"
            "<!-- topic_id: wealth-resource -->\n财务范围有自己的完整正文，说明资源取得、分配和留存条件。\n"
            "<!-- topic_id: career-work -->\n事业范围有自己的完整正文，说明任务、权限和交付结果。\n"
            "<!-- topic_id: formative-major-luck -->\n"
            "<!-- luck_period_id: LP-01-TEST -->\n第一步大运有独立正文，说明临时增量、原局保留和到期退出。\n"
            "<!-- timing_year: 2027 -->\n2027 年有独立正文，说明旧结构、本人选择和外部结果。\n",
            encoding="utf-8",
        )
        receipt = case / "render-card-receipt.yaml"
        receipt.write_text(
            "raw_card_access: forbidden\n"
            "render_input_mode: audited-envelopes-only\n"
            "raw_card_read: false\n"
            "F-TEST-001\nJ-F-TEST-001-01\nJ-F-TEST-001-02\nJ-F-TEST-001-03\n",
            encoding="utf-8",
        )
        (case / "topic-lenses").mkdir()
        (case / "composition").mkdir()
        for relative in (
            "topic-lenses/natal-core.yaml",
            "composition/natal-core-coverage-index.yaml",
            "composition/hidden-manifestation-matrix.yaml",
            "composition/cross-topic-claim-registry.yaml",
            "composition/composition.md",
        ):
            (case / relative).write_text("fixture\n", encoding="utf-8")
        reader = case / "reader"
        reader.mkdir()
        (reader / "00-natal-core.md").write_text(core_markers, encoding="utf-8")
        timing = case / "structure" / "timing"
        timing.mkdir(parents=True)
        (timing / "year-2027-interaction-census.yaml").write_text("year: 2027\n", encoding="utf-8")
        (timing / "year-2027-overlay-diff.yaml").write_text("year: 2027\n", encoding="utf-8")
        for suffix in (
            "interaction-census.yaml",
            "activation-overlay.yaml",
            "process-state-diff.yaml",
        ):
            (timing / f"LP01-TEST-{suffix}").write_text("fixture: true\n", encoding="utf-8")

        result = scan(case, scope, render, receipt)
        assert result["verdict"] == "PASS", result
        (case / "composition" / "hidden-manifestation-matrix.yaml").unlink()
        result = scan(case, scope, render, receipt)
        assert result["verdict"] == "FAIL", result
        assert any("hidden-manifestation-matrix.yaml" in item for item in result["blockers"]), result
        (case / "composition" / "hidden-manifestation-matrix.yaml").write_text(
            "fixture\n", encoding="utf-8"
        )
        (timing / "LP01-TEST-process-state-diff.yaml").unlink()
        result = scan(case, scope, render, receipt)
        assert result["verdict"] == "FAIL", result
        assert any("LP-01-TEST" in item for item in result["blockers"]), result

    print("PASS: independent delivery scan catches current natal, reader, receipt, major-luck, and annual artifacts")


if __name__ == "__main__":
    main()
