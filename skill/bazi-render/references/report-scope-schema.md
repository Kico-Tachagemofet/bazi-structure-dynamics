# Report Scope Schema

`report-scope.yaml` 是结构冻结后、生活断局开始前的范围合同。它只记录求测中心、报告板块和问题，不产断语，也不保存用于证明命理结论的生活经历。

## Header

- `schema_version: "1.1"`
- `case_id`
- `scope_id`
- `structure_freeze_id`
- `delivery_mode`：full-reading／structure-only／limited-topic
- `chart_owner`
- `querent_role`：self／proxy／unknown
- `scope_status`：pending-user／confirmed／declined-extra-topics
- `created_at`
- `report_depth`：`detailed-natal`／`summary`；`full-reading` 默认且通常必须为 `detailed-natal`，只有用户明确要求简版时才可选 summary
- `feedback_offer_state`：`pending`／`offered`／`accepted`／`declined`

`feedback_offer_state` 与 `validation_state` 是两条不同状态线：前者只记录是否向用户提供低负担核验入口，后者记录是否进入有资格的验证流程。完整报告生成前可为 `pending`；交付时必须改为 `offered`，用户已拒绝则为 `declined`。

## Reading Center

- `default_center`：完整原局通常为 chart-owner／day-master
- `user_language_center`：求测者用自然语言说的“围绕谁／哪段关系／哪件事”
- `center_type`：self／person／relationship／family-system／event／organization／object
- `center_relation_to_chart_owner`
- `technical_taiji_assignment_status`：固定为 `pending-topic-lens`；实际领域体、用神枢纽与关系轴写入 per-topic lens，不回写求测者的范围原话
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

full-reading 还必须逐项保存八个不可选的原局 core section：

```yaml
natal_core_sections:
  - natal-facts-boundaries
  - natal-system-engine
  - natal-four-pillars
  - natal-hidden-manifestation
  - natal-relation-network
  - natal-ten-god-functions
  - natal-pattern-use-agency
  - natal-synthesis-tensions
```

这八项是“原局详批”，四个 baseline topics 是生活领域展开；两组不能互相替代。

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
- `explicit_question`：可为空；只有求测者真正提出具体问题时填写
- `explicit_question_source`：user-verbatim／scope-confirmed／faithful-restatement；问题为空时亦为空
- `explicit_question_source_ref`
- `user_language_center`
- `scope`：natal／timing／synastry／relationship-field
- `time_window`
- `requires_upstream_diff_or_overlay`

## Timing Scope

涉及岁运时另存：

```yaml
timing_scope:
  requested: true
  luck_periods:
    - luck_period_id: DAYUN-GUI-CHOU
      label: 癸丑大运
  annual_years: [2021, 2022, 2023]
```

`annual_years` 中每一个年份都必须在 Topic Lens、Structure overlay、Finding 与 Render 中拥有独立 scope atom 与 marker。不得把一个年份范围字符串、一个大运总述或一个多年 finding 当作逐年交付。

## User-facing Intake

范围入口至少确认：

1. 默认是否以命主本人为中心；若不是，围绕谁、哪段关系或哪件事；
2. 是否只看原局，或另有具体时间；
3. 除基础四板块外还想看什么；
4. 若求测者有具体追问，原样记录；若只说“看这个专题”，保留为空，由 coverage profile 保证完整展开，不替用户编问题。

不得用“请选择太极点／用神”要求普通求测者掌握术语。求测者只确认自然语言问题中心；用神枢纽由冻结 `use-kernel.md` 与 Topic Lens 选择。不得在此阶段索取可能参与后续盲 finding 或流运验证的详细经历。

## Experience and Validation State

`report-scope.yaml` 只记录意图和状态，不保存回答正文。完整报告不强制经历映射或验证：

- `manifestation_mapping_requested`：true／false
- `manifestation_mapping_state`：none／not-ready／awaiting-user／completed／declined／contaminated
- `manifestation_response_ref`
- `manifestation_map_ref`
- `validation_requested`：true／false
- `validation_mode`：none／timing-preregistered／natal-discriminative
- `validation_response_mode`：quick-feedback／expanded-opt-in／none
- `validation_state`：none／ineligible／planning／hypotheses-frozen／awaiting-user／scored／unscored／declined／contaminated
- `validation_plan_ref`
- `hypothesis_freeze_ref`
- `validation_response_ref`
- `quick_feedback_ref`
- `validation_scorecard_ref`
- `validation_score_audit_ref`

状态约束：

- finding audit 前不得运行 manifestation mapping；
- timing 假设冻结前不得索取或读取对应年史；
- 默认使用 quick-feedback，用户未明确选择时不得启动 expanded-opt-in；quick feedback 不计分、不自动追问；
- `validation_mode: none` 不得把 `feedback_offer_state` 自动设为无或省略；它只关闭正式验证，不关闭报告末尾的低负担邀请；
- 用户拒绝时记 `declined`，报告继续；缺失历史或记不清记 `unscored`，不当作反证；
- 已知经历必须在 validation plan 登记并排除／降权；无法隔离时记 `contaminated`，不得声称盲验证；
- 显化映射不得改结构或增置信度；验证结果也只能支持／削弱冻结的时间假设，不能反向改写 natal。

## Completeness Rules

- full-reading 缺任一 mandatory section：FAIL。
- full-reading／detailed-natal 缺任一 `natal_core_sections`、或 `report_depth` 未声明：FAIL。
- 任一 selected optional section 没有下游 Topic Lens／finding／render：FAIL。
- `timing_scope.requested: true` 时，任一 `annual_years` 没有独立下游 atom／finding／year marker：FAIL。
- 报告已交付而 `feedback_offer_state` 仍为 `pending` 或缺失：FAIL。
- reading center 未定义且无法默认到 chart-owner：FAIL。
- 把经历写入 blind finding，或在 hypothesis freeze 前读取年史却声称盲验证：FAIL。
- structure-only 不得创建伪完整 report-scope；交付必须明确只到结构层。
