# 八字 Deep Card Schema

Deep Card 是“可推导的符号语义底座”，不是命局裁决表，也不是把古书句子改写成更多口诀。

它回答：一个五行、天干、地支或十神关系，**在什么结构状态和问题中心下，可能以哪些性质、动作、形态和现实载体出现**。它不回答：本盘一定发生什么、谁一定是什么性格、命主一定从事哪个行业。

## 与条件规则卡的分工

| 类型 | 主要问题 | 进入流水线的位置 | 能否直接裁决结构 |
|---|---|---|---|
| 条件规则卡 | 某条结构规则在什么条件下成立 | Source Lookup → Structure Core | 只能按 hook 与依赖进入裁决 |
| Deep Card | 一个符号可怎样被理解和展开 | 结构冻结 → Topic Lens 查询 → Source Lookup 读卡 → Imagery Composition | 不能；只解释已审计节点、状态和路线 |

Deep Card 不新增生克边，不替代 Reader 的干支、藏干和十神确定性事实，也不替代 Structure Core 的旺衰、合化、通量、格局与用神裁决。

## 推导主链

```text
五行运行方式
  × 阴阳表达方式
  × 当前关系后状态
  × 相对日主的十神功能
  × 柱位／领域体／问题中心
  × 可见性、承载力与现实环境
= 候选性质 → 候选载体 → 有条件的生活表达
```

这条链是检查路径，不是机械乘法。后一步必须继承前一步，不能从“甲像树”跳到“本人一定高大”，也不能因为这种跳跃有风险，就删掉“高大、修长、挺拔”这些本来可能成立的形态候选。

## 最低字段

每张卡至少包含：

- `card_id`、版本、状态和适用范围；
- `core_process`：该符号最底层的运行方式，优先使用动词和方向；
- `derivation_path`：本层怎样由五行、阴阳、季节或关系推出；
- `paired_contrast`：与同五行阴阳配对项，或同关系族正偏项的区别；
- `state_switches`：得时、失令、受生、受制、过盛、无根、被合、被冲等怎样改变表达；
- `topic_axes`：身体外形、行为方式、家庭、学习、财富、职业、关系、场所或物件等哪些问题中心可调用；
- `candidate_expressions`：性质、动作、形态和载体分层列出；
- `bridge_requirements`：要把候选写进 finding，至少需要哪些本盘锚点；
- `alternative_carriers`：同一机制还可能落在哪些现实载体；
- `cannot_decide`：本卡单独不能决定的结构与事件；
- `source_receipts`：来源身份、完整读取范围、可迁移层与不可迁移层；
- `review_questions`：遇到竞争解释时给 Composition／校准阶段的问题。

自卡片 `version: 0.3` 起另须包含 `runtime_unit_map`。旧 draft 可继续共同审稿，但未补该表前不得升为 `approved`。

## Runtime unit map 与权限分层

Deep Card 母卡只能由 Source Lookup 全文读取，且不能把全文中的每个例子都视为本题可用结论。`runtime_unit_map` 把卡内内容拆成下列单元：

| `unit_class` | 内容 | 默认结论上限 |
|---|---|---|
| `semantic_core` | 本义、底层过程、阴阳／气质配对 | `mechanism`；只解释已冻结结构 |
| `state_modifier` | 已知关系后状态怎样改换表达 | `mechanism`；不得自行重算状态 |
| `symbol_carrier` | 与本符号直接相连的形态、材料、物件、身体功能 | `candidate`；符合本题桥接后可升级 |
| `relational_carrier` | 由十神关系进入的六亲、人物、物件或领域功能 | `candidate`；必须先锁定 topic body、关系口径与参与节点 |
| `composite_domain_carrier` | 具体职业、岗位、身份、事件或复杂生活场景 | `context-only`；必须由领域载体推导和多项结构证据激活 |
| `cross_system_context` | 其他术数可迁移的共同符号层 | `context-only`；不能参与八字结构裁决 |

每个单元至少记录：

- `unit_id`、`unit_class` 与卡内对应章节；
- `allowed_topics`；
- `activation_requirements`：必须引用哪些 axis、node／edge／route、关系后状态、十神／柱位与现实结果 gate；
- `claim_ceiling`；
- `forbidden_promotions`：不能从本单元直接升级成哪些人物、职业、事件或结构判断；
- `source_layer`。

Source Lookup 为每个实际查询登记 `activated／context-only／forbidden／source-gap`。只有 `activated` 单元的受控编译内容可以进入 runtime packet；`context-only／forbidden／source-gap` 只把 unit ID、原因或缺口留在 source-only manifest，不把正文交给下游。Composition 不读取母卡，Render 不读取母卡或 runtime packet。

具体职业、岗位、正式身份或事件不得由一张天干、地支或十神卡独立升到 `supported`。它们至少需要：相关领域轴、合格关系功能、位置与可见接口、完整做功路线、日主承载／调用、现实结果条件以及竞争载体比较。但 L5 的高门槛不得反向删除 L2 性质与 L3 动作／材料候选；只要 activated gate 成立，这些候选必须进入 runtime `candidate_palette`，供 Composition 与其他十神、干支和柱位交会。天干地支为载体提供动作、形态、材料或风格着色，组合是否支持具体家族与身份由后续裁定。

### 母卡只在 Source 可见，下游只见编译单元

- Topic Lens 只申请单元类别和用途，不读卡。
- Source Lookup 完整读相关卡并建立 `deep_card_manifest`，不得只凭片段判断上下文。
- Source Lookup 把本题 activated units 编译为 `deep-card-runtime-packet-<topic>.json`；需要的配对、状态与限定必须写进单元 payload，不把整卡交给下游补上下文。
- Composition 只读编译包，完成认识论组合，产出 `resonance_map`、载体排名与自足的 `render_use_envelope`。
- Render 只读审计后的 finding、composition 与自足 envelope；不得打开母卡、runtime packet 或 Source manifest。
- Render 发现未组合的新象时登记 `render-gap`，退回增量 Topic／Source／Imagery；不得现场补断。

地支卡另须继承 [十二地支共同底座](deep-cards/earthly-branches-core.md)，并记录 `branch_manifestation_contract`：本卡怎样在 `场在／气在／用起／果显` 四层中解释符号、哪些非外显模式仍成立、哪些判断必须回读 Structure Core 的 `branch_manifestation_handoff`；若涉及 timing／synastry，还须引用 `activation_interface` 与受审计 overlay，不自行发明触发。

每张进入 runtime 的单支卡还必须声明：

- `static_hidden_stems_authority: Reader`：静态藏干集合及本／中／余等级只继承 Reader，不由象意卡改表；
- `static_hidden_stems: [...]`：把本卡所继承的 Reader 藏干集合显式列出，供逐气 runtime interface 覆盖校验；
- `commander_authority: Reader_month_command_with_source`：月令内部司令另走带节气偏移与表源的 `month_command`；
- `commander_sequence: [...]`：只保存已核来源中的气序候选，实际命盘值仍以 Reader 为准；
- `commander_does_not_rewrite_hidden_stems: true`：司令气序说明某段时间谁秉令，不把该干增删进静态藏干，也不改写 qi_rank；
- 复合支中的每个藏干必须有独立 runtime interface；透出、会动或后天触发只重算实际命中的节点和边，不得整支批量激活。

若八字原典、评注、课程或跨体系材料对藏干等级、司令日数或方位口径不同，须在 `source_receipts` 分层登记。Deep Card 无权静默选边；运行事实仍由 Reader 的 `framework_lock`、表源与审计结果决定。

## 天干／地支统一 Topic axes

`derivation_routes` 与 `topic_axes` 不得混为一层：前者说明一个象意从五行、阴阳、季节、形态或来源中的哪条路径推出；后者说明求测者问到哪个现实领域时，应怎样调用这些路径。所有进入 runtime 的天干、地支卡都必须逐项交代下列七轴：

| 轴键 | 问题中心 | 最低要求 |
|---|---|---|
| `behavior_personality` | 性格、行为方式、反应习惯 | 说明底层过程怎样在“以人为体、反复且稳定”时转成行为候选，并列状态改写；不得把一时动作直接定为人格 |
| `appearance_body` | 外形、体态、身体功能 | 区分形态候选、功能候选与疾病结论；疾病仍须身体专题及多重锚点 |
| `learning_cognition` | 学习、理解、表达、认知路径 | 描述怎样吸收、组织、处理或输出信息，不从符号直接判断学历与成绩 |
| `career_work` | 事业、岗位、工作内容 | 先写工作性质，再列能承载该性质的行业／岗位例子 |
| `wealth_resource` | 财富、资源、获得与处置方式 | 只有领域体或十神关系把该节点接到财／资源轴时才调用；符号本体不自动等于有钱或破财 |
| `family_relationship` | 家庭、六亲、亲密关系、协作 | 六亲身份由十神、宫位与求测关系确定；本卡只展开该节点在关系中的动作和载体 |
| `object_place` | 物件、空间、环境、现实载体 | 同时比较形状、材料、功能、环境与同柱／同路线复核，不靠单一类比锁死对象 |

每一轴必须标明 `coverage`，取值为：

- `supported_candidate`：有直接来源或已有来源链支持，可进入桥接；
- `derived_candidate`：由已审来源的核心过程推得，必须标为当前归纳，不能倒署成原文；
- `source_gap`：该轴缺少足够依据，保留检索缺口，不以模型记忆补齐；
- `not_applicable`：只有说明为什么本类符号无法回答该轴时才能使用，不能用来规避补卡。

七轴是检索收据，不要求七种互不相干的结论。允许多轴调用同一底层过程，但每次都必须重新接上领域体、十神／柱位、关系后状态和竞争载体。

## 地支显化专用桥

地支的“显”不能只看有没有同字透干。凡涉及地支或藏干，先完整读取 [十二地支共同底座](deep-cards/earthly-branches-core.md)，再沿下列四层收据处理：

```text
field_layer（季节／空间／场景／容器仍怎样存在）
  + qi_layer（逐藏干仍参与库存、根气、环境供给或待时的范围）
  + function_layer（direct-action gate、实际 edge、通量、承接与竞争）
  + result_layer（topic axis、carrier bridge 与现实结果条件）
= branch_manifestation_receipt
```

四层不强制线性串联：环境题可由 `field_layer` 直接进入领域载体；藏干也可只通过 root-support 扶持另一个节点。`透清`、得令本气、同气成势、经裁定的会局、位置接近和下游承接都只是显化依据束的一部分；任一单项都不得自动推出“得用”或“外部结果已显”。

若 result layer 未通过，仍按收据保留 `field-background／stock-root-support／environmental-feed／internal-latent／direct-function／timing-pending` 中实际成立的模式。不得把“不外显”改写成“无作用”，也不得把“有直接功能”改写成“事件已兑现”。

`timing-pending` 必须保留“如果透清／会动，应重算哪些功能候选”的接口，但这不是当前结果。岁运／合盘命中接口后，Deep Card 只读取 `natal_visibility → overlay_visibility`、重算后的 function layer、覆盖范围与 expiry；不得把临时显性写成原局显性，也不得仅因另一人有同字便生成关系场结论。

### 性格取象专用桥

```text
core_process
  × person_anchor（日主、人物体、六亲体或明确的人格问题中心）
  × repeated_and_stable（全局重复、持续得载或多锚点支持）
  × post_relation_state
  × position_and_ten_god_function
= 行为／性格候选
```

短时流运、单次受制或一次关系动作，优先写成当下行为，不提升为稳定人格。没有 `person_anchor` 与 `repeated_and_stable` 时，只能描述“该节点怎样动作”，不能写“这个人就是怎样”。古书或跨体系材料中的品德褒贬，只可拆回可观察的状态候选；不能直接继承为善恶、贵贱或固定性格。

## 来源层与迁移边界

### 1. `bazi_primary`

八字原典或高保真原文。可支持八字语境中的概念边界，但仍须保留原文太极点、限定词和流派归属。

### 2. `bazi_course`

八字课程或现代整理。可以扩展取象，不能倒署为古人原意。

### 3. `cross_system_common_symbol`

其他术数材料中关于阴阳、五行、天干、地支共同符号的展开。只有同时满足下列条件才可迁移：

1. 去掉该术数独有的宫、星、门、神、起局法后，语义仍成立；
2. 能回接阴阳、五行、季节、形态或干支共同结构，而不是只靠命例类比；
3. 不被用来决定八字中的旺衰、合化、刑冲、格局、用神或吉凶；
4. 与八字来源冲突时分层并列，不静默覆盖。

奇门材料中的九宫、九星、八门、八神、宫位吉凶、奇门合化口径和具体断验，不得迁入八字 Deep Card。

### 4. `current_synthesis`

为便于模型推导而做的当前架构归纳。必须能追溯到前述来源，并明确它是工作模型，不冒充原书句子。

## 载体桥接与表达强度

### 候选层 `candidate`

符号本身允许这种性质或形态。例如甲木允许“向上、挺拔、修长、高大”成为外形候选。候选不等于已经适用于命主。

### 支持层 `supported`

问题中心与本盘锚点同时支持，且没有更强的相反证据。可以自然地写“更可能……”“常表现为……”，无需机械追加“但也不一定”。

### 优先层 `preferred`

比较过竞争载体后，该表达最能承载当前结构与领域轴。可以把它放在结论前部，并把其他载体放在例子或次场景。

### 定案层 `assertable`

只有具体事实、多个独立锚点或求测者明确要核验的窄问题支持时，才可直接判断；仍按证据强度说话，不把象意写成逻辑必然。

## “禁止无桥接定案”而非“禁止出现”

需要阻止的是：没有从结构、问题中心和状态搭桥，就把一个象意例子写成唯一事实。

- 不合格：`甲木，所以你一定很高。`
- 合格候选：`甲木的曲直与向上性，使高挑、修长、骨架舒展成为外形候选。`
- 有盘面支持：`以日主体象、得令有根且少折损来看，外形更可能偏高挑挺拔。`
- 职业表达：先说工作性质，再列“符合这些性质的行业／岗位包括……”。

不要为了显示谨慎，把每条判断写成“可能……但是……”。只有真实存在竞争锚点、状态切换或来源分歧时，才展开转折；否则直接用与证据相称的强度表达。

## 默认加载顺序

1. Reader 先冻结干支、藏干、月令、十神等事实；
2. 结构用 Source Lookup 读取结构原文与条件规则，不加载 Deep Card；
3. Structure Core 与结构审计完成关系后状态、路线、结构核和冻结；
4. Topic Lens 只根据冻结结构与问题中心生成 `deep_card_queries`，不读卡、不产象意；
5. 取象用 Source Lookup 先读 `five-elements-core`；若 query 涉及地支，再读 `earthly-branches-core`，然后加载相关单支卡；天干 query 直接加载相关天干卡，不全库预热；
6. 涉及人物关系或领域功能时加载 `ten-gods-core`；Source Lookup 完整读卡，并按 query 生成 source-only manifest；具体职业、身份、疾病或事件另接 `domain_carrier_requests`；
7. Source Lookup 只把 activated units 与受控 carrier leads 编译入 runtime packet；Imagery Composition 不读取母卡，只用该包执行载体桥接、共振组合、竞争解释比较和表达强度裁定，产出 `resonance_map` 与自足 `render_use_envelope`；
8. Audit 检查是否在冻结前偷读象意、是否漏掉有效候选、是否无桥接定案、是否把 context-only 单元升格或把跨体系材料越权当八字规则；
9. Render 只按 `render_use_envelope` 展开；语义不足或发现新象意时退回上游，不以回读母卡补充。

timing／synastry topic 在第 5 步之前必须已经完成 activation interface 匹配、受影响结构重算、overlay audit 与 freeze。Deep Card 不参与触发匹配或重算。

Deep Card 只允许写入 `imagery`／`supplemental-imagery` Source Packet。它不得进入结构 `source-packet.md` 的 decision rules，也不得成为 Structure Core 的输入依赖。

## 非死板审查问题

每次调用卡片至少问：

1. 当前要解释的是符号本体、符号在关系中的动作，还是现实载体？
2. 哪些状态会让同一符号改换表现，而不是简单“好／坏”？
3. 当前候选有几个现实载体？为什么其中一个更符合本题？
4. 是否真的存在相反证据，需要写转折？如果没有，不制造无意义的“但是”。
5. 这个结论来自八字结构、共同符号层，还是仅来自另一术数的局部规则？
6. 七条 Topic axes 是否都有收据？若某轴没有可靠内容，是否明确记为 `source_gap` 而非凭模型记忆补齐？
7. 当前说的是原局显隐还是 overlay 显隐？若称“被激活”，是否有 matched interface、重算与 expiry 收据？
