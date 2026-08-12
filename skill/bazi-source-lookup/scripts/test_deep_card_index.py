#!/usr/bin/env python3
"""Self-test the Deep Card index and Earthly Branch runtime contracts."""

from __future__ import annotations

import shutil
import tempfile
from pathlib import Path

from validate_deep_card_index import validate


def copy_fixture(temp_root: Path) -> Path:
    skill_root = Path(__file__).resolve().parents[1]
    source_references = skill_root / "references"
    target_references = temp_root / "skills" / "bazi-source-lookup" / "references"
    target_references.mkdir(parents=True)
    shutil.copy2(source_references / "deep-card-index.yaml", target_references)
    shutil.copytree(source_references / "deep-cards", target_references / "deep-cards")
    reader_source = skill_root.parent / "bazi-reader" / "scripts" / "bazi_fact_enumerator.py"
    reader_target = temp_root / "skills" / "bazi-reader" / "scripts"
    reader_target.mkdir(parents=True)
    shutil.copy2(reader_source, reader_target)
    return target_references / "deep-card-index.yaml"


def main() -> None:
    skill_root = Path(__file__).resolve().parents[1]
    live_index = skill_root / "references" / "deep-card-index.yaml"
    assert validate(live_index) == []
    xu_text = (live_index.parent / "deep-cards" / "branch-xu.md").read_text(encoding="utf-8")
    assert "`XU-MEDIA-CARRIER-GOVERNANCE`" in xu_text
    assert "离火／信息／媒介轴已独立冻结" in xu_text
    assert "`XU-VIRTUAL-" not in xu_text

    with tempfile.TemporaryDirectory() as temp:
        index = copy_fixture(Path(temp))
        zi = index.parent / "deep-cards" / "branch-zi.md"
        zi.write_text(
            zi.read_text(encoding="utf-8").replace(
                "- `commander_does_not_rewrite_hidden_stems`: true\n", ""
            ),
            encoding="utf-8",
        )
        errors = validate(index)
        assert any("missing branch contract declarations" in error for error in errors)

    with tempfile.TemporaryDirectory() as temp:
        index = copy_fixture(Path(temp))
        chou = index.parent / "deep-cards" / "branch-chou.md"
        rows = chou.read_text(encoding="utf-8").splitlines()
        chou.write_text(
            "\n".join(line for line in rows if not line.startswith("| `CHOU-QI-XIN-RESIDUAL` |"))
            + "\n",
            encoding="utf-8",
        )
        errors = validate(index)
        assert any("hidden stem 辛 needs exactly one runtime interface" in error for error in errors)

    with tempfile.TemporaryDirectory() as temp:
        index = copy_fixture(Path(temp))
        text = index.read_text(encoding="utf-8")
        if "  planned_on_new_runtime_contract: []\n" in text:
            mutated = text.replace(
                "  planned_on_new_runtime_contract: []\n",
                "  planned_on_new_runtime_contract:\n    - DC-BRANCH-ZI\n",
                1,
            )
        else:
            mutated = text.replace(
                "  planned_on_new_runtime_contract:\n",
                "  planned_on_new_runtime_contract:\n    - DC-BRANCH-ZI\n",
                1,
            )
        index.write_text(
            mutated,
            encoding="utf-8",
        )
        errors = validate(index)
        assert any("contains non-planned cards" in error for error in errors)

    with tempfile.TemporaryDirectory() as temp:
        index = copy_fixture(Path(temp))
        chen = index.parent / "deep-cards" / "branch-chen.md"
        chen.write_text(
            chen.read_text(encoding="utf-8").replace(
                "- `static_hidden_stems`: [戊, 乙, 癸]\n",
                "- `static_hidden_stems`: [戊, 癸, 乙]\n",
                1,
            ),
            encoding="utf-8",
        )
        errors = validate(index)
        assert any("do not match Reader" in error for error in errors)

    with tempfile.TemporaryDirectory() as temp:
        index = copy_fixture(Path(temp))
        zi = index.parent / "deep-cards" / "branch-zi.md"
        zi.write_text(
            zi.read_text(encoding="utf-8").replace(
                "- `status`: approved\n",
                "- `status`: draft_pending_human_review\n",
                1,
            ),
            encoding="utf-8",
        )
        errors = validate(index)
        assert any("index status approved does not match card declaration" in error for error in errors)

    with tempfile.TemporaryDirectory() as temp:
        index = copy_fixture(Path(temp))
        zi = index.parent / "deep-cards" / "branch-zi.md"
        zi.write_text(
            zi.read_text(encoding="utf-8").replace(
                "- `review_state`: runtime_approved_by_human_2026-08-10\n",
                "- `review_state`: source_audited_pending_human_review\n",
                1,
            ),
            encoding="utf-8",
        )
        errors = validate(index)
        assert any("approved card missing human runtime approval receipt" in error for error in errors)

    with tempfile.TemporaryDirectory() as temp:
        index = copy_fixture(Path(temp))
        index.write_text(
            index.read_text(encoding="utf-8").replace(
                "  status: production_enabled\n",
                "  status: staged\n",
                1,
            ),
            encoding="utf-8",
        )
        errors = validate(index)
        assert any("missing production approval declarations" in error for error in errors)

    print(
        "PASS: approved Deep Cards match index approval receipts and branch cards match Reader "
        "hidden stems while keeping commander, manifestation, and migration states separate"
    )


if __name__ == "__main__":
    main()
