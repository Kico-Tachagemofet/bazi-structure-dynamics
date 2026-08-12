# 八字问题—答案闭环 Schema v2.0

本 schema 把“完整断局覆盖了哪些面”与“用户真正问了什么”分开。它不规定报告版式；coverage facets 进入 `coverage-receipt.json`，只有有来源的真实 Reader Answer Contract 才进入 `question-answer-map.yaml`。

## 1. 闭环单位

问答闭环单位是 Topic Lens v4.1 `explicit_reader_questions` 中的 `reader_answer_contract`，不是 topic、facet、mandatory judgment dimension、finding、judgment、标题或十神。一个 finding 可以服务多个 contract，但每个真实 contract 必须有自己的 direct answer claim 和 Render obligation。

完整原局的内部检查项不是问题。家庭角色、收入接口、学习输出、职场权限等由 coverage receipt 验收，可以共同写进一条连续散文，不得为了提高“问题闭合率”改写成模型自问自答。

每个 contract 回答三个对象：

- `subject_or_role`：在断谁、哪一类关系角色或哪一方；
- `matter_or_domain_object`：在断什么事、资源、任务、关系、身体层面或时间窗口；
- `result_or_outcome`：主要落法、成事方式、结果倾向或为什么暂不能定。

## 2. question-answer-map.yaml

建议使用 JSON-compatible YAML；最低结构：

```yaml
schema_version: "2.0"
case_id: CASE-ID
structure_freeze_id: FREEZE-ID
report_scope_ref: report-scope.yaml
topic_lens_index_ref: topic-lens-index.yaml
question_answers:
  - closure_key: QA-CAREER-01
    contract_id: RAC-CAREER-01
    source_kind: user-verbatim
    source_ref: report-scope.yaml#explicit_questions[0]
    topic_id: career-work
    explicit_question_id: UQ-CAREER-01
    facet_id: role-and-result
    exact_reader_question: 命主在职场更可能承担什么角色，怎样形成成果，又会付出什么代价？
    answer_status: conditional
    answer_target:
      subject_or_role: 命主在组织中的岗位与责任角色
      matter_or_domain_object: 任务承接、专业输出和组织资源
      result_or_outcome: 主要成事方式、可见成果与责任代价
    direct_answer_summary: 更容易以承接高要求任务、整理复杂问题并交付成果建立职位信用，但成果常连带新增责任；是否升为授权与位置取决于组织结果门。
    direct_answer_claim_ids: [AC-CAREER-01]
    finding_refs: [F-CAREER-001]
    source_coverage_refs: [imagery-source-packet-career-work.md#QSC-CAREER-01]
    process_refs: [PROC-01]
    obligation_refs:
      formation: [F-CAREER-001#formation]
      advantage: [F-CAREER-001#advantage]
      cost: [F-CAREER-001#cost]
      result-gate: [F-CAREER-001#result-gate]
      switch: [F-CAREER-001#switch]
      verification: [J-F-CAREER-001-01]
    domain_specific_delta: 本题把共享的杀印与食神路线限定到岗位责任、专业交付、授权和职位信用，而不是泛说责任感。
    shared_mechanism_refs: [PROC-01]
    shared_answer_ref: null
    strongest_alternative: 若现实岗位没有授权和成果归属，同一结构更可能只表现为临时救火与责任增加。
    personality_role: explanatory-only
    advice_role: after-answer
    advice_substitutes_answer: false
    render_obligation_id: RO-CAREER-01
    gap_or_na_reason: null
```

若本轮没有真实显式问题，`question_answers` 可以为空；这不影响 full-reading 的 coverage 验收。

## 3. Coverage Receipt

`coverage-receipt.json` 逐 facet 记录 scene-kernel refs、finding refs、关键 claim refs、正文 span 与 disposition。它不得含 synthetic question、direct answer summary 或 question marker obligation。coverage receipt 与 question-answer map 不得互相复制生成。

## 4. Answer Status

- `complete`：在当前证据强度内，人／事／结果、直接答案、六类职责和边界均齐全。
- `conditional`：直接答案成立，但结果受现实门、时间窗、载体或竞争路线限制；条件必须写清。
- `not-applicable`：问题经审计确实不适用；必须写 `gap_or_na_reason`。
- `source-gap`：结构或问题成立，但来源／载体材料不足；必须写具体缺口，不得补故事。

`complete／conditional` 必须含非空 `direct_answer_summary`、至少一个 `direct_answer_claim_id`、finding/source/process refs、六类非空 obligation refs、`domain_specific_delta`、`strongest_alternative` 与 `render_obligation_id`。

## 5. 直接答案与从属材料

直接答案先回答事情如何运作、可能落成什么以及结果边界。下列内容不得单独充当 direct answer：

- 性格、感受、偏好或“你通常会怎样处理”；
- 建议、趋避、解决方案或“你需要怎样做”；
- 格局、十神、用神、路线等技术标签；
- “本专题仍由同一主链控制”之类跨专题泛化总结；
- 只列 formation／advantage／cost 等内部字段而不收束结论。

性格可以解释命主如何参与这件事，故 `personality_role` 只允许 `explanatory-only／not-used`。建议只能在答案之后，故 `advice_role` 只允许 `after-answer／not-used`，且 `advice_substitutes_answer` 必须为 false。

## 6. 六类解释职责

每个 complete／conditional closure 都必须能追到：

1. `formation`：为什么形成，哪条冻结 process、十神关系、柱位和载体共同支持；
2. `advantage`：具体在本题怎样成事，不是泛称“有能力”；
3. `cost`：日主、关系、资源、时间或身体付出的代价；
4. `result-gate`：从内部机制到现实结果还要通过什么外部门；
5. `switch`：增强、减弱、改道、失效或反转条件；
6. `verification`：可由命主核对的动作、对象、条件和结果。

六栏是材料责任，不是六个可见标题。不得用同一句通用机制无差别填满六栏。

## 7. 跨专题复用

同一 process 可以进入多个专题，但每个专题必须有非空 `domain_specific_delta`。如果多个 contract 的 `direct_answer_summary` 完全相同，只允许在以下条件下复用：

- 明确填写同一 `shared_answer_ref`；
- 各自仍有不同且实质的 `domain_specific_delta`；
- Render 只完整展开一次，其余位置以 marker 和自然回扣闭环。

若没有新增对象、载体、条件或结果，则它不是新的答案，应交叉引用已有 closure，而不是复制正文。

## 8. Render 与 Reader Receipt

每个 complete／conditional closure 在最终报告中必须恰有一个不可见 marker：

```html
<!-- question_id: QA-CAREER-01 -->
```

并进入 `reader-answer-receipt.yaml`：

```yaml
schema_version: "1.0"
case_id: CASE-ID
report_ref: full-reading.md
question_answer_receipts:
  - closure_key: QA-CAREER-01
    contract_id: RAC-CAREER-01
    render_obligation_id: RO-CAREER-01
    marker_count: 1
    direct_answer_present: true
    answer_before_advice: true
    body_ref: full-reading.md#reader-block-career
    audit_status: pending-independent-audit
```

Render 生产者只能生成 receipt 并标 `pending-independent-audit`，不得自判 semantic PASS。最终 PASS 由独立 `$bazi-finding-audit` 执行问题闭环、正文抽查与 delivery scan 后给出。

## 9. BLOCKER

- contract 没有自然语言问题或 answer target；
- contract 没有 `user-verbatim／scope-confirmed／faithful-restatement` 来源与可追溯 source ref；
- 把 coverage facet、专题名或模型生成的问题冒充用户问题；
- complete／conditional 没有直接答案或六类职责收据；
- 用性格、建议、技术标签或泛化摘要代替领域答案；
- supporting／cross-ref 没有 domain-specific delta；
- 同一 closure 在正文出现零次或多次；
- Render receipt 自称已通过独立语义审计。
