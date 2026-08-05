---
name: bazi-render
description: 在结构冻结后向求测者确认命盘中心与报告范围，强制完整原局覆盖家庭、学业、财运、事业，并把已审计的 composition 与 topic findings 写成不压缩原始象意、可由命主核验的中文解读；同时负责家庭盲 finding 后的校准入口和受约束追问。用户要求完整断盘、选择要看的板块、生成八字报告、解释断语、继续聊干支十神、把经历与原局对照、追问职业关系健康神秘学象意，或质疑前后判断时使用。Render 只负责范围入口、校准提问与翻译，不得自行创造上游没有的结构、路线、finding 或事件结论。
---

# 八字解读与追问

本技能既是最终文字层，也是后续聊天入口。它允许问题越问越细，但不允许分析边界越聊越松。

## 必读规则

首次运行前完整读取：

- [Render Contract](references/render-contract.md)
- [Conversation Routing](references/conversation-routing.md)
- [Report Scope Schema](references/report-scope-schema.md)

报告模式必须读取：

- `report-scope.yaml`；
- `composition.md` 及通过的 composition audit；
- 对应 `topic-findings/*.md`；
- `calibration-map.md`（若存在）；
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
2. 用自然语言确认默认是否以命主本人为中心；若不是，询问围绕谁、哪段关系或哪件事。
3. full-reading 固定列明家庭、学业、财运、事业四个基础板块，不让用户误以为必须四选一。
4. 询问是否增加感情、健康、神秘学、创作、人际、子女或任意自定义专题，以及每个专题的具体问题。
5. 确认只看原局还是涉及时间／合盘；后者只做范围标记并退回对应上游。
6. 按 [Report Scope Schema](references/report-scope-schema.md) 产出 `report-scope.yaml`，随后调用 `$bazi-topic-lens`。本模式不得输出任何生活断语。

若用户没有附加专题，记录 `selected_optional_sections: []` 后继续基础四板块；不得反复逼问。不得在此时索取详细家庭经历。

### Mode A：完整报告

1. 以 `composition.md` 为总骨架，不重新综合结构。
2. 每条 finding 独立成节，不把数条 finding 压成概述。
3. 保留原象、十神功能、柱位、同柱互染、藏干、全局修正、条件、代价和反证。
4. 把技术词翻译成生活过程；八字术语可以出现，但首次出现须说明它在本盘具体做什么。
5. 每节写可验证生活判断、条件与代价、inline 技术依据。
6. 先给领域性质，再给行业或现实例子。
7. 调用 `$bazi-finding-audit` 的 render 模式；FAIL 必须重写。

full-reading 报告必须逐节覆盖 `family-home`、`education-learning`、`wealth-resource`、`career-work`，并覆盖 `selected_optional_sections` 的全部专题。四个基础板块可以互相引用，但不能合并成一段“综合性格”。

报告不需要假装穷尽每个天干地支的所有象意。结尾说明哪些方向已有结论、哪些可在追问时增量展开。

### Mode B：追问对话

先按 [Conversation Routing](references/conversation-routing.md) 产出最小 `qa-route.yaml`，再回答。路由只决定去哪一层，不自行产新 finding。

#### 可直接回答

若问题只是澄清已有 finding、比较已有表达带或询问已有技术依据，可直接渲染。回答只需覆盖当前问题，不必复述整份报告，但必须保留与答案有关的限制、代价和反证。

#### 需要增量取象

若结构锚点已存在，但用户问了首次报告未展开的象意或新领域：

1. 调用 `$bazi-topic-lens` 生成增量 lens；
2. 调用 `$bazi-source-lookup` 加载本轮完整 imagery units；
3. 调用 `$bazi-imagery-composition` 生成并审计增量 finding；
4. 写 `qa/<turn-id>/qa-composition.md`；
5. 再回答。

这正是“天干象意无法一次穷尽”的正常扩展路径。不得因首次报告没写便回答“盘里没有”。

### Mode C：Family Calibration Gate

只在 `family-home` 的 blind findings 通过 imagery-finding audit 后运行：

1. 从已审计 finding 的 `verifiable judgments` 选取 2 至 6 条，不补充新判断；
2. 请命主逐条标记“符合／只在某条件下符合／不符合”，可补一句关键事实；
3. 将原始回应写入独立 `calibration-response-family.md` 或对应 context item，不回写 finding；
4. 用户拒绝或暂无回应时把 `family_calibration_state` 记为 `declined`／`uncalibrated`，继续报告，不得假装已验证；
5. 回应交给 `$bazi-imagery-composition` 生成 calibration map，再进入 composition。

家庭经历若在 blind finding 审计前已经进入当前上下文，优先改用新鲜隔离上下文生产 blind findings；做不到时标记 `contaminated`，不得把家庭板块当盲回验。若这些事实实际参与生成却仍声称 blind，则交给 `$bazi-finding-audit` 判 FAIL；不得用“我没有主动引用”代替隔离。

#### 必须退回上游

- 新的大运、流年、流月：退回 timing diff。
- 新的合盘、关系场或直接叠盘：退回 synastry overlay。
- 质疑旺衰、司令、格局、合化、开库、路线端点或主问题：退回 structure audit。
- 前后回答方向冲突：先做 contradiction audit，不得现场圆成“两种都对”。
- 完整取象来源缺失：补 Source Packet；补不到则明确 source gap。

## 经历与回验

用户说“这很像我的经历”时：

- 把经历映射到已有 finding 的表达带或领域载体；
- 说明它支持哪一部分、不能证明哪一部分；
- 若经历提示新领域，开增量 Topic Lens；
- 若经历与 finding 相反，记录为 disconfirmed 或 structural challenge。

禁止用回验创造新的格局、路线或通用命理规则。

## 文字纪律

- 先给问题的直接答案，再展开形成过程。
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

范围／校准模式：

- `report-scope.yaml`
- `family-calibration-prompt.md`
- `calibration-response-family.md` 或拒绝／未校准状态

对话模式：

- `qa/<turn-id>/qa-route.yaml`
- 必要时的增量 lens、source packet、finding、qa-composition
- `qa/<turn-id>/answer.md`
- 更新 `conversation-state.yaml`

`conversation-state.yaml` 只记录已答问题、引用的 finding、未决 source gap、当前 topic 和需回退事项；不得把用户叙述写成结构事实。

## 自查

正式报告运行 `scripts/check_render_coverage.py --scope report-scope.yaml`，同时检查 finding 与小节的一一覆盖、基础四板块和已选专题是否齐全。脚本只查机械完整性，不能代替 `$bazi-finding-audit` 的语义审计。
