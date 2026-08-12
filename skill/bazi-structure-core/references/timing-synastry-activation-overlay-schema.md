# 岁运／合盘激活覆盖层 Schema v3.1

本文件定义冻结原局之上的临时激活层。它回答“外来干支进入当前时间窗或关系场后，哪些原局待时接口需要重算”，不把藏干改写成原局明干，也不把“可能被激活”写成“已经兑现”。

新产物使用 `schema_version: "3.1"`，并同时遵循 [五行克应过程 Handoff Schema v4](five-element-process-handoff-schema.md)。旧 v2–v3.0 只读兼容，不得与 v3.1 混合冻结。

## 1. 前置输入

- `natal_structure_freeze_ref`：已通过审计的原局冻结版本；
- `timing_scope_seed_ref` 或 `synastry_scope_seed_ref`：必须通过 [Timing／Synastry Scope Seed Schema v1.0](../../bazi-topic-lens/references/timing-scope-seed-schema.md)，只含时间／关系 atom、自然语言问题中心、领域范围和待查 interface；不得使用尚未生成的 canonical timing Topic Lens 作前置输入；
- `post-branch-node-ledger.activation_interfaces`；
- 原局 branch state、qualified edge map、route 与 conditions refs；
- 原局 `structure-process-handoff.yaml`；
- 岁运的新增干支节点，或另一张已分别审计并冻结的 natal；
- 合盘时的真实关系／问题中心。对方盘出现同字，不自动构成激活。

缺任一原局冻结、激活接口或外来节点来源时，不得产出激活结论。

## 2. Overlay Header

每个覆盖层至少含：

- `overlay_id`
- `overlay_type`：timing／synastry／relationship-field
- `scope_start`、`scope_end` 与 `expiration_rule`
- `natal_structure_freeze_ref`
- `scope_seed_ref`
- `canonical_topic_lens_ref`：覆盖层冻结后由 Topic Lens 回填；覆盖层生成时可为 `pending`
- `external_node_source`
- `natal_backwrite_forbidden: true`

岁运时间窗与关系存续期只是覆盖层边界，不改变原局 node identity。

## 3. External Trigger Nodes

逐个外来节点记录：

- `temporary_node_id`
- `source_scope`：大运／流年／流月／对方 natal／关系场
- `stem_or_branch`
- `position_or_time_window`
- `availability_in_overlay`
- `relation_candidates`
- `topic_relevance`
- `do_not_infer`

合盘外来节点必须同时通过“跨盘关系形式成立”与“本题确实调用该关系场”两道门。字面相同、五行相同或对方拥有某干支，都不足以自动激活。

## 4. Matched Activation Interfaces

逐项匹配原局预登记接口：

- `interface_id`
- `natal_node_ref`
- `trigger_signature`
- `matched_external_node_refs`
- `match_evidence` 与 `counterevidence`
- `natal_visibility`：冻结原值，不得修改
- `overlay_visibility_candidate`：activated-visible／activated-latent／unchanged
- `status`：registered-unmatched／matched-pending-requalification／active-overlay／blocked-overlay／expired-overlay
- `recompute_from`
- `affected_branch_relation_refs`
- `affected_node_refs`
- `affected_edge_candidate_refs`
- `affected_route_condition_refs`

匹配只表示进入重算队列。不得把 `matched-pending-requalification` 直接翻译成 direct action、得用、结果或事件。

## 5. Before／After Diff

覆盖层只写差分：

- `branch_state_diff`
- `node_state_diff`：identity、availability、overlay visibility、participation scope、support gate、direct-action gate；
- `edge_requalification_diff`：受影响边必须重新执行候选、关系形式、竞争、分配、剩余容量、效果维度与 finalize；
- `route_condition_diff`
- `manifestation_handoff_diff`
- `unchanged_natal_refs`
- `process_state_diff_refs`

禁止只翻转一个 `active` 开关。若触发改变支局、共享节点占用、承接、availability、allocation、residual capacity 或 start gate，必须从最早受影响阶段重跑，并沿 `structure-process-handoff.yaml` 传播到同 process 的下游 edge、route condition 与 phase；未受影响部分须写明确继承收据，不能只引用原局后静默省略。

外来节点不只可以“新增一条边”，也可能通过生克合与原局主路争用同一节点。因此 `edge_requalification_diff` 必须另给 `shared_node_competition_diff`：哪个原局节点被外来关系占用、原路线 before／after 分配、剩余通量、备用路线与最强反条件。“有合”不得直接写成原路线消失，“原局有根”也不得直接写成完全不受影响。

### 5A. 逐年 Interaction Census（用户要求逐年时强制）

每一个被用户点名的流年必须是独立 `timing-annual` scope atom，并拥有自己的 census 与 diff；大运总述不能替代逐年文件。每年先完整列清楚“原局 + 当前大运 + 当前流年”的全部节点，再裁哪一条关系主导，禁止只挑与预想结论相符的两三个字。

每个年度 census 至少包含：

- `timing_year`、`year_ganzhi`、`luck_period_ref`、`scope_atom_ref`；
- `combined_node_inventory`：原局四柱、大运干支、流年干支逐位置列出，不把同字或同五行先合并；
- `stem_relation_scan` 与 `branch_relation_scan`：生克合、冲刑害破、六合、半合／三合／三会、重复支及每类 negative scan；
- `relation_concurrency_groups`：同时成立、共享节点、互相竞争或可并行的关系分别成组；
- `element_and_ten_god_delta`：相对原局新增、加强、受制、改道的五行及十神功能；
- `affected_natal_relations_retained`：外来节点加入后仍持续成立的原局关系，不能因新关系出现而静默删除；
- `branch_state_diff`、`node_state_diff`、`edge_requalification_diff`、`route_condition_diff`；
- `process_state_diff_ref`：指向本年完整 process before／after 与 propagation closure；
- `old_structure_refs`、`external_forcing`、`subject_agency`、`non_controlled_outcome`；
- `candidate_carriers_ranked`、`new_container_requirements`、`failure_if_unchanged`、`next_window_transition`。

“同一五行达到四个或以上节点”、两组以上冲刑并发、或同一节点同时参与两种以上关系时，必须另建 `high_contrast_structure`：逐个写出节点来源、十神身份、关系成员、哪条旧关系仍在、哪条是本年新增、共享节点如何分配。可以说“土最旺／官杀集中”，但必须紧接着回答：旺在哪里、通过什么关系改变旧结构、外部怎样逼近、命主能主动决定哪一段、以及哪些结果不由命主单独控制。

例如一个年度同时含原局辰戌冲、大运丑、流年未时，census 必须分别核对并保留：原局辰戌冲是否持续、丑未冲是否新增、丑未戌刑是否成形、各关系是否共享戌／丑／未及其竞争结果。不得把它偷换成“所有土互冲”，也不得只写成“换容器”。

年度交付必须按 `timing/year-YYYY-interaction-census.yaml`、`timing/year-YYYY-overlay-diff.yaml`、`timing/year-YYYY-process-state-diff.yaml` 分文件保存；汇总文件只能建索引和大运阶段综述，不能承载多个年份的唯一正文。

### 5B. Process Propagation Closure（v3 强制）

edge／route 重算后，按 `structure-process-handoff.yaml` 为每个受影响 process 写 before／after。至少覆盖 start gate、逐 phase 状态、throughput、allocation、daymaster cost、therapeutic effect、residual problem、bypass／rebound 与 can-start／carry／redirect／stop。

每个重算根另写 `propagation_closure`：访问过的 node、edge、route、condition 与 process，以及每个下游是 `requalified` 还是 `explicitly-inherited-with-no-impact`。上游容量变化却因下游节点没有单独命中 activation interface 而停止传播，直接 FAIL。

`reallocated-overlay`、`re-evaluated`、`residual capacity recalculated` 只能作为 trace；若没有明确 before／after 方向与结果，不得向 Topic／Composition 交付。

### 5C. 原局基线保留与影响边界（v3.1 强制）

每个受影响 process 另建 `natal_route_retention`，至少含：

- `retention_id`：供临时功能、Topic Lens 与 Composition 稳定引用；
- `natal_process_ref`、`affected_phase_refs` 与 `affected_centrality`；
- `before_throughput`、`after_throughput` 与 `retention_state`：`retained`／`reduced`／`redirected`／`blocked`／`enhanced`／`undetermined`；
- `shared_node_allocation_refs`；
- `unchanged_natal_phase_refs`；
- `backup_route_refs` 与备用路线当前可用度；
- `overlay_layer_stack`：原局、大运、流年、流月／关系场的来源、时长、透藏／根势与关系形式；
- `structural_impact_band`：`background`／`noticeable`／`material`／`dominant`／`undetermined`；
- `impact_reasoning`、`strongest_countercondition` 与 `expiry_rule`。

`structural_impact_band` 只裁“本窗口对原局过程改动到什么程度”，不等于现实事件已发生或严重度已知。原局是基线架构，不是永远比流年强的定理；流年是有期变量，也不是一出现便覆盖原局的定理。必须按层级、持续时间、得根得势、关系形式、节点分配和备用路线裁定。

### 5D. 临时显化资格交付（v3.1 强制）

对每个 matched natal node 产出 `overlay_function_transition`：

- `natal_node_ref`、`natal_visibility`、`natal_participation_scope` 与 `natal_direct_action_gate`；
- `external_trigger_refs` 与 `activation_interface_ref`；
- `overlay_visibility`、`overlay_participation_scope` 与 `overlay_direct_action_gate`；
- `qualified_overlay_functions`：分开 root-support、environmental-feed、direct-function 与 visible-interface；
- `blocked_functions` 与 `requalification_refs`；
- `natal_route_retention_ref`；
- `topic_handoff_ceiling`：`mechanism-only`／`relation-function-candidate`／`domain-carrier-candidate`；
- `persistence_mode` 与 `expiry_rule`。

该交付只能说“什么功能在本窗口取得了什么资格”。具体人物、岗位、组织、资源或事件必须交正式 timing Topic Lens 与 Composition 裁定。

例如：原局某癸只有 root-support／`timing-only`，岁运癸透只表示透干接口命中。若它又与原局戊发生合关系，先裁合的主形式和戊节点分配，再比较戊原本生印路线的 before／after 通量。生印主路若仍有剩余，只能说部分受占用或改道，不得说杀印尽破。至于癸的比劫关系在事业题中是否落成同事、同级合作者、竞争者或资源分配参与者，取决于 Topic、柱位／关系场、可见接口与命主当时位置；Core 在此不定人。

## 6. 显化与持续方式

覆盖层可以记录：

- `persistent-in-window`：当前时间窗内持续成立；
- `intermittent`：条件反复满足／退出；
- `pulse`：短促触发；
- `relationship-bound`：只在该关系场内成立。

持续方式由时间窗、关系质量、竞争与实际承接共同裁决，不能预设“渐渐透出”或“一来就爆发”。`overlay_visibility` 只描述当前覆盖层的接口显性，不等于 `natal_visibility` 改变。

## 7. 审计、冻结与失效

产出：

- `timing-activation-overlay.yaml` 或 `synastry-activation-overlay.yaml`
- `overlay-qualified-edge-diff.yaml`
- 每个年度的 `timing/year-YYYY-process-state-diff.yaml`
- 每个受影响 process 的 `natal_route_retention` 与每个 matched node 的 `overlay_function_transition`
- `overlay-audit.md`
- `overlay-freeze-receipt.yaml`

审计至少确认：接口真实存在、触发匹配有证据、受影响边已重算、process propagation closure 完整、before／after 含实质状态、共享节点分配与原局主路剩余已裁定、临时功能与人物载体未混层、原局未被反写、现实结果仍另过 Topic／Composition gate。覆盖层到期时仅把 overlay 状态改为 `expired-overlay`；原局的 hidden／latent 状态、process baseline 与已登记接口继续保留。

## 8. 一票否决

- 把原局藏干永久改成明干；
- 把“登记接口”写成“当前已激活”；
- 把“匹配触发”写成“已直接做功”；
- 不重算作用边便宣布路线开启；
- 上游容量或分配改变，却未传播到同 process 的下游 edge、condition 与 phase；
- process diff 只有 `reallocated／re-evaluated` 等泛化标签，没有 start gate、通量、成本、治疗、回病与能动性 before／after；
- 受影响的原局主路没有 `natal_route_retention`，或只用“原局有保护／流年更强”代替剩余通量与共享节点分配；
- 把本窗口临时功能资格直接写成“同事／上司／伴侣等人出现”；
- timing finding 使用未出现在本年 process diff 或 unchanged receipt 的路线；
- 因对方盘有同字便自动激活；
- 覆盖层结束后仍沿用临时 node／edge 状态。
