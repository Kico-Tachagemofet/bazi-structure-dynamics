---
name: bazi-source-lookup
description: 为四柱八字建立可追溯的结构规则包与取象材料包：根据 chart-stage1、冻结结构、report-scope 与 Topic Lens 太极场，完整读取本盘相关十神、天干、地支、藏干及现实载体材料，再按专题编译可供十神链—干支组合分析的 runtime units；只有用户真实提出的问题才另登记问答证据。用于旺衰格局、刑冲合害墓库合化的原典取证，以及完整原局、专题、岁运或合盘的取象供料。本技能不代替结构裁决或生活判断，也不能用一套通用卡片冒充所有专题均已获得具体材料。
---

# 八字 Source Lookup

根据盘面触发项加载本轮真正需要的完整材料，产出可审计的 Source Packet。结构规则包与取象包分开；后续追问允许增量加载，不要求首次报告穷尽一个干支的全部象意。首次使用还须完整读取 [八字现实断语合同 v1.0](../bazi-structure-dynamics/references/semantic-verdict-contract.md)：Source 的职责不是替下游选职业，而是防止已经激活的动作、材料和载体候选在进入 Composition 前被收窄丢失。

## 必读输入

- case-manifest.yaml
- chart-stage1.yaml
- 待判断的问题或来自 Structure Core 的 source_queries
- 取象阶段另需 `use-kernel.md`、`report-scope.yaml`、`topic-lens-index.yaml` 与对应 `topic-lens-<slug>.json`
- timing／synastry 取象另需冻结 natal、`activation_interfaces`、受审计 overlay diff 与 overlay freeze receipt

缺少 Stage 1 时停止，先调用 $bazi-reader。

## 来源层

从现有总技能的 reference 库读取：

- 《千里命稿》原典与高保真整理：基础旺衰、干支、人元、刑冲合害、墓库等。
- 《子平真诠》原本：月令格局、成败救应、变化、纯杂、相神、生克先后。
- 徐乐吾评注：仅作为评注层，不能署为沈孝瞻原意。
- 若境清课程全文：干支和十神取象、课程扩展；不得倒灌成韦千里原文。
- 其他流派：单列规则，不与子平或韦千里静默混用。

总索引入口：

- ../bazi-structure-dynamics/references/source-index.md
- ../bazi-structure-dynamics/references/ziping-zhenquan-source-map.md
- ../bazi-structure-dynamics/references/ruojing-course-source-map.md
- ../bazi-structure-dynamics/references/source-ingestion-fidelity.md

Deep Card 入口：

- [Deep Card Schema](references/deep-card-schema.md)
- [Deep Card Index](references/deep-card-index.yaml)

Deep Card 是五行、十神、天干和地支的可推导语义底座，不是结构规则卡。它只在结构审计与冻结之后进入 `imagery`／`supplemental-imagery` packet。完整原局先按 `natal_chart_card_inventory` 一次性完整读取本盘实际出现且参与关系链的十神总卡、各透干卡、四支卡、重要藏干卡及地支共同底座；随后每个 topic 只编译与其太极场和十神链有关的 units。限定追问可以按 Lens 增量读取。结构 packet 不得读取 Deep Card，不得全库预热，也不得用模型记忆补写 `planned` 卡。

Source Lookup 是 Deep Card 母卡的唯一阅读者、选择者与权限登记者。对每张被 query 命中的相关卡先完整读取以避免断章取义，再生成 source-only `deep_card_manifest`，逐单元登记 `activated／context-only／forbidden／source-gap`、claim ceiling 与禁用升格；随后只把 activated 单元编译进 `deep-card-runtime-packet-<topic>.json`。Imagery Composition 只能读该编译包，Render 完全不读母卡或 runtime packet。

`cross_system_common_symbol` 只允许迁移去掉另一术数专属组件后仍成立、并能回接阴阳五行／季节／形态的共同符号层。奇门的宫、星、门、神、起局、合化口径和断验不能进入八字裁决。Deep Card 为 `draft_pending_human_review` 时，只能用于共同审稿和样板测试，不得自动进入客户 finding；状态为 `approved` 时，允许按本技能的结构冻结、Topic Lens 查询、逐单元白名单编译、Composition 桥接和 Finding Audit 流程进入正式客户解读。批准只解除草案门禁，不授予母卡直达结论、结构重算或单符号直断权限。

条件规则卡入口：

- [条件规则卡 Schema](references/rule-card-schema.md)
- [《千里命稿》首批高风险规则束](references/rule-registry-qianli-high-risk.json)
- [地支参与与显化规则束](references/rule-registry-branch-manifestation.json)

规则卡只用于定位、提醒适用边界和生成待裁候选。`pending_human_review` 卡不得自动决定节点、边、用神、topic 主轴或 finding；即使已人工批准，也必须回读原文范围和本盘关系后状态。按卡内 `pipeline_hooks` 记录本轮路由收据；Source Lookup 只执行 `route` 和来源范围 `guard`，不得提前执行 Structure Core 的 `decide`。

规则卡准入前先检查 [条件规则卡 Schema](references/rule-card-schema.md) 的准入门槛。十神名称与正偏关系属于 Reader 的确定性事实，不建立规则卡；单一十神的能力、利弊和命例先作为按需来源材料。只有完成同层全套对称审校，才可建设独立十神知识层。未完成全套时，不得让“伤官制杀必喜”“印星必护身”“财星必为财”等局部口诀进入运行时裁决。

## 路由规则

1. 先从 Stage 1 提取触发项：月令、司令、强弱争议、透藏、合冲刑害、墓库、重支、空亡、调候和岁运层。
2. 读取 Topic Lens v4.1 的 `taiji_field`、`coverage_facets`、`mandatory_judgment_dimensions`、`topic_process_axes`、`ten_god_chain_plan`、`stem_branch_anchor_plan` 与 `candidate_palette_requests`；只对 `explicit_reader_questions` 中有用户／scope 来源的真实问题读取 Reader Answer Contract。Source 查询由本盘 axis、现实端点与材料缺口形成，不由 coverage 数量或问答数量形成。
3. 对每个关键结构判断列 source_query_id，并回链 `axis_id／scene_kernel_handoff／coverage_facet_ids`；真实问题存在时再回链 `contract_id／closure_key／explanatory_obligation_targets`。若规则注册表已有相关卡，先读取其立论太极点、所答／未答问题、限定词、`pipeline_hooks`、运行依赖和交叉引用，再读取完整相关章节；不只读搜索命中的单句，也不把规则卡当原文替代品。来源只支持共通机制时，必须明确记录它尚未提供的十神链作用、干支限定、领域对象、载体或结果，不能以“已读十神／干支总卡”记为专题 complete。
4. 岁运／合盘 query 若涉及“原局不透后来怎样”，须同时读取原局 `activation_interfaces`、本轮 matched interface、overlay 重算范围与完整触发来源。只找到透清／会动字句而没有 overlay receipt 时，不得宣布当前激活。
   v3.1 另必须读取 `natal_route_retention`、`overlay_function_transition` 与共享节点分配；不得只因岁运透出便忽略原局仍在运行的主路，也不得用“原局有保护”绕过 before／after 通量。
5. 仅对已经引用有效 structure freeze 与 Topic Lens 的取象 query 读卡。full-reading 先执行 `natal_chart_card_inventory`：五行总卡、十神总卡、地支共同底座、本盘全部透干与四支卡，以及进入主链／竞争链的重要藏干卡均完整读取一次并留 receipt。随后按各 topic 的 `deep_card_queries` 编译；地支／藏干必须回接 `post-branch-node-ledger.branch_manifestation_handoffs`。每张相关卡完整读取后，按 query 的 unit classes、activation basis、carrier scope、claim ceiling、selection purpose、excluded unit classes 与 excluded uses 建立 source-only `deep_card_manifest`；记录版本、审阅状态、activated／context-only／forbidden／source-gap units、实际使用的 core process、`branch_manifestation_receipt` 与未采用 unit ID。地支卡另须核对 `static_hidden_stems` 与 Reader 一致、逐藏气 interface 覆盖完整，并把 `commander_sequence` 只作为月令气序候选；司令不得增删静态藏干或改写 qi_rank。timing／synastry 另分栏记录 natal／overlay visibility、匹配接口、重算收据、范围与失效条件；结构 query 跳过本步。
6. 把 activated units 编译为 `deep-card-runtime-packet-<topic>.json`：每个单元须注明它准备贡献给十神链的哪一环，或准备由哪一干、哪一支、哪一柱限定；不能只把通用卡原样摊进去。保留完成推导所需的语义、来源层、状态开关和禁用升格，但不转发母卡路径、全文、context-only／forbidden 语义正文。Source Lookup 只能给 `mechanism／candidate` 上限，不得预判 supported 以上等级。若 Topic Lens 有 `candidate_palette_requests／domain_carrier_requests`，必须建立 `candidate_palette`：把所有经本盘激活且与所请求 L2–L4 端点相容的性质、动作、材料、器械、场所与载体家族送入，而不是只转发 Lens 已想到的泛化家族；同时提供 `domain_carrier_leads`，均标 `candidate／not_a_finding`，不得给最终排名。
7. 单一天干、地支或十神卡不得独立把具体职业、岗位、身份或事件升到 `supported`。但单卡中已经激活的 L2 性质和 L3 动作／材料候选必须进入 palette，不能因为它不足以证明 L5 身份便被删除。每个现实载体须记录从 `core_process → chart_anchor → post_relation_state → topic_axis → candidate_carrier` 的桥接；复合领域载体另须有合格关系功能、位置／可见接口、完整路线、日主承载与现实结果 gates，并比较替代载体。没有桥接时保留候选，不定案；桥接充分时允许下游自然使用“更可能／偏向／常表现为”。
   timing／synastry 中的人物身份还须经 `overlay relation function → topic field → position／visibility → runtime role context → candidate person carrier`。十神总卡只能提供关系功能与多个人物候选；不得把劫财单定为同事，也不得把官杀单定为上司。命主当时位置未知时，runtime packet 必须保留有意义的替代候选，不为下游预选唯一答案。
8. 记录本轮实际读取的文件、章节或时间段、来源身份和版本。
9. 原典冲突时建立分流矩阵；不得私自拼成一条“综合古法”。
10. 缺少完整取象展开时标 SOURCE_GAP，禁止凭缩略口诀补故事。
11. full-reading 先按 `natal-core-lens-index.yaml` 为原局八章建立 structural／imagery source coverage，再按 topic-lens-index 分别生成 family-home、education-learning、wealth-resource、career-work 与全部 selected optional topics 的 imagery packet；逐条读取 `topic_process_axis` 的十神链、实际控制者／承载者、两端、去处、干支柱位、日主关系及适用治疗枢纽所需的完整 imagery units。每个 topic 必须有独立 `topic_material_coverage`；真实 Reader Answer Contract 存在时才另有 `question_source_coverage`。允许共享 natal full-read receipt，但每个 topic 的 activated units、组合目的和 carrier 增量必须独立；所有 topic 若得到完全相同的 runtime unit signature，须给出逐 topic 差异证明，否则视为通用包伪装覆盖。
12. 原局详批必须给藏干显化矩阵提供足够来源层：本气／人元资格、位置与透干接口、关系后状态、root support、environmental feed、direct action、timing interface 与 result gate 分别回链。Source gap 可以限制具体人物／物件／事件载体与断语强度，但不能让下游把“未透／透出”压成一个开关或跳过结构解释。
13. 用户要求逐年时，每个 annual scope atom 独立登记当年实际读取范围与 coverage；大运通用来源可共享 receipt，但不得用一个十年 packet 代替各年 interaction census 所需的关系规则与取象证据。

### Packet roles

- `structure`：旺衰、司令、格局、合冲刑害、墓库、通关和路线条件。
- `imagery`：本 topic 涉及的干、支、十神、柱位、藏干、身体、场所、动作和领域取象。
- `supplemental-imagery`：追问时为同一冻结结构补充首次未展开的象意。

取象包中的每个 `imagery_unit` 必须保留来源展开的层次、适用条件、正反表现和边界，不得只存一句“某干像什么”。同一材料里的例子不能升级为固定行业或事件。

## Source Packet 最低字段

按 [Source Packet schema](references/source-packet-schema.md) 输出：

- case、framework lock、question scope
- source query
- triggering chart facts
- files and exact sections read
- extracted decision rules
- 每条 decision rule 的 `taiji_of_source`、`applicable_taiji`、`question_answered`、`questions_not_answered`、保留限定词与作用维度；引用规则卡时另记 card ref 与人工复核状态
- 每张规则卡的 pipeline hook receipt：本轮允许的 hook、角色、依赖状态、禁用 hook 与原因
- provenance：原典／评注／课程／现代模型
- Deep Card source-only receipt 与 manifest：card ref、版本、审阅状态、full-read receipt、source layer、core process、state switches、topic axis、query ref、unit class、activated／context-only／forbidden／source-gap、claim ceiling 与 forbidden promotions；不在 Source 阶段裁 bridge rank
- full-reading 的 `natal_chart_card_inventory` 与每张本盘卡的完整读取收据；每个 topic 的 unit selection signature、十神链贡献、干支限定任务及 cross-topic delta
- `deep-card-runtime-packet-<topic>.json`：含 activated units、按 judgment dimensions 编译的开放 `candidate_palette` 与按 `domain_carrier_requests` 编译的 candidate leads；明确 raw card／context-only payload 未转发
- timing／synastry activation receipt：原局 interface ref、trigger source、matched status、重算起点、overlay diff／audit／freeze、natal／overlay visibility、`natal_route_retention`、`overlay_function_transition`、共享节点分配、持续范围与 expiry
- conflicts and unresolved gaps
- allowed claims and forbidden overreach
- packet role、imagery unit registry 与 deferred coverage
- full-reading 另记录 report-scope ref、topic slug、topic body、use pivot、relation axis IDs、baseline required 与 topic-lens ref
- 每个 topic 的 `topic_material_coverage`：覆盖 facets、axes、十神链环节、干支锚点、carrier 请求、强替代材料与 source gap
- 每个真实 Reader Answer Contract 的 `question_source_coverage`：自然语言问题、answer target、解释职责的 source/unit refs、领域特有增量、强替代材料与未回答部分

## 硬门槛

- 声称“原书说”但没有实际读取记录：FAIL。
- 用徐评代替沈孝瞻、用课程代替韦千里：FAIL。
- 用索引摘要或搜索片段代替完整取象卡：FAIL。
- 流派规则冲突但未分栏：BLOCKER。
- 引用原文而未记录立论太极点，或跨太极点使用却没有显式论证：视同没有合格读取记录。
- 把 `pending_human_review` 规则卡当成自动裁决，或把“往往／若／稍解”等限定词删成硬规则：BLOCKER。
- 用单一十神命例代替完整十神层，或从十神名称直接推出喜忌、起效、能力和事件：BLOCKER。
- 用 `planned` 或未审阅 Deep Card 自动生成客户 finding，或用模型记忆补齐缺卡：BLOCKER。
- 在 structure freeze 与 Topic Lens 之前加载 Deep Card，或让它进入结构 decision rules／Core 输入：BLOCKER。
- imagery packet 缺 `deep_card_manifest` 或有效 runtime packet：BLOCKER。
- Composition 打开 Deep Card 母卡、读取 runtime packet 未选中的 unit，或收到 raw card／context-only payload：BLOCKER。
- Render 打开 Deep Card 母卡、Source runtime packet 或 Source manifest：BLOCKER。
- 把 `context-only`／`forbidden` 单元升级为 finding、职业、人物、事件或提高 claim strength：BLOCKER。
- 地支／藏干取象缺地支共同底座或 `branch_manifestation_handoff`，把透藏、参与层、直接功能和外部结果压成同一结论：BLOCKER。
- 地支卡的静态藏干与 Reader 不一致、漏掉任一逐藏气 interface，或以司令时序改写静态藏干／qi_rank：BLOCKER。
- timing／synastry 把待时接口当当前激活、只因对方有同字便激活、触发后未重算作用边，或把 overlay visibility 回写 natal：BLOCKER。
- timing／synastry 未读原局主路剩余便判影响轻重，或从临时十神功能直达唯一人物身份：BLOCKER。
- 把奇门宫星门神、起局／合化／断验规则静默迁入八字，或让共同符号层参与旺衰格局用神裁决：BLOCKER。
- 把有效的形态／行业候选当作禁词全部删掉，或反过来无桥接写成命主唯一事实：FAIL。
- Source Lookup 越权执行 `decide`、忽略 `depends_on`，或把最终 Edge Map 当成本卡生成同一字段的前置输入：BLOCKER。
- full-reading 缺任一基础 topic 或已选专题的 imagery coverage registry：BLOCKER。
- full-reading 未完整读取本盘实际参与关系链的十神总卡、透干、四支和重要藏干卡，或没有 natal chart-card inventory receipt：BLOCKER。
- topic runtime packet 没有说明 unit 在十神链／干支组合中的贡献任务，或所有 topic 使用完全相同 unit signature 而没有逐题差异收据：BLOCKER。
- 专题要求判断六亲、同侪、职业、身份、疾病或事件，却没有 relational／symbol carrier 或 domain carrier 材料，随后仍允许下游写具体载体：BLOCKER。
- activated 卡存在与本专题 L2／L3 端点相容的性质、动作、材料或器械单元，却因不能单独证明 L5 身份而未进入 candidate palette：BLOCKER。
- Source 只返回 Lens 预先点名的泛化职业家族，没有对实际 activated units 做开放候选扫描：BLOCKER。
- detailed-natal 缺任一原局 core section 的 source coverage，或藏干显化矩阵所需来源层不齐：BLOCKER。
- requested annual year 缺独立 coverage registry，或被多年 general packet 代替：BLOCKER。
- Topic Lens v4.1 的真实 Reader Answer Contract 缺独立 `question_source_coverage`，任一解释职责既无证据也无 source-gap 收据，或用通用十神／干支卡声称已回答领域人物、事情与结果：BLOCKER。
- 为 coverage facet 自造问题，或在 Source 包中填写直接答案、最终角色排序、职业偏好或事件结果：BLOCKER。
- 本轮所需原文缺失：允许继续结构枚举，但相关结论上限为低置信度。

## 输出边界

结构阶段产出 `source-packet.md`；取象阶段产出 `imagery-source-packet-<topic>.md` 与 `deep-card-runtime-packet-<topic>.json`，追问可产对应 turn-id 增量包。可以整理证据和分歧，不得决定谁旺、谁可用、是否成局、格局最终成立或事件必然发生。

完成规则卡新增或修改后运行 `scripts/validate_rule_registry.py`。该脚本只校验 schema、原文行内容指纹、限定词和人工复核门禁，不执行命理裁决。

完成 Deep Card 索引、状态或样板文件修改后运行 `scripts/validate_deep_card_index.py`。该脚本检查卡数、家族分布、路径、来源文件、索引／母卡状态一致性、批准收据、runtime unit、地支四层合同、静态藏干逐气接口、司令分离与迁移登记；它不判断象意是否正确。`approved` 表示已由人工维护者授权按受控 runtime 使用，后续实盘发现问题仍应回到母卡修订并重跑验证。

完成 runtime packet 后运行 `scripts/validate_deep_card_runtime_packet.py <packet.json>`。该脚本检查单元白名单、claim ceiling、raw/context payload 防火墙与 Source／Composition／Render 权限，不判断象意内容是否正确。
