# 八字 Coverage Receipt Schema v1.0

Coverage receipt 证明完整断局没有漏掉范围，不把内部 facets 变成问题、标题或段落模板。它与真实问题的 question-answer map 完全分开。

## Composition Receipt

`coverage-receipt.json` 最低结构：

```json
{
  "schema_version": "1.0",
  "case_id": "CASE-ID",
  "structure_freeze_id": "FREEZE-ID",
  "report_scope_ref": "report-scope.yaml",
  "coverage_items": [
    {
      "coverage_id": "CV-CAREER-TASK",
      "topic_id": "career-work",
      "facet_id": "task-and-problem-type",
      "coverage_status": "primary",
      "scene_kernel_refs": ["BSK-CAREER-01"],
      "finding_refs": ["F-CAREER-001"],
      "claim_refs": ["J-F-CAREER-001-01"],
      "explanatory_roles": {
        "formation": true,
        "advantage": true,
        "cost": true,
        "result-gate": true,
        "switch": true,
        "verification": true
      },
      "domain_specific_delta": "职业任务、组织结果与权限边界",
      "render_obligation_id": "CRO-CAREER-TASK"
    }
  ]
}
```

`not-applicable／source-gap` 可以没有 scene kernel／finding／claim refs，但必须有 `gap_or_na_reason`。其他状态必须有非空 kernel、finding、claim、领域增量与 render obligation。

## Render Receipt

正文在实际覆盖该 facet 的叙事位置放唯一不可见 marker：

```html
<!-- coverage_id: CV-CAREER-TASK -->
```

相邻 facets 可以在同一连续段落中各放 marker，不要求各自独占句子或段落。不得把 marker 转写成“关于这个问题”。

`coverage-render-receipt.json` 最低结构：

```json
{
  "schema_version": "1.0",
  "case_id": "CASE-ID",
  "report_ref": "full-reading.md",
  "coverage_render_receipts": [
    {
      "coverage_id": "CV-CAREER-TASK",
      "render_obligation_id": "CRO-CAREER-TASK",
      "marker_count": 1,
      "body_ref": "full-reading.md#career-storyline",
      "coverage_present": true,
      "audit_status": "pending-independent-audit"
    }
  ]
}
```

生产者不得把 `audit_status` 写成 PASS。机械 validator 只检查 ID、marker、receipt 与必要 refs 是否齐全；独立 Audit 仍须抽查正文是否真正讲到该 facet 的人事、场景、结果和边界，不能用字数或 marker 存在代替语义。
