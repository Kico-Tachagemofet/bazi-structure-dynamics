#!/usr/bin/env python3
"""Self-test the mechanical Bazi render coverage checker."""

from check_render_coverage import check


FINDINGS = """
## F-TEST-001
body
## F-TEST-002
body
"""

GOOD = """
### First
<!-- finding_id: F-TEST-001 -->
生活判断：A
条件与代价：B
技术依据：C
### Second
<!-- finding_id: F-TEST-002 -->
生活判断：D
条件与代价：E
技术依据：F
"""

BAD = """
### Compressed
<!-- finding_id: F-TEST-001 -->
生活判断：A
技术依据：C
"""


def main() -> None:
    good = check(FINDINGS, GOOD, "report", [])
    bad = check(FINDINGS, BAD, "report", [])
    assert good["verdict"] == "PASS", good
    assert bad["verdict"] == "FAIL", bad
    assert any("F-TEST-002" in item for item in bad["blockers"]), bad
    assert any("条件与代价" in item for item in bad["blockers"]), bad
    print("PASS: render coverage accepts 1:1 output and rejects compression")


if __name__ == "__main__":
    main()
