---
name: bazi-render
description: 在结构冻结后确认命盘中心与报告范围，并把已审计的全盘 composition、十神—干支 scene kernels 与 topic findings 写成因果连续、少标题、可核验的中文断命散文；完整原局覆盖家庭、学业、财运、事业及加选专题，真实用户问题另做 reader-answer receipt。也负责非证据性的经历显化映射、冻结后的流运验证回应和受约束追问。Render 只负责范围入口、回应收集与语言组织，不得自行取象、补答案、创造结构路线 finding 或事件结论。
---

# 八字解读与追问

本技能既是最终文字层，也是后续聊天入口。它允许问题越问越细，但不允许分析边界越聊越松。

## 必读规则

首次运行前完整读取：

- [八字现实断语合同 v1.0](../bazi-structure-dynamics/references/semantic-verdict-contract.md)
- [Render Contract](references/render-contract.md)
- [Conversation Routing](references/conversation-routing.md)
- [Report Scope Schema](references/report-scope-schema.md)
- [八字反套话与可核验表达](references/anti-cliche-bazi.md)
- [完整原局详批 Schema](../bazi-imagery-composition/references/natal-detailed-reading-schema.md)
- [问题—答案闭环 Schema v2](../bazi-imagery-composition/references/question-answer-closure-schema.md)
- [Coverage Receipt Schema v1](../bazi-imagery-composition/references/coverage-receipt-schema.md)
- [合格详批散文 Few-shot](references/few-shot-detailed-natal-prose.md)
- [失败问答台账 Negative Few-shot](references/negative-few-shot-question-ledger.md)

涉及经历合参、校准或验证时另完整读取 [经历映射与流运验证协议](../bazi-structure-dynamics/references/validation-protocol.md)。

报告模式必须读取：

- `report-scope.yaml`；
- `use-kernel.md`；
- `composition.md` 及通过的 composition audit；
- `coverage-receipt.json` 及通过的 coverage audit；
- `bazi-scene-kernels.yaml` 与 validator PASS receipt；
- `question-answer-map.yaml` 及 question-closure audit（存在真实 Reader Answer Contracts 时）；
- 对应 `topic-findings/*.md`；
- 每条 finding 的 `process_composition`、自足 `render_use_envelope`，以及实际生成的可选 `resonance-map.yaml`；
- 具体职业、身份、疾病或事件实际进入结论时，对应的已审计 `domain-carrier-resolution-<topic>.json`；
- `manifestation-map.md` 或标明 `non-evidentiary` 的 legacy `calibration-map.md`（若存在）；
- validation verdict、scorecard 与 score audit（若报告声称做过验证）；
- `topic-lens.md`；
- `structure-freeze-receipt.yaml`。

`full-reading`／`detailed-natal` 还必须读取 `natal-core-lens-index.yaml`、`natal-core-coverage-index.yaml`、`hidden-manifestation-matrix.yaml`、`cross-topic-claim-registry.yaml` 与原局八章 findings。任一缺失时停止，不得用生活专题拼成“原局详批”。

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
3. full-reading 默认 `report_depth: detailed-natal`，先列明固定原局八章，再列家庭、学业、财运、事业四个基础板块，不让用户误以为必须四选一。只有用户明确要求简版时才可改为 summary，且不得称为详批。
4. 询问是否增加感情、健康、神秘学、创作、人际、子女或任意自定义专题；若用户有具体问题则原样记录，没有就只登记专题，不替用户编问题。
5. 确认只看原局还是涉及时间／合盘；后者只做范围标记并退回对应上游。
6. 按 [Report Scope Schema](references/report-scope-schema.md) 产出 `report-scope.yaml`，随后调用 `$bazi-topic-lens`。本模式不得输出任何生活断语。

若用户没有附加专题，记录 `selected_optional_sections: []` 后继续基础四板块；不得反复逼问。不得在此时索取可能污染后续盲 finding 或流运验证的详细经历。

### Mode A：完整报告

1. **先读 composition、scene kernels 与 coverage receipt。** composition 决定全盘主锚、关键人生主线、跨专题张力与回扣关系；scene kernels 提供已经合成完毕的十神链、干支场景、主象、次象和反转象；coverage receipt 保证没有漏断。真实问题存在时再读 question-answer map，保证相应 closure key 在正文唯一闭环。报告的开头、章节顺序和过渡服从叙事骨架，不按 finding、facet、问题或内部字段机械排队，也不在 Render 阶段重新取象。
2. **内容覆盖是硬约束，读者排版是软约束。** 原局 core、topic、finding、judgment 与 timing year 都保留唯一 HTML marker；可见标题只按读者真正需要辨认的全盘主线或重大生活问题设置。不得为了审计方便给每条 finding 加标题，也不得把内部字段名直接翻成“生活判断／条件与代价／技术依据”等固定栏位。多个相邻 findings 可以在同一个有意义的大章节中自然衔接，但每条 finding 的实质内容仍须完整出现一次。
   coverage facets、十神链环节、finding 和 formation／advantage／cost／result-gate／switch／verification 都是不可漏的内容角色，不是目录配额。正文应尽量让一条因果链在连续数段中走完，而不是每换一颗十神、一个 facet 或一个信息角色就起标题。
3. **先做不可见的 coverage 与判断清单，再写散文。** 逐 coverage receipt 锁定每个 facet 和 mandatory judgment dimension 将由哪条 claim／scene kernel、finding 与正文 span 覆盖；真实问题存在时才逐 closure key 锁定原问题、direct answer claim 与 Render obligation。再锁定各 finding 的独立 judgments、specificity verdicts、原象、限制、代价、反证、source gap 和 claim strength。markers 是追踪工具，不得成为句式或段落模板。
4. 先读 finding 的 `process composition → topic body → scene kernel → locked claims` 并锁定结论范围，再读取自足 `render_use_envelope`；若该 finding 实际生成 resonance map，再读取该图。不得打开 Deep Card 母卡、runtime packet、Source manifest，或从排除 unit ID 猜回未激活候选。
5. **围绕主场景铺开，因果链必须完整可见。** 每一专题先说清最主要的人事画面，再自然展开它如何由旺衰承载、完整五行 process、十神传递和干支柱位组合形成。学历层级、专业性质、技术动作、权责、名声、收入、变动和代价可以在少量连续段落中合成，但每项已锁定主张都必须明确出现，不能只剩综合性格或工作流程。只有真实用户问题需要 question marker；内部判断维度不得渲染成问答目录。
6. 允许用 envelope 已物化的过程、配对、比喻、状态和符号共振，把技术词翻译成有起因、动作、对象、结果和开关的生活过程。八字术语可以出现，但首次出现须说明它在本盘具体做什么；技术证据可在自然叙事中简述或在连贯章节末集中收束，详细映射由 marker 与 receipt 保存。若 envelope 语义不足，登记 render-gap 回退 Composition，不自行读卡。
7. **跨专题必须回扣同一根结构，并交代现实增量。** 当同一主锚同时进入家庭、学业、财运、事业或加选专题，后文应自然说明这是前文哪条十神链在不同柱位或领域体中的另一种落法，同时写出本领域新增的角色、对象、载体、条件和结果。若只是同一场景的延伸，交叉回扣而不复制泛化段落。
8. 高反差结构必须让读者清楚分辨各方来源、方向、竞争和结果；优先写成因果清楚的散文。只有表格、列表或 before／after diff 确实比正文更清楚时才使用，信号数量本身不强制特定版式。
9. 岁运 finding 必须先写原局仍在运行什么，再写外来干支新增哪种关系、是否争用原局主路节点、主路还剩多少，然后才写临时功能在本领域可能落成什么人、事或制度。process before／after 的 start gate、throughput、allocation、cost、therapeutic effect、residual problem、rebound 与 agency transition 必须保留；另分开旧结构、外部逼迫、命主能动、非命主可控结果、候选现实载体、runtime role branches、结构影响带与下一窗口。不得把“原局有保护”当安慰句，须落到仍成立的 edge／phase、剩余通量和备用路线。命主当时位置未知时保留条件分支，不把比劫直写成同事、官杀直写成上司。每个用户要求的流年都有独立 year marker、finding 与正文，但年份可用段首年份或自然过渡呈现。
10. `reader/` 文件是覆盖与交付单元，不决定汇总报告的可见目录。汇总时按 composition 主线排列原段落，每段只出现一次，不缩写、不删独立 judgment 或真实 question closure；完成并校验 `render-card-receipt.yaml`、`coverage-render-receipt.json`，真实问题存在时再生成 `reader-answer-receipt.yaml`。生产者 receipt 只能标 `pending-independent-audit`，随后运行独立交付扫描并调用 `$bazi-finding-audit`；任一语义或覆盖 FAIL 必须重写，Render 不得自判通过。

Render 的权限是“语言性综合”，不是“认识论重断”：只能展开 envelope 的 locked claims、selected unit IDs 与已物化语言材料，不得接触 context-only／forbidden 内容，不得新增 finding 中没有的人物、职业、物件、事件、结构或提高 claim strength。`render-card-receipt.yaml` 必须明确 `raw_card_access: forbidden`、`render_input_mode: audited-envelopes-only`、`raw_card_read: false`，并登记实际使用的 envelope、finding、judgment 与 selected unit IDs。

full-reading 报告必须逐节覆盖 `family-home`、`education-learning`、`wealth-resource`、`career-work`，并覆盖 `selected_optional_sections` 的全部专题。四个基础板块可以互相引用，但不能合并成一段“综合性格”。

报告交付末尾必须提供一次低负担 quick-feedback 邀请（整体或逐条回复“准／部分准／不准／记不清”，可自愿补一句，不自动追问、不计分），并将 `feedback_offer_state` 从 `pending` 更新为 `offered`；用户已经明确拒绝时记 `declined`。`validation_mode: none` 只表示没有正式验证资格，不能被用来跳过反馈邀请。

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

#### C3：结构争议辨别回应收集

只在 `structural-ambiguity-freeze-receipt.yaml` 有效、双分支 blind findings 已审计冻结且用户主动同意后运行：

1. 每次只问一个不含“合／克／牵绊／压制／哪一种更像”等分支词的自然问题，请用户自由讲述过程、先后、最终仍能继续者和明显转折；
2. 允许“没有／记不清／不想答”，分别记 `unscored／declined`，不得补成反证；
3. 把原话逐字写入 `structural-ambiguity-response.md`，Render 不自行映射、不打分、不改冻结假设；
4. 只有一个缺口会实质改变辨别结果时，才补一个短追问；禁止用术语让命主自选“合还是克”；
5. 交由独立流程生成并审计 `case-ambiguity-overlay.yaml`。Render 只能据 overlay 调整分支呈现顺序，必须同时保留未偏好的冻结分支与限制。

若 freeze 缺失、hash 不一致、命主已被展示完整分支而未登记 exposure，或任一分支尚未完成 blind finding，停止并退回上游。

#### 必须退回上游

- 新的大运、流年、流月：退回 timing diff。
- 新的合盘、关系场或直接叠盘：退回 synastry overlay。
- 质疑旺衰、司令、格局、合化、开库、路线端点或主问题：退回 structure audit。
- 前后回答方向冲突：先做 contradiction audit，不得现场圆成“两种都对”。
- 完整取象来源缺失：补 Source Packet；补不到则明确 source gap。
- 读卡时发现上游尚未组合的新象、载体或共振：登记 `render-gap`，增量退回 Topic／Source／Imagery；不得现场补断。

## 经历、显化映射与验证

用户说“这很像我的经历”时：

- 先声明本轮属于显化映射还是已预注册验证；
- 显化映射把经历对应到已有 finding 的表达带或领域载体，并说明它不能证明结构；
- 验证只按冻结假设和固定 scorecard 说明支持、未支持或未计分的部分；
- 若经历提示新领域，开增量 Topic Lens；
- 若经历与 finding 相反，记录为 disconfirmed 或 structural challenge。

禁止用经历创造新的格局、路线或通用命理规则；禁止把“说得通”、通用关键词或事后换领域计作验证命中。

## 文字纪律

- 完整报告先立主场景，再沿十神链和干支组合展开；只有真实追问或显式问题才要求在相应段落明确给直接答案。
- 每个专题先定位领域体、scene kernel 与用神关系轴；找不到已有 kernel 时不得用泛化十神故事补答。
- 不以“某十神所以某性格”结束；要把干支、柱位、藏干和全局条件合起来。
- 不把 coverage facets 渲染成问卷、答题册或重复“关于……结论是……”句式。
- 不把内部能力、现实载体、外部成果混成一层。
- 不把名声、注意力、资源和收入混成“财”。
- 不只写优势；同时给受压、良性、反向或未显化版本。
- 不把象意组合写成真实生克边。
- 不以“容器、压力、资源、调整、重构、被推动”等抽象词替代本盘中的节点、关系、动作主体、现实载体和结果边界；术语与比喻必须在同段落落回具体机制。
- Render 不得看到或打开卡片全文、runtime packet 与 Source manifest；不得从排除 unit ID 猜回候选或把 candidate 升格。
- 医疗判断不替代诊断；神秘学取象不作为超自然本体论证明。

## 输出

报告模式：

- `report-scope.yaml`
- `reader/<NN>-<topic>.md`
- `render-card-receipt.yaml`
- `coverage-render-receipt.json`
- `reader-answer-receipt.yaml`（存在真实问题时）
- 可选汇总报告
- `render-audit.md`

范围／经历映射／验证模式：

- `report-scope.yaml`
- `manifestation-response.md` 与 `manifestation-map.md`（若运行显化映射）
- `timing-validation-quick-feedback.md`（默认低负担入口，非证据性）
- `timing-validation-response.md`（若已有有效假设冻结）
- `timing-validation-scorecard.md` 与 score audit（若完成验证）
- `structural-ambiguity-response.md`、`case-ambiguity-overlay.yaml` 与 overlay audit（若完成结构争议辨别）
- 拒绝、未验证、污染或未计分状态

对话模式：

- `qa/<turn-id>/qa-route.yaml`
- 必要时的增量 lens、source packet、finding、qa-composition
- `qa/<turn-id>/answer.md`
- 更新 `conversation-state.yaml`

`conversation-state.yaml` 只记录已答问题、引用的 finding、未决 source gap、当前 topic 和需回退事项；不得把用户叙述写成结构事实。

## 自查

正式报告必须对 canonical findings 目录运行 `scripts/check_render_coverage.py <findings-dir> <report> --scope report-scope.yaml --receipt render-card-receipt.yaml`，并由独立 Audit 运行 `validate_coverage_render_receipt.py <coverage-receipt.json> <report> <coverage-render-receipt.json>`；只有真实 Reader Answer Contracts 存在时才运行 `validate_question_answer_closure.py`。同时检查原局八章、scene-kernel／judgment 实质正文、finding、基础四板块、已选专题与逐年 marker。不得把只含 finding ID 的汇总文件当 canonical findings 输入。机械检查不审标题数、固定栏位或段落数；随后再由 `$bazi-finding-audit` 独立运行交付扫描与语义审计，机械 PASS 不能替代语义审计，Render 也不得把自己生成的 receipt 写成 PASS。
