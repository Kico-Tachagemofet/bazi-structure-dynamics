# Source Packet Schema

source-packet.md 是本轮分析的读书收据，不是书目清单。

## Header

- case_id
- framework_lock
- question_scope
- packet_date
- source_coverage：complete／partial／blocked
- packet_role：structure／imagery／supplemental-imagery
- structure_freeze_id：imagery packet 必填
- report_scope_ref：full-reading imagery packet 必填
- topic_slug
- topic_lens_ref
- taiji_center
- topic_body_refs
- use_kernel_ref
- conventional_symbol_candidate_ids
- actual_controller_or_carrier_ids
- therapeutic_pivot_ids：可为空
- topic_process_axis_ids
- coverage_facet_refs
- topic_material_coverage_registry_ref
- reader_answer_contract_refs：可为空；只收真实问题
- question_source_coverage_registry_ref：真实问题存在时填写
- natal_chart_card_inventory_ref：full-reading imagery packet 必填
- topic_unit_selection_signature 与 cross-topic delta
- baseline_required：true／false
- deep_card_index_ref
- deep_card_manifest：imagery／supplemental-imagery packet 必填；只保存 Source Lookup 的完整读取收据和单元选择清单
- deep_card_runtime_packet_ref：imagery／supplemental-imagery packet 必填；指向 `deep-card-runtime-packet-<topic>.json`
- earthly_branches_core_ref：涉及地支／藏干的 imagery packet 必填
- activation_overlay_ref、overlay_audit_ref、overlay_freeze_ref：timing／synastry imagery packet 必填
- natal_route_retention_refs、overlay_function_transition_refs、shared_node_competition_refs：v3.1 timing／synastry 必填
- runtime_context_policy_ref：只用于载体分支与能动范围，不作结构证据

## Source Queries

每个 query 单独编号：

| 字段 | 说明 |
|---|---|
| query_id | SQ-01 等 |
| topic_axis_refs | 本 query 服务的 process／十神链／干支锚点 |
| coverage_facet_refs | 本 query 最终帮助覆盖哪些面；不等于问题 |
| reader_answer_contract_ref | 若服务真实问题，记录 contract_id／closure_key；否则为空 |
| trigger | 来自哪个盘面事实或待裁决关系 |
| decision_needed | 需要判断什么 |
| explanatory_obligation_targets | formation／advantage／cost／result-gate／switch／verification 中实际服务哪几项 |
| domain_specific_need | 本专题必须补足的人／角色、事情／对象、现实载体或结果材料；不得只写“十神取象” |
| framework | 采用哪个来源口径 |
| search_terms | 仅用于定位 |
| full_section_required | 必须读取的完整章节 |

## Topic Material Coverage Registry

imagery／supplemental-imagery packet 必须逐 topic 登记：coverage facets、topic axes、十神链环节、透干／地支／藏干／柱位锚点、selected unit refs、carrier requests、强替代材料、source gaps、unit selection signature 与相对其他 topics 的 delta。通用 full-read receipt 可以共享，但 activated units 和组合任务不能无差别复制。

## Question Source Coverage Registry

只有真实 Reader Answer Contract 存在时才逐 contract 登记；一条记录至少含：

- `contract_id`、`closure_key`、`source_ref`、`exact_reader_question`
- `answer_target`：`subject_or_role／matter_or_domain_object／result_or_outcome`
- `source_query_refs` 与 `selected_unit_refs`
- `obligation_coverage`：formation／advantage／cost／result-gate／switch／verification 各自列 `status: covered／source-gap／not-applicable`、source／unit refs 与理由
- `domain_specific_evidence`：本领域相对共通结构新增了哪些角色、对象、载体、结果门或反转材料
- `shared_mechanism_refs`：可以跨题共享的结构或语义；它本身不计作领域答案
- `strongest_alternative_source_refs`
- `questions_still_not_answered`
- `coverage_status`：complete／partial／source-gap／not-applicable

`complete` 只表示本问题需要的来源层齐全，不表示 Source Lookup 已作生活结论。六类职责任何一项无材料时，必须是明确的 source-gap／not-applicable，不能以同一条通用 unit 重复填满六栏。不同专题可以引用同一 read receipt，但 `domain_specific_evidence` 不得因此相同或为空。

## Read Receipt

每个实际读取段落记录：

- source_id
- 文件路径
- 书名、作者、原典／评注／课程身份
- 章节或课程时间段
- 是否完整读取
- OCR 或断句疑点
- 可支持的规则
- 不可越界的推论

## Decision Rules

只摘录本轮真正会进入结构裁决的规则。每条必须带：

- rule_id
- source_id
- `rule_card_ref` 与 `curation_status`：若已进入条件规则注册表；`pending_human_review` 仅作候选提醒
- 原意转述
- `taiji_of_source`：该条原文的立论主体或关系视角
- `applicable_taiji`：本条可以回答哪些太极点；跨太极点使用须另列论证
- `question_answered`
- `questions_not_answered`
- `preserved_qualifiers`：不得删除“往往、若、则、反是、稍解”等语气和条件
- `effect_dimensions`：按需分列 `material_damage`／`functional_restraint`／`protective_effect`／`relation_form`，不允许用一维答案替代另一维
- 适用条件
- 改判／覆盖条件
- 反例或限制
- 与其他来源是否冲突
- `pipeline_hook_receipt`：记录本卡本轮被路由到哪些 hook、以 `route／propose／decide／guard／audit` 哪种角色进入、依赖是否满足、哪些 hook 因条件不符而禁用
- `activation_interface_source_receipt`：若规则用于待时接口，记录它只支持参与层守门、触发签名、重算范围还是 overlay 裁决；原文未回答的具体年份／人物／结果继续列在 `questions_not_answered`

规则卡在 Source Packet 中只取得“本轮可被引用”的资格。Source Lookup 不执行 Structure Core 的 `decide` hook；`approved` 也不等于已经适用于本盘。

避免大段复制原文；需要取象时保留完整展开的结构与层次，不压缩成一句口诀。

## Imagery Units

仅 imagery／supplemental-imagery packet 使用。每个单元至少含：

- `imagery_unit_id`
- `symbol_type`：stem／branch／ten-god／pillar-position／hidden-stem／relation／body／place／action／domain
- `symbol`
- `imagery_type`：`core-process`／`mechanism-bearing`／`candidate-carrier`／`unsupported-fixed-verdict`
- `unit_class`：`semantic_core`／`state_modifier`／`symbol_carrier`／`relational_carrier`／`composite_domain_carrier`／`cross_system_context`
- `unit_permission`：下游 imagery unit 只允许 `activated`；其余状态只留在 source-only manifest 的排除收据中，不转发语义内容
- `deep_card_query_ref`、`activation_basis_refs`、`claim_ceiling` 与 `forbidden_promotions`
- `deep_card_ref`、版本与审阅状态：若本单元使用 Deep Card
- `branch_manifestation_receipt`：涉及地支／藏干时必填；分别引用 `field_layer`、逐藏干 `qi_layer`、`function_layer` 与本题 `result_layer`，不得用透干一项代替
- `activation_overlay_receipt`：timing／synastry 涉及待时节点时必填；分开原局接口、触发匹配、重算 diff 与覆盖期
- `natal_route_retention_ref`：临时关系占用或改道原局节点时必填；保留 before／after 通量、共享节点分配与备用路线
- `overlay_function_transition_ref`：分开原局参与层、本窗口临时功能资格与 claim ceiling
- `source_id` 与完整读取范围
- `expanded_imagery`：保留原材料的分项层次，不缩成标签
- `derivation_path`：如何由五行、阴阳、季节或关系推出，不得只写名词对应
- `functional_meaning`
- `positive_or_supported_expression`
- `pressured_or_distorted_expression`
- `state_switches`
- `topic_axis`
- `conditions_and_limits`
- `examples_in_source`
- `candidate_carriers` 与 `alternative_carriers`
- `bridge_requirements`
- `source_selection_state`：`selected`；Source Lookup 不裁 `supported／preferred／assertable`
- `caveat_trigger`：只有真实竞争锚点、状态切换、来源冲突或证据缺口才填写
- `prohibited_generalization`：只记录无桥接定案，不得把合理候选本身列为禁词
- `mechanism_trace`：性质怎样参与已审计作用；无机制连接时不得从物象跳到事件
- `provenance_layer`
- `ocr_or_transcription_risk`

`candidate-carrier` 只以 `candidate` 上限进入 Composition；是否达到 `supported／preferred／assertable` 由 Composition 桥接并审计。`unsupported-fixed-verdict` 指“从一个符号直接宣布唯一人物／外形／行业／事件”，不是指某个物象或行业例子永远不能出现。旧字段 `fixed-label` 只作 legacy alias，新增 packet 不再使用。

只有 `unit_permission: activated` 的编译单元可以进入 Composition。`context-only／forbidden／source-gap` 只登记 unit ID、排除原因和缺口，不转发对应语义内容。需要避免断章取义时，由 Source Lookup 在内部完整读卡后把必要上下文压入获准单元的 `semantic_payload／state_switches／derivation_path`；不得把整卡交给下游解决上下文问题。

## Deep Card Manifest

每张被 query 命中的卡记录：

- `card_id`、path、版本、审阅状态与 `full_read_receipt`；
- `query_refs` 与 `axis_refs`；
- `activated_units`、`context_only_units`、`forbidden_units`、`source_gap_units`；
- 每个 unit 的 `unit_class`、topic、activation basis、claim ceiling 与 forbidden promotions；
- `raw_card_access: source-lookup-only`；
- `composition_access: compiled-units-only`；
- `render_access: none`；
- `raw_card_forwarded: false`；
- `context_only_payload_forwarded: false`；
- `claim_authority: activated-units-only`；
- `unused_candidate_receipt`：只记录未采用 unit ID 与理由，不复制候选正文。

完整读卡是 Source Lookup 的编译职责，不表示整卡激活，也不授权 Composition／Render 打开母卡。具体职业、岗位、正式身份或事件若只得到单张天干／地支／十神卡支持，权限上限仍为 candidate；只有领域载体推导完成多项结构桥接并在 finding 中升格后，Render 才可陈述。

## Deep Card Runtime Packet

Source Lookup 另产机器事实源 `deep-card-runtime-packet-<topic>.json`，新产物使用 `schema_version: "1.1"`。它是 Composition 唯一可读取的 Deep Card 内容边界，至少含：

- `schema_version: "1.0"`
- `case_id`、`topic_id`、`structure_freeze_id`、`topic_lens_ref`、`source_packet_ref`
- `raw_card_access: source-lookup-only`
- `composition_access: compiled-units-only`
- `render_access: none`
- `raw_card_forwarded: false`
- `context_only_payload_forwarded: false`
- `query_receipts`
- `selected_units`
- `candidate_palette`：按 mandatory judgment dimensions 编译的开放 L2–L4 候选象池
- `domain_carrier_leads`：可为空

每个 `query_receipt` 至少含：

- `query_id`、`card_id`、`full_read_receipt_ref`
- `requested_unit_classes`、`selection_purpose`、`selection_basis_refs`
- `topic_claim_ceiling`
- `selected_unit_ids`
- `context_only_unit_ids`、`forbidden_unit_ids`、`source_gap_unit_ids`、`excluded_unit_ids`
- `raw_card_text_forwarded: false`

各 ID 分栏不得重叠。`selected_unit_ids` 必须与本 packet 中实际 `selected_units` 一一对应；其他分栏只保留 ID 与 source-only manifest 收据，不携带语义正文。

每个 `selected_unit` 是“某个 authoring unit 在某次 query／axis 下的编译实例”，至少含：

- `runtime_unit_id`：本 packet 内唯一；建议格式 `<query_id>::<authoring_unit_id>`
- `authoring_unit_id`：回链母卡 `runtime_unit_map` 的稳定 ID；同一 authoring unit 可在不同 query 中生成不同 runtime instance
- `query_ref`、`card_id`、`unit_class`、`topic_axis`
- `semantic_payload`：Source Lookup 从完整卡编译出的本题所需完整语义，不是断章单句
- `derivation_path`、`state_switches`
- `activation_requirements`、`activation_basis_refs`、`allowed_topics`
- `claim_ceiling`：只允许 `mechanism／candidate`
- `forbidden_promotions`
- `source_layer`、`source_receipt_refs`
- `candidate_carriers`、`alternative_carriers`
- `mechanism_trace`

`semantic_core／state_modifier` 的上限为 `mechanism`。`symbol_carrier／relational_carrier` 的上限为 `candidate`。`composite_domain_carrier／cross_system_context` 不得作为 selected unit 转发：前者只能进入下列领域候选线索，后者只留 source-only 上下文收据。

`candidate_palette` 由 Topic Lens 的 `candidate_palette_requests` 触发。每项至少含：

- `palette_item_id`；
- `judgment_dimension_refs`；
- `specificity_level`：仅 L2／L3／L4；
- `nature_action_material_or_family`；
- `contributing_selected_unit_refs`；
- `activation_anchor_refs` 与 `post_relation_state_refs`；
- `ten_god_chain_contribution`；
- `compatible_carrier_families` 与 `competing_palette_item_ids`；
- `claim_ceiling: candidate`；
- `not_a_finding: true`。

开放扫描以“本盘已激活且与 judgment dimension 相容”为边界，不以 Lens 预先点名的职业家族为边界。同一天干或地支的精密、器械、切割、修复、审查等动作材料象即使不足以证明具体职业，只要通过 activation gate，也必须以 L3 候选进入 palette。Source 不排序、不定案，但必须让 Composition 看见有资格竞争的完整候选。

`domain_carrier_leads` 只有 Topic Lens 已建立对应 `domain_carrier_request` 时才可出现。每项至少含 `lead_id`、`domain_request_ref`、`label`、`carrier_family`、`contributing_selected_unit_refs`、`source_receipt_refs`、`source_support_scope`、`claim_ceiling: candidate` 与 `not_a_finding: true`。它只给 Domain Carrier Resolver 建候选池，不能携带 bridge rank 或最终结论。

timing／synastry 人物 lead 另含 `relation_function_transition_ref`、`retained_natal_route_ref`、`runtime_context_dependency`、`role_candidate_class` 和 `alternative_role_lead_ids`。当 runtime context 为 unknown／withheld 时，人物候选不得只剩一个；例如事业场中的比劫关系可先给同级协作、竞争、共享资源参与者等关系类别，不由 Source Lookup 单定为同事或小人。

Runtime packet 禁止出现母卡路径、母卡全文、context-only payload、`bridge_status`、`claim_strength` 或 `carrier_rank`。完成后运行 `scripts/validate_deep_card_runtime_packet.py`；FAIL 不得进入 Composition。

若存在 `candidate_palette_requests` 而 runtime packet 没有 `candidate_palette`，或 palette 只重述 Lens 的预选家族、未覆盖 activated symbol／action units，视为 SOURCE_GAP／BLOCKER，不得进入 Composition。

同柱干支组合、十神相对功能与全局改写由 Imagery Composition 完成，Source Packet 不替命局裁决。

`branch_manifestation_receipt` 至少记录：

- `branch_position_id`、`branch_manifestation_handoff_ref` 与地支共同底座版本；
- `static_hidden_stem_refs`：逐一引用 Reader 的藏干节点与 qi_rank；不得从单支卡或司令表补写、删减或改序；
- `month_command_ref`：仅月令支需要，引用 Reader 的司令值、节气偏移、口径与表源；非月令支写 not-applicable；
- `commander_static_separation`: true：确认司令气序未改写静态藏干集合／qi_rank，也未把整支藏气批量激活；
- `field_layer`：关系后仍存在的季节／空间／场景／容器状态；
- `qi_layer`：逐藏干的 visibility、participation scope、support gate 与非直接参与方式；
- `function_layer`：direct-action gate、实际 edge／route、容量、承接与竞争；
- `result_layer`：topic axis、carrier bridge、外部结果条件和当前上限；
- `activation_interface_refs`：原局已登记接口；普通 natal 只写 registered-unmatched／not-applicable，不把候选写成当前结果；
- `natal_visibility` 与 `overlay_visibility`：只在 timing／synastry 分栏比较，不得相互覆盖；
- `matched_trigger_refs`、`overlay_requalification_refs`、`overlay_scope`、`persistence_mode` 与 `expiry_rule`：仅 overlay topic 必填；
- `manifestation_modes`：可多选 field-background／stock-root-support／environmental-feed／internal-latent／direct-function／timing-pending／externalized-result；
- `prohibited_collapse`：至少注明“不透≠无效”“透出／会局≠自动得用”“直接做功≠外部结果已兑现”。

四层不要求线性串联。环境题可以由 field layer 直接进入载体；藏干也可只通过 root-support 扶持另一节点。Source Packet 只能登记已冻结状态与候选桥接，不得重新裁 direct-action gate。activation interface 是未来重算入口，不是第五层结果；overlay 命中后也只能引用 Core 已重裁的状态。

## Coverage Registry

- 本轮 Topic Lens 要求的 imagery units
- 本轮实际加载的 Deep Cards、版本、审阅状态与未加载理由
- 逐条 relation axis 已覆盖的两端、支持／损用／去处／日主关系 units
- 已完整加载的 units
- missing units
- deferred units：首次未展开、后续追问可增量加载
- 不相关或明确排除的 units 及理由

## Conflict Matrix

| 议题 | 来源 A | 来源 B | 本轮处理 |
|---|---|---|---|
| 合化条件 | 规则与适用域 | 规则与适用域 | 分流，不混用 |

## Gaps

每个缺口标：

- gap_id
- missing material
- affected claim
- confidence cap
- fallback allowed

没有证据包的判断不能在后续被写成“原书明确说”。
