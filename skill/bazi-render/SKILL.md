---
name: bazi-render
description: 把已审计的八字 composition 与 topic findings 写成不压缩原始象意、可由命主核验的中文解读，并以受约束的对话模式承接后续追问：识别问题所属领域和结构锚点，判断可直接解释、需要补取象、新开 Topic Lens、重算岁运合盘或退回结构审计。用户要求生成八字报告、解释某句断语、继续聊某干支十神、把经历与原局对照、追问职业关系健康神秘学象意，或质疑前后判断时使用。Render 可增量扩展象意，但不得自行创造上游没有的结构、路线或事件结论。
---

# 八字解读与追问

本技能既是最终文字层，也是后续聊天入口。它允许问题越问越细，但不允许分析边界越聊越松。

## 必读规则

首次运行前完整读取：

- [Render Contract](references/render-contract.md)
- [Conversation Routing](references/conversation-routing.md)

报告模式必须读取：

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

## 两种模式

### Mode A：完整报告

1. 以 `composition.md` 为总骨架，不重新综合结构。
2. 每条 finding 独立成节，不把数条 finding 压成概述。
3. 保留原象、十神功能、柱位、同柱互染、藏干、全局修正、条件、代价和反证。
4. 把技术词翻译成生活过程；八字术语可以出现，但首次出现须说明它在本盘具体做什么。
5. 每节写可验证生活判断、条件与代价、inline 技术依据。
6. 先给领域性质，再给行业或现实例子。
7. 调用 `$bazi-finding-audit` 的 render 模式；FAIL 必须重写。

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

- `reader/<NN>-<topic>.md`
- 可选汇总报告
- `render-audit.md`

对话模式：

- `qa/<turn-id>/qa-route.yaml`
- 必要时的增量 lens、source packet、finding、qa-composition
- `qa/<turn-id>/answer.md`
- 更新 `conversation-state.yaml`

`conversation-state.yaml` 只记录已答问题、引用的 finding、未决 source gap、当前 topic 和需回退事项；不得把用户叙述写成结构事实。

## 自查

正式报告运行 `scripts/check_render_coverage.py` 检查 finding 与小节的一一覆盖。脚本只查机械完整性，不能代替 `$bazi-finding-audit` 的语义审计。
