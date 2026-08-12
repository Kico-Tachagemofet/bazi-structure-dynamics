# 八字 Render Contract

## 四条输入通道

Render 同时读取：

1. **分析脊柱**：冻结 process handoff／timing process diff、已审计 process composition、finding、locked claims、claim strength 与边界，决定“能够说什么”；
2. **象核语境**：通过校验的 `bazi-scene-kernels.yaml`，决定十神链怎样由干支、藏干和柱位具体化为主场景、次场景与反转场景；
3. **覆盖闭环**：`coverage-receipt.json` 决定哪些原局与专题内容不能漏掉，但不决定标题、段落和问答格式；
4. **真实问题闭环**：仅在真实 Reader Answer Contracts 存在时读取 `question-answer-map.yaml`，决定相应问题的直接答案、对象与结果。

进入正文前先锁定分析脊柱，再读取 scene kernel 与 envelope。认识顺序固定为旺衰承载 → 五行克应 → route／phase／agency → 十神关系链 → 天干动作／地支场景／藏干层级／柱位 → 现实载体。Render 只改变叙事顺序与语言，不重复执行这个分析，不得打开 Deep Card 母卡、runtime packet 或 Source manifest，也不能重新决定结构、process state、载体、人物、职业、事件或提高结论强度。

## 报告骨架：硬覆盖，软排版

完整原局先读取 `report-scope.yaml`。`full-reading` 默认 `report_depth: detailed-natal`，必须先交付以下八个原局 core section，且每个 marker 只能出现一次：

```markdown
<!-- core_section_id: natal-facts-boundaries -->
<!-- core_section_id: natal-system-engine -->
<!-- core_section_id: natal-four-pillars -->
<!-- core_section_id: natal-hidden-manifestation -->
<!-- core_section_id: natal-relation-network -->
<!-- core_section_id: natal-ten-god-functions -->
<!-- core_section_id: natal-pattern-use-agency -->
<!-- core_section_id: natal-synthesis-tensions -->
```

这八个 core coverage unit 必须来自原局 core findings 与 composition，不能由家庭、事业等生活专题反向拼接。它们是内容覆盖单元，不等于必须向读者展示八个标题：marker 应放在实际展开该内容的段落之前，可以按 composition 的主线组合进少量连贯章节，但不能把八个 marker 堆在一起后只写一个总括段。

领域范围同样使用稳定 topic marker：

```markdown
<!-- topic_id: family-home -->
```

full-reading 必须且只能各出现一次：

- `family-home`
- `education-learning`
- `wealth-resource`
- `career-work`

`selected_optional_sections` 中每个 slug 也必须各有一个 topic marker。topic marker 证明范围已经进入正文，不强制它前面必须有同名标题。相关专题可以在同一条人生主线中相邻展开，也可以独立成章；由读者逻辑决定。限定问题报告可以不含基础四项，但标题与交付说明必须明确“限定问题分析”，并列出未覆盖板块。

### Composition 先决定目录

写正文前，先从 `composition.md` 提取：

- 全盘一句话或开篇 hook；
- 主问题、paradox 或最重要的结构锚；
- 几条关键人生主线及其先后；
- 哪些 topic 是同一根结构的不同落点；
- 哪些地方存在必须明说的张力、转折或反例。

可见目录围绕这些内容设置少量有意义的大标题。finding 数、judgment 数、core unit 数和 topic 数都不得直接换算成标题数。工作底稿中的字段名、审计标签和技术产物名默认不可见。

coverage facets 与 `explanatory_obligations` 是内容责任，不是版式模板。Render 必须在正文中完整处理每项 primary／supporting／cross-reference need，并保留“形成—成事—代价—结果门—切换—核验”的解释功能；但不得把这些字段逐项翻译成问题、标题、固定六段或重复栏位。相邻段落应承接同一十神—干支因果链，而不是每段重新从十神定义起笔。

### Reader Answer Contract 只服务真实问题

只有 `question-answer-map.yaml` 中真实来源的 complete／conditional closure 才在正文放一个 marker：

```markdown
<!-- question_id: QA-CAREER-01 -->
```

marker 后先出现本题 direct answer：谁／哪类角色、什么事／对象、主要落法、结果倾向与现实边界。随后可以跨数个自然段展开 formation、advantage、cost、result-gate、switch 与 verification；这些职责不构成六段或六个标题。

内部 coverage facet 不得生成 question marker，也不得渲染成“关于某项，结论是……”。它只需在自然叙事中被 coverage receipt 定位到一个或多个正文 span。

性格、感受与处理偏好只能解释命主如何参与这件事，不能代替事情本身；建议只能出现在直接答案之后。技术标签只说明依据，不能充当答案。若 question-answer map 标 source-gap／not-applicable，正文应直接说明为什么暂不下断或为什么不适用，不得填入安慰性建议。

Topic Lens 的 mandatory judgment dimensions 不是标题配额，但每一维的 directional verdict、not-applicable 或 source-gap 必须在正文有唯一 span。共享根因可以只完整解释一次；学历、专业性质、技术动作、资格／权责、名声、收入、变动、冲突和代价等不同现实端点不能被一条“擅长解决问题／承担责任”替代。L5 具体身份未锁定时，仍须完整写出 L1–L4 已审计判断。

多个 closure 可以共享一个可见章节，也可以共用一段结构形成说明，但每个 closure 的 direct answer 与 `domain_specific_delta` 必须可辨。若 map 指向 `shared_answer_ref`，完整答案只展开一次，交叉位置以自己的 marker、领域增量和自然回扣完成闭环；不得复制同一段泛化文字。

### Finding 与 judgment 是可追踪主张，不是正文块配额

每条 finding 保留唯一 marker，独立 judgments 在相关主张出现处保留 marker。多个 findings 可以沿同一 scene kernel 写成连续散文；不要求每个 finding 独占一段或一个完整正文块，但每项 locked claim 必须在全文唯一完整展开：

```markdown
<!-- finding_id: F-XXX-001 -->

<!-- judgment_id: J-F-XXX-001-01 -->
先给命主能够直接核验的判断，随后在同一段或相邻自然段说明：盘里由谁发动，作用落向谁，途中被谁承接、消耗或改道，最后在本领域变成什么结果；成立条件、代价与边界随因果自然写入。

<!-- judgment_id: J-F-XXX-001-02 -->
承接上文继续展开下一条判断，不重复起手，不另贴固定标签。
```

同一 finding 的每条独立 judgment 都使用 `judgment_id` marker，并在相关叙事位置唯一展开一次。marker 只负责追踪，不能把若干 marker 连续堆放，再由一个摘要句假装全部覆盖。

每条 finding 另须有对应 `render_use_envelope`：locked claims、runtime packet ref、selected unit IDs、领域载体 resolution refs、已物化的允许语言展开、排除 unit receipts、禁止新增结论与 `render_gap_route`。`render-card-receipt.yaml` 不再记录读卡，而是证明 `raw_card_access: forbidden`、`render_input_mode: audited-envelopes-only`、`raw_card_read: false`，并登记实际使用的 envelope、finding、judgment 与 selected unit IDs。

不设固定段数、句群数或“生活判断／条件与代价／技术依据”可见标签。简单 finding 可以一两个丰满自然段完成，复杂 finding 可以跨更多段；唯一标准是所有 judgment、形成机制、作用方向、现实落点、条件、代价和边界均已说清。若某一信息角色在上游明确为 `not-applicable`，正文可自然略过或在确有辨识价值时说明其不参与；不能用空泛的“有帮助／有压力”占位。

详细度以 scene kernel、finding 的 `render obligations` 与全部独立 judgments 是否实质保留为准，不以段落数、问题数或每条 finding 的固定 judgment 数验收。技术 ID、selected unit 和 confidence 的完整对应由 HTML marker 与 receipts 保存；不得让审计脚手架切碎正文。

## 高反差结构与逐年呈现

四个以上同五行节点、多组冲刑并发、一个节点多重占用、重要藏干显／不显对照等结构，必须让读者分辨节点来自哪里、十神身份是什么、旧关系是否仍在、本轮新增了什么、共享节点怎样竞争、现实上有哪些候选载体。默认优先用因果清楚的散文；只有矩阵、逐条列表或 before／after diff 能显著降低理解成本时才使用。信号数量只触发“必须讲清”，不触发某一种版式。只写“压力最大”“换容器”“结构调整”仍不算展开。

用户要求逐年时，每年必须有独立 marker：

```markdown
<!-- timing_year: 2027 -->
```

年度正文先覆盖 process before／after 中的 start gate、phase、throughput、allocation、daymaster cost、therapeutic effect、residual problem、rebound 与 agency transition，再覆盖 `old_structure_refs`、`external_forcing`、`non_controlled_outcome`、`candidate_carriers_ranked`、`new_container_requirements`、`failure_if_unchanged` 与 `next_window_transition`。若本轮触发原局隐伏／待时节点，还必须沿正文说明：原局该节点原先处于什么状态，本轮新增了什么关系，相关共享节点怎样被重新分配，原局路线还保留多少或由哪条备用路线承接，临时十神关系在本 topic 中承担什么功能，以及 overlay 退出后什么随之失效。不得把这些内部字段逐个做成可见小标题。年份可以作为段首引导语或简短年标，不要求每年叠加多级标题。这里的“容器”若使用，必须在同段落落到组织、合同、岗位、居住、关系制度、身体管理或其他已审计候选载体，不能单独成为结论。

“原局有保护／底子还在，所以问题不大”不是合格的影响边界。正文必须说出实际保留的 edge／route／phase、before／after throughput 或备用承接，以及临时占用影响的是哪一段；只有这些材料支持时，才能把影响写成局部、可恢复或不至于改写主轴。反过来也不得因一个流年／大运关系出现，直接宣告原局路线整体失效。

岁运十神先写关系功能，再写现实人物。比如职场中的劫财可以落为同事、协作者、竞争者或共同占用资源的人，只有 domain-carrier resolution 已结合 topic field 与当时职位／权限／可见度把候选收窄时，正文才可具体到某类人物。若 runtime position 未知，保留两个以上紧凑的条件分支；这些分支只改变人物载体与命主能动性，不得改写同一个冻结的结构差分。

## 一一覆盖

- 多条 finding 可以共享标题并沿同一 scene kernel 合写，但不得压成泛化概述；每条实质主张仍有唯一展开位置。
- 一个 primary relation axis 必须进入至少一个完整 scene kernel；supporting axis 可作修正层，但不得吞掉主轴。
- 同一 finding 可在别处交叉引用，但完整展开只保留一处，避免重复。
- finding 中的 mandatory imagery、conditions、costs、counterevidence、source gap 必须进入正文或明确的技术依据。
- finding 中的 topic body、use pivot、完整十神链、干支柱位组合、main／secondary／switch scene 必须进入正文。
- finding 的 process ref、完整 edge closure、phase 顺序、日主成本、治疗效果、剩余问题、回病与启动／停机不得删除。
- `do_not_render` 不得泄漏到正文。
- canonical findings 中每个 judgment ID 必须在正文恰好出现一次；只含 finding ID 的聚合索引不能作为 coverage 事实源。
- question-answer map 中每个真实 complete／conditional closure key 必须在正文恰好出现一次，并有可辨 direct answer；source-gap／not-applicable 也必须有唯一处置收据。coverage facets 不生成 question markers。
- 每个 closure 的 formation／advantage／cost／result-gate／switch／verification 必须在正文或明确 cross-ref 中可追踪；字段齐全但正文没有收束答案仍视为未闭环。
- 不得让性格、建议、技术标签或跨专题共通机制占据 direct answer 的位置。
- `reader/` 中的模块正文是覆盖与交付单元；汇总报告按 composition 主线重组连续叙事，但每个主张只出现一次，不得缩写或删除独立 judgment。

## 生活语言与术语

八字读者可能需要看见“壬寅、偏印、食神制杀”等术语，因此不采用紫微 Render 的术语全禁规则。要求是：

- 首次出现术语时立刻说明它在此盘承担什么功能；
- 不把术语本身当结论；
- 技术 ID 由 marker 与 receipt 保持完整；读者版只有在有助理解时才用低干扰依据说明，不强制每条 finding 显示技术行；
- 正文始终能由不熟悉完整模型的命主判断是否符合。
- 遵守 [八字反套话与可核验表达](anti-cliche-bazi.md)：抽象词、技术词和比喻必须落回本盘具体节点、动作主体、条件与现实载体。

## Confidence

- high：直接陈述，但仍保留适用条件。
- medium：使用“更容易／倾向于／在……时”。
- low：明确说证据不足，只给候选表现。
- gap：不产肯定断语；说明还缺哪份材料。

## 领域例子

职业、行业、关系角色或神秘学实践均先写性质，再写例子。不得把例子反过来当结构证据。

## Q&A 与完整报告的差别

- 完整报告要求 findings 一一展开。
- Q&A 只回答当前问题涉及的 findings，可引用而不重写无关章节。
- Q&A 若新增经审计 finding，应写入增量 composition 与 conversation state，供后续继续引用。
- Q&A 不得因追求即时性跳过必要的 Source、Topic 或 Audit 回退。
- Q&A 或报告发现 envelope 外的新象意，登记 `render-gap` 并退回增量 Topic／Source／Imagery；不能读卡或现场补 finding。

## 经历映射与验证边界

- 家庭、职场、关系等都只是领域载体；不得把 family-home 设为唯一或强制校准入口。
- 显化映射只能在 findings 审计后运行，只调整表达带、呈现顺序、措辞、领域载体或追问方向，并明确 `non-evidentiary`。
- 报告若声称验证，必须引用有效的 timing hypothesis freeze、verbatim response、scorecard 与 score audit；否则只能说“经历合参”或“显化映射”。
- 报告交付时默认邀请“准／部分准／不准／记不清”的 quick feedback，可自愿补一句；不自动追问、不计分。`feedback_offer_state` 必须记为 `offered` 或 `declined`，不能因 `validation_mode: none` 静默消失。详细验证必须由用户主动说“展开验证”等意图后启用。
- 详细模式每次只用一个自然问题处理一个时间窗，不把事件数量、月份、先后、领域和返工一次性列成必填表格。
- 流运回应以自由叙事为主，不用宽泛关键词和逐条认同制造命中；“说得通”不增加置信度。
- 用户不提供经历时写“未做经历映射／验证”，不得降低结构审计结论，也不得声称已经回验。

## Render Audit

至少检查：

- finding 覆盖是否一一对应；
- coverage receipt 是否逐 facet 指到有效 scene kernel、finding 与正文 span，而没有被改造成问答台账；
- 真实 Reader Answer Contracts 是否逐问题闭环：到底回答了谁／什么角色、什么事／对象、什么结果，direct answer 是否清楚；
- 每个 complete／conditional closure 是否有唯一 question marker、领域特有增量和六类职责正文；shared answer 是否只展开一次且各题增量仍清楚；
- 形成层次是否被压成十神标签；
- 是否真实使用十神关系链并由天干、地支、藏干与柱位具体化，还是只把一个抽象 process 改写成性格测试；
- 同柱互染是否双向且未伪造成作用边；
- 是否把领域体、用神做功、生用／损用、去处和日主能动性写成了完整过程；
- 是否把多条关系轴重新压成一个泛化机制；
- 藏干的可用条件是否保留；
- 全局修正、反向表现和最强替代解释是否保留；
- 行业是否先性质后例子；
- 经历是否被正确区分为显化映射或预注册验证；
- 对话是否发生 scope creep；
- 前后结论冲突时是否先审计。
- report-scope、基础四板块、已选专题与 topic markers 是否完整；
- 相关经历是否在 blind finding 或 timing hypothesis 冻结前污染生成；已知先验是否排除／降权。
- 是否只读取 finding、composition、自足 envelope 与实际 resonance map，并生成声明禁止 raw card access 的 render-card receipt。
- 是否从排除 unit receipt、Source manifest 或模型记忆捞回新人物、职业、物件、事件或提高 claim strength。
- 是否先把 process composition 说成完整生活过程；实际存在 resonance map 时，是否利用已组合内容解释所用物象，而非反过来让共振改写机制。
- detailed-natal 的原局八个 coverage unit、hidden manifestation matrix、scene kernels、judgment markers、每条 judgment 的实质正文与 reader 模块是否完整。
- 用户要求的每个流年是否有独立 year marker、finding 和旧结构／外部逼迫／本人能动／不可控结果四层。
- 高反差结构是否已经让来源、方向、竞争和结果可分辨；是否出现只有“容器／压力／调整”等抽象名词而没有本盘机制的段落。
- 可见目录是否由 composition 的主线组织；是否把 finding、judgment、技术字段或审计标签机械转换成标题，造成叙事碎裂。
- `render-card-receipt.yaml` 与 quick-feedback offer 状态是否存在并可核对。
- `coverage-render-receipt.json` 是否逐 facet 记录正文 span；存在真实问题时，`reader-answer-receipt.yaml` 是否逐 closure 记录唯一 marker、direct answer 与 body ref，且 audit status 仍为 `pending-independent-audit`，没有由 Render 自判 PASS。
