# 匿名结构回归期望

这些样例只验证流程能否发现候选关系和阻止历史逻辑捷径，不预存生活经历、身份或最终命理结论。

## Fixture K

四柱：戊寅／丙辰／壬寅／庚戌

最低机械覆盖：

- 两个寅必须保留为两个位置节点并报告 repeated branch。
- 辰戌冲必须被枚举。
- 寅寅不属于自刑，不得误报。
- 自刑成员全集按本链规则锁为辰、午、酉、亥；只有辰辰、午午、酉酉、亥亥可在重复支之外另登记自刑。卯卯、子子、丑丑、寅寅、巳巳、未未、申申、戌戌均只作重复支，不得误报自刑；子卯是相刑，不是各自自刑。
- 戊、丙、庚与全部藏干十神须相对壬重算。

结构审计必须阻止：

- 辰戌冲自动等于强力开库。
- 辰戌所有藏干同等冲出。
- 以“辰旬空”为“不自动开库”的原因；两者必须分列。
- Branch State 判冲力低后，Edge Map 又绕回原节点批量生成不受约束的藏干边。
- 辰中戊、乙、癸仅因同支共存就自动形成持续 active 生克边。
- 因禁止同支自动边，反向把两寅甲、寅中丙等全部未透人元统一降为 weak／conditional。
- 删除甲→丙 direct-action 后，同时删除木对丙火的 root-support／environmental-feed，导致自治子系统只剩明火→土。
- 庚透出或戌藏辛自动等于稳定印路。
- 木火土只按日主损耗描述而不检查自治链。
- 已知戊司令仍写成 unknown，或只改 Structure Kernel 而不重跑节点和下游。
- 路线手写的 source／target 与 qualified-edge-map 不一致。
- 把实际通量较高的食神生财→财生杀路线列为优先救应或 outlet。
- 未先锁定 kill-heavy／body-light 主问题就直接排名用神路线。

关系写回最低要求：

- `branch-relation-census` 必须单列两寅重复、辰戌冲、寅午戌缺午与寅卯辰缺卯，并完成六合、刑、自刑、害、破的 negative scan。
- `post-branch-node-ledger` 必须覆盖全部原始节点；辰、戌及其六个藏干必须引用对应 branch effect。
- `qualified-edge-map` 每条实际边必须引用 post-state；不得直接使用 pre-branch availability。
- 每条边必须标 edge layer；同支 composition-only 不得 active，但有来源的 hidden direct-action、root-support 与 environmental-feed 必须分别裁决。
- 系统层必须重新比较“木提供背景供给、明丙直接生戊”的混合层木火土子系统，不得因缺一条 active 甲→丙边便自动删除整段木供给。
- `problem-state`、结构化 route、conditions matrix、use-kernel 与 structure freeze 必须齐全；route 只保存 edge refs。
- `use-kernel` 必须把“食神制杀”与“食神生财、财再生杀”拆成两条关系轴，并把庚印生身与庚印制食的竞争用途分开；不得用一句“木火土可运行”代替。
- 取象测试若解释壬寅或庚戌，必须覆盖同柱干支双向着色和该支全部藏干，并把互染保持为 composition-only。

## Fixture A

四柱：癸卯／戊午／戊午／庚申

最低机械覆盖：

- 两个午必须报告 repeated branch。
- 午午自刑必须被枚举。
- 年癸与月戊的天干合候选必须被枚举。
- 庚坐申的同柱根关系必须保留。

结构审计必须阻止：

- 午午只当两份完全协调的火。
- 戊癸见合直接判化火。
- 庚申有根直接等于泄秀畅通。
- 年癸在被合绊后仍被多条路线满额调用。
- 合绊修正后的节点状态未冻结，却继续沿用旧 topic findings。

## Overlay Fixture

只允许在两张单盘各自 PASS 后运行。

必须阻止：

- 五行箭头连成一圈即宣布完整周流。
- 跨盘根气改写成双方本命永久根。
- 方会与三合共享节点却不做竞争裁决。
- 直接叠盘未标明为案例采用的模式。
- 对话 Render 把新合盘问题当成已有 finding 的自由延伸。

## Timing activation fixture：隐癸遇癸运

本 fixture 只测试流程边界，不预存“同事作梗”或任何真实经历。设原局存在未直接外显但已登记 activation interface 的癸水节点，戊土同时参与一条原局杀生印／压力转方法路线；岁运再见癸，且形成戊癸关系候选。

最低要求：

- `timing-scope-seed` 先登记本时间原子，overlay 重算并冻结后，才能生成 canonical timing Topic Lens；
- 岁运癸与原局接口匹配只代表进入重算，不代表劫财事件已经发生；
- 戊癸关系必须完成 relation requalification，并把戊在临时关系与原局杀生印路线之间的共享分配写清；
- `natal_route_retention` 必须比较杀生印路线的 before／after throughput、仍成立的 phase、备用承接与 expiry；若仍有 residual route，不得写成“原局杀印路线被破坏”；
- `overlay_function_transition` 必须分开 natal visibility／participation、overlay visibility／direct action 与本轮临时功能；
- 进入职业 topic 后，劫财先解释为同类分配、并行协作、竞争或资源共享关系，再给同事、协作者、竞争者、共同占用名额／预算者等候选；
- 命主当时职位未知时至少保留两个 role branches。职位只改变人物载体、作用方向和命主能动性，不得改变戊癸关系是否成立、戊怎样被分配或原局 route retention；
- 影响写成轻重、局部／全局、短期／跨期或可恢复／难恢复时，必须引用结构影响带与实际保留线路，不得以“原局保证较大”代替。

必须阻止：

- `癸运 → 劫财 → 同事／小人` 的单步人物结论；
- `见戊癸合 → 杀生印路线自动中断`；
- `原局有杀印相生 → 所有劫财运都不严重`；
- 用已知职级或实际经历反向提高合、占用或路线保留的结构置信度；
- overlay 退出后仍沿用临时人物功能或 visibility。

## Reader-density fixture

职业、学业、神秘学等宽泛主题不得各只剩一个“核心机制”。Topic Lens v4.1 按 coverage profile 记录 required facets 与 mandatory judgment dimensions，但不得把它们改写成问题；axes 必须由本盘 process、十神链和干支锚点形成。Composition 不按 facet、问题或十神逐颗拆 finding，却必须按不同现实结果端点形成 claim kernels，再合成 scene。Render 必须覆盖形成、现实层级、成事方式、代价、结果门、切换与核验，但不得机械变成问答或固定标题。

自由发挥样章可以作为 `reverse-spec-useful` 的密度与叙事参照；若其格局、用神、节点功能或路线方向与冻结结构冲突，semantic verdict 必须 FAIL，且只允许倒推“读者需要问清哪些问题”，禁止复用其中命理判断。

## Cross-case semantic gates

任何命例都必须阻止：

- 把月支本气、禄地或十二长生重复计成当前司令。
- 因 topic 名称先封常规对应星为主角，再围绕它找证据。
- 从节点有气直接跳到命主“能力强／是强项／能形成成果”。
- 把来源站在金太极回答的形质毁伤问题，直接拿去否定木太极中的保护效果。
- 把“阳干往往不克阴干”改写成绝不克，或反向把形式上的克写成必然克掉。
- 用一栏“克／不克”同时代替形质实损、功能制抑和第三方保护。
- 审计正文仍有 BLOCKER，summary／verdict 却写成 PASS。
- 判断方向改变后只补边或改文字，未重做关系后节点、资格裁定与全部受影响下游。
- 当前目录有旧 lens／finding 未分类，或 active 文件混用不同 structure freeze。
- 把自由发挥样章的文风／密度 PASS 混同为结构语义 PASS。
- 因具体职业无法达到 L5 而删除已成立的学历层级、专业性质或技术动作。
- 把加重日主承载的高产出路线直接判成低学历、低事业成就或低赚钱能力。
- 以 case-specific 预期句、固定 finding 数、禁词或答案文件让生产器与审计器共享结论。
- 所有命例都被断成高学历、技术权威或正式官职；反例盘必须能给出不同方向。
