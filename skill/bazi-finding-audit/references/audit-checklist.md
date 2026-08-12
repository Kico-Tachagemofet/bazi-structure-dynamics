# 八字结构审计清单

## 目录

1. 输入与来源
2. 节点覆盖
3. 关系覆盖
4. 地支裁决
5. 传输与通关
6. 系统与格局
7. 领域、时间与合盘
8. 输出保真

## 1. 输入与来源

- 四柱、日主、月令、司令、旬空是否已核。
- 已有出生日期／节后日数或用户已给司令时，是否仍错误写 unknown；司令是否带 provenance、framework 与 offset。
- 时间或节气有跨界风险时是否保留候选盘。
- 十神是否由日干重算。
- 原典、评注、课程和现代模型是否分层。
- Deep Card 是否只在结构冻结与 Topic Lens 后由 Source Lookup 读取，而未混入结构规则包或 Structure Core 输入；母卡内容是否未进入 Composition／Render。
- `cross_system_common_symbol` 是否通过迁移门；奇门宫星门神、起局、奇门合化和断验是否被排除。
- 实际读取章节是否有收据。
- 每条 decision rule 是否记录 `taiji_of_source`、适用太极点、所答／未答问题与保留限定词。
- 引用处太极点是否与来源一致；不一致时是否有显式跨太极论证。
- `pending_human_review` 规则卡是否只作候选提醒，而未自动裁决命局。
- 用户经历和旧解读是否隔离。

## 2. 节点覆盖

- 四个天干是否逐位置记录。
- 每个地支全部藏干是否逐位置记录。
- 重复支中的重复藏干是否错误合并。
- 每个节点是否有支持证据与反证。
- 根、同类、余气是否混称为“有根”。
- 透出是否被误当成强。
- 藏而有力与藏而受困是否区分。

## 3. 关系覆盖

- 天干合、生、克是否全部枚举。
- 六冲、六合、刑、自刑、害、破是否全部枚举。
- 方会、三合、半合和共享支是否枚举。
- 同柱、紧邻、隔柱和遥隔是否区分。
- 中间节点是否阻断越干作用。
- 同一节点是否被多条路线重复满额使用。

## 4. 地支裁决

- 是否有独立 branch-relation-census，而不是把支局埋在普通五行候选边中。
- 三会、三合、半合／拱合、六合、六冲、刑、自刑、害、破、重复支是否逐类正扫与 negative scan。
- 候选组合与正式成局是否分开。
- 旺支、月令、完整度、紧贴、空亡、冲刑破损是否逐项判断。
- 方会、三合与六合竞争是否分流派裁决。
- 形式上的支局状态与残余功能是否分开。
- 冲是否被写成自动开库。
- 墓库冲是否先判断本气与土势。
- 被冲藏干是否逐个比较援军，而非同等冲出。
- 自刑是否漏掉；其权重是否超出来源规则。
- 是否把普通重复支误写成自刑。Reader 的确定性枚举是关系事实基线：辰辰、午午、酉酉、亥亥可同时具有 `repeated_branch` 与 `self_punishment`；其他同支重复只能登记 `repeated_branch`，不得新增自刑。
- 每张 Branch State 卡是否列出逐支、逐藏干的 effect manifest。
- 旬空造成的兑现度变化与“不自动开库”的流派规则是否分开判断。
- Post-Branch Node Ledger 是否覆盖全部原始节点，包括 unchanged 节点。
- 是否每个地支位置都有 `branch_manifestation_handoff`，分别列 field layer、逐藏干 qi layer、function layer 与 result handoff。
- 藏干存在、库存／根气、direct action、pattern eligibility 是否分层。
- 同支藏干是否被误作持续互相生克；若允许 direct action，是否有明确来源规则。
- 是否仅因“未透”便把得令本气、有原典人元依据或同气透出的藏干统一降为 conditional／weak。
- visibility 是否被直接等同于 participation 或 direct-action；透出／会局是否被写成自动得用，不透是否被写成没有实质参与。
- hidden／latent／timing-only 节点是否登记 activation interface 或不适用收据；接口是否含 trigger signature、重算起点、受影响结构与最强反条件。
- 当前不透是否被写成永不透清；接口中的 projected effect 是否被误写成原局当前作用。

## 5. 传输与通关

- 每条边是否引用 source／target 的 post-branch state。
- Edge Map 是否绕回原始 Node Ledger 恢复被合绊、受损、改道或潜伏的力量。
- direct-action gate 为 forbidden 的节点是否仍生成 active／weak 边。
- conditional gate 是否只生成 conditional／weak 边并保留补齐条件。
- direct-action、root-support、environmental-feed、branch-relation 与 composition-only 是否分层。
- 删除 direct-action 后，原有根气／环境供给是否被错误一并删除。
- 每条边是否检查上游可用量。
- 是否检查调候环境。
- 是否检查中间占用、合绊、争合、妒合。
- 是否检查下游承接。
- 每条克／制／合边是否分开关系形式、目标形质实损、目标功能制抑与第三方保护。
- 十神是否只作相对关系标签；每项实际功能是否有 node／edge，且在主问题锁定后分别记录净效果、代价旁路、反证与反转条件。
- 是否从单一十神名称或口诀直接推出固定喜忌、用神资格、稳定能力或事件。
- 是否存在未经同层全套审校却参与裁决的单一十神基础卡。
- 有根是否被直接写成泄秀顺畅。
- 相生是否忽略火熔、土埋、寒水不生木等条件。
- 五行齐全或图上闭合是否被写成完整周流。
- 每条路线是否列最弱环。
- 药是否经旁路重新生病。

## 6. 系统与格局

- 身强身弱是否在节点和边之后才判断。
- 是否区分库存、吞吐和蓄积。
- 是否寻找自治子系统。
- 是否区分系统运行、日主受益、日主启动和日主停机。
- 格局是否先列候选再定案。
- 成败救应、太过不及、清杂、变化、相神和生克先后是否覆盖。
- 不同流派是否使用各自矩阵。
- 唯一格名是否在有 BLOCKER 时被提前宣布。
- 主问题是否在路线评价前单独锁定，并有证据、反证与改判条件。
- route 是否只存 edge refs；source、target、action、layer、distance 是否由 Edge Map 唯一展开。
- actual throughput、net effect on primary problem、therapeutic priority 与 realization rank 是否分开。
- aggravating route 是否误入 rescue／outlet 排名。
- conditions matrix 是否列必要先后、触发节点与反转节点。
- structure freeze 是否覆盖全部上游结构文件；下游是否引用同一版本。
- audit state 的 BLOCKER／WARNING 计数和 verdict 是否机械一致；方向改变的修复是否重推全部下游。
- active artifact manifest 是否把全部可路由文件标为 active／inactive，且 active 文件只引用当前 freeze。
- use-kernel 是否在主问题、路线和 Structure Kernel 之后生成，并与其他结构文件一起冻结。
- 格局用神、病药／制化主用、扶身辅用和调候需要是否分开；“最需要”与“当前最能用”是否分栏。
- 同一节点若分别制病、被损或经旁路回病，是否拆成不同实际关系轴并记录竞争分配。

## 7. 领域、时间与合盘

- 是否先完整执行 `references/semantic-verdict-audit.md` 的 P0 语义门；P0 FAIL 时是否仍被程序字段判 PASS。
- 每个宽专题的 mandatory judgment dimensions 是否逐项得到 directional verdict、not-applicable 或 source-gap；是否有现实端点被 mega-kernel 静默吞并。
- process 是否分开日主承载、客观产出、社会兑现与持续代价；是否把 aggravating／therapeutic 直接翻译成外部成就低／高。

- 完整原局是否有 report-scope、命盘主人、求测者关系和 reading center。
- full-reading 是否分别覆盖家庭、学业、财运、事业四个基础板块。
- full-reading 是否声明 `report_depth`；detailed-natal 是否在生活专题前分别覆盖原局八章，并有 natal-core lens／coverage index。
- 求测者加选专题是否全部进入 Topic／Source／Imagery／Render。
- 每个 topic 是否分开自然语言领域体与冻结的用神枢纽；是否错误地要求普通用户自选十神／柱位／用神。
- Topic Lens 是否只生成 Deep Card query 而未读取卡片内容；query 是否由冻结轴端点、相关柱、藏干和问题中心触发，并登记 unit classes、activation basis、carrier scope、claim ceiling、selection purpose、excluded classes／uses 与 `raw_card_access_requested: false`；具体职业／身份／事件是否改走 domain carrier request。
- Topic 前五项冻结事实快照是否分开月支本气、当前司令与季节阶段，并记录透干、主支场、日主根／调用、常规星关系后去处。
- 常规对应星是否有 `star_eligibility`；不具资格时是否允许实际控制者／承载者替代主轴。
- 描述／能力／结果问题是否被强行塞入治疗枢纽；治疗问题是否只引用冻结 use-kernel。
- 能力与外部结果是否完成 potential → daymaster access → visibility → sustainability → destination → external result 的适用 gate 检查。
- 每条 primary 体—用关系轴是否有 axis scene 与 finding，或明确的 deferred／source-gap 收据。
- Topic Lens v4.1 是否把 coverage facets、mandatory judgment dimensions 与真实用户问题分开；axes 是否由冻结 process、十神链计划与干支锚点形成，而非由 facet／问题数量形成；Lens 是否出现预写答案或载体排序；不同现实结果端点、四柱、重要藏干、大运段或多个流年是否被静默合并。
- `bazi-scene-kernels.yaml` 是否完整摊开十神链、透干、地支、藏干、柱位与竞争载体，并做关系合成；是否只有 process 摘要、性格画像或单星／单字直断。
- full-reading 的 per-topic runtime unit signatures 是否有真实差异；完全相同的通用包是否被改文件名后冒充专题材料。
- Source Lookup 是否完整读相关卡并建立 source-only activated／context-only／forbidden／source-gap manifest；是否另产通过验证的 compiled runtime packet，只转发 selected units；Composition 是否没有打开母卡；Render 是否没有读取母卡、runtime packet 或 Source manifest。
- blind finding 是否先于相关详细经历生成并审计。
- 家庭、职场、关系等是否被当作竞争载体，而非把家庭设成唯一强制校准锚点。
- 显化映射是否明确 `non-evidentiary`，只调整表达带、领域载体或后续问题，未回写结构或提高 confidence。
- 具体取象是否引用已审计路线。
- 内部机制、领域载体和外部结果是否区分。
- 涉及地支／藏干时，Source Packet 与 finding 是否都有 `branch_manifestation_receipt`；场在、气在、用起、果显是否分栏且可回链。
- 没有 externalized-result 时，field-background、stock-root-support、environmental-feed、internal-latent、direct-function、timing-pending 中实际成立者是否仍被保留。
- direct-function 是否被错误升级成外部成果；环境题是否错误要求藏干先透，才允许地支场成为现实载体。
- 岁运是否按 `report-scope → timing-scope-seed → overlay 重算／审计／freeze → canonical timing Topic Lens` 运行，而非在 overlay 前伪造依赖 overlay diff 的 canonical lens；scope seed 是否通过 v1.0 validator，且只含 atoms、自然语言问题、领域与 activation interfaces，没有正式轴、finding、Deep Card query 或人物载体；岁运是否以前后差分表达，而非重写原局。
- 用户要求逐年时，每个流年是否有独立 scope atom、全量 interaction census、overlay diff、primary axis 与 finding；大运综述是否错误替代逐年重算。
- 同一年度出现四个以上同五行节点、多组冲刑并发或共享节点多重占用时，是否完整保留旧关系、枚举新增关系与竞争，而不是笼统说“某五行最旺／换容器”。
- 岁运／合盘是否先匹配原局 activation interface；trigger match 后是否从登记起点重裁支局、节点、竞争分配、作用边与路线条件，而非只翻转 active。
- overlay 是否逐项产出 `shared_node_competition`、`natal_route_retention` 与 `overlay_function_transition`；是否比较受影响原局 route／phase／throughput 的 before／after，记录保留、降额、中断、备用承接与 expiry，而非只说“原局有保护”或“流运盖过原局”。
- 临时十神是否先经 `overlay relation function → topic field → runtime role context → candidate carrier` 才落到人物；命主当时职位／权限／可见度未知时是否保留至少两个条件分支；runtime context 是否只改变人物载体与能动性，而未改写结构 diff 或提升结构置信度。
- `natal_visibility` 与 `overlay_visibility` 是否分栏；覆盖层是否有持续方式、scope 与 expiry，结束后是否仍错误沿用临时状态。
- 合盘是否只因对方盘有同字／同五行便自动激活；是否检查双方 natal freeze、跨盘关系形式与本题相关性。
- 若声称流运验证，是否先有 validation plan、受审计 timing overlay、复杂假设、hypothesis audit 与 freeze，随后才读取年史。
- 每条验证假设是否包含时间窗／对照、事件顺序、路线机制、有限的领域排序、失败条件和 observation cutoff。
- 已知经历或先验是否登记并排除／降权；已知领域的 domain hit 是否按协议限分。
- verbatim response 是否独立保存；evidence extraction 与 scorecard 是否未改写用户原话。
- 默认入口是否允许只答准／部分准／不准／记不清；quick feedback 是否标 non-evidentiary、没有被计分或触发自动追问。
- 详细模式是否由用户主动启用；是否避免把事件数量、月份、顺序、领域、返工等字段一次性全部丢给用户填写。
- “说得通”、宽泛关键词、单一领域命中或记不清是否被错误加分；缺失历史是否正确标 `unscored`。
- 冻结后假设是否被改写、扩充领域或更换机制以贴合回应。
- 双盘是否分别审计。
- 跨盘节点是否被错误写成本命永久根。
- 直接叠盘是否标为案例前提。
- 关系内部场与外部职业场是否混为一谈。
- 健康和超自然断语是否越过证据边界。

## 8. 输出保真

- 学业是否判断学历／认证层级、专业训练与形成期兑现，而不只写学习方式。
- 事业是否判断专业性质、核心动作／材料、资格／权责、名声、收入、变动与冲突，而不只写流程、责任和收尾。
- L1–L3 是否因 L5 具体职业／身份无法确定而被过度删除；L4 是否比较最多三个有差异的候选家族。
- 形成期财、官杀、印、食伤是否比较供给型教育、单位培养、实习／临床／学徒、边学边做与正式任职，避免学习／工作虚假二分。

- 每个判断是否能追溯到 node、edge、route 和 source。
- 反证、限制、条件是否在最终文字中保留。
- render 是否添加上游没有的新断语。
- 完整取象是否被压缩到丢失关键分支。
- 经历显化映射与证据验证是否分开；两者均未篡改普遍规则或 natal 结构。
- 杯卦、灵体反馈是否只作待检假设提示或非证据性显化映射，而未冒充八字结构／流运验证。
- 相关柱是否合成天干本象、十神、柱位、地支、全部藏干与同柱双向着色。
- 同柱互染是否被误写成 active 生克边。
- 每条 finding 是否有 full-chart sweep、基线／受压／良性／反向表达带。
- 每条独立可核对生活主张是否有稳定 judgment ID，并在 composition 与 render 中唯一展开；是否为凑固定数量拆成重复性格句，或发生“ID 在、内容不在”的伪覆盖。
- 每条 finding 是否能回溯到一个具体领域体、用神枢纽和主关系轴；是否完整保留生用、损用、去处和日主能动性。
- 每条主 finding 是否有完整 process composition 与 render-use envelope；实际使用物象／载体竞争时是否保留 resonance map，未使用时是否有 `not-used` 收据；是否锁定 cards、units、claim strength、允许语言展开和禁止新增结论。
- render 是否把主关系轴展开为起因、动作、对象、结果和切换条件，而非重复“压力、支持、资源、输出”等泛化总结。
- 每个 render finding marker 后是否有完整 claim body，每个 judgment marker 后是否有足够的命主可核验正文；是否为了审计把 finding、字段或固定标签机械做成标题。高反差结构是否已讲清来源、方向、竞争与结果；表格／列表／before-after diff 只在比散文更清楚时使用。
- timing render 是否分开旧结构、共享节点占用、原局路线剩余量、临时关系功能、外部逼迫、命主能动、非命主可控结果、候选载体、runtime position 分支、结构影响边界、结构不变代价与下一窗口。
- Render 是否只读取 finding、composition、自足 envelope 与实际 resonance map，是否有声明 `raw_card_access: forbidden／raw_card_read: false` 的 render-card receipt；是否从排除 unit ID、Source manifest、runtime packet或模型记忆捞回新人物、职业、物件、事件或提高 claim strength。
- 内部机制、领域载体、外部结果、时间条件和反向代价是否齐全。
- 行业与现实例子是否先由工作性质推导，且区分岗位、任务、收入、可见度和名声。
- 具体职业、岗位、正式身份或事件是否错误地由单张天干／地支／十神卡升为 supported，而没有复合领域 gates 与竞争载体比较。
- 具体职业、岗位、正式身份、疾病或事件是否缺 `domain-carrier-resolution`，或该 resolution 没有过程／工作性质、关系功能、位置／可见接口或路线、独立锚点与替代载体比较。
- 每个外形、物件、行业或人物载体是否有 core process、chart anchor、关系后状态、topic axis 与 carrier rank；桥接充分的候选是否被错误当成禁词。
- 没有真实竞争锚点、状态切换、来源冲突或 source gap 时，是否用机械“但是／也不一定”把 supported／preferred 判断冲淡。
- 对话追问是否先路由；新象意是否增量走 Topic／Source／Imagery；新结构是否退回 Core。
- 只有 structure kernel 的交付是否被误称为“完整断局”。
- report-scope 的 mandatory 与 selected topics 是否各有唯一 topic marker。
- report-scope 的八个 natal core sections 是否各有唯一 core marker；每个 requested annual year 是否有唯一 year marker。
- render-card receipt 是否覆盖全部 finding 与 judgment；报告交付的 feedback offer 状态是否为 offered／declined。
- 是否独立运行 delivery evidence scan 与 question-closure evidence scan；任一 scan 为 FAIL 时 audit state 是否仍错误自报 PASS。

## 问题—答案闭环专项

逐 Reader Answer Contract 审，不按 topic 篇幅、finding 数或字段数量抽象打包：

- `exact_reader_question` 是否是命主会问的具体自然语言问题，而非 facet ID、topic 名、英文 slug、`完整回答<facet>` 或内部任务说明；
- `answer_target` 是否明确谁／哪类角色、什么事／对象、要判断什么落法或结果；
- source packet 是否逐 contract 覆盖 formation／advantage／cost／result-gate／switch／verification，缺项是否明确 source-gap／not-applicable；
- finding 是否为每个 contract 生成独立 direct answer claim；一个 finding 服务多题时是否逐题收束，而非只解释一遍共享机制；
- direct answer 是否先说明现实事情怎样运作、可能落成什么与结果边界；若只剩“你容易／你倾向／你会感到”，视为性格替代；
- 建议是否只在答案之后；若正文主要回答“应该怎么办”而没有先断现状、形成与结果，视为建议替代；
- 格局、十神、用神、路线等技术词是否只作依据；若术语本身占据答案位置，视为技术标签替代；
- `domain_specific_delta` 是否提供本领域新增角色、对象、载体、条件或结果；多个专题复用同一 process 时，是否复制相同泛化答案；
- `question-answer-map.yaml` 中 complete／conditional 条目是否含 direct answer、独立 claim IDs、六类 refs、最强替代、Render obligation；source-gap／not-applicable 是否有真实理由；
- 最终报告中每个 closure key 是否恰有一个 question marker，其后是否实际出现直接答案；reader-answer receipt 是否与正文一致；
- Render 生产者是否只把 receipt 标为 `pending-independent-audit`；自写 semantic PASS 不得进入独立审计证据；
- 抽查问题能否用一句话回答“这段到底断了什么”。若只能回答“讲了一个机制／性格／建议”，即使格式齐全也判 FAIL。

## 已知高风险模式

命中以下模式至少 WARNING，改变主结构则 BLOCKER：

- ROOT_EQUALS_FLOW：有根等于畅通。
- ARROW_EQUALS_EFFECT：有箭头等于制化完成。
- LOOP_EQUALS_CIRCULATION：成环等于周流。
- COMBINE_EQUALS_TRANSFORM：见合即化。
- CLASH_EQUALS_OPEN_STORAGE：见冲即开库。
- HIDDEN_EQUAL_RELEASE：所有藏干同等引动。
- SELF_PUNISHMENT_OMITTED：漏自刑。
- SELF_PUNISHMENT_OVERRATED：轻刑压过月令主结构。
- NODE_DOUBLE_SPEND：同一节点在多路线重复满额使用。
- DAYMASTER_ONLY：只看日主，漏自治系统。
- STORY_BACKSOLVE：由贴切经历倒推结构。
- FRAMEWORK_BLEND：流派规则静默混用。
- BRANCH_STATE_NOT_PROPAGATED：地支裁决没有写回节点，下游继续用原始状态。
- RAW_NODE_REUSE：Edge／System 绕过 post-branch ledger 回读原始 availability。
- HIDDEN_LAYER_COLLAPSE：藏干存在、根气、直接做功和格用资格混成一层。
- COHIDDEN_AUTO_EDGE：同支藏干仅凭五行关系自动生成 active 边。
- VOID_CAUSES_NO_OPEN：把旬空降力误当作“不自动开库”的成立原因。
- HIDDEN_ALWAYS_WEAK：仅因未透便把全部藏干作用统一降为 weak／conditional。
- SUPPORT_ERASED_WITH_EDGE：删除伪 direct-action 时一并抹掉 root-support／environmental-feed。
- DIRECT_ONLY_SYSTEM：系统与路线只认 direct-action，漏掉可证的混合层供给。
- BRANCH_MANIFESTATION_RECEIPT_MISSING：涉及地支／藏干却没有从 Post-Branch Node Ledger 到 Source／Finding 的四层显化收据。
- BRANCH_MANIFESTATION_COLLAPSE：把 visibility、参与范围、direct-function 与 externalized-result 压成“透／不透”一个开关。
- NONEXTERNAL_BRANCH_ERASED：未形成外部结果便抹掉已成立的场景、根气、环境供给、内部功能或待时接口。
- DIRECT_FUNCTION_EQUALS_RESULT：有 direct-action 或功能起效便宣布现实载体、成果或事件已经兑现。
- ACTIVATION_INTERFACE_DROPPED：hidden／latent／timing-only 节点没有待时重算接口或不适用收据。
- POTENTIAL_ACTIVATION_AS_CURRENT：把 activation interface、projected effect 或 trigger match 写成当前已经发用。
- TRIGGER_WITHOUT_REQUALIFICATION：命中岁运／合盘触发后只翻转 active，没有重裁受影响支局、节点、竞争分配与作用边。
- OVERLAY_VISIBILITY_BACKWRITTEN：把临时 overlay visibility、节点或边回写成原局永久属性。
- SYNASTRY_SYMBOL_AUTO_ACTIVATES：只因对方盘有同字／同五行便宣布本命节点被激活。
- TIMING_LENS_ORDER_CYCLE：在 overlay diff／freeze 之前生成依赖该 diff 的 canonical timing Topic Lens，或让 overlay 反过来依赖 canonical timing lens，形成循环或伪造占位。
- NATAL_ROUTE_RETENTION_DROPPED：临时关系占用原局共享节点后，没有比较原局 route／phase／throughput 的 before／after、备用承接与 expiry。
- NATAL_ALWAYS_OVERRIDES_TIMING：未经节点分配与路线剩余量裁决，预设“原局保证永远大于流运”。
- TIMING_ALWAYS_OVERWRITES_NATAL：仅因流运关系出现便宣布原局路线整体失效。
- TIMING_TEN_GOD_EQUALS_PERSON：从流运十神直接推出固定人物，如劫财＝同事、官杀＝上司，未经过关系功能、topic field、runtime context 与载体竞争。
- RUNTIME_CONTEXT_REWRITES_STRUCTURE：以命主当时职位、身份或现实经历反向决定结构 diff、节点资格、路线保留量或结构置信度。
- READER_FACET_DISPOSITION_MISSING：reader question profile 的 required facet 未唯一登记去向，导致主题内容漏层或重复铺陈。
- BROAD_TOPIC_SINGLE_GENERALIZATION：一个宽泛主题只产一条泛化 finding，没有处理其不同问题层面。
- ONE_TEN_GOD_ONE_FINDING：把十神清单机械转换成 findings／标题，未按不同因果场景组织。
- PROTOTYPE_STYLE_AS_SEMANTIC_PASS：样章或自由发挥稿虽有较好问题密度／文风，但与冻结结构冲突，仍被判 semantic PASS 或允许复用判断。
- COMMANDER_STALE_UNKNOWN：可确定司令仍写未知，或司令修正后沿用旧下游。
- ROUTE_ENDPOINT_DRIFT：路线手写端点与 Edge Map 不一致。
- THROUGHPUT_EQUALS_RESCUE：实际通量排名冒充治疗优先级。
- AGGRAVATION_AS_OUTLET：加重主问题的路线被列为出口／救应。
- SYMBOL_LIST_WITHOUT_COMPOSITION：只列干支十神象意，不做同柱与全局合成。
- MUTUAL_COLORING_AS_EDGE：同柱互染被伪造成 active edge。
- PARTIAL_PILLAR_READING：相关柱漏天干、地支或藏干。
- INDUSTRY_NAME_FIRST：先报行业，再反向拼性质。
- CHAT_SCOPE_CREEP：Render 在追问中越权新增结构或 finding。
- CONTEXT_CREATES_CLAIM：用户经历直接创造新断语或结构。
- MISSING_REPORT_SCOPE：完整原局没有结构冻结后的报告范围入口。
- TAIJI_CENTER_UNSET：topic 没有命盘中心／领域中心，或把太极点技术选择推给求测者。
- MAIN_QI_EQUALS_COMMAND：把月支本气、禄地、十二长生或当前司令叠成重复得令证据。
- NODE_STRENGTH_EQUALS_SUBJECT_CAPABILITY：节点有气直接等于命主可调用、可持续或可外显的能力。
- RAW_NODE_REUSE_IN_TOPIC：Topic 绕过关系后状态，重新按原始本气、禄地或 pre-branch availability 判强。
- TOPIC_STAR_FORCED：因题目名称强制常规对应星为主轴，不允许不具资格。
- TAIJI_MISMATCH：来源立论太极点与引用太极点不一致且无显式论证。
- EFFECT_DIMENSION_COLLAPSE：把关系形式、形质实损、功能制抑与第三方保护合并成一个“克／不克”。
- TEN_GOD_LABEL_EQUALS_VERDICT：从十神标签或口诀直接推出固定喜忌、实际功能、用神资格、稳定能力或事件。
- PARTIAL_TEN_GOD_LAYER_BIAS：未完成同层全套对称审校，却让单一十神基础卡改变运行结果。
- IMAGERY_OVER_SUPPRESSED：因禁用固定物件标签而删除承担机制的气、质、刚柔或动作性质。
- DEEP_CARD_BEFORE_FREEZE：Deep Card 在结构冻结／Topic Lens 前进入结构判断。
- DEEP_CARD_MANIFEST_MISSING：取象或 Render 读卡却没有逐卡 full-read 与单元权限 manifest。
- UNSCOPED_DEEP_CARD_QUERY：Topic query 缺 unit allowlist、selection purpose、claim ceiling、排除范围或错误申请母卡全文。
- WHOLE_CARD_TO_COMPOSITION：Composition 收到或打开 Deep Card 母卡、完整章节或未经编译的整卡上下文。
- UNREQUESTED_UNIT_FORWARDED：runtime packet 转发 Topic 未请求的 unit，或携带 context-only／forbidden 语义正文。
- SOURCE_CLAIM_OVERREACH：Source Lookup 在 runtime packet 中给出 supported／preferred／assertable、bridge rank 或最终载体结论。
- CONTEXT_ONLY_PROMOTED：把 context-only／forbidden 单元升级为 finding、新载体或更高 claim strength。
- SINGLE_CARD_COMPOSITE_VERDICT：单张天干、地支或十神卡直接支持具体职业、岗位、正式身份或事件。
- DOMAIN_CARRIER_RESOLVER_MISSING：具体职业、岗位、正式身份、疾病或事件进入 finding，却没有通过验证的多层领域载体 resolution。
- PROCESS_ROUTE_TRUNCATED：process／finding／composition 从已冻结路线中挑选有利子边，遗漏起始、日主泄耗、通关、下游承接或回病边。
- TREATMENT_COST_COLLAPSED：把制杀／泄杀等治疗效果与日主泄气、资源占用、剩余问题合并成单一“有用／没用”。
- TIMING_PROPAGATION_INCOMPLETE：岁运改变上游 availability、allocation、start gate 或 throughput 后，没有传播到同 process 的全部下游 edge、condition、phase 和 agency。
- PROCESS_SPINE_COMPRESSED：Composition 未保留完整五行克应过程、phase、日主成本或回病，把机制压成无法还原的泛化结论。
- RESONANCE_COMPRESSED：finding 实际使用了物象／载体竞争，却未保留 resonance map，导致所用符号贡献无法追溯；未使用 resonance map 本身不构成问题。
- ENVELOPE_CONTEXT_STARVED：Composition 的 render envelope 未物化足够过程、配对、状态和共振解释，导致 Render 只能复述压缩摘要；修复点在 Composition，不得以开放母卡补救。
- RAW_CARD_TO_RENDER：Render 打开 Deep Card 母卡、runtime packet 或 Source manifest。
- RENDER_ENVELOPE_DRIFT：Render 越过 locked claims／selected units／allowed expansions，新增或升级载体与结论。
- RENDER_CONTEXT_STARVED：legacy alias；按 ENVELOPE_CONTEXT_STARVED 处理，不再授权 Render 回卡。
- RENDER_CARD_DRIFT：legacy alias；按 RAW_CARD_TO_RENDER／RENDER_ENVELOPE_DRIFT 处理。
- RENDER_GAP_BYPASSED：Render 发现 envelope 外新象后现场补断，没有增量回到 Topic／Source／Imagery。
- CROSS_SYSTEM_RULE_LEAK：把另一术数的专属组件或裁决口径当成八字规则。
- UNBRIDGED_CARRIER_VERDICT：从一个符号直接定唯一外形、人物、行业、物件或事件，没有载体桥接收据。
- CARRIER_CANDIDATE_SUPPRESSED：桥接成立的形态或现实载体因过度防御被删除。
- EMPTY_CAVEAT_OVERUSE：没有真实竞争证据却反复用“但是／也可能不是”冲淡可核验判断。
- AUDIT_SUMMARY_DRIFT：审计 finding、summary 与 verdict 互相矛盾。
- PATCH_AFTER_DIRECTION_CHANGE：判断方向改变却只补箭头／改文字，未从受影响阶段重推。
- STALE_FREEZE_DEPENDENCY：active 下游文件引用旧 freeze，或可路由文件未归类 active／inactive。
- BASELINE_TOPIC_OMITTED：完整原局缺家庭、学业、财运、事业任一板块。
- SELECTED_TOPIC_OMITTED：求测者已选专题没有完整走到报告。
- EXPERIENCE_LEAKS_INTO_FINDING：经历在 blind finding 审计前参与生成。
- MANIFESTATION_AS_VALIDATION：显化映射或普通经历讨论被表述为证据验证。
- VALIDATION_WITHOUT_FREEZE：相关年史在 timing hypothesis 审计与冻结前已读取，或缺 freeze 仍声称盲验证。
- HYPOTHESIS_WITHOUT_COUNTERFACTUAL：验证命题缺时间差、顺序、机制或失败条件，因而不可证伪。
- GENERIC_AGREEMENT_SCORED：给“说得通”、忙／压力／变化等宽泛词或单一关键词重合加分。
- PRIOR_EXPOSURE_UNDISCOUNTED：已知经历、已知年份或已知领域未登记、排除或降权。
- RESPONSE_REINTERPRETED：scorecard 改写原始回应、跨假设拼接零散命中或事后换机制／领域。
- INCOMPLETE_WINDOW_OVERSCORED：未结束时间窗的未来部分被提前计分，或缺 observation cutoff。
- FORCED_DETAILED_VALIDATION：用户未主动展开时即进入多字段详细回填，或为填满 rubric 连续追问。
- STRUCTURE_ONLY_MISLABELED_COMPLETE：只有技术结构却声称完成断局。
- NATAL_CORE_OMITTED：full-reading／detailed-natal 缺原局八章，或用生活专题冒充原局详批。
- SCOPE_ATOM_COMPRESSED：四柱、重要藏干、大运段或多个逐年范围被一个综合 axis／finding 代替。
- ANNUAL_CENSUS_OMITTED：用户要求的流年没有独立全量关系枚举与 overlay diff。
- JUDGMENT_TRACE_DROPPED：上游 judgment 无稳定 ID，或 composition／render 未逐条唯一展开。
- RENDER_CLAIM_BODY_COLLAPSE：finding／judgment marker 齐全但对应正文为空、只剩技术依据或被一个总括句伪覆盖。
- RENDER_AUDIT_SCAFFOLD_EXPOSED：把 finding 数、judgment 数、内部字段或审计标签机械转成可见标题／固定栏位，导致全盘主线与段内因果被切碎。
- HIGH_CONTRAST_STRUCTURE_FLATTENED：四个以上同五行、多组冲刑并发、节点多重占用或显／不显对照被压成抽象词。
- AGENCY_LAYER_COLLAPSED：把外部逼迫、本人能动和不可控结果混成“主动换容器／发生调整”。
- FEEDBACK_OFFER_DROPPED：报告交付后 feedback offer 仍 pending／缺失，或因 validation none 静默省略。
- EVIDENCE_SCAN_OVERRIDDEN：独立交付扫描 FAIL，但 audit state／报告自报 PASS。
- READER_QUESTION_PLACEHOLDER：读者问题仍是 facet／topic／英文 slug／`完整回答<facet>` 等内部占位符。
- READER_ANSWER_CONTRACT_MISSING：实质问题没有人／角色、事／对象、结果目标、direct-answer obligation 或唯一 closure key。
- QUESTION_SOURCE_COVERAGE_MISSING：缺逐问题来源覆盖，或通用十神／干支材料冒充领域证据。
- ANSWER_CLOSURE_MISSING：字段、finding 或 judgment 齐全，但没有收束“本题到底怎样”的直接答案。
- PERSONALITY_AS_DOMAIN_ANSWER：用性格、感受、偏好或处理方式代替现实领域答案。
- ADVICE_AS_DOMAIN_ANSWER：用建议、趋避或解决方案代替现状、形成、结果与边界判断。
- TECH_LABEL_AS_DOMAIN_ANSWER：用格局、十神、用神、路线或泛化“主链”总结代替生活答案。
- CROSS_TOPIC_GENERIC_ANSWER_COPY：多个专题复制同一答案，没有 shared answer ref 或各自实质 domain-specific delta。
- READER_ANSWER_RECEIPT_DRIFT：question marker 缺失／重复、direct answer 晚于建议、receipt 与正文不符，或 Render 自判 semantic PASS。

命中 `BRANCH_STATE_NOT_PROPAGATED` 或 `RAW_NODE_REUSE` 一律 BLOCKER。`HIDDEN_ALWAYS_WEAK`、`SUPPORT_ERASED_WITH_EDGE` 或 `DIRECT_ONLY_SYSTEM` 若改变主路线、日主承载力、自治子系统或格局，也为 BLOCKER；其余模式改变主结构时为 BLOCKER，否则至少 WARNING。

`ROUTE_ENDPOINT_DRIFT`、`THROUGHPUT_EQUALS_RESCUE`、`AGGRAVATION_AS_OUTLET`、`MUTUAL_COLORING_AS_EDGE`、`CHAT_SCOPE_CREEP` 或 `CONTEXT_CREATES_CLAIM` 一律 BLOCKER。`PARTIAL_PILLAR_READING` 或 `SYMBOL_LIST_WITHOUT_COMPOSITION` 改变 finding 方向时为 BLOCKER，否则至少 WARNING。

`PROCESS_ROUTE_TRUNCATED`、`TREATMENT_COST_COLLAPSED`、`TIMING_PROPAGATION_INCOMPLETE` 或 `PROCESS_SPINE_COMPRESSED` 一律 BLOCKER。`DEEP_CARD_MANIFEST_MISSING`、`UNSCOPED_DEEP_CARD_QUERY`、`WHOLE_CARD_TO_COMPOSITION`、`UNREQUESTED_UNIT_FORWARDED`、`SOURCE_CLAIM_OVERREACH`、`CONTEXT_ONLY_PROMOTED`、`SINGLE_CARD_COMPOSITE_VERDICT`、`DOMAIN_CARRIER_RESOLVER_MISSING`、`RAW_CARD_TO_RENDER`、`RENDER_ENVELOPE_DRIFT`、`RENDER_CARD_DRIFT` 或 `RENDER_GAP_BYPASSED` 一律 BLOCKER。`RESONANCE_COMPRESSED`、`ENVELOPE_CONTEXT_STARVED` 或 legacy `RENDER_CONTEXT_STARVED` 至少 WARNING；使已实际使用的象意无法追溯或报告无法供命主核验时为 BLOCKER，修复时仍不得开放母卡给 Render。

`JUDGMENT_TRACE_DROPPED` 或 `RENDER_CLAIM_BODY_COLLAPSE` 一律 BLOCKER。`RENDER_AUDIT_SCAFFOLD_EXPOSED` 至少 WARNING；若标题与固定栏位已取代 composition 主线、造成逻辑链无法连续阅读，则为 BLOCKER。`HIGH_CONTRAST_STRUCTURE_FLATTENED` 依可辨识度裁决，不得仅因未使用表格而报错。

`READER_QUESTION_PLACEHOLDER`、`READER_ANSWER_CONTRACT_MISSING`、`QUESTION_SOURCE_COVERAGE_MISSING`、`ANSWER_CLOSURE_MISSING`、`PERSONALITY_AS_DOMAIN_ANSWER`、`ADVICE_AS_DOMAIN_ANSWER`、`TECH_LABEL_AS_DOMAIN_ANSWER`、`CROSS_TOPIC_GENERIC_ANSWER_COPY` 或 `READER_ANSWER_RECEIPT_DRIFT` 在实质报告问题中一律 BLOCKER。不得因术语正确、结构完整、篇幅够长或建议有用而降级。

`BRANCH_MANIFESTATION_RECEIPT_MISSING` 或 `BRANCH_MANIFESTATION_COLLAPSE` 在涉及地支的结构／finding 中一律 BLOCKER。`DIRECT_FUNCTION_EQUALS_RESULT` 一律 BLOCKER。`NONEXTERNAL_BRANCH_ERASED` 至少 WARNING；改变主路线、领域载体或 finding 方向时为 BLOCKER。

`POTENTIAL_ACTIVATION_AS_CURRENT`、`TRIGGER_WITHOUT_REQUALIFICATION`、`OVERLAY_VISIBILITY_BACKWRITTEN`、`SYNASTRY_SYMBOL_AUTO_ACTIVATES`、`TIMING_LENS_ORDER_CYCLE`、`NATAL_ROUTE_RETENTION_DROPPED`、`NATAL_ALWAYS_OVERRIDES_TIMING`、`TIMING_ALWAYS_OVERWRITES_NATAL`、`TIMING_TEN_GOD_EQUALS_PERSON` 与 `RUNTIME_CONTEXT_REWRITES_STRUCTURE` 一律 BLOCKER。`ACTIVATION_INTERFACE_DROPPED` 在 timing／synastry 或改变 conditions matrix／路线时为 BLOCKER；普通 natal 中至少 WARNING，并须补接口或不适用收据。

`READER_FACET_DISPOSITION_MISSING`、`BROAD_TOPIC_SINGLE_GENERALIZATION` 与 `PROTOTYPE_STYLE_AS_SEMANTIC_PASS` 一律 BLOCKER。`ONE_TEN_GOD_ONE_FINDING` 至少 WARNING；若造成 reader facet 漏项、因果场景重复或可见标题碎裂，则为 BLOCKER。

`EXPERIENCE_LEAKS_INTO_FINDING` 在 blind finding 中一律 BLOCKER。`VALIDATION_WITHOUT_FREEZE`、`MANIFESTATION_AS_VALIDATION`、`GENERIC_AGREEMENT_SCORED`、`PRIOR_EXPOSURE_UNDISCOUNTED` 或 `RESPONSE_REINTERPRETED` 在声称完成验证时一律 BLOCKER。`HYPOTHESIS_WITHOUT_COUNTERFACTUAL` 必须在读取回应前退回重写；`INCOMPLETE_WINDOW_OVERSCORED` 至少 WARNING，改变总 verdict 时为 BLOCKER。

`FORCED_DETAILED_VALIDATION` 在用户未 opt in 时为 BLOCKER；用户已展开但问题过密时至少 WARNING，必须改为一次一个时间窗的一句自然问题。

`MISSING_REPORT_SCOPE`、`TAIJI_CENTER_UNSET`、`BASELINE_TOPIC_OMITTED`、`SELECTED_TOPIC_OMITTED` 或 `STRUCTURE_ONLY_MISLABELED_COMPLETE` 在 full-reading 中一律 BLOCKER。limited-topic 必须显式声明范围，否则按误标完整处理。

`MAIN_QI_EQUALS_COMMAND`、`NODE_STRENGTH_EQUALS_SUBJECT_CAPABILITY`、`RAW_NODE_REUSE_IN_TOPIC`、`TOPIC_STAR_FORCED`、`AUDIT_SUMMARY_DRIFT`、`PATCH_AFTER_DIRECTION_CHANGE`、`STALE_FREEZE_DEPENDENCY`、`DEEP_CARD_BEFORE_FREEZE` 与 `CROSS_SYSTEM_RULE_LEAK` 一律 BLOCKER。`TAIJI_MISMATCH`、`EFFECT_DIMENSION_COLLAPSE` 或 `UNBRIDGED_CARRIER_VERDICT` 改变 finding 方向时为 BLOCKER，否则至少 WARNING。`IMAGERY_OVER_SUPPRESSED` 与 `CARRIER_CANDIDATE_SUPPRESSED` 至少 WARNING，改变 finding 方向时为 BLOCKER。`EMPTY_CAVEAT_OVERUSE` 至少 WARNING，使判断失去可核验性时为 BLOCKER。
