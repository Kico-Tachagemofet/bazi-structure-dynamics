# 八字取象 Finding Schema

## 目录

1. Imagery Coverage
2. Five-Element Process Composition
3. Pillar Coloring and Use-Axis Projection
4. Ten-God–Stem/Branch Scene Kernel
5. Resonance Map and Render Envelope
6. Topic Finding
6. Full-chart Sweep
7. Experience and Validation Maps

## 1. Imagery Coverage

`imagery-coverage.yaml` 至少包含：

- `case_id`
- `topic_id`
- `taiji_field_ref` 与 coverage facet IDs
- `explicit_reader_question_refs`：可为空；只收真实问题
- `structure_freeze_id`
- `report_scope_ref`
- `topic_lens_ref`
- `taiji_center`
- `use_kernel_ref`
- `conventional_symbol_candidate_ids`
- `actual_controller_or_carrier_ids`
- `therapeutic_pivot_ids`：可为空
- `topic_process_axis_ids`
- `baseline_required`：true／false
- `required_anchors`：柱、节点、边、路线
- `required_imagery_units`：干、支、十神、柱位、藏干、关系、领域
- `loaded_units`
- 每个 loaded unit 的 `imagery_type`：`core-process`／`mechanism-bearing`／`candidate-carrier`／`unsupported-fixed-verdict`
- `deep_card_runtime_packet_ref` 与 validator PASS receipt
- `selected_unit_ids`：仅列 runtime packet 中实际获准的 units
- `excluded_unit_receipts`：context-only／forbidden／source-gap IDs 与理由，不含对应语义正文
- 每个 selected unit 的 `unit_class`、claim ceiling 与 forbidden promotions
- `mechanism_trace`：机制型性质怎样连接到已审计 node／edge／route
- `carrier_bridge`：`core_process → chart_anchor → post_relation_state → topic_axis → candidate_carrier`
- `bridge_status`：unbridged／supported／preferred／assertable
- `claim_strength`：candidate／supported／preferred／assertable
- `caveat_trigger`：真实竞争锚点、状态切换、来源冲突或 source gap；无则为空
- `missing_units`
- `deferred_units`：本轮不相关但可供追问加载
- `tempting_but_excluded`
- `coverage_verdict`

本账本记录本轮覆盖，不宣称穷尽一个字的全部象意。

## 2. Five-Element Process Composition

v4 新 finding 必须先按 [五行克应 Composition Schema v4](process-composition-schema.md) 建 `process-compositions.yaml`。每条至少引用：

- `process_ref` 与冻结收据；
- 旺衰／司令／日主承载快照；
- 完整 `route_closure_receipt` 与 ordered edge refs；
- ordered phases、start gate、throughput 与 competing allocation；
- `daymaster_cost`、`therapeutic_effect`、`residual_problem`、`bypass_and_rebound`；
- can-start／carry／redirect／stop；
- timing 时的 `process_state_diff_ref` 与 before／after。

以上为机制事实源。十神、柱位、藏干、物象与 resonance 只能解释或着色这些字段。

## 2B. Pillar Composite／Coloring

`pillar-composites.yaml` 每个相关柱至少含：

- `pillar_id` 与 `position_role`
- `stem_node_id`
- `stem_raw_imagery` 与 source unit IDs
- `stem_ten_god_function`
- `branch_position_id`
- `branch_raw_imagery` 与 source unit IDs
- `hidden_stems`：逐节点列 node ID、十神、气序、关系后状态、参与层、可用条件、不可越界项
- `branch_manifestation_receipt`：引用 Structure Core handoff 与地支共同底座，分别记录 `field_layer`、逐藏干 `qi_layer`、`function_layer`、本题 `result_layer`
- timing／synastry 时另列 `activation_interface_ref`、`matched_trigger_refs`、`natal_visibility`、`overlay_visibility`、`overlay_requalification_refs`、`persistence_mode`、`overlay_scope` 与 `expiry_rule`
- `manifestation_modes`：可多选 field-background／stock-root-support／environmental-feed／internal-latent／direct-function／timing-pending／externalized-result
- `nonexternal_expression`：外部结果门未通过时，该支仍怎样作为场、根、供给、内部功能或待时接口存在
- `stem_colors_branch`：天干怎样改变该支场景的呈现
- `branch_colors_stem`：地支怎样给天干提供根基、环境、阻力、去处或存储
- `coloring_asymmetry`：哪一面占主导及理由
- `season_and_commander_modifier`
- `branch_relation_modifier`
- `problem_state_role`
- `route_roles`
- `baseline_expression`
- `pressure_expression`
- `healthy_expression`
- `counterexpression_or_nonmanifestation`
- `technical_refs`
- `source_refs`
- `confidence`

v3 中本文件是 process 的柱位／藏干着色投影。每柱另加 `process_refs` 与 `phase_role_refs`；不得以 `route_roles` 的自由列表代替完整 process closure，也不得独立支持 timing verdict。

### 同柱互染边界

- 互染描述组合画面，不自动生成生、克、合、制或通关边。
- 天干坐支不等于能调用支中全部藏干。
- 地支藏财库不等于资源已到账；必须读取 visibility、participation scope、route 和 trigger。
- 同柱双方都要解释，但力度可以明显不对称。

## 3. Use-Axis Scene

`axis-scenes.yaml` 每条 scene 至少含：

- `axis_scene_id`
- `topic_id`、coverage facet refs 与可选 explicit question refs
- `topic_process_axis_id`
- `topic_body_refs`
- `conventional_symbol_refs`
- `controller_or_carrier_refs`
- `therapeutic_pivot_ref`：可为空
- `focal_question`
- `endpoint_anatomy`：逐端列干支本象、十神、柱位、相关藏干与关系后状态
- `audited_mechanism`：只引用 node／edge／route／condition
- `process_composition_ref`、`process_ref` 与 `route_closure_receipt_ref`
- `complete_edge_closure`：必须等于 process closure，不得人工挑选
- `phase_focus_refs`
- `strength_and_bearing_snapshot_ref`
- `daymaster_cost`、`therapeutic_effect`、`residual_problem`、`bypass_and_rebound`
- `agency_transition`
- `source_to_use_scene`
- `damage_diversion_or_occupation_scene`
- `destination_and_feedback_scene`
- `daymaster_agency_scene`
- `competing_allocation`
- `baseline_scene`
- `activated_or_supported_scene`
- `diverted_or_pressured_scene`
- `failure_or_reversal_scene`
- `candidate_domain_carrier_properties`
- `deep_card_unit_refs`：只列 selected units；另以 `excluded_unit_receipts` 保存未获准 ID，不得读取其正文
- `branch_manifestation_refs`：本轴涉及地支／藏干时必填；不得在 scene 内重裁 visibility、participation scope 或 direct-action gate
- `activation_overlay_refs`：timing／synastry 本轴必填；须从原局 interface 经 trigger match 回链到重算后的 branch／edge diff
- `external_result_requirements`
- `main_scene`
- `secondary_scene`
- `switch_scene`
- `do_not_infer`
- `technical_refs`／`source_refs`／`confidence`

一条 scene 只处理一条主关系轴；不得在此重新计算作用边，也不得用用户经历补画面。`audited_mechanism` 是 process closure 的投影，不再允许自由列 edge／route 子集。

## 4. Required Ten-God–Stem/Branch Scene Kernel

每轮必须按 [十神—干支象核 Schema v2.0](ten-god-stem-branch-kernel-schema.md) 产出 `bazi-scene-kernels.yaml`。每个 kernel 至少含：

- `scene_kernel_id`、topic／coverage refs 与一个或多个 axis refs；
- 完整 `process_refs` 与 material-spread receipt；
- `ten_god_chain`：领域体、起点、功能传递、终点、反馈、竞争、命主能动性与反转；
- `stem_branch_composition`：透干动作、地支场、藏干层级、柱位人事、同柱与跨柱限定；
- 每项材料的 interaction type；
- 主场景、次场景、切换场景、未显化层、独特细节、最强替代与 do-not-render；
- `mandatory_judgment_dimension_refs` 与按现实端点拆开的 `claim_kernels`；
- 每个 claim kernel 的 specificity level、方向判断、证据强度、结果门、日主代价与反转条件；
- 形成、成事面、代价、结果门、反转与核验义务。

kernel 可以聚合多个 axes，也可因不同结果端点、specificity level、载体家族或相反结果分支拆开；数量不得由 coverage facet、问题或十神数量机械决定。共享 process 不能作为合并学历、技术、权责、名声、收入、变动和代价的理由。

## 5. Optional Resonance Map and Required Render Envelope

仅当 finding 实际使用物象措辞、符号贡献或现实载体竞争时才生成 `resonance-map.yaml`；此时每条相关主轴至少含：

- `resonance_map_id`、`axis_scene_id`、finding target；
- `symbol_contributions`：逐项列天干、地支、十神、柱位、藏干、状态与 source unit；
- `interaction_type`：reinforces／colors／carries／limits／diverts／context-only；
- `composition_trace`：这些贡献怎样形成主、次、切换场景；
- `carrier_competition`：每个现实载体通过和未通过的结构／现实 gates；
- `unused_context_receipts`：未激活 unit IDs 与排除理由，不复制候选正文。

每条 finding 的 `render_use_envelope` 至少含：

- `locked_claims` 与各自 claim strength；
- `deep_card_runtime_packet_ref`、`selected_unit_ids` 与可选 `domain_carrier_resolution_refs`；
- `excluded_unit_receipts`；
- `allowed_linguistic_expansions`：Composition 已物化的自足语义；
- `forbidden_new_claims`；
- `render_gap_route`。

Render 不读取母卡、runtime packet 或 context-only 内容，只能使用 envelope 中已经物化的解释。所有具体人物、职业、物件、事件和结论强度必须留在 locked claims 范围内。

## 6. Topic Finding

每条 finding 使用独立小节，标题包含稳定 ID，例如 `## F-CAREER-001`。至少填写：

### Identity

- `finding_id`
- `topic_id`
- `coverage_facet_refs`
- `scene_kernel_ref`
- `claim_kernel_refs`
- `mandatory_judgment_dimension_refs`
- `specificity_verdicts`：L1–L5 分栏；L1–L3 有支持时必须有方向，L4 排序候选，L5 可 not-claimed
- `topic_process_axis_ids`：可多条
- `reader_answer_contract_refs`：可为空；只收真实问题
- `closure_keys`：可为空
- `exact_reader_questions`：逐真实 contract 原样保留，不得改成 facet／topic 标签
- `answer_targets`：逐真实 contract 保留 subject_or_role／matter_or_domain_object／result_or_outcome
- `confidence`
- `scope`：natal／timing／synastry／relationship-field
- `taiji_center`
- `topic_body`
- `use_kernel_ref`
- `conventional_symbol_refs`
- `controller_or_carrier_refs`
- `therapeutic_pivot_ref`：可为空
- `axis_scene_ids`
- `resonance_map_id`：可空；为空时必须写 `resonance_map_status: not-used`
- `report_section_slug`
- `baseline_required`

### Question Answer Claims

若 finding 服务真实 Reader Answer Contract，必须逐 contract 建一条记录；没有真实问题时本节可以为空，不能从 coverage facets 反造问题：

- `contract_id`、`closure_key`、`source_ref`、`exact_reader_question`
- `answer_status`：complete／conditional／not-applicable／source-gap
- `answer_target`
- `direct_answer_claim_id`：稳定且唯一；complete／conditional 必填
- `direct_answer`：先说明本题的人／角色、事情／对象、主要落法与结果倾向，不得只写性格、感受、建议或技术名称
- `answer_strength` 与现实结果边界
- `formation_refs`、`advantage_refs`、`cost_refs`、`result_gate_refs`、`switch_refs`、`verification_refs`
- `domain_specific_delta`：相对共享 process／其他 topic，本题新增的角色、对象、载体、条件或结果
- `shared_mechanism_refs` 与可选 `shared_answer_ref`
- `strongest_alternative`
- `personality_role`：explanatory-only／not-used
- `advice_role`：after-answer／not-used
- `advice_substitutes_answer: false`
- `render_obligation_id`

一个 direct answer 可以是有条件的，但不能是空的。若答案只能说到机制、尚无领域载体或结果材料，应标 source-gap／conditional 并具体指出缺口；不得用“谨慎起见”的建议填满。一个 finding 服务多个 contract 时，上述记录必须逐 contract 独立存在。

### Anchor Set

- pillar IDs
- node IDs
- edge IDs
- route IDs
- problem-state claim IDs
- source unit IDs
- pillar composite IDs
- process ID 与 process composition ID
- phase focus IDs
- route closure receipt ref
- timing process diff ref：岁运／合盘必填

edge IDs 必须由 process closure 自动展开并完全相等；Anchor Set 不再拥有删减路线 edge 的权限。

### Composition Trace

按顺序说明：

1. 旺衰、司令、实际可用量与日主承载；
2. 完整五行生克泄耗／通关过程；
3. route 条件、phase 先后、成本、治疗、剩余问题与回病；
4. 十神怎样解释该作用相对日主与领域体的关系；
5. 柱位、藏干与同柱着色怎样限定落法；
6. 干支物象与候选载体怎样帮助显化；
7. 以上内容怎样收束成可验证判断。

每个进入组合的性质取象须标 `core-process／mechanism-bearing` 并给出 `mechanism_trace`。人物外形、物件、场所、行业或事件例子标为 `candidate-carrier`；只要桥接达到 `supported` 就可进入 finding。只有无桥接却被写成唯一事实的内容才标 `unsupported-fixed-verdict` 并放入 `tempting_but_excluded` 或 `do_not_render`。不得因防止刻板套象而反向删除有效的形态或载体候选。

### Use Relation

- `what_the_use_does`
- `what_supports_the_use`
- `what_damages_diverts_or_occupies_it`
- `where_the_use_goes_after_action`
- `whether_the_daymaster_can_start_carry_redirect_or_stop_it`
- `how_this_relation_changes_in_the_current_topic_body`
- `daymaster_cost`
- `therapeutic_effect`
- `residual_problem`
- `bypass_and_rebound`
- `phase_transition`

### Full-chart Sweep

- `reinforcing_facts`
- `weakening_facts`
- `reversing_facts`
- `competing_routes`
- `checked_but_irrelevant`
- `net_effect`

### Expression Bands

- `baseline`
- `under_pressure`
- `when_supported_or_well_routed`
- `counterexpression`
- `nonmanifestation_condition`

### Manifestation Layers

- `internal_mechanism`
- `domain_carrier`
- `external_result_requirement`
- `timing_or_field_condition`
- `counter_cost`

涉及地支／藏干时另加：

- `branch_manifestation_refs`
- `field_layer_expression`
- `qi_layer_expression`
- `function_layer_expression`
- `result_layer_state`：unbridged／supported／preferred／assertable；不得由 visibility 或 direct-function 自动填入
- `manifestation_modes`：从 field-background／stock-root-support／environmental-feed／internal-latent／direct-function／timing-pending／externalized-result 中按证据多选
- `nonexternal_expression`：若无 externalized-result，说明仍以何种形式成立；不得只写“没有显化”

timing／synastry 涉及待时节点时另加：

- `activation_interface_ref`
- `activation_state`：registered-unmatched／matched-pending-requalification／active-overlay／blocked-overlay／expired-overlay
- `natal_visibility`
- `overlay_visibility`
- `requalification_refs`
- `persistence_mode` 与 `expiry_rule`
- `natal_backwrite_forbidden: true`
- `natal_process_ref`
- `timing_process_diff_ref`
- `propagation_closure_ref`
- `process_before_after`
- `shared_node_competition_ref`
- `natal_route_retention_ref`
- `overlay_function_transition_ref`
- `structural_impact_bounds`
- `runtime_context_branches`：当时职位／角色未知时保留条件分支；只调载体和 agency

`projected_effect_candidates` 只能进入 switch／timing condition，不能冒充本轮 current verdict。只有 active-overlay 且相关功能边已重算通过，才可继续桥接领域载体；现实结果仍另过 result layer。

四层分栏不等于必须线性通过。环境／居所题可由 field layer 直接桥接领域载体；root-support 也可经另一可见节点间接影响结果。`externalized-result` 只表示本题的载体与结果门已通过，不反向证明藏干必透、会局必成或原结构规则正确。

### Verifiable Judgments

列出足以核对主场景、次场景与反转场景的具体生活判断，不设固定数量。不要把术语改写成同义术语；每条应包含动作、对象、条件、结果或竞争载体，避免只有“忙、压力、变化、敏感”等高基率词。静态判断即使可回答“是／否／有条件”，也不自动具备证据验证资格。

宽专题必须先逐项处置 Topic Lens 的 mandatory judgment dimensions。`directional-verdict` 必须明确主要方向及相对强弱；`not-applicable／source-gap` 必须给出具体证据，不能用“谨慎”“无法确定具体职业”代替。学业 finding 若只写学习能力／方法而不判断学历、认证和专业训练，事业 finding 若只写流程／责任而不判断职业性质、动作材料、权责、名声、收入和变动，均为未闭合。

每条独立判断必须分配稳定 ID：`J-<FINDING-ID>-NN`。判断 ID 是 Composition、Render 与机械审计的覆盖键；最终文字可以将紧密相关判断写进同一连续段落，但不能删除实质主张或用一条泛化摘要替代。若两条判断实质重复，应在 Finding 阶段合并并重新审计。

桥接已经达到 `supported／preferred` 且没有相反锚点时，可以直接写清偏向，不要用例行“但是／也不一定”把可核验判断冲淡。真实存在的改判条件统一进入 `switch_scene`、`counterexpression` 或 `strongest_alternative`。

### Interpretive Kernel Handoff

- `scene_kernel_ref`：指向 `bazi-scene-kernels.yaml`；
- `material_spread_receipt_ref`；
- `ten_god_chain_ref`；
- `stem_branch_composition_ref`；
- `main／secondary／switch／do_not_render` claim refs。

finding 不得临时重写一份较薄象核。kernel 必须由 process composition、完整十神链和干支柱位组合共同生成，不能由 resonance map、逐柱符号列表或问题答案字段单独生成。

同一专题最后可以把多个 claim kernels 合成连续 finding 或 composition 段落，但每个独立判断必须保留自己的 judgment ID 与完整语义 span；不得只保留综合句。

岁运／合盘 finding 另必须含：

- `old_structure_refs`：本轮覆盖前实际在运行的制度、角色分配、路线或容器结构；
- `old_process_state_ref`：冻结 natal process；
- `process_state_diff_ref`：本时间窗 before／after；
- `agency_transition`：逐 phase 的主动／被动／自治／停滞变化；
- `external_forcing`：外来干支／关系场客观增加、打断或重排什么；
- `subject_agency`：命主能启动、承载、协商、改道、停止哪一段；
- `non_controlled_outcome`：仍由环境、他人、制度或现实门决定的部分；
- `candidate_carriers_ranked`：最多两个 primary carriers，另列 secondary／excluded；
- `new_container_requirements`：旧结构若失效，新承载结构必须具备什么；
- `failure_if_unchanged`：继续沿用旧结构时会在哪个环节失效；
- `next_window_transition`：下一时间窗会保留、撤销或反转什么。
- `natal_route_retention`：原局主路仍成立的 phase、剩余通量、共享节点占用与备用路线；
- `overlay_function_transition`：原局节点在本窗口从什么参与层变成什么临时功能；
- `relation_function_before_person_carrier`：先写关系功能，再给人物／组织载体；不得十神直达人物；
- `runtime_role_branches`：命主当时位置已知时引用问题 context，未知时保留至少一个主候选与有意义的替代候选；
- `structural_impact_band`：`background`／`noticeable`／`material`／`dominant`／`undetermined`，只表示对原局 process 的改动，不冒充事件已发生。

“建议主动调整”不等于“事情由命主主动造成”。Render 必须同时保留 external forcing 与 subject agency。

### Boundaries

- `strongest_alternative`
- `do_not_render`
- `source_gap`
- `not_proven`

### Render Obligations

列出最终文字不可删除的：旺衰承载、完整五行克应过程、领域体、用神做功、支持／损用、去处、phase 顺序、日主成本、治疗效果、剩余问题、回病、启动／停机、核心画面、切换条件、反证、技术追踪映射与需要交叉引用的其他 finding。技术追踪必须进入 marker／receipt；是否在读者版逐条显示，由 Render 依理解价值决定。

每条 finding 必须回链 `coverage_facet_refs` 与 `explanatory_obligations`，证明 formation／advantage／cost／result-gate／switch／verification 的必需材料已齐全或有明确不适用收据。这些是信息角色，不得直接变成六个可见标题。

真实问题的每个 `closure_key` 另须回链对应 `direct_answer_claim_id` 与唯一 `render_obligation_id`。Render obligation 要求该问题在相关叙事段落中得到清楚回答，但不得强制所有 coverage facets 都变成问答模板。不存在真实问题时只保留 coverage obligation。

另附完整、自足的 `render_use_envelope`。若 Render 想采用 envelope 外的新象，必须登记 `render-gap` 并退回增量 Topic／Source／Imagery；不得打开母卡补齐。

若 finding 有三条以上独立信号、同一节点两条相反路线、四个以上同类节点、原局／覆盖层显著反转或跨两个以上 topic，另加 `high_contrast_explanation_required: true`、`signal_count` 与逐信号 refs，并说明读者必须能够区分哪些来源、方向、竞争或前后状态。可以给出 `recommended_presentation`，但仅当信号清单、状态矩阵、before／after diff 或能动性三栏确实比因果散文更清楚时才选用；不得把信号数量直接换算成固定版式。

每条 blind finding 另加：

- `blind_generation: true`
- `subject_context_read_before_audit: false`
- `manifestation_mapping_eligible_after_audit: true`
- `validation_candidate`：true／false
- `validation_discriminators`：若为 true，列时间差／顺序／竞争载体／失败条件中已具备的部分
- `known_prior_exposure`：none／partial／contaminated

## 7. Full-chart Sweep

Full-chart sweep 不是重断全盘，而是防止局部象遮住全局。至少检查：

- 同一十神在其他位置是否有不同状态；
- 同一节点是否被竞争路线占用；
- 主问题会放大、压制或倒逼该象；
- 救应路线是否改变表达质量；
- 显而易见的相反证据；
- 内部能力、现实载体与外部成果是否被错误等同。

## 8. Experience and Validation Maps

`manifestation-map.md` 逐 finding 记录：

- `finding_id`
- `context_item_id`
- `mapping_state`：matched／conditional／carrier-shift／disconfirmed／new-question／structural-challenge
- `affected_expression_band`
- `allowed_change`：priority／wording／domain carrier／next question
- `forbidden_change`：node／edge／route／pattern／universal rule
- `non-evidentiary: true`
- `next_action`

经历不能填补 source gap，也不能把低通量路线改成高通量或提高结构 confidence。历史兼容文件 `calibration-map.md` 只有在显式写入 `non-evidentiary: true` 时才可继续使用。

流运验证不写入 manifestation map，按 [Validation Protocol](../../bazi-structure-dynamics/references/validation-protocol.md) 单独产出并冻结。至少记录：

- `validation_plan_ref`
- `timing_overlay_freeze_ref`
- `hypothesis_freeze_ref`
- `verbatim_response_ref`
- `scorecard_ref`
- `score_audit_ref`
- `validation_state`：scored／unscored／declined／contaminated
