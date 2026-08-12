#!/usr/bin/env python3
from __future__ import annotations

import copy
import importlib.util
import unittest
from pathlib import Path


PATH = Path(__file__).with_name("validate_coverage_render_receipt.py")
SPEC = importlib.util.spec_from_file_location("coverage_validator", PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(MODULE)


def fixtures():
    coverage = {
        "schema_version": "1.0", "case_id": "CASE", "structure_freeze_id": "FRZ",
        "report_scope_ref": "report-scope.yaml", "coverage_items": [{
            "coverage_id": "CV-CAREER-TASK", "topic_id": "career-work", "facet_id": "task",
            "coverage_status": "primary", "scene_kernel_refs": ["BSK-01"],
            "finding_refs": ["F-01"], "claim_refs": ["J-F-01-01"],
            "explanatory_roles": {role: True for role in MODULE.ROLES},
            "domain_specific_delta": "职业任务、成果与权限边界",
            "render_obligation_id": "CRO-01",
        }],
    }
    receipt = {
        "schema_version": "1.0", "case_id": "CASE", "report_ref": "full-reading.md",
        "coverage_render_receipts": [{
            "coverage_id": "CV-CAREER-TASK", "render_obligation_id": "CRO-01",
            "marker_count": 1, "body_ref": "full-reading.md#career",
            "coverage_present": True, "audit_status": "pending-independent-audit",
        }],
    }
    report = "<!-- coverage_id: CV-CAREER-TASK -->\n职业任务与成果怎样转成权限，正文在这里连续展开。"
    return coverage, report, receipt


class CoverageReceiptTests(unittest.TestCase):
    def test_valid_receipts_pass(self):
        self.assertEqual(MODULE.validate(*fixtures()), [])

    def test_missing_kernel_ref_fails(self):
        coverage, report, receipt = fixtures()
        coverage = copy.deepcopy(coverage)
        coverage["coverage_items"][0]["scene_kernel_refs"] = []
        self.assertTrue(any("scene_kernel_refs" in error for error in MODULE.validate(coverage, report, receipt)))

    def test_producer_self_pass_fails(self):
        coverage, report, receipt = fixtures()
        receipt = copy.deepcopy(receipt)
        receipt["coverage_render_receipts"][0]["audit_status"] = "PASS"
        self.assertTrue(any("self-pass" in error for error in MODULE.validate(coverage, report, receipt)))


if __name__ == "__main__":
    unittest.main()
