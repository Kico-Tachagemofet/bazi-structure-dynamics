# 八字结构动力 Pipeline Spec

## 目录

1. 总原则
2. 阶段与产物
3. 恢复顺序
4. Context 隔离
5. 分析模式
6. 完成条件

## 1. 总原则

八字分析不得在一次连续生成中同时完成事实校验、原典读取、节点力量、关系裁决、格局、取象和渲染。

每一阶段都必须产生可审计产物。下游只能引用上游产物，不得凭印象重算；缺失时按固定顺序恢复。

## 2. 阶段与产物

| Stage | Skill | 产物 | 硬门槛 |
|---|---|---|---|
| 0 | orchestrator | case-manifest | 模式、问题、流派锁定 |
| 1 | bazi-reader | chart-stage1、audit、subject-context | FAIL 停止 |
| 1.2 | bazi-source-lookup | source-packet | 关键来源缺失则降置信度 |
| 1.5A | bazi-structure-core | node-ledger | 节点覆盖 100% |
| 1.5B | bazi-structure-core | interaction-census | 关系覆盖通过 |
| 2A-1 | bazi-structure-core | branch-relation-census | 地支关系与 negative scan 独立覆盖 |
| 2A-2 | bazi-structure-core | branch-state | 共享支竞争已裁决 |
| 2A-3 | bazi-structure-core | post-branch-node-ledger | 全部节点已写回关系后状态 |
| 2B | bazi-structure-core | qualified-edge-map | 只从 post-branch state 起边；存在与起效分开 |
| 2C | bazi-structure-core | system-state | 最弱环、控制权齐全 |
| 2D | bazi-structure-core | problem-state | 主问题与判定依据先锁定 |
| 3A | bazi-structure-core | pattern-candidates、route-candidates.yaml、conditions-matrix | 端点只引用 Edge Map；通量与治疗优先级分开 |
| 3B | bazi-structure-core | structure-kernel | 只写技术结构 |
| 3.5 | bazi-finding-audit | audit-report、structure-freeze-receipt | BLOCKER 必修；hash 冻结 |
| 4A | bazi-topic-lens | topic-lens | 只引用冻结结构，列 imagery needs |
| 4B | core timing／synastry mode | diff／overlay structure | 仅相关 topic 运行；不改写 natal |
| 4C | bazi-source-lookup | imagery-source-packet | 读取完整展开，不用缩略口诀 |
| 4D | bazi-imagery-composition | imagery-coverage、pillar-composites、topic-findings | 分段生产，不读 context |
| 4.5 | bazi-finding-audit | finding-audit | 通过后才可校准 |
| 5A | bazi-imagery-composition | calibration-map、composition | 经历只校准已有分支 |
| 5.5 | bazi-finding-audit | composition-audit | 不新增 finding、不丢限制 |
| 6 | bazi-render | report 或 Q&A answer | Render 自身不新增 finding |
| 6.5 | bazi-finding-audit | render／conversation audit | 防压缩与聊天越界 |

## 3. 恢复顺序

发现输入缺失时固定回退：

case-manifest → Reader → Structure Source Packet → Node Ledger → Interaction Census → Branch Relation Census → Branch State → Post-Branch Node Ledger → Edge Map → System State → Problem State → Pattern／Structured Routes → Conditions Matrix → Structure Kernel → Audit → Freeze → Topic →〔必要时 Timing／Synastry diff／overlay + audit〕→ Imagery Source Packet → Pillar Composites → Topic Findings → Finding Audit → Calibration → Composition → Composition Audit → Render。

不得为了回答快而跳过缺失阶段。用户只问一个术语时可以缩小 question scope，但不能伪装成完整断局。

## 4. Context 隔离

- chart-stage1：只存盘面事实。
- subject-context：用户经历、旧解读、杯卦、灵体反馈；Structure Core 盲结构阶段禁读。
- source-packet：只存来源规则和边界。
- core artifacts：只存技术结构。
- calibration：structure 与 blind findings 均审计通过后才允许读 subject-context。
- composition：只组合通过审计的 findings，可引用 calibration 调整顺序和语气。
- render：只能翻译已有 finding；对话中新问题须按 routing 回到对应上游。

## 5. 分析模式

### Natal

完整执行 Stage 0 至 3.5；需要具体问题时再进 Topic。

### Timing

先锁定 natal。按大运、流年、流月逐层做 before／after diff，记录新增根、关系补齐、边状态变化和触发路线。

### Synastry

双方 natal 各自 PASS 后建立跨盘临时节点和边。直接叠盘必须在 case-manifest 显式声明。

### Audit Existing Reading

先 Reader 重建事实，再把旧解读拆为 claims；每条 claim 追溯到 node／edge／route／source，不能只按“听起来合理”审。

### Source or Imagery Question

允许只运行 Reader 的最小事实层加 Source Lookup，但若用户要求落到具体命局，仍需 Core。

### Conversational Follow-up

先判断是已有 finding 的澄清、同结构的新取象、新 topic、新时间／合盘层，还是结构争议。只有第一类可直接 Render；第二、三类增量运行 Topic → Source → Imagery；后两类退回 Core／Audit。首次报告不视为穷尽全盘象意。

## 6. 完成条件

完整原局只有在以下全部满足时才可称完成：

- Stage 1 PASS 或明确说明 PARTIAL；
- 节点和关系覆盖通过；
- 地支关系已独立扫描并完成 negative scan；
- 地支竞争无未决 BLOCKER；
- 关系后节点覆盖全部原始节点，且 Edge Map 没有绕回 pre-branch 状态；
- 每条主路线有最弱环和反证；
- 主问题已独立锁定；每条路线的端点与 Edge Map 一致，并分开 actual throughput、net effect 与 therapeutic priority；
- conditions matrix 与 structure freeze receipt 存在且下游版本一致；
- 格局候选按流派分开；
- Structure Kernel 审计 PASS；
- 具体问题已有完整 imagery source、逐柱复合、full-chart sweep 和 finding audit；
- 最终文字没有新增、压缩或反向改写 finding；追问新增内容已经走过增量 finding 流程。
