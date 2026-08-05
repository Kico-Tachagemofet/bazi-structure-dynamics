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
- `use-kernel.md`
- `structure-freeze-receipt.yaml`
- 通过的 structure audit
- `report-scope.yaml`
- `topic-lens-index.yaml` 与本轮全部 `topic-lens-*.md`
- 本 topic 的完整 `imagery-source-packet-<topic>.md`
- timing／synastry topic 另需对应 diff／overlay artifacts、审计报告与 overlay freeze receipt

任一结构文件晚于 freeze receipt，或 hash／版本不一致时停止并退回结构审计。不得读取 `subject-context.md`，直到相关 blind findings 通过审计；若要做流运验证，还须等 hypotheses 审计并冻结后才能读取对应年史。

岁运或合盘 finding 必须同时引用冻结 natal 与受审计 overlay；overlay 只能描述本轮新增接口和状态差分，不得把它写成本命永久属性。

## 固定分段流程

### Mode A：象意覆盖账本

先根据 Topic Lens 建立 `imagery-coverage.yaml`：

- 本轮问题涉及的柱、干、支、十神、藏干、关系和路线；
- 每个相关柱必须读取的完整取象单元；
- 已加载、缺失、暂不相关的象意范围；
- 被排除但容易误取的符号及排除理由；
- 后续追问可以增量加载的未穷尽范围。
- 每条 `body_use_axis` 的两端及生用、损用、去处、日主关系所需象意。

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

### Mode B2：用神关系轴场景

在逐柱复合后，逐条处理 Topic Lens 的 primary／supporting axes，产出 `axis-scenes.yaml`。这是八字断局的主要思考单位；finding 只是它的输出接口。

每次只处理一条关系轴：

1. 读取领域体和用神枢纽；
2. 展开两端干支本象、十神功能、柱位、相关地支与全部藏干；
3. 继承已审计的生用、损用、占用、竞争分配、去处和日主能动性；
4. 合成基线、被触发、被改道、失败／反转四幅场景；
5. 给出可承载该过程的现实性质，不直接宣布唯一事件或行业；
6. 写明不能从本轴推出什么。

同一节点的两种方向必须分别成 scene。例如“制病”和“生出回病旁路”不能糊成一条“既好又坏”。本技能不照搬紫微的词条全列与语义交叉；八字直接在完整干支—十神—柱位—藏干—路线关系上合成场景。

### Mode C：轴驱动领域 Finding

产出 `topic-findings/<slug>.md`。每条 primary finding 必须对应一个 `body_use_axis` 和一个 `axis_scene`；supporting axis 可进入同一 finding 的修正层，但不得取代主轴。每条 finding 必须完成：

- `anchor set`：柱、节点、边、路线和来源单元；
- `full-chart sweep`：检查其他柱和竞争路线是加强、改写、反转还是无关；
- `composition trace`：原象、十神、柱位、同柱互染、藏干、结构修正如何逐层合成；
- `use relation`：领域体、用神枢纽、处理对象、支持／损用、去处和日主能动性；
- `expression bands`：基线／受压／条件良好／反向或未显化；
- `manifestation layers`：内部机制／领域载体／外部结果／时间条件／反向代价；
- 3 至 6 条可由命主回答“符合／不符合／只在某条件下符合”的生活判断；
- `interpretive kernel`：主场景、次场景、切换场景与禁止渲染项；
- 最强替代解释与禁止渲染项。

不能只从十神标签跳故事，也不能只讲干支本象而漏掉十神和全局。A 带 B 的特性时，同时检查 B 如何承载或限制 A；但两者权重不要求相等。

full-reading 的四个基础 topic 必须分别拥有独立 finding 文件和稳定 topic ID：

- `family-home`：家庭系统、父母／家庭资源压力、家庭角色、居住和生活环境维持；不自动代替爱情或子女。
- `education-learning`：学习输入、理解与输出、考试资格、专业和教育路径。
- `wealth-resource`：资源、收入、积累、支出、流动性、可见度与变现。
- `career-work`：任务、岗位、组织环境、责任压力、职业发展与成果。

相同结构可跨 topic 引用，但必须说明领域体或体—用关系怎样改变了场景；若完全相同则交叉引用，不复制泛化段落。不得用一条“综合性格 finding”代替四个领域。每个 selected optional topic 也必须有独立 finding。

### Mode D：Finding 审计、显化映射与验证接口

先调用 `$bazi-finding-audit` 的 imagery-finding 模式。FAIL 必须退回对应 finding 或 source packet。

完整读取 [经历映射与流运验证协议](../bazi-structure-dynamics/references/validation-protocol.md)，再选择：

1. **不合参**：记录 `manifestation_mapping_state: none` 与 `validation_state: none`，直接进入 composition；
2. **显化映射**：审计后读取经历，产出 `manifestation-map.md`。可记录 matched／conditional／carrier-shift／disconfirmed／new-question／structural-challenge，但必须标 `non-evidentiary: true`；
3. **流运验证**：在读取相关年史前，基于冻结 natal、受审计 timing overlay 与 timing imagery 形成复杂假设，交 `$bazi-finding-audit` 审计并冻结。之后由 `$bazi-render` 收集 verbatim response，再按固定 rubric 生成 scorecard 并重审。

显化映射可以调优先级、语气和领域载体，不能创造新的结构、路线或普遍规则，也不能增加 confidence。验证结果只能评价冻结的时间假设，不反写 natal。

若用户拒绝或没有可回忆材料，记录 `declined`／`unscored` 并继续；不得补写“根据反馈验证”。若详细经历在 blind finding 或 timing hypothesis 冻结前已经进入生成上下文，须在 validation plan 排除／降权；无法隔离时记录 `contaminated` 并放弃验证资格，但可做显化映射。若仍把既有事实写入 finding 或声称盲验证，退回 `$bazi-finding-audit`。

### Mode E：Composition

只使用通过审计的 findings 与可选 manifestation map 产出 `composition.md`；没有 subject context 时明确记录“未做经历映射”，不得虚构验证结果。它负责：

- 全盘一句话主轴；
- 主问题、主要救应与日主能动性的生活化总框架；
- 各 topic 的 finding 顺序；
- 用神关系轴场景及其跨领域差异；
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
- use-kernel 缺失、Topic Lens 未锁定用神枢纽，或 primary axis 没有 axis scene／finding／deferred 收据：FAIL。
- 相关柱漏一天干、地支或任一藏干：FAIL。
- 同柱互染被当成 active edge：FAIL。
- 只列符号、不做组合：FAIL。
- 只讲局部而未做 full-chart sweep：FAIL。
- 把多条用神关系轴压成一条泛化机制 finding：FAIL。
- 完整取象来源缺失却写高置信生活故事：FAIL。
- 用户经历创造新 finding：FAIL。
- 经历在 blind findings 审计前参与生成，或年史在 timing hypotheses 冻结前参与验证命题：FAIL。
- 用一条 general finding 代替家庭、学业、财运、事业任一基础板块：FAIL。
- 行业名先于工作性质：退回改写。
- composition 压掉 finding 的条件、代价或反证：FAIL。

## 输出边界

本技能产出可供 Render 使用的分析材料，不直接替用户写最终报告。后续追问若进入新领域，允许增量重跑 Mode A 至 E；不得把首次报告误当成穷尽全部天干地支象意。
