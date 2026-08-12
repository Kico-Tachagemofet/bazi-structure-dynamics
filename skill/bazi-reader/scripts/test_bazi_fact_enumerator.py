#!/usr/bin/env python3
"""Regression checks for deterministic branch-relation facts."""

from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).with_name("bazi_fact_enumerator.py")
SPEC = importlib.util.spec_from_file_location("bazi_fact_enumerator", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def relation_types(pillars: list[str], branch: str) -> set[str]:
    payload = MODULE.branch_candidates(pillars)
    return {
        item["type"]
        for item in payload["pair_relations"]
        if item.get("branches") == [branch, branch]
    }


class BranchRelationFactTests(unittest.TestCase):
    def test_repeated_mao_is_not_self_punishment(self) -> None:
        types = relation_types(["甲卯", "丁丑", "丙戌", "辛卯"], "卯")
        self.assertIn("repeated_branch", types)
        self.assertNotIn("self_punishment", types)

    def test_repeated_wu_is_also_self_punishment(self) -> None:
        types = relation_types(["甲午", "丁丑", "丙戌", "辛午"], "午")
        self.assertIn("repeated_branch", types)
        self.assertIn("self_punishment", types)

    def test_self_punishment_members_are_closed(self) -> None:
        self.assertEqual(MODULE.SELF_PUNISH_BRANCHES, set("辰午酉亥"))


if __name__ == "__main__":
    unittest.main()
