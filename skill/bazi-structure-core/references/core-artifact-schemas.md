# Structure Core 中间产物 Schema

## 目录

1. Node Ledger
2. Interaction Census
3. Branch Relation Census
4. Branch State
5. Post-Branch Node Ledger
6. Qualified Edge Map
7. System State
8. Problem State
9. Pattern Candidates
10. Structured Route Candidates
11. Conditions Matrix
12. Structure Kernel

## 1. Node Ledger

node-ledger.yaml 中每个位置节点至少含：

- node_id
- pillar_position
- layer：stem／hidden-main／hidden-middle／hidden-residual
- stem
- element
- ten_god
- seasonal_status
- command_status
- roots：本根、同类根、余气根分别列
- exposed_or_hidden
- sources
- drains
- controls_received
- distance_notes
- void_effect
- climate_effect
- candidate_relations
- availability_state
- supporting_evidence
- counterevidence
- confidence

聚合层必须在全部位置节点完成后另建，不得覆盖原节点。

## 2. Interaction Census

interaction-census.yaml 每条候选关系含：

- interaction_id
- type
- participants
- positions
- adjacency
- distance
- same_pillar
- deterministic_basis
- shared_nodes
- source_query_id
- unresolved_conditions

Coverage 区必须报告：

- visible stems checked
- all hidden stems checked
- all six pairs of pillars checked
- repeated branches checked
- combinations／clashes／punishments／self-punishments／harms／breaks checked
- three-harmony and directional meetings checked
- shared-node competition checked

这一阶段不得写吉凶、用神或事件。

## 3. Branch Relation Census

branch-relation-census.yaml 必须是地支专表，不得与普通五行候选边混写。至少含：

- pair checks：六组地支位置对全部存在；
- relation hits：六合、六冲、刑、自刑、害、破与重复支；
- group checks：三会、三合、半合／拱合的 required／present／missing members；
- shared-node map：每个地支同时参与的候选关系；
- negative scans：每个未命中类别也标 completed；
- unresolved conditions：月令、旺支、距离、旬空、透干、冲刑破损和流派分歧；
- coverage verdict。

这里只确认形式候选，不裁吉凶、不决定化局、不改写节点。

## 4. Branch State

branch-state.md 每一组关系使用独立卡片：

- relation ID and candidate type
- member branches and positions
- complete／partial／candidate
- month and command support
- cardinal or旺支 status
- adjacency and distance
- void branches
- clash／punishment／break damage
- shared-node competition
- framework-specific priority
- formal branch-state verdict
- residual element functions
- hidden-stem consequences：逐藏干
- natal state versus timing trigger
- unresolved alternative
- effect manifest：逐成员支与逐藏干列 pre-state → post-state change
- relationship mechanism：合绊／聚拢／改道／冲动／受损／转化／无实质变化
- clash throughput 与 storage-opening doctrine 分列，不得写成因果替代

“正式归某局”与“仍会向其他五行输送”必须分别写。

## 5. Post-Branch Node Ledger

post-branch-node-ledger.yaml 必须覆盖 node-ledger.yaml 的全部 node_id。每个节点至少含：

- node_id
- pre_branch_state_ref
- branch_relation_refs
- branch_effect_refs
- identity_after：原五行保留／条件性改道／已转化；不得无证据改写
- availability_after
- visibility_after：visible／hidden／latent；冲不把 hidden 自动改成 visible
- root_type_after：本根／同类根／墓库根／余气根／同类背景／无；注明流派
- participation_scope：stock／root-support／direct-action／pattern-eligible／timing-only，可多选
- support_gate：allowed／conditional／forbidden；单独裁 root-support／environmental-feed
- direct_action_gate：allowed／conditional／forbidden
- direct_action_basis：来源规则与条件；同支藏干不得只用五行关系作依据；不得只写“未透”便降级
- allocation_cap
- retained_functions
- lost_or_reduced_functions
- supporting_evidence
- counterevidence
- confidence

无关系影响的节点仍须写 `branch_relation_refs: []`、`identity_after: retained`，防止下游只回写有变化者。

## 6. Qualified Edge Map

qualified-edge-map.yaml 每条边含：

- edge_id
- source_node
- target_node
- source_post_state_ref
- target_post_state_ref
- branch_effect_refs
- edge_layer：direct-action／root-support／environmental-feed／branch-relation／composition-only
- action：生／克／泄／耗／合绊／制／化／通关／冲动
- upstream_availability
- distance_and_order
- intermediary
- climate_gate
- receiver_capacity
- competing_edges
- feedback_or_bypass
- state
- capacity：high／medium／low
- weakest_condition
- supporting source rules
- counterevidence

同一节点进入多条 active 边时，必须建立 allocation note，防止重复计算全部力量。

任一 active／weak direct-action 边若缺 post-state 引用，或其 source direct_action_gate 为 forbidden，视为 schema failure。conditional direct-action gate 只能生成 conditional／weak 边，并须写出补齐条件。root-support／environmental-feed 边改查 support_gate，不得伪装成 direct-action，也不得因 direct-action gate 关闭而自动删除。

## 7. System State

system-state.md 按以下顺序：

1. 五行与十神库存；
2. 可用吞吐；
3. 日主承载力及反证；
4. 主要蓄积点；
5. 第一瓶颈与次瓶颈；
6. 自治子系统；
7. 启动权、控制权、停机能力；
8. 正反馈、负反馈和旁路；
9. 调候；
10. 结构改变所需的最小条件。

必须明确区分：

- 系统能运行；
- 日主从中受益；
- 日主能够主动调用；
- 日主能够停止。

## 8. Problem State

`problem-state.yaml` 至少含：

- `problem_id`
- `label`
- `priority`：primary／secondary／background／not-a-problem
- `affected_nodes`
- `pressure_edge_refs`
- `maintaining_route_refs`
- `daymaster_bearing_relation`
- `system_autonomy_relation`
- `evidence_refs`
- `counterevidence`
- `reversal_conditions`
- `confidence`

必须先裁主问题，后谈药、出口和路线治疗优先级。若两个问题竞争，保留候选并写 arbitration，不得按熟悉格局先定病。

## 9. Pattern Candidates

pattern-candidates.md 为每个流派建立独立矩阵：

- framework
- month-order basis
- candidate pattern
- 格神来源与透藏
- success conditions
- failure conditions
- rescue
- excessive／insufficient
- pure／mixed
- transformation
- 相神
- 生克先后
- current verdict
- confidence
- strongest alternative

唯一格名只在一个候选显著胜出且无未决 BLOCKER 时允许。

## 10. Structured Route Candidates

`route-candidates.yaml` 每条路线含：

- route_id
- route name
- edge_refs：只允许引用 qualified-edge-map 的 edge ID，按发生顺序使用 YAML inline list
- topology：chain／parallel／mixed；mixed 必须附 continuity_notes
- expanded_endpoints_ref：指向审计生成的 endpoint map，不得人工录入另一份端点
- start condition
- end function
- weakest link
- actual_throughput：high／medium／low／conditional
- net_effect_on_primary_problem：therapeutic／aggravating／mixed／neutral／unknown
- therapeutic_priority：仅在 therapeutic 或 mixed 时填写；与 throughput 分开
- realization_rank：按原局实际成立度排列
- cost to day master
- benefit to system
- outlet_eligible：true／false；只有确实释放主问题者可为 true
- bypass
- feedback
- competing route
- trigger conditions
- reversal conditions
- natal／timing／synastry scope
- evidence and counterevidence

端点唯一事实源是 `qualified-edge-map.yaml`。路线只存 edge refs；任何手写 ordered nodes 与 Edge Map 不一致均为 schema failure。

必须主动搜索：

- 格神直接作用日主；
- 印化杀；
- 食伤制杀；
- 食伤生财、财再生杀；
- 财制印／枭；
- 枭夺食；
- 比劫分财；
- 自治木火土、金水等子系统；
- 闭环候选及其最弱边；
- 药重新回到病处的旁路。

### Route endpoint expansion

审计阶段由脚本读取 Edge Map 和 `edge_refs` 生成 `route-edge-endpoint-map.yaml`。至少检查每个 edge ref 存在且唯一；相邻 edges 的 target／source 是否连续；source、target、action、layer、distance 是否与 Edge Map 一致；aggravating route 是否误列为 rescue／outlet；throughput rank 与 therapeutic priority 是否分栏。不连续时须显式声明 `interface_gap`，不能偷偷改端点。

## 11. Conditions Matrix

`conditions-matrix.md` 每条主路线至少列：

- exact natal edge sequence
- original-chart state
- actual throughput
- direction versus primary problem
- necessary conditions and order
- weakest link
- external node／interface that can trigger
- node or condition that causes reversal
- natal realizability rank
- therapeutic priority rank

触发节点只表达条件类型，不自动构成岁运预测。

## 12. Structure Kernel

structure-kernel.md 只写以下七项：

1. Dominant organizer：全局最强组织或压力。
2. Support and rescue：实际能到达的支援。
3. Bottleneck：为什么路线堵。
4. Outlet：现有真实出口及容量。
5. Feedback：什么会回流、过热或蓄积。
6. Agency：谁启动、谁控制、谁停机。
7. Switches：最小改变条件与最强反证。

每项必须引用 problem ID、node ID、edge ID、route ID 和 source rule ID。禁止直接写职业、性格、关系或灵异故事。
