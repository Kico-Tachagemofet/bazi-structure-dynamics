# 八字太极场 Topic Lens Schema v4.1

v4.1 把“完整断局的材料组织”与“用户问题的答案闭环”分开，并增加必须判断的现实端点。完整原局与常规专题先建立太极场、覆盖 facets、mandatory judgment dimensions、十神关系轴和开放取象请求；只有用户真实提出的具体问题才建立 Reader Answer Contract。内部 coverage profile 不得伪装成几十个用户问题，更不得预写答案。

## 一、核心原则

- Topic Lens 的主产物是 `taiji_field_packet`，不是问题答案表。
- coverage facets 只说明必须检查哪些面，不要求逐 facet 建 axis、finding、标题或段落。
- mandatory judgment dimensions 说明最终必须对哪些现实结果端点作方向裁决；它们不是问题，也不预填答案，但不得被 scene kernel 聚合静默删除。
- axis 由本盘真实 process、十神关系链和柱位场景生成，不由问题数量生成。
- 一个 axis 可以覆盖多个 facets；一个 facet 也可以由数个 axes 共同回答。
- Lens 只登记要判断的结果维度，不得填写实际结果、角色排序、职业偏好、事件或最终载体。

## 二、最低结构

```yaml
schema_version: "4.1"
case_id: CASE-ID
topic_id: career-work
structure_freeze_id: FREEZE-ID
report_scope_ref: report-scope.yaml
taiji_field:
  user_language_center: 命主本人在职业中的任务、位置与发展
  field_type: person-domain
  people_or_roles_in_scope: []
  matters_or_objects_in_scope: []
  result_dimensions_to_determine: []
  boundaries: []
coverage_facets:
  - facet_id: task-and-problem-type
    coverage_status: required
    reader_relevance: 要判断实际处理哪类任务
    attached_axis_ids: []
    final_disposition: pending-finding

mandatory_judgment_dimensions:
  - dimension_id: education-attainment-level
    required_disposition: directional-verdict|not-applicable|source-gap
    specificity_floor: L1-outcome-level
    supporting_process_refs: [P-01]
    candidate_axis_refs: [AX-EDU-01]
    downstream_claim_endpoint: formal-education-attainment
    no_silent_merge: true
explicit_reader_questions: []
topic_process_axes:
  - axis_id: AX-CAREER-01
    axis_formation_basis: distinct-process-ten-god-pillar-scene
    process_ref: P-02
    route_closure_receipt_ref: structure-process-handoff.yaml#P-02
    phase_focus_refs: []
    focal_relation_problem: null
    actual_controller_or_carrier_refs: []
    ten_god_chain_plan:
      domain_body: null
      required_relation_functions: []
      result_dimension_to_determine: null
      feedback_and_competition_to_check: []
      forbidden_shortcuts: []
    stem_branch_anchor_plan:
      visible_stem_refs: []
      branch_position_refs: []
      hidden_stem_refs: []
      pillar_role_refs: []
      relation_after_state_refs: []
    scene_kernel_required: true
    attached_facet_ids: []
    attached_explicit_question_ids: []
deep_card_queries: []
domain_carrier_requests: []

candidate_palette_requests:
  - palette_id: PAL-EDU-01
    judgment_dimension_refs: [education-attainment-level]
    requested_specificity_levels: [L2-domain-nature, L3-action-material, L4-carrier-family]
    activation_anchor_refs: []
    excluded_preselection: [preferred-career, exact-school, exact-identity]
source_and_kernel_handoff:
  required_claim_endpoint_refs: [formal-education-attainment]
  endpoint_differentiation_required: true
  scene_synthesis_count_policy: chart-derived-after-differentiation
  required_material_spread: true
  required_ten_god_stem_branch_synthesis: true
```

## 三、显式问题合同

`explicit_reader_questions` 只收：

- 用户主动问出的具体问题；
- 代看者明确要求回答的具体问题；
- report scope 中逐字确认的专项问题。

每项只登记：

- 原样问题；
- `source_kind: user-verbatim／scope-confirmed／faithful-restatement` 与可追溯 `source_ref`，证明它不是模型为 coverage 自造的问题；
- 涉及的人／角色；
- 事情／对象；
- 要裁定的结果维度；
- 允许的答案状态与边界；
- 闭合键。

不得出现：

- `external_result_target`；
- `direct_answer`／`direct_answer_summary`；
- 已经写好的角色、职业、事件或排序；
- `answer_status: complete／conditional`；
- 任何准备原样复制到 finding 或 Render 的结论句。

完整原局的内部 facet 不是用户问题，不自动生成 Reader Answer Contract。Composition 完成后可以建立 coverage receipt，证明相关面已在象核和正文中得到处理。

## 四、关系轴形成规则

每条 axis 必须由以下至少三层共同形成：

1. 一个冻结 process／phase；
2. 一条可区分的十神关系链或链内分叉；
3. 一组特定柱位／干支／藏干关系后锚点。

只有以下变化才宜拆成独立 axis：

- 起点或结果端不同；
- 同一节点分别走向两个相反结果；
- 柱位使同一关系链落到明显不同的人事场；
- 日主能动性或现实结果门不同；
- timing window 改写了 process phase 或人物载体。

不得因为 facet 多、问题多或十神多便机械拆轴。也不得把全专题所有差异压成一条“压力—支持—输出”泛化轴。不同现实结果端点可以共享 axis 和 process，但必须分别进入 downstream claim endpoint；`axis 可合成` 不等于 `结果可以不判断`。

## 五、取象请求

每个 full-reading topic 至少请求：

- `DC-FIVE-ELEMENTS-CORE`；
- `DC-TEN-GODS-CORE`；
- 涉及地支时的 `DC-EARTHLY-BRANCHES-CORE`；
- 所有进入主轴的独立天干卡；
- 所有进入主轴的地支卡；
- 重要藏干对应天干卡；
- 人物、工作、关系、身体、场所或事件需要的 relational／symbol carrier units；
- 具体职业、正式身份、疾病或事件候选需要的 `domain_carrier_request`。

完整原局另建立 natal chart-card inventory：本盘实际出现的全部独立天干、地支和重要藏干卡只需完整读取一次，各 topic 可以共享 full-read receipt，但必须独立选择和组合单元。对 L2–L4 现实取象另发 `candidate_palette_requests`；它要求 Source 返回所有已激活且相容的动作、材料和载体家族，不得由 Lens 预先缩成一个泛化职业答案。

## 六、机械门槛

- Topic Lens 出现任何预写结论字段：BLOCKER。
- synthetic coverage facet 被冒充成 user question：BLOCKER。
- axis 与 question 一一机械对应、却没有独立结构形成依据：BLOCKER。
- axis 缺 process、十神链计划或干支锚点任一项：BLOCKER。
- full-reading topic 需要现实载体却没有相应 carrier request：BLOCKER。
- 宽专题缺 mandatory judgment dimensions，或任何 required dimension 没有 downstream claim endpoint 且无具体 `not-applicable／source-gap`：BLOCKER。
- 用一个预定 mega-kernel 吞并学历、专业性质、权责、名声、收入、变动等不同结果端点：BLOCKER。
- 所有 topic 使用完全相同 query／unit 组合且没有差异收据：BLOCKER。
- expected finding 数由 question 数直接计算：BLOCKER。
