# Report Scope Schema

`report-scope.yaml` 是结构冻结后、生活断局开始前的范围合同。它只记录求测中心、报告板块和问题，不产断语，也不保存用于证明命理结论的生活经历。

## Header

- `case_id`
- `scope_id`
- `structure_freeze_id`
- `delivery_mode`：full-reading／structure-only／limited-topic
- `chart_owner`
- `querent_role`：self／proxy／unknown
- `scope_status`：pending-user／confirmed／declined-extra-topics
- `created_at`

## Reading Center

- `default_center`：完整原局通常为 chart-owner／day-master
- `user_language_center`：求测者用自然语言说的“围绕谁／哪段关系／哪件事”
- `center_type`：self／person／relationship／family-system／event／organization／object
- `center_relation_to_chart_owner`
- `technical_taiji_assignment_status`：固定为 `pending-topic-lens`；实际技术锚点写入 per-topic lens，不回写求测者的范围原话
- `center_uncertainty`

若求测者没有另行指定，使用 `default_center: chart-owner`，不得因此阻塞标准原局。

## Required Baseline Topics

full-reading 必须逐项保存，slug 固定：

```yaml
mandatory_sections:
  - family-home
  - education-learning
  - wealth-resource
  - career-work
```

- `family-home`：原生家庭／父母与家庭系统／家庭资源压力／居住与维持生活环境；不自动等于婚恋或子女。
- `education-learning`：学习、吸收、输出、考试资格、专业与教育路径。
- `wealth-resource`：资源、收入机制、积累支出、流动性、可见度与变现。
- `career-work`：任务性质、岗位角色、组织环境、责任压力与职业发展。

limited-topic 可以不含四项，但必须记录 `omitted_baseline_sections` 与“不得称完整断局”。

## Optional Topics

```yaml
selected_optional_sections: []
```

可选 slug 示例：

- `love-relationship`
- `health-body`
- `occult-perception`
- `creation-expression`
- `social-collaboration`
- `children-parenting`
- 求测者自定义的稳定 slug

每个已选专题记录：

- `topic_slug`
- `exact_question`
- `user_language_center`
- `scope`：natal／timing／synastry／relationship-field
- `time_window`
- `requires_upstream_diff_or_overlay`

## User-facing Intake

范围入口至少确认：

1. 默认是否以命主本人为中心；若不是，围绕谁、哪段关系或哪件事；
2. 是否只看原局，或另有具体时间；
3. 除基础四板块外还想看什么；
4. 每个附加板块最想问清楚什么。

不得用“请选择太极点”要求普通求测者掌握术语。不得在此阶段索取详细家庭经历；家庭事实只在家庭 blind findings 审计后进入校准。

## Family Calibration Gate

`report-scope.yaml` 只记录门状态，不保存回答正文：

- `family_calibration_required`：full-reading 默认为 true
- `family_blind_finding_audit_id`
- `family_calibration_state`：not-ready／awaiting-user／completed／declined／uncalibrated／contaminated
- `calibration_response_ref`

状态约束：

- finding audit 前只能是 `not-ready`；
- 审计通过后才可变为 `awaiting-user`；
- 用户拒绝时记 `declined`，报告标未校准并继续；
- 用户在 blind finding 前已主动提供详细家庭事实且无法使用新鲜隔离上下文时记 `contaminated`，不得把家庭板块当盲回验，但仍可完成未校准报告；
- 回应只能校准 expression band、优先级、措辞或领域载体，不得修改结构。

## Completeness Rules

- full-reading 缺任一 mandatory section：FAIL。
- 任一 selected optional section 没有下游 Topic Lens／finding／render：FAIL。
- reading center 未定义且无法默认到 chart-owner：FAIL。
- 把家庭校准回答写入 blind finding：FAIL。
- structure-only 不得创建伪完整 report-scope；交付必须明确只到结构层。
