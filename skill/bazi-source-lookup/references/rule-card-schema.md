# 条件规则卡 Schema

Schema version: 1.1

规则卡是原典的可检索裁决候选，不是把书句改写成自动断命的 `if/else`。它只回答一个明确问题，并把未回答的问题、立论太极点、限定词、改判条件和证据边界一起保存。

## 1. 三层边界

1. 原始证据仍在原文文件；规则卡只保存行号、内容指纹和保真转述。
2. `curation.status: pending_human_review` 的卡只可用于提醒读取与提出候选，不得自动决定节点、作用边、主轴或 finding。
3. 即使 `approved`，规则卡也只提供默认倾向；具体命局仍须读取关系后节点、位置、力量、竞争、去处和反证。
4. 规则卡的原书编排顺序、人工审校顺序与命盘执行顺序可以不同；运行顺序由 `pipeline_hooks`、明确的 artifact `reads／writes` 与真正的 `depends_on` 共同决定。若前卡只提供守门语义、后卡读取的是已经存在的结构字段，不得为“看起来相关”建立硬卡依赖。

## 1.1 准入门槛

只有同时满足以下条件的内容才进入高风险规则卡：它不是 Reader 可确定计算的事实；它会改变关系形式、节点分配、通量、效果维度或路线；原文存在容易被截断的条件、反例或适用边界；现有通用 pipeline 门槛不能充分阻止误用。

- 十神名称、五行生克方向、阴阳正偏等确定性映射留在 Reader，不制卡。
- 某一十神的常见能力、利弊或命例，默认留在完整 Source Packet，不能因单个例子建立运行时基础卡。
- 若要建设十神基础知识层，必须一次性声明覆盖范围并对同层全部十神做对称审校；未完成全套前，不得让单一十神卡改变运行结果。
- 能由“实际节点 → 作用边 → 主问题 → 净效果 → 反转条件”统一裁决的内容，优先加强通用门槛，不为每个十神复制一张同构卡。
- 不以预定卡片数量作为准入理由。

## 2. Registry Header

- `schema_version`
- `registry_id`
- `release_state`：`seed_pending_review`／`reviewed_partial`／`reviewed`
- `source_policy`
- `cards`

## 3. Rule Card

每张卡至少含：

- `rule_id`
- `title`
- `rule_type`：`conditional-principle`／`interaction-arbitration`／`mechanism-with-examples`／`mechanism-bearing-imagery`／`fixed-label-prohibition`
- `fixed-label-prohibition` 是 legacy 类型名，实际只禁止“无结构与问题中心桥接便定案”；不得据此删除合理的形态、物象或行业候选。
- `source`
  - `file`：项目根相对路径
  - `line_start`／`line_end`
  - `excerpt_sha256`：按原文行以 LF 连接并保留末尾 LF 的 SHA-256
  - `provenance_layer`
  - `framework`
- `taiji_of_source`：原文站在谁或哪种关系的角度立论
- `applicable_taiji`
- `question_answered`
- `questions_not_answered`
- `rule_summary`：保留语气强度的转述
- `preserved_qualifiers`：如“往往、若、则、反是、稍解”
- `effect_dimensions`：作用规则按需分别回答
  - `material_damage`：目标形质是否被实质削弱
  - `functional_restraint`：目标功能是否被压制、羁绊或改道
  - `protective_effect`：第三方是否因此减压或得护
  - `relation_form`：形式上优先按克、合或并存候选
- `conditions`
  - `required_state_refs`
  - `applicability_conditions`
  - `override_conditions`
  - `failure_conditions`
- `prohibited_shortcuts`
- `cross_refs`
- `pipeline_hooks`
  - `hooks`：按执行先后列出本卡允许进入的阶段；每项含：
    - `hook`：固定 pipeline hook ID；
    - `role`：`route`／`propose`／`decide`／`guard`／`audit`；
    - `reads`：进入该 hook 前必须已存在的产物或字段；
    - `writes`：该 hook 允许写入的产物或字段。不得用本卡写入目标反过来充当同一 hook 的前置输入。
  - `depends_on`：运行时必须先完成的规则卡 ID；只表达执行依赖，不替代 `cross_refs` 的语义关联。
  - `may_not_decide`：本卡即使适用也不得裁决的字段或问题。
- `curation`
  - `status`：`pending_human_review`／`approved`／`rejected`
  - `reviewed_by`／`reviewed_at`
  - `confidence_cap`：`low`／`medium`／`high`
- `auto_application`：解释性规则卡固定为 `false`。`approved` 只表示允许进入相应 hook 的人工／模型裁决，不表示自动生成命盘结论。

藏干／地支显化卡若涉及后天触发，还须分开两个阶段：

- Stage 1.5C 只登记原局 `activation_interfaces`、触发签名候选和 `if_matched_recompute_from`；接口不是当前激活结论。
- Stage 4B 只在冻结 natal 上匹配岁运／合盘临时节点，写 overlay diff；命中后必须重新裁受影响 branch／node／edge／route condition，并经 Stage 4B.5 审计。不得回写 natal visibility，也不得把另一张盘的同字当自动触发。

## 4. 非死板化约束

- 原文含“往往、若、或、反是、但、稍”等限定词时不得删除。
- `questions_not_answered` 不得为空。跨太极点使用必须新增论证，不能扩大原卡答案。
- “作合论”不自动等于没有功能性抑制；“能制／敌杀”也不自动等于把目标形质克掉。
- 原文例句不得直接升级为所有位置、所有强弱、所有日主都适用的总则。
- 十神身份只回答相对关系，不自动回答吉凶、是否起效、是否为药、是否可由日主调用；同一十神必须允许随问题状态、路线和旁路反转。
- 规则卡不得直接产生生活事件、能力强弱或 topic 主角资格。
- Source Lookup 只能执行 `route`／来源范围 `guard`，不得代替 Structure Core 执行 `decide`。
- 同一张卡可以先 `propose`、后 `decide`、再 `audit`；前一阶段只写候选，不得偷写后一阶段结论。
- 地支人元与显化规则固定先在 `stage-1.5C-post-branch-node-ledger` 保存参与底线与显化依据束，再进入 Edge Qualification；不得先由透干／会局生成结果，再反向补节点资格。
- Stage 2B 内部固定按：候选边 → 关系形式 → 竞争裁决 → 节点分配 → 残余能力 → 四维效果 → final Edge Map。不得用最终 Edge Map 作为生成自身的前置条件。
- `depends_on` 必须无环；待审卡即使被依赖，也不得实际放行下游裁决。
- 语义交叉引用使用 `cross_refs`；只有缺前卡就无法产生当前 hook 输入时才使用 `depends_on`。已有 artifact 字段足以表达先后时，以字段依赖为准。

运行 `../scripts/validate_rule_registry.py` 校验字段、来源行内容指纹、限定词与人工复核状态。
