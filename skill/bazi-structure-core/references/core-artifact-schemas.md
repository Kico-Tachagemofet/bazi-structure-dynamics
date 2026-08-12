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
13. Use-God Kernel
14. Five-Element Process Handoff
15. Timing／Synastry Activation Overlay

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
- participation_scope：stock／root-support／environmental-feed／direct-action／pattern-eligible／timing-only，可多选
- support_gate：allowed／conditional／forbidden；单独裁 root-support／environmental-feed
- direct_action_gate：allowed／conditional／forbidden
- direct_action_basis：来源规则与条件；同支藏干不得只用五行关系作依据；不得只写“未透”便降级
- manifestation_basis_bundle：分栏记录司令／气序、同气或本气透出、位置远近、关系后支局、空亡与受损、占用竞争、下游承接／去处及 source rule refs；任一单项不得自动等于得用
- activation_interfaces：当前为 hidden／latent／timing-only 的节点逐项登记待时接口；每项至少含 `interface_id`、`natal_node_ref`、`natal_visibility`、`natal_participation_scope`、`trigger_classes`、`trigger_signature`、`if_matched_recompute_from`、`affected_branch_relation_refs`、`affected_node_refs`、`affected_edge_candidate_refs`、`affected_route_condition_refs`、`projected_effect_candidates`、`strongest_counterconditions`、`status: registered-unmatched` 与 `projection_is_not_current_verdict: true`
- nonexternal_roles_retained：field-background／stock-root-support／environmental-feed／internal-latent／timing-pending，可多选；不得因无 direct-action 而留空
- allocation_cap
- retained_functions
- lost_or_reduced_functions
- supporting_evidence
- counterevidence
- confidence

无关系影响的节点仍须写 `branch_relation_refs: []`、`identity_after: retained`，防止下游只回写有变化者。

文件顶层另建 `branch_manifestation_handoffs`，每个地支位置至少含：

- `branch_position_id`、`branch_symbol`、`branch_state_refs` 与全部 `hidden_node_refs`；
- `field_layer`：`field-present` 及其季节／空间／场景／容器状态，另列 relation-after modifier；位置事实不得因藏干未透而删除；
- `qi_layer`：逐藏干引用 visibility、participation scope、support gate、direct-action gate 与 nonexternal roles；
- `function_layer`：已获直接做功资格的 node refs、仍属 conditional 的 node refs、禁止直接做功者及依据；实际容量须待 Qualified Edge Map 回链补齐；
- `activation_interface_refs`：本支各藏干已登记的待时接口及其重算起点；这里只交接候选，不写当前激活；
- `result_handoff`：允许 Topic Lens／Composition 查询的 edge／route／condition refs、未决开关，以及 `external_result_not_decided_here: true`；
- `prohibited_collapse`：不透≠无效；透出／会局≠自动得用；有 direct-action≠外部结果已兑现。

`branch_manifestation_handoffs` 是结构到取象的收据，不是 Deep Card 反向进入 Core 的入口。环境题可以在下游由 field layer 直接桥接现实场所；藏干也可以只通过 root-support 扶持另一节点，不要求四层线性串联。

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
- relation_form：形式候选与主裁决，如 `control-primary`／`combine-primary`／`coexisting`／`undetermined`
- effect_dimensions：不得由 action 一栏代替
  - `target_material_effect`：目标形质是否实质受损，记录 state、evidence 与 counterevidence
  - `target_functional_effect`：目标功能是否被抑制、羁绊、占用或改道
  - `third_party_protective_effect`：第三方是否因此减压；另列 `beneficiary_refs`
- upstream_availability
- distance_and_order
- intermediary
- climate_gate
- receiver_capacity
- competing_edges
- `qualification_trace`：按 `2B.0` 至 `2B.6` 顺序记录每一步读取的上游 refs、候选、裁决、未决条件和写入字段；不得缺步后直接补最终 verdict
- `rule_application_receipts`：每次规则卡参与时记录 card ID、curation status、Source Packet rule ref、hook、role、依赖完成状态、命中条件、失败条件、写入维度与明确未裁问题
- feedback_or_bypass
- state
- capacity：high／medium／low
- weakest_condition
- supporting source rules
- counterevidence
- ambiguity_ref：只有完成全部 2B trace 后仍未决且会改变下游路线时填写，指向 `structural-ambiguity-register.yaml`

同一节点进入多条 active 边时，必须建立 allocation note，防止重复计算全部力量。

运行顺序固定为：edge candidate → relation form → competition arbitration → allocation → residual capacity → effect dimensions → finalize。规则卡的原书顺序和人工审校顺序不得覆盖此顺序。任何卡若在同一 hook 读取自己将写入的最终字段，或在依赖未完成时参与裁决，视为 schema failure。

### Structural Ambiguity Register

`structural-ambiguity-register.yaml` 仅收录 Core 无法依来源、位置、力量、占用和竞争裁定，且不同分支会改变 route／condition／topic axis 的真实争议。每项至少含：

- ambiguity_id、relation refs、shared nodes；
- candidate branch IDs 与各自 edge／route／condition refs；
- exhausted evidence 与 unresolved reason；
- 每支的结构后果、最强反证与 reversal conditions；
- discriminating observables：过程顺序、最终仍能做功者及可区分载体；
- `experience_read: false`；
- `case_overlay_allowed: true／false`；
- prohibited updates：rule registry、natal facts、已冻结分支。

若两个分支没有可辨别过程，或只因分析者懒于裁位置强弱而并列，视为 schema failure。

任一 active／weak direct-action 边若缺 post-state 引用，或其 source direct_action_gate 为 forbidden，视为 schema failure。conditional direct-action gate 只能生成 conditional／weak 边，并须写出补齐条件。root-support／environmental-feed 边改查 support_gate，不得伪装成 direct-action，也不得因 direct-action gate 关闭而自动删除。

任一地支相关 edge 若未回链到 `branch_manifestation_handoffs[branch_position_id].function_layer`，或下游把 `visibility_after` 直接当作 `direct_action_gate`，视为 schema failure。`visible` 仍可能受制、占用或无承接；`hidden` 仍可能保留根气、环境供给，证据充分时也可获得 direct-action gate。

`target_material_effect`、`target_functional_effect` 与 `third_party_protective_effect` 分别回答不同问题。任一维度可为 `none／low／medium／high／conditional／unknown`，但必须保留来源、命局条件与反证；不得建立“阳克阴永远只抑制”或“见克必有实损”的自动映射。

### Ten-God Function Gate

十神标签由 Stage 1 确定性计算，只表示相对关系。System State 中每个被引用十神另列 `function_candidates` 与 edge refs，不写固定喜忌；Problem State 与 Route Matrix 再逐项记录 `actual_function`、`throughput`、`net_effect_on_primary_problem`、`cost_or_bypass`、`counterevidence` 与 `reversal_conditions`。缺任一实际 edge 或主问题引用时，只能保留十神库存，不能生成“为喜／为忌／能制／能护／命主擅长”的结论。

任何十神都适用同一门槛。不得只为一个十神放宽或收紧证据要求；单一十神来源例证只能解释当前路线，不能成为其他十神缺省规则。

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
- activation interface refs 与 if-matched recomputation scope
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

## 13. Use-God Kernel

`use-kernel.md` 在 Structure Kernel 之后生成，并与全部结构产物一起冻结。完整字段、流派分层和关系轴规则见 [用神太极核 Schema](use-kernel-schema.md)。

最低要求：

- 格局用神、病药／制化主用、扶身辅用、调候需要与备用路线分栏；
- “治疗优先级”与“当前可用度／实际通量”分栏；
- 主用与病神、生用、损用、去处、日主能动性及备用路线中的实际关系逐轴列出；
- 每条关系轴只回答一个主过程，并引用现有 node／edge／route／condition；
- 不写生活故事，不用一个五行标签替代关系过程。

## 14. Five-Element Process Handoff

`structure-process-handoff.yaml` 是冻结结构向 Topic／Composition 交付的唯一过程级事实源。它在 `use-kernel.md` 后生成，完整字段见 [五行克应过程 Handoff Schema v4](five-element-process-handoff-schema.md)。最低要求：

- 每个 process 先引用旺衰、司令、实际吞吐与日主承载，再引用完整 route／condition；
- ordered edges 必须覆盖路线的启动、成本、通关、分叉与回病边；
- 被动承受、主动发动、自治运行、停滞与恢复分别成 phase；
- 日主成本、治疗效果、剩余问题与回病旁路分栏；
- `life_effect_matrix` 分开日主承载、客观产出、社会兑现和持续代价；治疗方向不得替代外部成果方向；
- 十神只解释已成立作用相对日主的关系，不重新裁 edge；
- process closure 与 phase agency 通过审计后才能冻结。

## 15. Timing／Synastry Activation Overlay

冻结原局后的岁运或合盘只按 [岁运／合盘激活覆盖层 Schema](timing-synastry-activation-overlay-schema.md) 产出临时 diff。最低要求：

- 逐项引用原局 `activation_interfaces`，没有接口不得凭模型联想新增激活；
- 分开 `natal_visibility` 与 `overlay_visibility`；
- trigger match 后从登记的最早受影响阶段重新裁 branch／node／edge／route condition；
- 同时从 `structure-process-handoff.yaml` 重算受影响 process 的 start gate、phase、throughput、allocation、日主成本、治疗效果、剩余问题、回病与能动性；
- 用户要求逐年时，每年另产 `timing/year-YYYY-process-state-diff.yaml`，并证明上游变化已传播至同 process 的全部下游或有明确无影响继承收据；
- 记录覆盖范围、持续方式、反证与失效条件；
- overlay 审计与 freeze 通过后才可进入下游；
- 不回写原局，不把另一张盘的节点变成本命永久节点。
