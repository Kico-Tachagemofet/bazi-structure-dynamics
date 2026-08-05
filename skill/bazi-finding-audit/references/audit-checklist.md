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
- 实际读取章节是否有收据。
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
- 每张 Branch State 卡是否列出逐支、逐藏干的 effect manifest。
- 旬空造成的兑现度变化与“不自动开库”的流派规则是否分开判断。
- Post-Branch Node Ledger 是否覆盖全部原始节点，包括 unchanged 节点。
- 藏干存在、库存／根气、direct action、pattern eligibility 是否分层。
- 同支藏干是否被误作持续互相生克；若允许 direct action，是否有明确来源规则。
- 是否仅因“未透”便把得令本气、有原典人元依据或同气透出的藏干统一降为 conditional／weak。

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
- use-kernel 是否在主问题、路线和 Structure Kernel 之后生成，并与其他结构文件一起冻结。
- 格局用神、病药／制化主用、扶身辅用和调候需要是否分开；“最需要”与“当前最能用”是否分栏。
- 同一节点若分别制病、被损或经旁路回病，是否拆成不同实际关系轴并记录竞争分配。

## 7. 领域、时间与合盘

- 完整原局是否有 report-scope、命盘主人、求测者关系和 reading center。
- full-reading 是否分别覆盖家庭、学业、财运、事业四个基础板块。
- 求测者加选专题是否全部进入 Topic／Source／Imagery／Render。
- 每个 topic 是否分开自然语言领域体与冻结的用神枢纽；是否错误地要求普通用户自选十神／柱位／用神。
- 每条 primary 体—用关系轴是否有 axis scene 与 finding，或明确的 deferred／source-gap 收据。
- blind finding 是否先于相关详细经历生成并审计。
- 家庭、职场、关系等是否被当作竞争载体，而非把家庭设成唯一强制校准锚点。
- 显化映射是否明确 `non-evidentiary`，只调整表达带、领域载体或后续问题，未回写结构或提高 confidence。
- 具体取象是否引用已审计路线。
- 内部机制、领域载体和外部结果是否区分。
- 岁运是否以前后差分表达，而非重写原局。
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

- 每个判断是否能追溯到 node、edge、route 和 source。
- 反证、限制、条件是否在最终文字中保留。
- render 是否添加上游没有的新断语。
- 完整取象是否被压缩到丢失关键分支。
- 经历显化映射与证据验证是否分开；两者均未篡改普遍规则或 natal 结构。
- 杯卦、灵体反馈是否只作待检假设提示或非证据性显化映射，而未冒充八字结构／流运验证。
- 相关柱是否合成天干本象、十神、柱位、地支、全部藏干与同柱双向着色。
- 同柱互染是否被误写成 active 生克边。
- 每条 finding 是否有 full-chart sweep、基线／受压／良性／反向表达带。
- 每条 finding 是否能回溯到一个具体领域体、用神枢纽和主关系轴；是否完整保留生用、损用、去处和日主能动性。
- render 是否把主关系轴展开为起因、动作、对象、结果和切换条件，而非重复“压力、支持、资源、输出”等泛化总结。
- 内部机制、领域载体、外部结果、时间条件和反向代价是否齐全。
- 行业与现实例子是否先由工作性质推导，且区分岗位、任务、收入、可见度和名声。
- 对话追问是否先路由；新象意是否增量走 Topic／Source／Imagery；新结构是否退回 Core。
- 只有 structure kernel 的交付是否被误称为“完整断局”。
- report-scope 的 mandatory 与 selected topics 是否各有唯一 topic marker。

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

命中 `BRANCH_STATE_NOT_PROPAGATED` 或 `RAW_NODE_REUSE` 一律 BLOCKER。`HIDDEN_ALWAYS_WEAK`、`SUPPORT_ERASED_WITH_EDGE` 或 `DIRECT_ONLY_SYSTEM` 若改变主路线、日主承载力、自治子系统或格局，也为 BLOCKER；其余模式改变主结构时为 BLOCKER，否则至少 WARNING。

`ROUTE_ENDPOINT_DRIFT`、`THROUGHPUT_EQUALS_RESCUE`、`AGGRAVATION_AS_OUTLET`、`MUTUAL_COLORING_AS_EDGE`、`CHAT_SCOPE_CREEP` 或 `CONTEXT_CREATES_CLAIM` 一律 BLOCKER。`PARTIAL_PILLAR_READING` 或 `SYMBOL_LIST_WITHOUT_COMPOSITION` 改变 finding 方向时为 BLOCKER，否则至少 WARNING。

`EXPERIENCE_LEAKS_INTO_FINDING` 在 blind finding 中一律 BLOCKER。`VALIDATION_WITHOUT_FREEZE`、`MANIFESTATION_AS_VALIDATION`、`GENERIC_AGREEMENT_SCORED`、`PRIOR_EXPOSURE_UNDISCOUNTED` 或 `RESPONSE_REINTERPRETED` 在声称完成验证时一律 BLOCKER。`HYPOTHESIS_WITHOUT_COUNTERFACTUAL` 必须在读取回应前退回重写；`INCOMPLETE_WINDOW_OVERSCORED` 至少 WARNING，改变总 verdict 时为 BLOCKER。

`FORCED_DETAILED_VALIDATION` 在用户未 opt in 时为 BLOCKER；用户已展开但问题过密时至少 WARNING，必须改为一次一个时间窗的一句自然问题。

`MISSING_REPORT_SCOPE`、`TAIJI_CENTER_UNSET`、`BASELINE_TOPIC_OMITTED`、`SELECTED_TOPIC_OMITTED` 或 `STRUCTURE_ONLY_MISLABELED_COMPLETE` 在 full-reading 中一律 BLOCKER。limited-topic 必须显式声明范围，否则按误标完整处理。
