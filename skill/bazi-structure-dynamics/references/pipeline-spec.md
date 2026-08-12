# 八字结构动力 Pipeline Spec

## 目录

1. 总原则
2. 阶段与产物
3. 恢复顺序
4. Context 隔离
5. 分析模式
6. 完成条件
7. 标准原局断局协议
8. 经历映射与验证入口

## 1. 总原则

八字分析不得在一次连续生成中同时完成事实校验、原典读取、节点力量、关系裁决、格局、取象和渲染。

每一阶段都必须产生可审计产物。下游只能引用上游产物，不得凭印象重算；缺失时按固定顺序恢复。

完整原局必须把“技术结构完成”和“生活领域断局完成”分开。结构冻结是进入断局的门槛，不是完整断局的终点。

## 2. 阶段与产物

| Stage | Skill | 产物 | 硬门槛 |
|---|---|---|---|
| 0 | orchestrator | process notice、case-manifest | 先说明结构盲跑与后置选题；模式、命盘主人、本人／代看、流派锁定 |
| 1 | bazi-reader | chart-stage1、audit、subject-context | FAIL 停止 |
| 1.2 | bazi-source-lookup | source-packet | 关键来源缺失则降置信度 |
| 1.5A | bazi-structure-core | node-ledger | 节点覆盖 100% |
| 1.5B | bazi-structure-core | interaction-census | 关系覆盖通过 |
| 2A-1 | bazi-structure-core | branch-relation-census | 地支关系与 negative scan 独立覆盖 |
| 2A-2 | bazi-structure-core | branch-state | 共享支竞争已裁决 |
| 2A-3 | bazi-structure-core | post-branch-node-ledger、activation interfaces | 全部节点已写回关系后状态；hidden／latent／timing-only 节点有待时重算入口或不适用收据 |
| 2B | bazi-structure-core | qualified-edge-map（内含 2B.0–2B.6 qualification trace 与 rule receipts） | 只从 post-branch state 起边；按候选→形式→竞争→分配→余力→四维效果→finalize 执行；存在与起效分开 |
| 2C | bazi-structure-core | system-state | 最弱环、控制权齐全 |
| 2D | bazi-structure-core | problem-state | 主问题与判定依据先锁定 |
| 3A | bazi-structure-core | pattern-candidates、route-candidates.yaml、conditions-matrix | 端点只引用 Edge Map；通量与治疗优先级分开 |
| 3B | bazi-structure-core | structure-kernel | 只写技术结构 |
| 3C | bazi-structure-core | use-kernel | 分开用神框架；锁定主用／辅用／备用与实际关系轴 |
| 3.5 | bazi-finding-audit | audit-state、audit-report、structure-freeze-receipt、active-artifact-manifest | BLOCKER 必修；verdict 机械生成；use-kernel、audit state 与其他结构一起 hash 冻结 |
| 3.6 | bazi-render scope-intake | report-scope.yaml | 确认太极中心、完整／限定模式、基础四板块与附加专题；不产断语 |
| 4A | bazi-topic-lens | natal topic-lens-index、Topic Lens v4.1 太极场、coverage ledger、mandatory judgment dimensions、真实问题 contracts（若有）；timing／synastry scope seed | axes 由冻结 process、十神链计划与干支锚点形成；判断维度不生成问题／答案配额但不得被静默删除；Lens 不预写载体或结论；timing seed 在 overlay 前不伪造 canonical axes／finding／人物载体 |
| 4B | core timing／synastry mode | activation match、diff／overlay structure、overlay-qualified-edge-diff、natal-route-retention、overlay-function-transition | 按 scope seed 运行；命中接口后重裁受影响 branch／node／edge／route condition，比较原局剩余主路；不改写 natal，不定人物载体 |
| 4B.5 | bazi-finding-audit | overlay-audit、overlay-freeze-receipt | 原局／覆盖层显隐分栏；scope／expiry 齐全；共享节点、原局剩余主路与临时功能资格已审 |
| 4B.7 | bazi-topic-lens | canonical timing／synastry topic-lens-*.json | 只读已冻结 overlay；逐 atom 建 axis，分开原局剩余主路、临时功能、关系功能、载体候选、现实位置分支与影响边界 |
| 4C | bazi-source-lookup | natal chart-card inventory、imagery-source-packet、topic material coverage | 完整读取本盘相关十神／干支卡，再按专题编译；通用卡不得伪装领域覆盖；具体载体只给 candidate leads |
| 4D | bazi-imagery-composition | imagery-coverage、pillar-composites、axis-scenes、bazi-scene-kernels、topic-findings、coverage-receipt、按需 question-answer-map | 先十神链、再干支柱位合成主／次／反转场景；findings 由象核驱动，不由问题数驱动 |
| 4.5 | bazi-finding-audit | kernel／finding／coverage audit、按需 question-answer semantic audit | 查预写答案循环、材料摊开、十神链、干支组合、现实结果与语义闭合；通过后才可呈现或读取经历做映射 |
| 4.6a（可选） | orchestrator + bazi-render + audit | structural-ambiguity plan／hypotheses／freeze／response、case-ambiguity-overlay | 仅对已冻结双分支；先冻结两套 blind findings，后问一个中性自由叙述问题；只形成个案偏好 |
| 4.6b（可选） | orchestrator + timing core + audit | validation-plan、timing hypotheses、hypothesis audit／freeze | 声称流运验证时必须先于相关年史完成并冻结 |
| 4.7（可选） | bazi-render + bazi-finding-audit | ambiguity response／overlay audit、quick feedback，或 opt-in verbatim response／scorecard／score audit | 默认低负担；详细模式须用户主动启用；不得事后改假设 |
| 5A | bazi-imagery-composition | manifestation-map（可选）、coverage-receipt、按需 question-answer-map、composition | 经历只映射已有分支；以全盘主线与 scene kernels 组织散文，不把 coverage 变成问答骨架 |
| 5.5 | bazi-finding-audit | composition／coverage audit、按需 question closure audit | 不新增 finding、不丢十神链、干支限定与现实结果；真实问题不能被性格或建议代替 |
| 6 | bazi-render | report 或 Q&A answer、coverage-render-receipt、按需 reader-answer-receipt | Render 不取象、不新增 finding；coverage 在后台验收，正文围绕象核连续铺开 |
| 6.5 | bazi-finding-audit | render／conversation audit | 防压缩与聊天越界 |

## 3. 恢复顺序

发现输入缺失时固定回退：

process notice → case-manifest → Reader → Structure Source Packet → Node Ledger → Interaction Census → Branch Relation Census → Branch State → Post-Branch Node Ledger／Activation Interfaces → Edge Map → System State → Problem State → Pattern／Structured Routes → Conditions Matrix → Structure Kernel → Use-God Kernel → Audit State／Report → Freeze／Active Manifest → Report Scope Intake →〔natal：Taiji Field／Coverage Ledger → chart-driven Topic Process Axes → ten-god chain plans／stem-branch anchor plans → 仅真实问题 contracts；timing／synastry：Scope Seed → trigger match → 重算受影响 branch／node／edge／route／process → natal route retention／overlay function transition → overlay audit／freeze → canonical timing／synastry Topic Lens〕→ Natal Chart-card Inventory → Per-topic Imagery Source Packet → Process Compositions → Pillar Composites → Axis Material Projection → Ten-God–Stem/Branch Scene Kernels → Kernel-driven Topic Findings → Coverage Receipt／按需 Question Answer Map → Finding／Kernel／Coverage Audit →〔可选验证流程〕→ Composition → Composition／Coverage Audit → Render → Coverage Render Receipt／按需 Reader Answer Receipt。

不得为了回答快而跳过缺失阶段。用户只问一个术语时可以缩小 question scope，但不能伪装成完整断局。

规则卡的书中出现顺序、人工审校顺序与 runtime 顺序互相独立。Source Lookup 按问题路由卡；Structure Core 只按卡内 hook 和无环依赖图执行；Audit 复核每次应用收据。已批准卡仍不得自动断命。

## 4. Context 隔离

- chart-stage1：只存盘面事实。
- subject-context：用户经历、旧解读、杯卦、灵体反馈；Structure Core 盲结构阶段禁读。
- source-packet：只存来源规则和边界。
- core artifacts：只存技术结构。
- use-kernel：只存用神框架、功能枢纽和实际关系轴；不得提前写生活故事。
- report-scope：只存求测中心、范围与问题，不存用于证明结论的生活故事。
- blind findings：必须在未读取会参与本轮判断的详细经历时生成并审计；既有经历不得反向进入 finding。
- manifestation mapping：structure 与 findings 均审计通过后才允许读取 subject-context；只调整表达带、领域载体、顺序或后续问题，明确 `non-evidentiary`。
- evidence validation：相关年史必须晚于 timing hypotheses 的审计与冻结；已知先验逐项登记并排除／降权，无法隔离时标 `contaminated`。
- structural ambiguity discrimination：相关经历必须晚于争议分支、双分支 blind findings 和辨别假设的审计冻结；结果只写 case overlay，不回写 natal 或规则卡。
- composition：只组合通过审计的 findings，可引用 manifestation map 调整顺序和语气；validation verdict 与结构 verdict 分栏记录。
- render：只能翻译已有 finding；对话中新问题须按 routing 回到对应上游。

## 5. 分析模式

### Natal

- `full-reading`：执行 Stage 0 至 6.5；结构冻结后必须运行 Report Scope Intake，基础四板块不可省略。
- `structure-only`：只执行 Stage 0 至 3.5，交付名称必须是“原局结构分析”，不得称完整断局。
- `limited-topic`：结构冻结后只为约定专题生产 finding；必须明确未覆盖基础板块，不得称完整原局报告。

### Timing

先锁定 natal。由 Report Scope 产时间 atoms，Topic Lens 只先建 scope seed；按大运、流年、流月逐层建立临时节点，匹配原局 activation interface；匹配只是重算入口。按登记范围重新裁关系补齐、支局竞争、节点参与层、边状态与触发路线，输出 before／after diff、原局主路剩余、临时功能资格、持续方式与 expiry。审计冻结 overlay 后回到 Topic Lens 建正式 timing axes。原局 `natal_visibility` 不变。若用于经历验证，另完整执行 [Validation Protocol](validation-protocol.md)：先选对照窗、审计冻结复杂假设，再读年史和计分。

### Synastry

双方 natal 各自 PASS 后建立跨盘临时节点和边。对方节点只有在跨盘关系成立、本题确实调用且匹配预登记接口时才进入重算；同字／同五行不自动激活，也不成为本命永久根。直接叠盘必须在 case-manifest 显式声明，并记录 relationship-bound scope 与 expiry。

### Audit Existing Reading

先 Reader 重建事实，再把旧解读拆为 claims；每条 claim 追溯到 node／edge／route／source，不能只按“听起来合理”审。

### Source or Imagery Question

允许只运行 Reader 的最小事实层加 Source Lookup，但若用户要求落到具体命局，仍需 Core。

### Conversational Follow-up

先判断是已有 finding 的澄清、同结构的新取象、新 topic、新时间／合盘层，还是结构争议。只有第一类可直接 Render；第二、三类增量运行 Topic → Source → Imagery；后两类退回 Core／Audit。首次报告不视为穷尽全盘象意。

## 6. 完成条件

完整原局只有在以下全部满足时才可称完成：

- Stage 1 PASS 或明确说明 PARTIAL；
- 节点和关系覆盖通过；
- 地支关系已独立扫描并完成 negative scan；
- 地支竞争无未决 BLOCKER；
- 关系后节点覆盖全部原始节点，且 Edge Map 没有绕回 pre-branch 状态；
- 原局待时节点有 activation interface；若本题运行 timing／synastry，overlay 已重算受影响边、通过审计冻结且未回写 natal；
- 每条主路线有最弱环和反证；
- 主问题已独立锁定；每条路线的端点与 Edge Map 一致，并分开 actual throughput、net effect 与 therapeutic priority；
- conditions matrix 与 structure freeze receipt 存在且下游版本一致；
- audit state 的 summary／verdict 已机械验证，active artifact manifest 无 stale、mixed 或未归类文件；
- use-kernel 已区分格局、病药／制化、扶身与调候口径，并列出可追溯的实际关系轴；
- 格局候选按流派分开；
- Structure Kernel 与 Use-God Kernel 审计 PASS；
- full-reading 已有 `report-scope.yaml`，命盘主人、求测者关系和领域太极场均明确；逐 topic 的 coverage ledger、冻结事实、常规星资格、实际控制者／承载者、Topic Process Axes、十神链计划与干支锚点均由 Topic Lens 锁定；
- coverage facets 全部由 scene kernels／findings／正文 span 闭合；只有真实显式问题建立 Reader Answer Contract、直接答案 claim 与 `question-answer-map.yaml`；
- full-reading 的 family-home、education-learning、wealth-resource、career-work 四个基础 topic 均有独立 lens、完整 imagery source、finding 与 render section；
- 求测者已选专题没有被漏掉；
- 已明确记录 `manifestation_mapping_state` 与 `validation_state`；两者均可为 `none`，且不阻塞完整报告；若声称验证，则预注册、冻结、原始回应、scorecard 与 score audit 齐全；
- 每个 topic 已有完整 imagery source、逐柱复合、十神—干支 scene kernels、full-chart sweep 和 finding audit；
- 每条 primary 关系轴已进入至少一个 scene kernel 与 finding，或明确 deferred／source-gap；
- 最终文字没有新增、压缩或反向改写 finding；追问新增内容已经走过增量 finding 流程。
- 最终文字中的每个 coverage facet 有 coverage-render receipt；真实问题有唯一完整答案位置和 reader-answer receipt；性格画像、建议、字段／marker 齐全或重复主机制均未被当作断局完成。

## 7. 标准原局断局协议

### 启动说明

首次启动 `full-reading` 时，先用用户能理解的语言说明：本轮先判断全盘结构，结构冻结后才开始分领域断局；个人经历不会进入盲结构；基础报告固定含家庭、学业、财运、事业；专项问题后置确认。

### 范围入口

结构冻结后暂停一次，由 Render 询问：

- 默认是否以命主本人为中心；若不是，围绕谁、哪段关系或哪件事；
- 是否只看原局，或另有具体时间；
- 除基础四板块外，是否增加感情、健康、神秘学、创作、人际、子女或其他专题；
- 每个专题最想核清的具体问题。

用户无需理解“太极点”术语。Render 把自然语言写入 `report-scope.yaml`，Topic Lens 再转换为技术中心。

## 8. 经历映射与验证入口

家庭只是基础报告领域之一，不再承担强制校准锚点。默认不索取逐条“符合／不符合”；这类回应若只有宽泛认同，区分度不足。

- 用户只是补充经历时：在 findings 审计后写 `manifestation-map.md`，说明它更常落在哪个现实载体，以及哪些结构部分仍未被证明。
- 用户只想告诉 AI 准不准时：默认收 `准／部分准／不准／记不清`，允许补一句，不追问、不计分；说明用户可随时说“展开验证”。
- 用户主动要求展开验证时：优先选择跨领域流运对照，完整读取并执行 [经历映射与流运验证协议](validation-protocol.md)。详细叙述有助于分辨时间、顺序、机制与领域载体，但不是完成报告的义务。
- 原局静态验证只有在命题同时具备复合机制、竞争载体、条件和反事实时才允许；否则跳过，不为完成流程制造低价值问题。
- 用户拒绝、没有年史或记不清时记录 `declined`／`unscored`，继续报告，不得伪造验证。
