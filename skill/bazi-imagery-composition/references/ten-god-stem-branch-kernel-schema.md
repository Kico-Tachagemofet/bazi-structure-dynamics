# 八字十神—干支象核 Schema v2.0

本文件定义八字从冻结五行过程进入生活断局时的核心思考单位。八字不以符号数量或自由联想取胜；它先锁定真实生克过程，再把这个过程翻译成十神关系链，最后用天干、地支、柱位与藏干共同限定场景。最终 finding 的思考单位是 `process-anchored bazi scene kernel`，不是问题、facet、单颗十神或单张干支卡。

## 一、固定认识顺序

```text
冻结五行 process
→ 十神关系链
→ 天干显性动作
→ 地支场景与关系后状态
→ 柱位和藏干参与层
→ 同柱／跨柱组合
→ 现实载体竞争
→ 主象、次象与反转象
```

后层只解释和收窄前层，不得反向重算旺衰、作用边、格局、用神、通量、日主成本或 timing diff。

## 二、十神关系链

每条进入生活判断的主链必须先建立 `ten_god_chain`，至少回答：

1. **领域体**：本题究竟在断谁、什么事或什么结果层；
2. **起点**：哪一个实际起效节点先发动，当前是主动、被动还是自治；
3. **关系功能**：该节点相对日主与领域体实际承担输入、同类、输出、资源、权责中的哪一种功能；
4. **传递次序**：关系怎样沿完整 process 传递，途中谁生、克、泄、耗、合绊、占用或改道；
5. **结果端**：链条最后形成哪一类结果资格，结果是否已经可见；
6. **反馈端**：结果是否回头占用日主、用神或另一条有利路线；
7. **竞争用途**：同一十神或节点是否还被家庭、事业、关系或另一 process 调用；
8. **日主权限**：命主能否启动、承接、改变方向、停止或只能接受结果；
9. **反转门**：什么条件使同一十神由有利转为有害，或由压力转成职位、成果、支持与可用资源。

十神名称只给关系坐标，不直接给人物、性格、行业、吉凶或事件。比如事业场的财可以先表示项目、成果、预算、客户或交换结果；哪一种成为主载体，要再经柱位、显隐、完整路线、现实接口与替代载体比较。

## 三、干支怎样组合十神链

### 1. 天干

天干优先提供：

- 当前可见、可被外界识别的关系功能；
- 动作方式、形态、质地、速度和处理风格；
- 公开接口、明确角色或可直接调用的操作端；
- 与其他透干发生的合、克、生、泄及其后果。

天干物象只能给已经成立的十神链着色。不得因为某干“像刀、树、水源、灯火”便直接推出职业、身体事件或人物身份。

### 2. 地支

地支优先提供：

- 事情发生或长期反复的场景、环境与关系场；
- 季节、根基、库存、惯性、阻力和去处；
- 合冲刑害破及支局裁决后的占用、牵动、压制和分配变化；
- 藏干进入十神链的资格与层级。

地支必须继承 `post-branch-node-ledger`。不得把原始藏干表、冲开库口诀或“有气”直接写成现实结果。

### 3. 柱位

柱位只限定十神链主要落到哪一层人事与时间结构：

- 年柱：原生、外缘、较大环境、早段形成或较远关系层；
- 月柱：家庭根基、日常制度、社会／工作环境与持续运行层；
- 日柱：本人、贴身关系、婚居与日常实际承受层；
- 时柱：后续安排、结果、长期方法、晚段发展与延伸层。

以上只是候选职责，必须与当前 topic、十神关系后状态和完整 process 共同裁定。柱位不能单独指定父母、上级、配偶、子女或某件历史事件。

### 4. 藏干

每个相关藏干逐位置保留，并区分：

- `field-present`：场在；
- `qi-or-stock`：气／库存／根气在；
- `environmental-feed`：只经环境供给另一节点；
- `direct-function`：已取得低量或明确直接做功资格；
- `visible-interface`：已有可见接口；
- `timing-pending`：只在接口命中并重算后可提高参与层；
- `externalized-result`：另经领域载体和现实结果门后才成立。

“未透”不等于没有作用，“能做功”也不等于已经发生外部事件。

### 5. 同柱与跨柱

同柱组合必须双向说明：

- 天干如何给地支场景染色；
- 地支如何给天干提供根、环境、阻力、去处或占用；
- 哪一面更强及其依据。

跨柱组合再说明同一十神链怎样从一个场域传到另一个场域。所有组合均为 composition-only，不得生成新的结构作用边。

## 四、材料摊开与场景合成

每个专题强制执行五步，不得只填一个 `main_scene` 字段：

### A. 完整材料摊开

逐项列出并保留来源：

- 完整 process 与 phase；
- process 的 `life_effect_matrix` 四面裁决；
- 参与链条的全部十神关系功能；
- 相关透干的语义单元；
- 相关地支、全部藏干和关系后状态；
- 柱位职责；
- 同柱与跨柱组合；
- runtime candidate palette、领域载体候选、原典例子及其限定；
- 相反锚点、未通过 gate 的候选与 source gaps。

这里只摊开本盘、本题相关卡，不预热全库，也不把 raw card 交给 Render。

### B. 关系合成

按十神链逐项判断材料之间是：

- `reinforces`：同向加强同一生活动作或结果；
- `specifies`：把抽象关系收窄到场景、角色或处理方式；
- `carries`：提供根基、环境、接口或去处；
- `limits`：降低可见度、持续性或结果强度；
- `diverts`：把同一节点导向另一结果端；
- `competes`：与另一 process／topic 争用同一节点；
- `contradicts`：形成真实反证或替代场景；
- `context-only`：有解释价值但不能进入判断。

八字的合成不是自由词义共振。任何合成关系都必须回到十神链中的具体位置和冻结 process。

### C. 现实端点拆分

按 `mandatory_judgment_dimensions` 建立 `claim_kernels`。每个 claim kernel 只处理一个可独立证伪的现实端点，至少含：

- `claim_endpoint_id` 与 judgment dimension；
- `specificity_level`：L1／L2／L3／L4／L5；
- `directional_verdict` 与强度；
- 支持、反证、竞争链和日主代价；
- 结果门、反转和最强替代；
- 对应 process／十神链／干支柱位／candidate palette refs。

同一 process 支持学历、技术、权责、名声、收入、变动或代价时，必须分别建 claim kernel。共享 process 只允许共用事实脊柱，不允许把不同现实端点先压成一条泛化主象。

### D. 五级断语裁决

- L1–L3 有完整组合支持时必须给方向，不得因具体职业不确定而回避；
- L4 比较最多三个载体家族，并说明支持、缺口与排序；
- L5 具体身份或事件采用最高门槛，可以 `not-claimed`；
- 结果方向与日主成本分别裁决，不得以“承载不足”自动否定外部成就。

### E. 场景收束

每个象核至少形成：

- `main_scene`：最主要的生活过程，必须含主体／角色、场景、动作、对象与结果；
- `secondary_scene`：支持、损伤、结果回流或另一柱位带来的第二层；
- `switch_scene`：条件改变后怎样改道、升级、减弱或反转；
- `nonmanifestation_scene`：结构存在但外部结果门未过时，实际仍以什么层级成立；
- `distinctive_detail_palette`：可自然写入正文的本盘特有动作、关系分配、场所或结果细节；
- `strongest_alternative`：最强替代载体及为何不优先；
- `do_not_render`：不能从本象核推出的固定人物、职业、事件或强度。

`main_scene` 不得只是“压力、资源、输出、支持如何运作”。它必须是一个命主能够说符合／不符合／只在某条件下符合的现实画面。

## 五、象核最低结构

产出 `bazi-scene-kernels.yaml`。每个 kernel 至少含：

```yaml
kernel_id: BSK-CAREER-01
topic_id: career-work
taiji_center: 父亲本人在职业场中的任务、位置与结果
process_refs: [P-02]
phase_focus_refs: [P-02-A, P-02-B, P-02-C]
topic_process_axis_refs: [AX-CAREER-01]
ten_god_chain:
  body_or_subject: 日主及职业角色
  start_node_and_agency: null
  ordered_relation_functions: []
  result_endpoint: null
  feedback_to_daymaster: null
  competing_uses: []
  agency: {can_start: null, can_carry: null, can_redirect: null, can_stop: null}
  reversal_gate: null
stem_branch_composition:
  exposed_stems: []
  branch_fields: []
  hidden_stem_layers: []
  pillar_roles: []
  same_pillar_coloring: []
  cross_pillar_transfer: []
material_spread_receipt:
  runtime_packet_ref: null
  selected_unit_ids: []
  unit_dispositions:
    - unit_id: null
      disposition: used | counterevidence | context-only | excluded-with-reason
      claim_kernel_refs: []
      reason: null
  source_refs: []
  excluded_unit_receipts: []
  coverage_validator_receipt_ref: pending-independent-validator
composition_relations: []
mandatory_judgment_dimension_refs: []
claim_kernels:
  - claim_kernel_id: CK-CAREER-01-A
    judgment_dimension_ref: occupational-nature
    claim_endpoint_id: occupational-nature
    specificity_level: L2-domain-nature
    disposition: directional-verdict
    directional_verdict: null
    claim_strength: null
    support_refs: []
    counterevidence_refs: []
    support_unit_refs: []
    counterevidence_unit_refs: []
    counterevidence_check: null
    result_gate: null
    reversal_condition: null
    daymaster_cost_ref: null
    competing_claim_or_carrier_refs: []
main_scene: null
secondary_scene: null
switch_scene: null
nonmanifestation_scene: null
distinctive_detail_palette: []
candidate_carriers_ranked: []
strongest_alternative: null
do_not_render: []
confidence: null
```

## 六、质量门槛

以下任一情况为 BLOCKER：

- 没有十神关系链，直接把干支物象拼成故事；
- 只有 process 摘要，没有十神、干支、柱位与藏干组合；
- 只列十神功能，不说明起点、传递、结果端与反馈端；
- 用一颗十神或一个干支直接支持具体人物、职业、疾病或事件；
- `main_scene` 与另一个 topic 只替换名词，十神链、柱位和结果完全相同；
- 没有材料摊开收据，却直接写主象；
- `selected_unit_ids` 与 runtime packet 的全部 selected units 集合不相等，或任一 selected unit 没有且只有一条 disposition；
- producer 只取前 N 个 unit、用固定 limit 截断，或自行填写 `all_chain_links_covered: true` 代替外部重算；
- `used／counterevidence` unit 没有回链 claim，directional claim 没有材料级 support／counterevidence 引用与相反证据检查；
- 象核只含建议、性格、高基率词或技术标签；
- 载体强度高于 runtime unit claim ceiling 或缺 Domain Carrier Resolver；
- 用户经历参与 blind 象核生产；
- 问题清单反过来预写象核结论。
- mandatory judgment dimension 没有 claim kernel，且无具体 `not-applicable／source-gap` 收据；
- 用一个 mega-kernel 吞掉不同现实结果端点，或因 L5 不足删除已成立的 L1–L3；
- 把日主成本、治疗方向和外部成果方向压成一个吉凶标签。
