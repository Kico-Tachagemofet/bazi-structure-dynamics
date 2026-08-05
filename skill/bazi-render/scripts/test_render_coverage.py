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
## Family
<!-- topic_id: family-home -->
### First
<!-- finding_id: F-TEST-001 -->
生活判断：A
条件与代价：B
技术依据：C
## Education
<!-- topic_id: education-learning -->
### Second
<!-- finding_id: F-TEST-002 -->
生活判断：D
条件与代价：E
技术依据：F
## Wealth
<!-- topic_id: wealth-resource -->
## Career
<!-- topic_id: career-work -->
"""

BAD = """
### Compressed
<!-- finding_id: F-TEST-001 -->
生活判断：A
技术依据：C
"""

SCOPE = """
delivery_mode: full-reading
mandatory_sections:
  - family-home
  - education-learning
  - wealth-resource
  - career-work
selected_optional_sections: []
family_calibration_state: uncalibrated
"""

BAD_SCOPE = """
delivery_mode: full-reading
mandatory_sections:
  - family-home
  - education-learning
selected_optional_sections:
  - love-relationship
family_calibration_state: awaiting-user
"""


def main() -> None:
    good = check(FINDINGS, GOOD, "report", [], SCOPE)
    bad = check(FINDINGS, BAD, "report", [])
    bad_scope = check(FINDINGS, GOOD, "report", [], BAD_SCOPE)
    assert good["verdict"] == "PASS", good
    assert bad["verdict"] == "FAIL", bad
    assert bad_scope["verdict"] == "FAIL", bad_scope
    assert any("F-TEST-002" in item for item in bad["blockers"]), bad
    assert any("条件与代价" in item for item in bad["blockers"]), bad
    assert any("baseline" in item.lower() for item in bad_scope["blockers"]), bad_scope
    assert any("calibration" in item.lower() for item in bad_scope["blockers"]), bad_scope
    assert any("love-relationship" in item for item in bad_scope["blockers"]), bad_scope
    print("PASS: render coverage enforces findings, topics, baseline, and calibration gates")


if __name__ == "__main__":
    main()
