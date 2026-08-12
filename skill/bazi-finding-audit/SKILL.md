---
name: bazi-finding-audit
description: 以独立检察官模式审计八字结构、十神—干支象核、领域 findings、composition、render、真实问题闭环、岁运、合盘及验证：既查冻结事实与路线，也查现实断局是否真的由完整十神链和干支柱位组合推出，是否回答了人、事、载体、结果与反转，而非用性格、建议、技术标签或泛化机制冒充。另专查 Lens 预写答案、跨专题通用包、硬编码 PASS、字数冒充语义、经历污染、报告压缩与交付越界。发现 BLOCKER 必须返工，生产者自报 PASS 不构成证据。
---

# 八字 Finding Audit

首次审计必须完整读取 [八字现实断语合同 v1.0](../bazi-structure-dynamics/references/semantic-verdict-contract.md) 与 [现实断语语义审计 v1.0](references/semantic-verdict-audit.md)。审计 scene kernel、finding 或完整报告时另完整读取 [象核 Agent 隔离生产协议 v1.0](../bazi-imagery-composition/references/scene-kernel-agent-protocol.md)。审计顺序固定为 `P0 现实断语 → A 程序完整性 → B 内容可靠性 → C 输出保真 → D 交付边界`。P0 FAIL 时，不得因其他层字段齐全而 PASS。

只审计，不替原分析补故事。依据固化产物逐项给出 PASS、PASS_WITH_WARNINGS 或 FAIL。

## 必需输入

结构审计至少读取：

- case-manifest.yaml
- chart-stage1.yaml 与 audit
- source-packet.md
- node-ledger.yaml
- interaction-census.yaml
- branch-relation-census.yaml
- branch-state.md
- post-branch-node-ledger.yaml
- qualified-edge-map.yaml
- system-state.md
- problem-state.yaml
- pattern-candidates.md
- route-candidates.yaml
- route-edge-endpoint-map.yaml
- conditions-matrix.md
- structure-kernel.md
- use-kernel.md
- structure-process-handoff.yaml

Topic、timing、synastry、composition 或 render 审计还必须读取对应上游文件。

验证假设或 scorecard 审计必须完整读取 [经历映射与流运验证协议](../bazi-structure-dynamics/references/validation-protocol.md)，并读取 validation plan、timing overlay audit／freeze、假设 audit／freeze、verbatim response 和 scorecard 中本阶段已存在的全部文件。

结构争议辨别审计另读取 `structural-ambiguity-register.yaml`、全部分支 edge／route／condition、per-branch blind findings 与 finding audit、ambiguity plan／hypotheses／audit／freeze、verbatim response、case overlay 与 overlay audit 中本阶段已存在的全部文件。

full-reading 的 topic／composition／render 审计另必须读取：

- `report-scope.yaml`；
- `natal-core-lens-index.yaml`、`natal-core-coverage-index.yaml` 与原局八章 findings；
- `hidden-manifestation-matrix.yaml` 与 `cross-topic-claim-registry.yaml`；
- `topic-lens-index.yaml` 与全部 per-topic lens；
- 全部 Topic Lens v4.1 太极场、coverage facets、mandatory judgment dimensions、axes、真实 Reader Answer Contracts（若有）、`coverage-receipt.json`、可选 `question-answer-map.yaml` 与相应 source coverage；
- 基础四板块和已选专题的 imagery coverage、source packets、findings；
- natal chart-card inventory、Source-only Deep Card manifests、通过验证的 runtime packets、`bazi-scene-kernels.yaml` 与 validator receipt、实际生成的 domain-carrier resolutions、resonance maps、自足 render-use envelopes 与 render-card receipt（运行到相应阶段时）；未生成 resonance map 时检查 `not-used` 收据；
- 命中复杂象核 Agent 协议时，读取无答案 `scene-kernel-jobs/<topic>/job-packet.json`、producer receipt、完整 material disposition ledger 与独立 auditor state；核对三者上下文隔离、输入 hash、实际读取路径和产物时间顺序。不得把 producer 自审或总 session 的修复说明当独立审计；
- render 阶段另读取 `coverage-render-receipt.json`、真实问题存在时的 `reader-answer-receipt.yaml` 与最终报告；receipt 的 `pending-independent-audit` 是正常输入，任何生产者自写 semantic PASS 均不得采信；
- manifestation mapping／validation state 与引用（若有）；若声称验证，检查最低产物集完整。

render 审计不得只读取作者自报的 audit state。必须先独立运行 delivery scan 与 coverage scan；真实 Reader Answer Contracts 存在时才运行 question-closure scan。任一 scan 有 BLOCKER 时审计结论只能 FAIL。机械 scan 之后仍须抽查正文语义：人物／事情／场景／结果是否具体，十神链与干支限定是否真正进入断语，不能以字段齐全、段落字数或 marker 数量替代语义。

## A 层：程序完整性

- Stage 1 是否 PASS 或明确 PARTIAL；
- 节点是否覆盖四干及全部逐位置藏干；
- 每一重复支是否保留独立节点；
- 关系枚举是否含合、冲、刑、自刑、害、破、方会、三合和共享支；
- `interaction-census.yaml` 是否逐项继承 Reader 的确定性关系枚举；是否把重复支与自刑分栏；是否只在辰辰、午午、酉酉、亥亥时登记自刑。出现卯卯、寅寅、子子、丑丑、巳巳、未未、申申或戌戌自刑，属于确定性结构事实 FAIL，不得因下游语义看似合理而放过；
- 地支关系是否从普通候选边中独立出来，并含全部 negative scan；
- Branch State 是否把裁决逐节点写入 Post-Branch Node Ledger；
- Post-Branch Node Ledger 是否覆盖全部原始节点；
- 每个地支位置是否有 `branch_manifestation_handoff`，并分开 field、qi、function 与 result handoff；
- hidden／latent／timing-only 节点是否有 activation interface 或明确的不适用收据；每个接口是否只预登记 trigger signature 与重算范围，而未写当前激活；
- Edge Map 是否只引用 post-branch state，而没有绕回 pre-branch availability；
- 每个结构结论能否追溯到 node／edge／source ID；
- Reader 已知司令是否被结构化记录；司令修正后是否重跑全部下游；
- route 是否只引用 Edge Map 的 edge ID，端点、action、layer 和 distance 是否完全继承；
- `structure-process-handoff.yaml` 是否逐 process 保留完整 route edge closure、旺衰承载、phase 先后、日主成本、治疗效果、剩余问题、回病与启动／停机；
- problem state 是否先于救应／出口；actual throughput、net effect 与 therapeutic priority 是否分开；
- use-kernel 是否在 Structure Kernel 之后生成，分开格局、病药／制化、扶身与调候口径，并只引用已存在的 node／edge／route／condition；
- 用神太极核是否把“最需要”与“当前可用”分开，并把同一节点的竞争用途拆成实际关系轴；
- conditions matrix 是否覆盖每条主路线；
- 本轮声称使用的原文是否出现在 Source Packet；
- 结构 Source Packet 与 Structure Core 输入中是否完全没有 Deep Card；Deep Card 是否只在有效 structure freeze 与 Topic Lens 之后进入 imagery packet；
- 每张实际读卡是否有 full-read receipt 与 activated／context-only／forbidden／source-gap source-only manifest；母卡是否只有 Source Lookup 读取；Composition 是否只读通过验证的 compiled runtime packet；Render 是否只读已审计 envelope，完全未读母卡、runtime packet 或 Source manifest；
- 每张参与裁决的规则卡是否为 `approved`、是否有 Source Packet hook receipt、是否只在声明 hook 写入允许字段；`depends_on` 是否先完成且无环；
- Edge Map 是否完整保留 2B.0–2B.6 qualification trace 与 rule application receipts，且没有用 final Edge Map 循环证明自身；
- structural ambiguity 是否只在来源、位置、力量与竞争均已穷尽后登记；每个分支是否有独立 edge／route／condition，且 structure freeze 是否同时保留全部分支；
- subject context 是否在结构审计前被隔离。
- full-reading 是否先交付启动说明，结构冻结后才生成 report-scope；
- report-scope 是否明确 chart owner、querent role、reading center、`report_depth`、原局八章、基础四板块与已选专题；
- blind findings 是否在相关详细经历进入生成上下文前完成；若声称流运验证，timing hypotheses 是否在对应年史进入前审计并冻结。
- timing／synastry 是否按 `report-scope → timing-scope-seed → overlay 重算／审计／freeze → canonical timing Topic Lens` 的顺序运行；scope seed 是否通过 v1.0 validator，且没有 canonical axis、finding handoff、Deep Card query 或人物载体结论；是否读取冻结 natal，逐项匹配 activation interface，重算受影响 branch／node／edge／route condition，并沿 process 依赖传播到下游 phase，产出 before／after、scope、expiry、overlay audit 与 freeze；
- overlay 是否逐个登记 `shared_node_competition`、`natal_route_retention` 与 `overlay_function_transition`：共享节点在原局路线和临时关系之间怎样分配，原局 route／phase／throughput 保留、降额、中断或转由备用路线承接，临时节点从 natal visibility／participation 变成何种 overlay function；
- 用户要求逐年时，是否每年有独立 scope atom、interaction census、overlay diff、primary axis、finding 与 render marker；大运总述是否错误替代逐年产物；
- `audit-state.json` 的 findings、summary 与 verdict 是否由同一机器状态计算；是否存在正文有 BLOCKER、末尾却手写为 0 的漂移；
- 方向改变的修复是否标 `re-derive` 并完成全部下游 propagation；
- `active-artifact-manifest.json` 是否把所有可路由下游文件标为 active／inactive，active 文件是否引用同一 freeze。
- Topic Lens 是否只登记领域、coverage、process、十神链计划与干支锚点，完全没有 `external_result_target／direct_answer／final_verdict／preferred_carrier` 等预写结论；任一下游答案若与 Lens 中预写文本同源复制，属于循环生产。
- Source、Finding、Composition 与 Render 的 producer／validator 是否真正独立；审计脚本是否硬编码 `personality_only = false`、预设 PASS、按正文长度或字符串存在判语义合格。生产脚本与审计脚本共同读取同一份预写答案，不构成独立证据。
- 是否按 Agent 隔离协议正确裁决强制调用：完整报告、多 process／多维度、载体竞争、timing／synastry、批量生产、runtime 大包、经历／预期答案污染时，是否由 fresh producer 生产并由另一 fresh auditor 验收；主 session 直接写断语、producer 继承历史、无法创建 agent 却继续均为 BLOCKER。
- job packet 是否只含冻结输入、范围和输出合同，没有 directional verdict、preferred carrier、known facts、用户纠错或预期答案；producer 实际读取集合是否严格等于 allowed inputs，是否触碰 forbidden inputs。
- runtime packet 全部 selected unit IDs 是否与 material disposition ledger 做集合等值比较；每个 unit 是否唯一处置为 `used／counterevidence／context-only／excluded-with-reason`，而不是只检查列表非空或相信 `all_chain_links_covered: true`。
- directional claim 是否引用实际 support／counterevidence unit IDs，正文能否由这些单位与 process、十神链、干支柱位组合共同推出；只挂 topic axis／process 总引用而没有材料级蕴含不构成通过。
- 是否存在 `selected_units[:N]`、固定 limit、TOPIC_CLAIMS／TIMING_CLAIMS、按 mandatory dimension 数组位置套句、先写 finding 后补 material receipt 等答案预写行为；任一命中为 P0 BLOCKER。
- full-reading 的 per-topic runtime packet signature 是否有真实差异；所有 topic 使用完全相同 selected units／carrier leads 且无逐 topic delta，不能因文件名不同视为独立材料。

任一缺失为 BLOCKER。

## B 层：内容可靠性

逐项扫描 [Audit checklist](references/audit-checklist.md)，重点包括：

- 有根是否被写成畅通；
- 字面相生是否忽略火熔、土埋、寒湿燥烈和下游承接；
- 合是否未经条件直接化；
- 冲是否直接开库；
- 藏干是否被同等冲出；
- 藏干存在、根气、直接做功和格用资格是否混为一层；
- 地支 visibility、参与层、direct-function 与 externalized-result 是否被压成“透／不透”一个开关；
- 当前不透是否被写成永不透清；反过来，activation interface 或 trigger match 是否被写成当前 direct-function；
- overlay 是否只翻转 active 而没有重新裁作用边，是否把临时 visibility 回写 natal，或把对方同字／同五行当自动激活；
- 无外部结果时，已经成立的场景、库存／根气、环境供给、内部功能或待时接口是否被抹掉；
- 同支藏干是否仅凭五行关系自动生成 active 边；
- 是否反向把所有未透藏干统一降为 weak／conditional，漏掉原典允许的人元作用、root support 或 environmental feed；
- 旬空降力是否被误写成“不自动开库”的原因；
- 自刑是否漏掉或被夸大；
- 方会、三合和共享支是否只按口诀裁决；
- 图上闭环是否被写成真实周流；
- 同一节点是否同时被多条路线重复占用；
- 是否只看日主而漏掉自治子系统；
- 是否把系统运行等同于日主受益或控制；
- 是否把 route／process 存在等同于 start gate 已开启，或把库存／自治流动等同于日主主动调用；
- process 是否遗漏路线起始、日主成本、通关或回病 edge；上游 capacity／allocation 改变后，下游是否缺重算或无影响继承收据；
- timing process diff 是否只有 `reallocated／re-evaluated` 等 trace，而没有 start gate、throughput、cost、therapeutic effect、residual problem、rebound 与 agency before／after；
- timing 是否用“原局有保护”或“流运一到原局就失效”代替共享节点分配与路线剩余量裁决；影响强弱、范围和恢复性是否有 before／after throughput、保留 phase、备用路线与 expiry 支撑；
- 是否把最强实际通道当成最佳救应，或把加重主问题的路线列为 outlet；
- 格局是否先定后证；
- 不同流派是否被混成一套；
- 用户经历、杯卦或灵体反馈是否被当成普遍规则证据。
- 月支本气、禄地、十二长生与当前司令是否被重复当成多份得令证据；
- 来源规则的立论太极点与引用太极点是否一致；
- 作用边是否把关系形式、目标形质实损、目标功能制抑与第三方保护混成一个“克”。
- 是否把十神身份直接写成固定吉凶、固定功能、用神资格或命主能力；同一十神的实际 edge、主问题净效果、代价旁路与反转条件是否完整。
- 是否把流运十神直接写成固定人物（如劫财＝同事、官杀＝上司），未先完成 `overlay relation function → topic field → runtime role context → candidate carrier`；命主当时职位／权限／可见度是否只用于人物载体与能动性分支，而未被反向用作结构证据或提升结构置信度；
- 是否让未经全套对称审校的单一十神卡改变运行结果，造成某十神被特殊优待或特殊限制。
- 是否按卡号或书页顺序替代 runtime 依赖顺序，或让 `pending_human_review` 卡改变结构字段；
- Deep Card 是否越权改变旺衰、合化、格局、用神、节点、边或路线；`planned`／未审阅卡是否被模型记忆补齐；
- 是否把单一天干、地支或十神卡直接升级成具体职业、岗位、正式身份或事件，而没有复合领域 gate 与载体竞争；
- 具体职业、岗位、正式身份、疾病或事件是否有通过验证的 `domain-carrier-resolution`；Source Lookup 是否只给 candidate leads，Composition 是否留下多层贡献与竞争收据；
- 是否把 `context-only／forbidden` 单元用于新增或提高 finding；
- `cross_system_common_symbol` 是否只保留共同符号层；奇门宫星门神、起局、奇门合化或断验规则是否静默迁入八字；

任一主结构错误为 BLOCKER；仅影响权重或表述者为 WARNING。

## C 层：输出保真

- topic finding 必须引用已审计结构路线；
- full-reading 是否分别覆盖 family-home、education-learning、wealth-resource、career-work；
- detailed-natal 是否先完整覆盖原局八章；生活专题是否错误冒充原局详批；
- selected optional topics 是否逐项有 lens、source、finding、composition 与 render；
- 每个 topic 是否有明确 taiji center，且技术中心由 Topic Lens 选择而非要求求测者自选十神；
- 常规对应星是否经过 `star_eligibility` 比较，实际控制者／承载者是否独立锁定，治疗枢纽是否只在适用问题中使用；
- 能力、强项、持续输出或外部成果是否通过 capability bridge，而非由节点有气直接升级；
- 每个 topic 是否分开领域体与用神枢纽；primary relation axis 是否引用完整 process／phase 并进入 process composition、axis scene 与至少一个 scene kernel／finding，或有明确 deferred／source-gap 收据；
- 取象覆盖是否包含相关柱的天干、地支、十神、柱位和全部藏干；
- Topic Lens v4.1 是否建立 taiji field、coverage facets、mandatory judgment dimensions、chart-driven axes、十神链计划与干支锚点；是否把 coverage facet 冒充用户问题、把问题数换算成 axis／finding 数，或预写现实结论；
- `deep_card_queries` 是否覆盖实际进入十神链的本盘干支与重要藏干，并限制 unit class／carrier scope／claim ceiling；full-reading 是否有 natal chart-card inventory；per-topic runtime packet 是否有可解释的 unit／carrier delta；
- 每个 primary scene kernel 是否先完整摊开 process、life effect matrix、十神链、透干、地支、藏干、柱位、形成期运势和开放 candidate palette，再逐项 intersect；是否按现实端点建立 claim kernels、完成 L1–L5 裁决后才合成主象、次象、反转象、未显化、独特细节与最强替代；
- 每个 primary scene kernel 的 runtime selected units 是否全量进入可复算 disposition ledger；validator 是否从 runtime packet 外部重建集合，而非让 producer 用布尔字段自证；每条 claim 的材料引用是否与 ledger disposition 一致。
- 十神链是否明确领域体、起点、传递、结果端、反馈、竞争用途、日主权限与反转门；天干是否限定显性动作，地支是否限定场景／根基／阻力／去处，藏干是否限定参与层，柱位是否限定人事范围；是否由单个十神或单个干支直断人物、职业、疾病或事件；
- findings 是否由 scene／claim kernels 生成而非由 coverage／问题表逐项填空；多个 axes 可以共享根因和散文主线，但学历、专业性质、技术动作、权责、名声、收入、变动、冲突与代价等不同现实端点是否被保留；相反分支是否拆开；
- `coverage-receipt.json` 是否覆盖全部 required facets，并能追到 scene kernel、finding 与正文 span；是否用一条 general finding 冒充多个领域；
- 只有真实显式问题是否进入 Reader Answer Contract；其 user／scope provenance、contract ID／closure key 是否在 source、finding、composition、render 连续传递；不存在真实问题时是否错误强造 question-answer map；
- 每个真实 complete／conditional closure 是否有直接答案及形成、成事、代价、结果门、切换和核验；是否只写性格、感受、处理方式或建议，却没有回答人事角色、怎样成事、结果如何；
- 同一 process 跨专题时是否写出柱位、十神链、对象、载体、条件或结果的真实增量；是否复制相同泛化段落冒充多个答案；
- 存在真实问题时，`question-answer-map.yaml` 是否唯一覆盖全部 contracts，每条 direct answer claim、解释职责与 Render obligation 是否可追踪；
- 地支／藏干 query 是否读取地支共同底座，并逐支提供可回链的 `branch_manifestation_receipt`；
- 是否逐层完成同柱双向着色，并明确其为 composition-only；
- 是否先完成旺衰承载 → 五行克应 → route／phase／agency，再形成十神链，最后由干支／藏干／柱位具体化；是否按 spread → intersect → differentiate → rank → synthesize 完成现实取象；是否把紫微式全库符号共振误作八字机制主轴，或反过来只剩抽象 process 而没有现实断语；
- 每条 finding 是否做 full-chart sweep、表达带和显化层，并保留领域体、用神做功、生用／损用、去处与日主能动性；
- 地支 finding 是否把场在／气在／用起／果显分栏；direct-function 是否另过领域载体与外部结果门；
- timing／synastry finding 是否保留 interface → trigger match → relation requalification → shared-node competition → natal route retention → process before／after → overlay relation function → topic carrier candidates → runtime role branches → impact bounds → result gate → expiry 全链，并分开 natal／overlay state；
- composition 不得加入 finding 没有的新判断，也不得压掉形成层次；
- 每条独立生活主张是否有稳定 judgment ID，并在 composition／render 唯一、完整展开；是否为凑固定数量拆成重复性格句，或出现 ID 齐全而正文只剩一句的伪覆盖；
- primary finding 是否有完整 process composition 与 render-use envelope；实际使用物象／载体竞争时是否另有 resonance map，未使用时是否有 `not-used` 收据；
- render 不得删掉关键原象、限制、代价和反证；
- Render 是否只读 locked claims、自足 envelope 与实际 resonance map，是否有声明 raw-card firewall 的 render-card receipt；是否未从排除 unit ID、Source manifest、runtime packet 或模型记忆捞回未激活载体；
- render 是否把每条主关系轴展开成有起因、动作、对象、结果和切换条件的生活过程，而非重新压成泛化机制；
- render 是否围绕 scene kernels 与人生主线展开，而没有把 coverage facets 写成“关于……结论是……”问答台账；真实 question marker 是否回答对象、事情与结果，性格和建议是否保持从属；
- finding／judgment markers 是否各有命主可核验的实质正文；多个 findings 沿同一象核合写时是否仍保留全部主张；可见目录是否服从 composition 主线，是否暴露固定审计栏位或用过量标题切碎因果链；
- timing finding 是否分开旧结构、共享节点占用、原局路线剩余量、临时关系功能、外部逼迫、命主能动、非命主可控结果、候选载体、runtime 位置分支、结构影响边界、旧结构不变的代价与下一窗口；
- 取象必须读取完整来源展开；
- 职业行业是否先推导性质，再给行业／岗位／任务／收入／可见度例子；
- 形貌、物件、行业或人物载体是否有 `core_process → chart_anchor → post_relation_state → topic_axis → candidate_carrier` 桥接；无桥接是否被定成唯一事实；桥接成立的有效候选是否反被过度防御删除；
- 表达强度是否与 candidate／supported／preferred／assertable 对齐；没有真实竞争锚点时是否用重复“但是／也可能不是”冲淡可核验判断；
- 显化映射是否明确 non-evidentiary，且只调整已有分支的表达带或领域载体；
- 验证是否先冻结复杂假设，逐条具备时间窗、顺序、路线机制、领域竞争和失败条件；
- scorecard 是否忠于 verbatim response，且没有给“说得通”、通用关键词、记不清或事后换领域加分；
- 已知先验是否登记并排除／降权，不完整时间窗是否保留 observation cutoff；
- quick feedback 是否明确 non-evidentiary、未进入正式计分，详细模式是否由用户主动启用且没有默认表格化追问；
- 完整报告交付是否把 `feedback_offer_state` 记为 offered／declined；是否错误因 `validation_mode: none` 静默省略核验入口；
- 结构争议的每个分支是否先有 blind finding 与失败条件；辨别问题是否在全部假设审计冻结后才提出，且第一问没有泄露“合／克／牵绊／压制”等分支关键词；
- case ambiguity overlay 是否忠于 verbatim response、登记 prior／exposure，只形成个案偏好，并保留未偏好分支；是否错误回写规则注册表或 natal 结构；

写作样章、自由发挥稿或“倒推规格”可以单独标记为 `reverse-spec-useful`／`style-prototype-pass`，但这不等于技术语义通过。凡样章与当前冻结结构、用神核、路线端点、节点资格或 overlay diff 冲突，semantic verdict 必须 FAIL，并明确“可借鉴其问题密度／叙事结构，禁止复用其命理判断”；不得用文风改善掩盖结构错误。
- 健康、精神和超自然断语必须标明边界，不替代现实诊断或本体论证明。

## D 层：报告入口与对话边界

对首次报告入口与 Q&A 额外检查：

- qa-route 是否先识别 clarification、new imagery、new domain、timing、synastry、structural challenge 或 contradiction；
- 直接回答是否确有已审计 finding 与完整 imagery unit；
- 新领域是否增量回到 Topic／Source／Imagery，而非 Render 自由发挥；
- Render 发现 envelope 外新象时是否登记 render-gap 并回退，而非现场补断；
- 新时间层、合盘接口或结构争议是否退回对应上游；
- 前后矛盾是否先审计；
- conversation state 是否把用户叙述误写成结构事实。
- 首次完整原局缺 report-scope 时是否错误 direct-render；
- 经历问题是否先分流为 manifestation mapping、quick feedback 或 preregistered validation；详细验证是否由用户主动启用；验证回应是否只在 hypothesis freeze 后收集；拒绝或记不清是否分别标 declined／unscored。
- 结构争议辨别是否先检查有效 ambiguity freeze 与双分支 blind findings；Render 是否只收原话而没有让命主自选术语、现场改假设或删除另一分支。

## 裁决

- 任一 BLOCKER：FAIL，列明应回退的阶段，修复后重审。
- 无 BLOCKER、有 WARNING：PASS_WITH_WARNINGS。
- 全部通过：PASS。

审计先按 [Audit State Schema v2](references/audit-state-schema.md) 产出 `audit-state.json`，再生成 Markdown 报告投影。结构审计 PASS 后产出 `structure-freeze-receipt.yaml`，记录所有结构输入、audit state 与报告的路径、hash、schema version。另按 [Active Artifact Manifest Schema](references/active-artifact-manifest-schema.md) 维护 active／inactive 下游图。任一结构文件改变或 active 文件引用其他 freeze 即失效。

机械检查优先运行：

- `scripts/validate_route_integrity.py`：从 Edge Map 展开路线端点，检查端点漂移、链条连续性与 aggravating／outlet 冲突。
- `scripts/validate_process_integrity.py`：检查 v4 process route closure、life-effect 四面裁决、phase／agency 完整性、timing 下游传播与 before／after；`legacy-overlay` 模式用于指出旧覆盖层的缺失传播。
- `scripts/validate_audit_state.py`：从 finding 状态计算 summary／verdict，拒绝方向变化后的 patch 与未传播修复。
- `scripts/make_structure_freeze.py`：只读取已验证 audit state，为必需结构文件生成 SHA-256 冻结收据；不接受手填 verdict。
- `scripts/validate_snapshot_integrity.py`：复核冻结 hashes，并拒绝 stale、mixed 或未分类的可路由下游文件。
- `scripts/validate_delivery_artifacts.py`：独立重扫原局八章、canonical findings、judgment、reader、receipt、报告范围与逐年文件；不得只相信审计员自报 0 issue。
- `scripts/validate_coverage_render_receipt.py`：独立核对 coverage receipt、最终报告不可见 coverage markers 与 render receipt；机械 PASS 后仍须语义抽查正文确实覆盖人事、场景、结果与边界。
- `../bazi-topic-lens/scripts/validate_taiji_field_lens.py`：拒绝 Lens 预写答案、synthetic questions、缺十神链计划或干支锚点的 axes。
- `../bazi-imagery-composition/scripts/validate_ten_god_stem_branch_kernel.py`：从 runtime packet 外部重算 selected unit 全集，检查逐 unit disposition、claim 材料回链、十神链、干支组合、关系合成与主／次／反转场景；须传 `--runtime-root`，并以 `--receipt-out` 保存机器收据。机械 PASS 仍不判断命理结论正确。
- `scripts/validate_topic_packet_diversity.py`：比较 full-reading 各 topic runtime packet 的 selected units 与 carrier leads；相同 signature 缺 cross-topic delta 或十神链贡献任务时拒绝通用包伪装专题材料。
- `scripts/validate_question_answer_closure.py`：只在存在真实 Reader Answer Contracts 时独立重扫 question-answer map、最终报告 question markers 与 reader-answer receipt；机械 PASS 后仍须人工审答案是否真正回答对象、事情与结果。

finding／composition／render 新审计使用 Audit State v2.1，并以 `--evidence-scan` 校验独立扫描结果。scan 为 FAIL 时禁止 force pass。

禁止 force pass。审计输出按 [Audit report schema](references/audit-report-schema.md) 生成，并对每个问题列：证据、影响、修复阶段、复验条件。
