# 八字结构动力 Pipeline Spec

## 目录

1. 总原则
2. 阶段与产物
3. 恢复顺序
4. Context 隔离
5. 分析模式
6. 完成条件
7. 标准原局断局协议

## 1. 总原则

八字分析不得在一次连续生成中同时完成事实校验、原典读取、节点力量、关系裁决、格局、取象和渲染。

每一阶段都必须产生可审计产物。下游只能引用上游产物，不得凭印象重算；缺失时按固定顺序恢复。

完整原局必须把“技术结构完成”和“生活领域断局完成”分开。结构冻结是进入断局的门槛，不是完整断局的终点。

## 2. 阶段与产物

| Stage | Skill | 产物 | 硬门槛 |
|---|---|---|---|
| 0 | orchestrator | process notice、case-manifest | 先说明结构盲跑与后置选题；模式、命盘主人、本人／代看、流派锁定 |
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
| 3.6 | bazi-render scope-intake | report-scope.yaml | 确认太极中心、完整／限定模式、基础四板块与附加专题；不产断语 |
| 4A | bazi-topic-lens | topic-lens-index、topic-lens-*.md | 只引用冻结结构；完整原局强制家庭／学业／财运／事业四镜头 |
| 4B | core timing／synastry mode | diff／overlay structure | 仅相关 topic 运行；不改写 natal |
| 4C | bazi-source-lookup | imagery-source-packet | 读取完整展开，不用缩略口诀 |
| 4D | bazi-imagery-composition | imagery-coverage、pillar-composites、topic-findings | 分段生产，不读 context |
| 4.5 | bazi-finding-audit | finding-audit | 通过后才可校准 |
| 4.6 | bazi-render family-calibration | family-calibration-prompt、calibration-response | 只展示已审计家庭判断；此前不得读取家庭经历 |
| 5A | bazi-imagery-composition | calibration-map、composition | 经历只校准已有分支 |
| 5.5 | bazi-finding-audit | composition-audit | 不新增 finding、不丢限制 |
| 6 | bazi-render | report 或 Q&A answer | Render 自身不新增 finding |
| 6.5 | bazi-finding-audit | render／conversation audit | 防压缩与聊天越界 |

## 3. 恢复顺序

发现输入缺失时固定回退：

process notice → case-manifest → Reader → Structure Source Packet → Node Ledger → Interaction Census → Branch Relation Census → Branch State → Post-Branch Node Ledger → Edge Map → System State → Problem State → Pattern／Structured Routes → Conditions Matrix → Structure Kernel → Audit → Freeze → Report Scope Intake → Topic Lens Index／per-topic Lens →〔必要时 Timing／Synastry diff／overlay + audit〕→ Imagery Source Packet → Pillar Composites → Topic Findings → Finding Audit → Family Calibration Gate → Calibration Map → Composition → Composition Audit → Render。

不得为了回答快而跳过缺失阶段。用户只问一个术语时可以缩小 question scope，但不能伪装成完整断局。

## 4. Context 隔离

- chart-stage1：只存盘面事实。
- subject-context：用户经历、旧解读、杯卦、灵体反馈；Structure Core 盲结构阶段禁读。
- source-packet：只存来源规则和边界。
- core artifacts：只存技术结构。
- report-scope：只存求测中心、范围与问题，不存用于证明结论的生活故事。
- family blind findings：必须在未询问、未读取详细家庭经历的新鲜上下文中生成并审计；若既有上下文已污染且无法隔离，只能标 `contaminated`，不得声称盲校准。
- calibration：structure 与 blind findings 均审计通过后才允许读取校准回应或 subject-context。
- composition：只组合通过审计的 findings，可引用 calibration 调整顺序和语气。
- render：只能翻译已有 finding；对话中新问题须按 routing 回到对应上游。

## 5. 分析模式

### Natal

- `full-reading`：执行 Stage 0 至 6.5；结构冻结后必须运行 Report Scope Intake，基础四板块不可省略。
- `structure-only`：只执行 Stage 0 至 3.5，交付名称必须是“原局结构分析”，不得称完整断局。
- `limited-topic`：结构冻结后只为约定专题生产 finding；必须明确未覆盖基础板块，不得称完整原局报告。

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
- full-reading 已有 `report-scope.yaml`，命盘主人、求测者关系、默认太极中心和逐 topic 中心均明确；
- full-reading 的 family-home、education-learning、wealth-resource、career-work 四个基础 topic 均有独立 lens、完整 imagery source、finding 与 render section；
- 求测者已选专题没有被漏掉；
- 家庭校准只发生在家庭 blind findings 审计之后；拒绝校准时明确标 `uncalibrated`，既有上下文污染时标 `contaminated`；
- 具体问题已有完整 imagery source、逐柱复合、full-chart sweep 和 finding audit；
- 最终文字没有新增、压缩或反向改写 finding；追问新增内容已经走过增量 finding 流程。

## 7. 标准原局断局协议

### 启动说明

首次启动 `full-reading` 时，先用用户能理解的语言说明：本轮先判断全盘结构，结构冻结后才开始分领域断局；个人经历不会进入盲结构；基础报告固定含家庭、学业、财运、事业；专项问题后置确认。

### 范围入口

结构冻结后暂停一次，由 Render 询问：

- 默认是否以命主本人为中心；若不是，围绕谁、哪段关系或哪件事；
- 是否只看原局，或另有具体时间；
- 除基础四板块外，是否增加感情、健康、神秘学、创作、人际、子女或其他专题；
- 每个专题最想核清的具体问题。

用户无需理解“太极点”术语。Render 把自然语言写入 `report-scope.yaml`，Topic Lens 再转换为技术中心。

### 家庭校准门

家庭是标准报告的一部分，也是首个校准锚点。先完成家庭 blind findings 与审计，再展示其中 2 至 6 条可核验判断，请求求测者标记 `confirmed`、`conditional` 或 `disconfirmed`。不得在 blind finding 之前索取详细家庭事实；不得用校准回应重写 node、edge、route、pattern 或通用规则。
