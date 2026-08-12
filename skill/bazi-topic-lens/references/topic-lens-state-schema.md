# Topic Lens State Schema v3.2

`topic-lens-<slug>.json` 是 Topic 阶段唯一机器事实源；Markdown 只作投影。v3.2 在 v3.1 的读者问题剖面上增加 Reader Answer Contract 与跨下游闭合键，禁止把英文 facet、性格画像、改善建议、技术标签或跨专题总括冒充问题答案。Topic Lens 仍不读取卡片内容，也不预写生活结论。

## 1. Header

- `schema_version: "3.2"`；既有 `2.0–3.1` 产物只读兼容，新产物使用 3.2，禁止混合冻结
- `case_id`
- `topic_id`
- `topic_intent`：`descriptive`／`capability`／`outcome`／`therapeutic`／`timing`／`synastry`
- `exact_question`
- `scope`
- `framework_lock`
- `structure_freeze_id`
- `structure_freeze_ref`
- `use_kernel_ref`
- `structure_process_handoff_ref`
- `report_scope_ref`
- `delivery_mode`
- `subject_context_available_to_finding: false`

## 2. Frozen Facts Snapshot

`facts_snapshot` 必须含五项，每项有 `status`、`value`、`refs`、`conflicts_or_limits`：

1. `commander`：`value` 内分列 `month_branch_main_qi`、`commander`、`seasonal_phase`；不得重复计权。
2. `exposed_stems`
3. `dominant_branch_field`
4. `daymaster_roots_and_access`
5. `conventional_symbol_post_state_and_destination`

无法裁定写 `undetermined`，不能用 topic 常识补空白。

## 3. Question Slices and Topic Body

v3.1 顶层必须有 `reader_question_profile`，它只记“应检查什么”：

- `profile_id`
- `profile_ref`：指向 [读者问题剖面](reader-question-profiles.md) 或已确认的自定义剖面
- `profile_type`：`baseline`／`optional`／`custom`／`timing`
- `required_facet_ids`
- `facet_dispositions`

每个 `facet_disposition` 至少含 `facet_id`、`disposition`（`primary`／`supporting`／`cross-ref`／`not-applicable`／`source-gap`）、`question_slice_ids`、`axis_ids`、`answer_contract_ids`、`domain_specific_delta`、`shared_answer_ref` 与 `reason`。每个 required facet 必须恰好出现一次。`primary／supporting／cross-ref` 的 `domain_specific_delta` 不得为空；cross-ref 的 `shared_answer_ref` 必填。not-applicable／source-gap 可以没有 slice／contract，但须给出 reason。这些 facet 不得直接当 finding 列表或 Render 标题。

每个 `question_slices` 项至少含：

- `question_slice_id`
- `user_language_center`
- `center_type`
- `relation_to_chart_subject`
- `body_anchor_refs`
- `internal_mechanism_target`
- `domain_carrier_target`
- `external_result_target`
- `strongest_alternative_body`
- `facet_id`
- `reader_need`
- `exact_reader_question`：自然中文、可由命主理解并指向具体答案对象；不得使用英文 facet slug、专题名或 `完整回答<facet>` 占位
- `explanatory_obligations`：从 `formation`、`advantage`、`cost`、`result-gate`、`switch`、`verification` 中列本 slice 必须交付的内容角色
- `reader_answer_contract`：见下节

`explanatory_obligations` 是材料合同，不是六段可见模板。某项确实不适用时，在 facet 处置或 finding 边界说明，不用空话占位。

### Reader Answer Contract

每个实质 question slice 的 `reader_answer_contract` 至少含：

- `contract_id`
- `answer_target`：含非空 `subject_or_role`、`matter_or_domain_object`、`result_or_outcome`
- `direct_answer_required: true`
- `allowed_answer_statuses`：完整列 `complete`、`conditional`、`not-applicable`、`source-gap`
- `prohibited_answer_substitutes`：完整列 `personality-only`、`advice-only`、`generic-cross-topic-summary`、`technical-label-only`
- `topic_specificity_required: true`
- `closure_key`：在本 case／freeze 下唯一，用于 Source、Finding、Composition、Render 和 Audit 一一闭合

本合同只锁定必须回答的问题与边界，不提前写盘面答案。一个 finding 可服务多个 contract，但每个 contract 必须在 `question-answer-map.yaml` 中拥有独立 direct answer claim；同一 process 或同一 summary 不能自动满足多个问题。

## 4. Centers

`centers` 分三栏：

- `conventional_symbol_candidates`：`candidate_id`、`symbol_refs`、`reason_conventional`
- `actual_controller_or_carrier`：`center_id`、`refs`、`mechanism`、`comparison_against_alternatives`
- `therapeutic_pivots`：可为空；每项须引用 `use-kernel.md` 已存在 pivot

`topic_intent: therapeutic` 时治疗枢纽不得为空；其他意图不得为了填字段强选用神。

## 5. Star Eligibility

`star_eligibility` 与常规候选一一对应：

- `candidate_id`
- `status`：`qualified`／`diverted`／`absorbed-by`／`suppressed-by`／`not-applicable`／`undetermined`
- `evidence_refs`
- `post_state_refs`
- `destination`
- `comparison_against_alternatives`
- `disposition_target`：改道／被接管／被压制时必填

`qualified` 不是“传统上相关”，而是比较关系后仍能主导本题过程。

## 6. Capability Bridge

`capability_bridge` 至少含：

- `claim_target`
- `claim_level`：`internal_potential`／`callable_capability`／`sustainable_output`／`external_result`／`not-claimed`
- `claim_strength`：`strong`／`conditional`／`not-claimed`
- `required_gates`
- `gates`
- `claim_disposition`

六个 gates：`potential`、`daymaster_access`、`visibility`、`sustainability`、`destination`、`external_result`。每项记录 `status`（`supported`／`conditional`／`blocked`／`not-applicable`／`undetermined`）、`evidence_refs` 与 `counterevidence`。

强结论的必需 gates 全部须为 `supported`。条件式结论不得绕过 `blocked` 或 `undetermined`；不同 claim level 可声明不同必需 gate，但须写明理由。

## 7. Topic Process Axes

每条 `topic_process_axes` 至少含：

- `axis_id`
- `question_slice_id`
- `axis_role`：`primary`／`supporting`／`contrast`／`deferred`
- `focal_question`
- `conventional_symbol_refs`
- `controller_or_carrier_refs`
- `therapeutic_pivot_ref`：可为 `null`
- `process_ref`
- `process_freeze_or_hash_ref`
- `route_closure_receipt_ref`
- `phase_focus_refs`
- `strength_and_bearing_snapshot_ref`
- `source_endpoint`／`target_endpoint`：仅作 phase 可读投影
- `node_refs`／`edge_refs`／`route_refs`：必须由 process closure 完整投影
- `complete_edge_closure`
- `mechanism`
- `base_state`
- `supporting_factors`
- `damage_diversion_or_occupation`
- `destination_and_feedback`
- `daymaster_agency_relation`
- `daymaster_cost_ref`
- `therapeutic_effect_ref`
- `residual_problem_ref`
- `bypass_and_rebound_ref`
- `agency_phase_refs`
- `competing_allocation`
- `switch_conditions`
- `failure_or_reversal`
- `strongest_alternative`
- `finding_disposition`：`required`／`deferred`／`source-gap`

primary axis 必须引用实际控制者／承载者。资格不是 `qualified` 的常规星不得仅凭自己成为主轴。

`complete_edge_closure` 必须与 `process_ref.route_closure_receipt` 相等。Topic 可以选择 phase focus，但没有删减 process edge 的权限。timing／synastry 轴另须含：

- `timing_process_diff_ref`
- `propagation_closure_ref`
- `process_before_after_ref`
- `agency_transition_ref`
- `expiry_rule`
- `timing_manifestation_adjudication`

缺任一项不得进入 Composition。

`timing_manifestation_adjudication` 至少含：

- `natal_node_state_refs`：原局逐位置节点的冻结显隐、参与层和 direct-action gate
- `activation_interface_refs` 与 `matched_trigger_refs`
- `overlay_function_transition`：原局功能→本窗口功能；区分 root-support、environmental-feed、direct-function 与 visible-interface
- `relation_requalification_refs`：包含合、克、生、泄、占用或改道的重裁收据
- `shared_node_competition_ref`：外来关系是否占用原局主路的同一节点
- `retained_natal_route_ref`：原局 process 哪些 phase 仍在、剩余通量与备用路线
- `temporary_relation_function`：在本 topic 中临时增强或改道的关系功能；不直接填具体人物
- `role_mapping_disposition`：`not-requested`／`candidate-requested`／`source-gap`
- `role_candidate_refs`：指向受控领域载体请求，可为空但必须与 disposition 一致
- `impact_bounds_ref`：受影响路线核心度、overlay 强度／持续、剩余主路和备用路线的结构边界
- `runtime_context_refs`：当时职位、角色或组织场景的条件分支；不得作结构证据
- `expiry_rule`

“原局有主路”不自动等于影响轻；“流年透出”也不自动等于影响重。必须通过 before／after、共享节点分配和 retained natal route 裁定。

v3.1 timing／synastry 顶层另含 `runtime_context_policy`：

- `context_status`：`known-from-question`／`unknown`／`withheld-for-blindness`
- `context_refs`：只可引用 report scope 或用户当前问题中公开的角色条件
- `allowed_use: carrier-branching-and-agency-only`
- `structural_inference_forbidden: true`
- `confidence_uplift_forbidden: true`
- `unknown_context_action: keep-conditional-branches`

现实位置可改变载体和可控范围，不改变五行关系或 process diff。

## 7B. Coverage Profile and Scope Atoms

v3 顶层必须含 `coverage_profile`：

- `profile_id`
- `scope_type`：natal-core／baseline-topic／optional-topic／timing-period／timing-annual／synastry
- `required_question_slices`
- `covered_question_slice_ids`
- `not_applicable_receipts`
- `deferred_or_source_gap_receipts`
- `primary_axis_count`
- `required_primary_axis_count`
- `expected_primary_finding_count`
- `coverage_verdict`

`required_primary_axis_count` 由本题真实 question slices 与 scope profile 计算，不是所有盘统一数字。每个 required slice 必须被 primary axis、cross-ref、not-applicable 或 source-gap 唯一处置；不得静默消失。

顶层 `scope_atoms` 用于不能被聚合替代的单位：

- detailed-natal：八个 core section 各是一个 atom；
- 四柱专题：四个柱位分别是 atom；
- 重要藏干显化：每个逐位置 node 是 atom；
- timing-period：每个大运段是 atom；
- 用户请求逐年：每个流年是 atom。

每个 atom 至少含 `atom_id`、`atom_type`、`label`、`required`、`axis_ids`、`finding_disposition`、`not_applicable_reason`。`required: true` 的年度 atom 必须至少引用一条 primary axis；综合十年 axis 不能同时满足十个年度 atom。

## 8. Finding Handoff and Index

### Deep Card Queries

v3 顶层 `deep_card_queries` 每项至少含：

- `query_id`
- `axis_id`：五行总卡可为 `null`，其他卡须引用本 topic 已存在 axis
- `symbol_family`：`foundation`／`heavenly_stem`／`earthly_branch`／`ten_god`
- `symbol`
- `card_id`
- `reason_needed`
- `topic_axis`
- `required_source_layers`
- `requested_unit_classes`：从 `semantic_core／state_modifier／symbol_carrier／relational_carrier／composite_domain_carrier／cross_system_context` 中按本题选择
- `activation_basis_refs`：触发此请求的冻结 axis、node／edge／route、关系后状态、中心或 capability gate；五行总卡可只引用 topic／freeze
- `requested_carrier_scope`：`none／symbol／relational／composite`
- `claim_ceiling`：Topic 阶段只允许声明本次请求最高可送到 `mechanism／candidate`；不得预判 supported 以上等级
- `selection_purpose`：本次申请只为解释什么，例如 process、性格行为、外形、身体功能、工作性质、物件或关系功能；不得填写具体职业／身份答案
- `excluded_unit_classes`：显式拒绝送往下游的单元类别；与 `requested_unit_classes` 不得重叠。未请求类别一律默认拒绝，不因整卡被 Source Lookup 读取而自动开放
- `excluded_uses`：本题明确不允许从该卡调用的领域、载体或结构用途
- `raw_card_access_requested: false`：Topic 无权申请母卡全文进入 Composition 或 Render
- `query_status`：`requested`／`deferred`

每个 topic 恰有一项 `DC-FIVE-ELEMENTS-CORE` foundation query。这里只声明需要什么，不读取 card path、内容或审阅状态；这些由 Source Lookup 根据 Deep Card Index 处理。

`deep_card_queries` 不得请求 `composite_domain_carrier`。具体职业、岗位、正式身份、疾病或事件统一进入下列 `domain_carrier_requests`，避免从符号卡预选现实答案。

### Domain Carrier Requests

v3 顶层 `domain_carrier_requests` 必填，可为空列表。每项至少含：

- `request_id`
- `axis_id`：引用本 topic 已存在 axis
- `topic_axis`
- `carrier_family`：`career／identity_role／kinship／object_place／health_condition／event_scenario`
- `question_target`：自然语言所问的现实层；不得填写预选答案
- `process_ref`
- `controller_or_carrier_refs`
- `relation_function_refs`
- `position_visibility_refs`
- `capability_gate_refs`
- `required_contribution_types`：本题要求领域 Resolver 组合的证据类型
- `excluded_shortcuts`：至少拒绝单字直达、单十神直达和行业名倒推
- `claim_ceiling: candidate`：Topic 只提出候选检索，不决定支持度
- `request_status`：`requested`／`deferred`

v3.1 的 timing／synastry 载体请求另含：

- `relation_function_transition_ref`：只写本窗口如何改变关系功能，不直达人物
- `retained_natal_route_ref`
- `runtime_context_refs`
- `role_candidate_scope`：至少保留一个主候选及有意义的替代候选；若现实位置未知，不得只申请唯一人物标签
- `impact_assessment_refs`：指向结构影响边界，不预判事件严重度

该请求只声明“需要比较哪一类现实载体”，不得因甲为十干之首而请求“领导”，也不得因印／食伤名称而请求“教育”。具体候选由 Source Lookup 在相关来源范围内编译，最终排名由 Composition 的 Domain Carrier Resolver 完成。

### Finding Handoff

`finding_handoff`：

- `primary_axis_ids`
- `supporting_axis_ids`
- `expected_primary_findings`
- `cross_topic_refs`
- `unresolved_source_gaps`

`topic-lens-index.yaml` 另记录 `shared_controller_or_pivot_summary` 与 `shared_reason`，防止把结构性共用误判成偷懒，也防止无理由复制同一主轴。

v3 的 `expected_primary_findings` 使用整数，并必须同时等于：

1. `finding_disposition: required` 的 primary axes 数；
2. `coverage_profile.expected_primary_finding_count`；
3. required scope atoms 经去重后要求的最少 finding 数。

一个 finding 可以覆盖同一 atom 内紧密相连的 supporting axes，但不得跨多个年度 atom、四柱 atom 或重要藏干 atom，以“综合序列”规避粒度。

旧 `body_use_axis` 与 v2 process axes 只用于兼容读取。新 v3.1 产物不得把它们作为唯一轴事实源。
