---
name: bazi-render
description: 在结构冻结后向求测者确认命盘中心与报告范围，强制完整原局覆盖家庭、学业、财运、事业，并把已审计的 composition 与 topic findings 写成不压缩原始象意、可由命主核验的中文解读；同时负责非证据性的经历显化映射、冻结后的流运验证回应收集和受约束追问。用户要求完整断盘、选择板块、生成报告、解释断语、把经历与原局对照、做准确性验证，或追问职业关系健康神秘学象意时使用。Render 只负责范围入口、回应收集与翻译，不得自行创造上游没有的结构、路线、finding、验证假设或事件结论。
---

# 八字解读与追问

本技能既是最终文字层，也是后续聊天入口。它允许问题越问越细，但不允许分析边界越聊越松。

## 必读规则

首次运行前完整读取：

- [Render Contract](references/render-contract.md)
- [Conversation Routing](references/conversation-routing.md)
- [Report Scope Schema](references/report-scope-schema.md)

涉及经历合参、校准或验证时另完整读取 [经历映射与流运验证协议](../bazi-structure-dynamics/references/validation-protocol.md)。

报告模式必须读取：

- `report-scope.yaml`；
- `use-kernel.md`；
- `composition.md` 及通过的 composition audit；
- 对应 `topic-findings/*.md`；
- `manifestation-map.md` 或标明 `non-evidentiary` 的 legacy `calibration-map.md`（若存在）；
- validation verdict、scorecard 与 score audit（若报告声称做过验证）；
- `topic-lens.md`；
- `structure-freeze-receipt.yaml`。

对话模式还读取：

- 用户当前原句；
- `conversation-state.yaml`（若存在）；
- 已交付报告或前一轮回答；
- Q&A Expansion Index。

## 四种模式

### Mode 0：Report Scope Intake

只在 natal 结构审计通过并冻结后、Topic Lens 之前运行。

1. 先告诉求测者：“全盘结构已经完成并冻结，下面才开始具体断局。”
2. 用自然语言确认默认是否以命主本人为中心；若不是，询问围绕谁、哪段关系或哪件事。这里只确认问题中心，不让求测者选择技术用神。
3. full-reading 固定列明家庭、学业、财运、事业四个基础板块，不让用户误以为必须四选一。
4. 询问是否增加感情、健康、神秘学、创作、人际、子女或任意自定义专题，以及每个专题的具体问题。
5. 确认只看原局还是涉及时间／合盘；后者只做范围标记并退回对应上游。
6. 按 [Report Scope Schema](references/report-scope-schema.md) 产出 `report-scope.yaml`，随后调用 `$bazi-topic-lens`。本模式不得输出任何生活断语。

若用户没有附加专题，记录 `selected_optional_sections: []` 后继续基础四板块；不得反复逼问。不得在此时索取可能污染后续盲 finding 或流运验证的详细经历。

### Mode A：完整报告

1. 以 `composition.md` 为总骨架，不重新综合结构。
2. 每条 finding 独立成节，不把数条 finding 压成概述。
3. 先读 finding 的 `topic body → use pivot → relation axis → interpretive kernel`，不得从 topic 标题自由发挥。
4. 每节按以下顺序完整展开：直接生活判断；领域体与用神在处理什么；原象／十神／柱位／藏干怎样组成该过程；谁生用、损用、占用或使其改道；做功后去向、日主能否启动／承接／停止；基线与切换条件；现实载体与外部成果条件；反向表现和边界。
5. 把技术词翻译成有起因、动作、对象、结果和开关的生活过程。八字术语可以出现，但首次出现须说明它在本盘具体做什么。
6. 每节逐条展开上游 3 至 6 条 verifiable judgments，不得把它们重新压成一个摘要句。
7. 先给领域性质，再给行业或现实例子；例子不能代替过程。
8. 调用 `$bazi-finding-audit` 的 render 模式；FAIL 必须重写。

full-reading 报告必须逐节覆盖 `family-home`、`education-learning`、`wealth-resource`、`career-work`，并覆盖 `selected_optional_sections` 的全部专题。四个基础板块可以互相引用，但不能合并成一段“综合性格”。

报告不需要假装穷尽每个天干地支的所有象意。结尾说明哪些方向已有结论、哪些可在追问时增量展开。

### Mode B：追问对话

先按 [Conversation Routing](references/conversation-routing.md) 产出最小 `qa-route.yaml`，再回答。路由只决定去哪一层，不自行产新 finding。

#### 可直接回答

若问题只是澄清已有 finding、比较已有表达带或询问已有技术依据，可直接渲染。回答只需覆盖当前问题，不必复述整份报告，但必须保留与答案有关的限制、代价和反证。

#### 需要增量取象

若结构锚点已存在，但用户问了首次报告未展开的象意或新领域：

1. 调用 `$bazi-topic-lens` 为当前问题定义领域体，从冻结 use-kernel 选择用神枢纽并建立增量关系轴；
2. 调用 `$bazi-source-lookup` 加载本轮完整 imagery units；
3. 调用 `$bazi-imagery-composition` 生成并审计增量 finding；
4. 写 `qa/<turn-id>/qa-composition.md`；
5. 再回答。

这正是“天干象意无法一次穷尽”的正常扩展路径。不得因首次报告没写便回答“盘里没有”。

### Mode C：Experience Mapping／Validation Intake

先根据上游状态二选一，不得混称：

#### C1：显化映射

只在相关 findings 已通过审计后运行。让命主自由说明经历，把原话写入独立 response 文件，再交给 `$bazi-imagery-composition` 生成 `manifestation-map.md`。它只能调整表达带、呈现顺序、措辞、领域载体或后续问题；必须标注 `non-evidentiary: true`，不得增加结构置信度。

家庭、职场、关系等都是候选载体。不得因为 finding 放在家庭章节，就把反馈限定为家庭场景；若同一机制实际主要落在职场，记录 carrier shift，不把它算成结构命中或失败。

#### C2：流运验证回应收集

只在 `timing-hypothesis-freeze-receipt.yaml` 有效且 hash 一致后运行：

1. 不改写、不扩充已冻结假设；
2. 默认只邀请用户回复整体或逐条“准／部分准／不准／记不清”，可自愿补一句；写 `timing-validation-quick-feedback.md`，标 `non-evidentiary`，不自动追问、不正式计分；
3. 同时用一句话说明：若用户想更细地定位时间、先后、机制和实际领域，可以说“展开验证”，不启用也不影响报告；
4. 只有用户明确选择详细模式后，才按一个时间窗一句自然问题请求自由叙事；允许“没有／记不清”，不抛多项填写清单；
5. 将详细模式的用户原话完整写入 `timing-validation-response.md`，另做 evidence extraction 时保留原文引用；
6. “说得通”或宽泛认同记 `indeterminate／non-discriminating`，不加分；记不清记 `unscored`；
7. 把足够详细的回应交给固定 rubric 生成 scorecard，再由 `$bazi-finding-audit` 审计。Render 不自行打圆场或修改假设。

详细模式中，只有评分所需的关键缺口才允许补一个短追问。禁止默认要求用户逐项填写“事件数量、月份、顺序、领域、返工”等表格。

若相关经历在假设冻结前已经进入生成上下文，须引用 `validation-plan.yaml` 的排除／降权处理；无法隔离时标 `contaminated`，不得声称盲验证。仍可继续做 C1 显化映射。

#### 必须退回上游

- 新的大运、流年、流月：退回 timing diff。
- 新的合盘、关系场或直接叠盘：退回 synastry overlay。
- 质疑旺衰、司令、格局、合化、开库、路线端点或主问题：退回 structure audit。
- 前后回答方向冲突：先做 contradiction audit，不得现场圆成“两种都对”。
- 完整取象来源缺失：补 Source Packet；补不到则明确 source gap。

## 经历、显化映射与验证

用户说“这很像我的经历”时：

- 先声明本轮属于显化映射还是已预注册验证；
- 显化映射把经历对应到已有 finding 的表达带或领域载体，并说明它不能证明结构；
- 验证只按冻结假设和固定 scorecard 说明支持、未支持或未计分的部分；
- 若经历提示新领域，开增量 Topic Lens；
- 若经历与 finding 相反，记录为 disconfirmed 或 structural challenge。

禁止用经历创造新的格局、路线或通用命理规则；禁止把“说得通”、通用关键词或事后换领域计作验证命中。

## 文字纪律

- 先给问题的直接答案，再展开形成过程。
- 每个回答先定位领域体与用神关系轴；找不到已有轴时不得用泛化十神故事补答。
- 不以“某十神所以某性格”结束；要把干支、柱位、藏干和全局条件合起来。
- 不把内部能力、现实载体、外部成果混成一层。
- 不把名声、注意力、资源和收入混成“财”。
- 不只写优势；同时给受压、良性、反向或未显化版本。
- 不把象意组合写成真实生克边。
- 医疗判断不替代诊断；神秘学取象不作为超自然本体论证明。

## 输出

报告模式：

- `report-scope.yaml`
- `reader/<NN>-<topic>.md`
- 可选汇总报告
- `render-audit.md`

范围／经历映射／验证模式：

- `report-scope.yaml`
- `manifestation-response.md` 与 `manifestation-map.md`（若运行显化映射）
- `timing-validation-quick-feedback.md`（默认低负担入口，非证据性）
- `timing-validation-response.md`（若已有有效假设冻结）
- `timing-validation-scorecard.md` 与 score audit（若完成验证）
- 拒绝、未验证、污染或未计分状态

对话模式：

- `qa/<turn-id>/qa-route.yaml`
- 必要时的增量 lens、source packet、finding、qa-composition
- `qa/<turn-id>/answer.md`
- 更新 `conversation-state.yaml`

`conversation-state.yaml` 只记录已答问题、引用的 finding、未决 source gap、当前 topic 和需回退事项；不得把用户叙述写成结构事实。

## 自查

正式报告运行 `scripts/check_render_coverage.py --scope report-scope.yaml`，同时检查 finding 与小节的一一覆盖、基础四板块和已选专题是否齐全。脚本只查机械完整性，不能代替 `$bazi-finding-audit` 的语义审计。
