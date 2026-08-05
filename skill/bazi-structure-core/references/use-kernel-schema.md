# 用神太极核 Schema

`use-kernel.md` 位于 `structure-kernel.md` 之后、结构审计与冻结之前。它把已锁定的主问题、路线和条件收束成后续断局的功能中心；不写职业、性格或生活故事。

## 1. Framework Separation

分别记录，不得静默混成一个“喜用神”：

- `pattern_use`：格局成立、成败救应所围绕的格神／相神；
- `therapeutic_use`：针对 `problem-state` 的病药／制化主用；
- `support_use`：提高日主承载、让主用可被调用的辅用；
- `climate_use`：仅处理寒暖燥湿的调候需要；
- `alternative_use`：原局较弱、待条件补齐的备用路线。

几者重合时说明重合依据；不重合时保留并列，不强行选成一个字。

## 2. Pivot Card

每个实际保留的用神枢纽至少含：

- `pivot_id`
- `framework_role`
- `problem_refs`
- `node_refs`／`route_refs`
- `function`：具体解决什么，不写“吉”“有利”作替代；
- `therapeutic_priority`
- `current_availability` 与 `actual_throughput`
- `daymaster_access`：日主能否启动、承接、改道、停止；
- `cost_or_side_effect`
- `necessary_conditions`
- `reversal_conditions`
- `strongest_counterevidence`
- `confidence`

“最需要”与“当前最能用”必须分栏。治疗优先级最高但原局通量低，仍可成为主用；须同时说明缺什么条件。

## 3. Actual Relation Axes

只建立盘中真实存在的关系轴，不机械凑齐类别。可选类别包括：

- `use-self`：主用节点自身的力量、位置、显隐和参与层；
- `use-problem`：主用怎样处理主问题；
- `source-to-use`：谁生用、助用、给用提供根或环境；
- `damage-or-diversion`：谁克用、合绊、冲损、占用或把用导向别处；
- `use-destination`：主用做功后流向哪里，是否形成成果或重新生病；
- `use-daymaster`：主用与日主的承载、启动和控制关系；
- `alternative-route`：备用制化与主用的竞争、接力或替代。

每条轴至少含：

- `axis_id`
- `axis_type`
- `focal_question`
- `source_endpoint`／`target_endpoint`
- `edge_refs`／`route_refs`
- `mechanism`
- `base_state`
- `competing_allocation`
- `switch_conditions`
- `failure_or_reversal`
- `topic_relevance_hints`
- `confidence`

一条轴只回答一个主过程。相同节点若一面制病、一面生出旁路，须拆成两条轴并记录竞争分配；不得在一句“有利有弊”里抹平。例如“甲制戊”与“甲生丙、丙再生戊”是两条轴；“庚生壬”与“庚克甲”也是两条轴。

## 4. Kernel Summary

文件末尾收束：

1. `primary_pivot`
2. `auxiliary_pivots`
3. `alternative_pivots`
4. `dominant_relation_axes`
5. `currently_blocked_axes`
6. `minimum_switches`
7. `topic_lens_handoff`

`topic_lens_handoff` 只提示哪些轴可能与家庭、学业、财运、事业或专项有关，不提前产生活断语，也不把一个领域固定等同于某个十神。

