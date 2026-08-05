---
name: bazi-structure-core
description: 分阶段建立四柱八字的结构动力模型：逐位置评估天干与藏干，完整枚举生克合冲刑害方会合局，裁决地支状态和节点占用，限定作用边通量，再锁定主问题、实际吞吐、日主承载、自治子系统、格局候选、只引用 Edge Map 的结构化路线、治疗优先级、条件矩阵及结构核。用户询问旺衰、通关、格局、用神、藏干起效、合化、墓库、路线或既有结构遗漏时使用。必须接收 Reader 和 Source Packet，不直接写生活故事。
---

# 八字 Structure Core

本技能是分析引擎，不是一次性解盘器。严格按模式产出中间文件；每个模式完成后停止或显式进入下一模式。

## 必需输入

- case-manifest.yaml
- chart-stage1.yaml
- chart-stage1-audit.md
- source-packet.md

Stage 1 为 FAIL 时停止。Source Packet 有缺口时，允许枚举事实，但不得对缺证据事项给高置信度裁决。

## 固定执行顺序

详细字段见 [Core artifact schemas](references/core-artifact-schemas.md)，状态词见 [State vocabulary](references/state-vocabulary.md)。

### Mode A：Node Ledger

逐一记录四个天干和每个地支藏干。不得先聚合重复支或同五行。

产出 node-ledger.yaml，至少含：得令、根型、透藏、来源、克泄耗、位置、空亡、调候环境、支局候选、当前占用与反证。

### Mode B：Interaction Census

先全枚举，后谈权重。检查：

- 天干生克合与相邻／隔柱；
- 同柱干支；
- 六合、六冲、刑、自刑、害、破；
- 三合、半合、方会及共享支竞争；
- 重复支；
- 藏干候选关系；
- 中间节点阻断和岁运待补条件。

优先用 Reader 的确定性枚举结果。产出 interaction-census.yaml。

### Mode C1：Branch Relation Census

从 Interaction Census 单独抽取并重新核对所有地支关系：三会、三合、半合／拱合、六合、六冲、刑、自刑、害、破、重复支及共享支。每一类别无命中时也必须留下 negative scan；不得让地支关系淹没在大量五行候选边中。

产出 branch-relation-census.yaml。覆盖未通过时不得进入 Mode C2。

### Mode C2：Branch Arbitration

对每组地支关系分别判断完整度、旺支、紧贴、月令、空亡、冲刑破损、共享节点和流派优先级。

分开记录：

1. 形式上的支局状态；
2. 成局后仍保留的本气和功能边；
3. 同一节点被多条关系占用的比例性限制；
4. 原局潜伏与岁运引动。

每张裁决卡必须说明该关系如何改变成员支与逐个藏干，而不只描述关系本身。分别裁定：形式成立度、实际通量、合绊／集中／改道／冲动／受损／转化、残余功能，以及旬空和“不自动开库”这两个独立条件。

产出 branch-state.md。有未解决共享节点竞争时不得进入 Mode C3。

### Mode C3：Post-Branch Node Ledger

把 Mode C2 的裁决逐节点写回，产出 post-branch-node-ledger.yaml。必须覆盖原 Node Ledger 的全部天干和逐位置藏干；没有受到地支关系影响的节点也要显式标记 retained／unchanged。

每个节点至少写明：pre-state 引用、关系引用、关系后身份与可用度、根型变化、透藏／显隐状态、允许参与的功能范围、direct-action gate、分配上限、反证与置信度。

藏干存在、提供库存／根气、环境供给、直接做功和成为格用是不同层级。冲不负责把藏干“释放”为明干；同支藏干也不得仅凭五行相生克自动获得 active direct-action gate。

但“不透”本身也不是把藏干一律降为 conditional／weak／forbidden 的充分理由。有原典人元规则、得令本气、位置近、同气透出、重复根群或成势支持时，藏干仍可获得 allowed direct-action gate；其实际容量留到 Mode D 裁决。即使 direct-action gate 不成立，root-support／environmental-feed 仍须单独保留，不能因删除伪直接边而抹去。

覆盖不足、共享节点未分配、或任一变化没有回链到 branch-state 时，不得进入 Mode D。

### Mode D：Edge Qualification

只允许从 post-branch-node-ledger.yaml 起边。原 node-ledger.yaml 仅用于追溯 pre-state，不得作为 availability 的当前事实源。

每条边标记为 candidate、active、weak、blocked、occupied、redirected、conditional 或 inactive。

分别检查：

- 上游可用量；
- 连接距离和先后；
- 中间是否受合、冲、制、泄；
- 调候与环境；
- 下游承接能力；
- 与其他路线的竞争；
- 是否把药重新导回病处。
- source／target 的 post-branch state 引用；
- edge layer：direct-action／root-support／environmental-feed／branch-relation／composition-only；
- direct-action gate 是否允许该层级节点起边；
- branch-state 已判 suppressed／occupied／redirected／conditional 的变化是否被继承。

“有根”“有箭头”“五行齐”都不能直接判畅通。产出 qualified-edge-map.yaml。

### Mode E：System State

在节点和边审计完成后，才聚合为：

- 五行／十神库存；
- 实际吞吐；
- 蓄积点；
- 最弱环与主堵点；
- 日主承载力；
- 启动权、控制权和停机能力；
- 自治子系统；
- 正反馈、负反馈和旁路；
- 调候状态。

产出 system-state.md。身强身弱只是其中一项。

### Mode E2：Primary Problem Arbitration

在比较救应和出口前，先产出 `problem-state.yaml`，锁定本轮的首要矛盾。至少列：主问题、次问题和非问题，受影响的核心节点，直接压力边与维持反馈，日主承载与系统自治的关系，判定证据、最强反证、置信度，以及什么变化会令主问题改判。

后续所有路线必须评价“对该主问题的净作用”。没有 problem state 时，不得使用“救应、出口、药、病、优先”这些词。

### Mode F：Pattern and Structured Route Matrix

按不同来源分别列格局候选，不静默混派。检查格局的成、败、救应、太过、不及、清杂、变化、相神和生克先后。

同时枚举所有竞争路线，不只写熟悉的格局术语。路线文件只引用 `qualified-edge-map.yaml` 的 edge ID，不得手抄或改写端点。每条路线分开记录实际通量、对主问题的净作用、治疗优先级、现实成立度、代价、旁路、反馈和成立条件。

产出：

- pattern-candidates.md
- route-candidates.yaml
- route-edge-endpoint-map.yaml：由审计脚本根据 Edge Map 展开，只作校验视图
- conditions-matrix.md

`conditions-matrix.md` 对每条主路线列原局状态、必要条件、最弱环、可触发的外部节点、反转节点和成立先后。新增岁运节点只是条件接口，不是本阶段预测。

实际通量最大不等于最能解决主问题。加重主问题的路线必须标 `aggravating`，不得进入 rescue／outlet 排名；混合路线必须分别写收益和回病旁路。

证据不足时保留多候选，禁止强行给唯一格名。

### Mode G：Structure Kernel

只收束技术结构：

1. 主组织／主压力；
2. 有效支援；
3. 主要瓶颈；
4. 可用出口；
5. 关键反馈；
6. 启动与控制；
7. 条件开关和最强反证。

每项须引用 `problem-state`、node、edge、route 和 source rule ID。产出 structure-kernel.md，然后调用 $bazi-finding-audit。审计通过并生成 structure freeze 前不得进入具体取象、岁运或合盘结论。

## 不可跨越的边界

- 不把关系存在等同于力量足够。
- 不把图上成环等同于真实流通。
- 不把冲等同于开库，不把合等同于化。
- 不把所有藏干同等引动。
- 不让 Edge Map 绕过 Branch Arbitration 回读原始节点。
- 不在 route 中重写 edge 的 source／target／action；Edge Map 是端点唯一事实源。
- 不把 actual throughput 排名当 therapeutic priority，也不把加重主问题的通道叫出口。
- 不把同支藏干的组成关系自动改写成持续发生的生克边。
- 不把“删除伪直接边”扩大成“所有藏干只剩库存”；混合路线必须同时保留可证的根气与环境供给层。
- 不把系统能运行等同于日主能主动控制。
- 不提前读取 subject context 以寻找“命中故事”。
- 不用杯卦、灵体反馈或已发生事件证明普遍命理规则。
