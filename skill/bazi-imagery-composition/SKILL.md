---
name: bazi-imagery-composition
description: 将已经通过结构审计的四柱八字转成可追溯、可验证且不损失原始象意层次的柱象、节点象、路线象与领域 findings：完整原局按 report-scope 至少分别完成家庭、学业、财运、事业四个基础板块，再处理求测者加选专题；同时合成天干本象、十神功能、柱位、地支场景、全部藏干、同柱双向着色、旺衰通量、全局主问题、条件开关和现实载体，并建立 composition 骨架。用户要求正常完整断盘、解释某柱某干支、职业或神秘学取象、把技术结构翻译成生活表现，或为后续可追问 Render 补充新领域象意时使用。不得凭用户经历倒推结构，也不得把取象组合冒充新的生克作用边。
---

# 八字取象与组合

把“结构上成立什么”加工成“它在具体生命领域里可能怎样表现”。本技能不重算旺衰、格局或作用路线；它只在冻结的结构核上完成分层取象、finding 生产和跨 finding 组合。

## 启动门槛

首次运行前完整读取：

- [取象 Finding Schema](references/imagery-finding-schema.md)
- [Composition Schema](references/composition-schema.md)
- [领域载体推导](references/domain-carrier-schema.md)

必需输入：

- `chart-stage1.yaml`
- `post-branch-node-ledger.yaml`
- `qualified-edge-map.yaml`
- `problem-state.yaml`
- `route-candidates.yaml`
- `conditions-matrix.md`
- `structure-kernel.md`
- `structure-freeze-receipt.yaml`
- 通过的 structure audit
- `report-scope.yaml`
- `topic-lens-index.yaml` 与本轮全部 `topic-lens-*.md`
- 本 topic 的完整 `imagery-source-packet-<topic>.md`
- timing／synastry topic 另需对应 diff／overlay artifacts、审计报告与 overlay freeze receipt

任一结构文件晚于 freeze receipt，或 hash／版本不一致时停止并退回结构审计。不得读取 `subject-context.md`，直到 blind findings 通过审计。

岁运或合盘 finding 必须同时引用冻结 natal 与受审计 overlay；overlay 只能描述本轮新增接口和状态差分，不得把它写成本命永久属性。

## 固定分段流程

### Mode A：象意覆盖账本

先根据 Topic Lens 建立 `imagery-coverage.yaml`：

- 本轮问题涉及的柱、干、支、十神、藏干、关系和路线；
- 每个相关柱必须读取的完整取象单元；
- 已加载、缺失、暂不相关的象意范围；
- 被排除但容易误取的符号及排除理由；
- 后续追问可以增量加载的未穷尽范围。

“本轮没展开”不得写成“此字没有该象”。缺完整来源时标 `SOURCE_GAP`，不得用一句口诀补齐。

full-reading 先建立总 `imagery-coverage-index.yaml`：逐项列出 family-home、education-learning、wealth-resource、career-work 和所有 selected optional topics 的 lens、source packet、pillar coverage 与状态。任一基础 topic 缺失时停止，不得先写其他章节后补。

### Mode B：逐柱复合

产出 `pillar-composites.yaml`。对 Topic Lens 涉及的每一柱，按以下顺序处理：

1. 天干原始物象与气质；
2. 相对日主的十神功能；
3. 年／月／日／时柱位职责；
4. 地支自身场景、季节与动静；
5. 该支全部藏干及每个藏干的关系后状态；
6. 天干怎样染色地支，地支怎样给天干提供场景、根基、阻力或去处；
7. 月令、司令、合冲刑害、旬空、路线占用和主问题怎样改写基础象；
8. 基线、受压、良性条件、反向表现四个表达带。

同柱双向着色是 `composition-only`，不是新的生克边，也不是五五对称。权重须引用显隐、司令、季节、位置、通量和关系后状态。

每个藏干都要列出，但必须区分：库存、根气、环境供给、直接做功、格用资格和岁运待引动。不得因“藏在库中”自动判可用，也不得因“不透”自动判无效。

### Mode C：领域 Finding

产出 `topic-findings/<slug>.md`。每条 finding 必须完成：

- `anchor set`：柱、节点、边、路线和来源单元；
- `full-chart sweep`：检查其他柱和竞争路线是加强、改写、反转还是无关；
- `composition trace`：原象、十神、柱位、同柱互染、藏干、结构修正如何逐层合成；
- `expression bands`：基线／受压／条件良好／反向或未显化；
- `manifestation layers`：内部机制／领域载体／外部结果／时间条件／反向代价；
- 可由命主回答“符合／不符合／只在某条件下符合”的生活判断；
- 最强替代解释与禁止渲染项。

不能只从十神标签跳故事，也不能只讲干支本象而漏掉十神和全局。A 带 B 的特性时，同时检查 B 如何承载或限制 A；但两者权重不要求相等。

full-reading 的四个基础 topic 必须分别拥有独立 finding 文件和稳定 topic ID：

- `family-home`：家庭系统、父母／家庭资源压力、家庭角色、居住和生活环境维持；不自动代替爱情或子女。
- `education-learning`：学习输入、理解与输出、考试资格、专业和教育路径。
- `wealth-resource`：资源、收入、积累、支出、流动性、可见度与变现。
- `career-work`：任务、岗位、组织环境、责任压力、职业发展与成果。

相同结构可跨 topic 引用，但不得用一条“综合性格 finding”代替四个领域。每个 selected optional topic 也必须有独立 finding。

### Mode D：Finding 审计与校准

先调用 `$bazi-finding-audit` 的 imagery-finding 模式。FAIL 必须退回对应 finding 或 source packet。

审计通过后才可读取 `subject-context.md`，产出 `calibration-map.md`。full-reading 的 family-home 另有强制先后：先完成并审计 family blind findings，再调用 `$bazi-render` 的 Family Calibration Gate，收到回应后才允许读取该回应并校准：

- `confirmed`：经历与已有表达带相符；
- `conditional`：只在特定领域或时间成立；
- `disconfirmed`：降低该表达分支的呈现优先级；
- `new-question`：提示一个此前未覆盖的领域，重新开 Topic Lens，不得直接新增 finding；
- `structural-challenge`：与结构矛盾，退回 audit，不得用故事改盘。

校准可以调优先级、语气和领域载体，不能创造新的结构、路线或普遍规则。

若用户拒绝家庭校准，记录 `family_calibration_state: declined` 或 `uncalibrated` 并继续；不得补写“根据反馈验证”。若详细家庭事实在 blind finding 审计前已经进入当前生成上下文，优先转交新鲜隔离上下文；无法隔离时记录 `contaminated` 并放弃盲回验资格。若仍把既有事实写入 finding 或声称盲验证，退回 `$bazi-finding-audit`。

### Mode E：Composition

只使用通过审计的 findings 与可选 calibration map 产出 `composition.md`；没有 subject context 时明确记录“未校准”，不得虚构校准结果。它负责：

- 全盘一句话主轴；
- 主问题、主要救应与日主能动性的生活化总框架；
- 各 topic 的 finding 顺序；
- 同一结构跨领域的共通点与差异；
- 必须保留的条件、代价、反证和 source gap；
- 后续 Q&A 可继续展开的象意索引。

完成后再次调用 `$bazi-finding-audit` 的 composition 模式。Render 不得绕过该审计。

full-reading 的 `composition.md` 必须按照 `report-scope.yaml` 建立基础四板块和全部已选专题的 topic order；缺任一项不得进入 Render。

## 职业与行业推导

不得从一个十神直接报行业名称。先按 [领域载体推导](references/domain-carrier-schema.md) 写工作性质，再给行业例子，并分开：

- 行业；
- 岗位／角色；
- 实际工作内容；
- 组织环境；
- 收入机制；
- 可见度、名声和真正变现。

例子只是性质的现实载体，不是命局唯一答案。

## 硬门槛

- 结构未冻结或审计未过：停止。
- full-reading 缺 report-scope、topic-lens-index、基础四镜头或任一已选专题镜头：FAIL。
- 相关柱漏一天干、地支或任一藏干：FAIL。
- 同柱互染被当成 active edge：FAIL。
- 只列符号、不做组合：FAIL。
- 只讲局部而未做 full-chart sweep：FAIL。
- 完整取象来源缺失却写高置信生活故事：FAIL。
- 用户经历创造新 finding：FAIL。
- 家庭事实或校准回应在 family blind findings 审计前参与生成：FAIL。
- 用一条 general finding 代替家庭、学业、财运、事业任一基础板块：FAIL。
- 行业名先于工作性质：退回改写。
- composition 压掉 finding 的条件、代价或反证：FAIL。

## 输出边界

本技能产出可供 Render 使用的分析材料，不直接替用户写最终报告。后续追问若进入新领域，允许增量重跑 Mode A 至 E；不得把首次报告误当成穷尽全部天干地支象意。
