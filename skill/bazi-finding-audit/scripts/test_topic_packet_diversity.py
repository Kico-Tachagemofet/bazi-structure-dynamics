#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


PATH = Path(__file__).with_name("validate_topic_packet_diversity.py")
SPEC = importlib.util.spec_from_file_location("packet_validator", PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(MODULE)


class PacketDiversityTests(unittest.TestCase):
    def test_identical_generic_packets_fail(self):
        packets = [
            ("career", {"selected_units": [{"unit_id": "TG"}, {"unit_id": "FIVE"}], "domain_carrier_leads": []}),
            ("wealth", {"selected_units": [{"unit_id": "TG"}, {"unit_id": "FIVE"}], "domain_carrier_leads": []}),
        ]
        self.assertTrue(MODULE.validate_packets(packets))

    def test_distinct_packets_pass(self):
        packets = [
            ("career", {"selected_units": [{"unit_id": "TG-KILL"}, {"unit_id": "ST-WU"}]}),
            ("wealth", {"selected_units": [{"unit_id": "TG-WEALTH"}, {"unit_id": "ST-BING"}]}),
        ]
        self.assertEqual(MODULE.validate_packets(packets), [])


if __name__ == "__main__":
    unittest.main()
