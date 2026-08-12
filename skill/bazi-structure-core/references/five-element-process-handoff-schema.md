# 五行克应过程 Handoff Schema v4

本接口是 Structure Core 向 Topic／Composition 交付结构事实的唯一过程级入口。它把已经裁定的旺衰、作用边、路线、通关、日主承载与条件先后组织为可冻结的过程单元；下游不得再从零散符号或任意 edge 子集重建另一套机制。

旧 v2–v3 产物允许只读追溯，不得与 v4 产物混合冻结。新产物使用 `schema_version: "4.0"`。v4 不改变既有 node／edge／route 事实；它增加现实结果所需的四面裁决，防止把治疗方向误写成社会成果方向。

## 1. 原局过程文件

Structure Core 在 `use-kernel.md` 完成后产出 `structure-process-handoff.yaml`。顶层至少含：

- `schema_version`
- `case_id`
- `structure_freeze_candidate_id`
- `problem_state_ref`
- `system_state_ref`
- `qualified_edge_map_ref`
- `route_candidates_ref`
- `conditions_matrix_ref`
- `use_kernel_ref`
- `process_units`

每个 `process_unit` 至少含：

- `process_id`：稳定 ID；
- `process_role`：pressure／support／therapeutic／aggravating／mixed／autonomous；
- `primary_problem_ref`；
- `strength_context`：司令、季节、相关五行库存、实际可用量、日主承载与调候限制的 refs 及结论；
- `ordered_edge_refs`：完整、有序引用 Edge Map；不得手抄端点；
- `route_refs` 与 `condition_refs`；
- `route_closure_receipt`：逐 route 展开其完整 `edge_refs`，并声明 `complete: true`；
- `elemental_actions`：按顺序写生／克／泄／耗／制／化／通关／改道，只解释已存在 edge；
- `ten_god_relations`：逐 edge 记录相对日主关系及本过程实际功能，不携带固定吉凶；
- `ordered_phases`；
- `daymaster_cost`；
- `therapeutic_effect`；
- `residual_problem`；
- `bypass_and_rebound`；
- `life_effect_matrix`：同一 process 的四面裁决；
- `competing_process_refs`；
- `switch_and_reversal_conditions`；
- `scope: natal`；
- `evidence_refs` 与 `counterevidence`。

### life_effect_matrix

每个 process 必须并列记录：

- `effect_on_daymaster_capacity`：对承载、供能、启动、改道和停止权的影响；
- `objective_output_capacity`：不论命主是否轻松，客观上能够持续生产、完成、控制、积累或兑现什么；
- `social_realization_channels`：只列允许 Topic 继续判断的领域通道，如 education／credential、career／technical-output、institution／authority、reputation、wealth／income、relationship；这里不写生活结论或具体职业；
- `sustainability_and_cost`：持续条件、日主代价、回病、资源占用与失效方式；
- `valence_separation_receipt`：明确 `effect_on_primary_problem`、外部成果方向和命主成本是否同向；若不同，逐项说明，禁止压成一个“吉／凶”。

Structure Core 只交付结构允许的结果通道，不替 Topic 或 Composition 判断学历、职业和事件。但它不得因为 process 加重主问题，就把其 `objective_output_capacity` 或 `social_realization_channels` 留空。

### ordered_phases

每个 phase 至少含：

- `phase_id` 与 `sequence_index`；
- `edge_refs`；
- `mode`：passive-reception／active-initiation／active-redirection／autonomous-flow／recovery／stalled；
- `controller_ref`：日主、外部节点或自治子系统；
- `source_capacity_requirement`；
- `start_gate`：open／conditional／blocked；
- `throughput_band`：high／medium／low／conditional／none；
- `allocation_target_refs` 与 `competing_allocation_refs`；
- `cost_to_daymaster`；
- `effect_on_primary_problem`；
- `failure_state`；
- `recovery_or_transition_trigger`；
- `agency_state`：can-start／can-carry／can-redirect／can-stop 分栏，不得只写一条泛化“主动性”。

同一路线中“先承压、后有余量才能输出”必须是两个 phase。节点库存仍在而日主供能失败时，phase 写 `stalled`，不得把库存节点删除，也不得把自治环境供给冒充日主主动调用。

## 2. 过程闭合

`route_closure_receipt` 必须满足：

1. process 引用的每条 route，其全部 edge 都在 `ordered_edge_refs` 中；
2. `ordered_edge_refs` 不得跳过决定启动、成本、通关或回病的上游边；
3. mixed／parallel 路线分别记录分叉点、共享节点、分配上限与不能双重满额计算的部分；
4. `daymaster_cost`、`therapeutic_effect`、`residual_problem` 与 `bypass_and_rebound` 各自引用实际 phase／edge，不能互相替代；
5. `system can run`、`daymaster benefits`、`daymaster can initiate`、`daymaster can stop` 四项分开。

任一主路线不闭合时不得冻结 `structure-process-handoff.yaml`。

## 3. 岁运过程差分

每个年度 overlay 在 edge／route diff 之后另产出 `timing/year-YYYY-process-state-diff.yaml`。Composition 只消费该过程差分与冻结原局过程，不直接用自然语言 `primary_process` 代替重算结果。

顶层至少含：

- `schema_version: "4.0"`
- `timing_year`
- `year_ganzhi`
- `luck_period_ref`
- `natal_structure_freeze_ref`
- `natal_process_handoff_ref`
- `interaction_census_ref`
- `overlay_diff_ref`
- `recompute_roots`
- `propagation_closure`
- `process_state_diffs`
- `unchanged_process_receipts`
- `scope_start`、`scope_end`、`expiry_rule`
- `natal_backwrite_forbidden: true`

### propagation_closure

逐个重算根记录：

- `recompute_root_ref`；
- `reason_changed`；
- `visited_node_refs`；
- `visited_edge_refs`；
- `visited_route_refs`；
- `visited_condition_refs`；
- `visited_process_refs`；
- `downstream_disposition`：requalified／explicitly-inherited-with-no-impact；
- `closure_complete`。

只要上游 availability、allocation、residual capacity 或 start gate 改变，沿同一 process 的下游 edge、route condition 和 phase 必须重算；若继承原值，须逐项给出无影响依据。不得以“本年没有命中该下游节点接口”为由停止依赖传播。

### process_state_diffs

每个受影响 process 至少含：

- `process_id`；
- `before_state_ref`；
- `changed_external_node_refs`；
- `changed_edge_refs`；
- `requalified_or_inherited_edge_receipts`：覆盖该 process 的完整 edge closure；
- `before` 与 `after`，两者均分栏记录：
  - `start_gate`
  - `phase_states`
  - `throughput_band`
  - `allocation_state`
  - `daymaster_cost`
  - `therapeutic_effect`
  - `residual_problem`
  - `bypass_and_rebound`
  - `agency_state`
  - `life_effect_matrix`
- `delta_direction`：strengthened／weakened／blocked／reopened／redirected／unchanged；
- `rhythm`：continuous／intermittent／pulse／stalled；
- `external_forcing`；
- `non_controlled_outcome`；
- `expiry_rule`。

`after_state: reallocated-overlay`、`route re-evaluated` 或“余量已重算”只能作 trace，不是过程结论。没有上述 before／after 实值时，过程差分为 FAIL。

## 4. Composition Handoff

原局 Composition 必须引用 `structure-process-handoff.yaml#process_id`；岁运 Composition 必须同时引用对应 `process_state_diff`。下游可以选择某个 phase 作为问题焦点，但不得：

- 手工缩短 process edge closure；
- 把 route 存在写成 start gate 已开启；
- 把库存或自治流动写成日主主动发动；
- 把治疗效果写成没有成本；
- 把十神标签或物象卡反向改写 process state；
- 把 `aggravating` 直接等同于外部成果差，或把 `therapeutic` 直接等同于学历、职位、收入已经兑现；
- 把某年的 after state 回写 natal。

## 5. 一票否决

- process 引用 route 却遗漏其起始、成本、通关或回病 edge；
- 上游容量改变而下游只因“未直接命中接口”未重算；
- before／after 只有泛化标签，没有启动、通量、成本、治疗与能动状态；
- 同一共享节点在两个 process 中被重复满额调用；
- timing finding 引用不存在于本年 process diff 或明确 unchanged receipt 的路线；
- v2／v3 与 v4 事实源混合冻结。
- 缺少 `life_effect_matrix`，或四面裁决被一条综合吉凶标签替代。
