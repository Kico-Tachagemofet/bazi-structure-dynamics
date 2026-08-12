# 象核 Agent 隔离生产协议 v1.0

本协议把复杂十神—干支象核从总编排上下文中隔离出来。目的不是增加一个形式角色，而是保证现实断语只能在完整材料进入同一判断现场后生成，杜绝主 session 先写答案、再批量套结构字段。

## 一、何时必须调用干净 agent

命中以下任一项，scene kernel 必须由全新上下文的语义生产 agent 完成：

1. `full-reading`、`detailed-natal` 或一次生产两个以上 scene kernels；
2. topic 含两个以上 process／axis、三个以上 mandatory judgment dimensions，或同一节点存在竞争用途、回病旁路、反向结果；
3. 需要比较 L4 现实载体，或分别裁学历、专业性质、技术动作、资格／权责、名声、收入、变动、冲突、健康负荷等多个现实端点；
4. timing、synastry、结构歧义分支、高反差节点或临时功能资格参与；
5. runtime packet 超过 12 个 selected units，或同时涉及多组天干、地支、藏干、柱位组合；
6. 当前编排 session 已读取旧报告、命主经历、用户纠错、预期答案、known facts 或其他会提示结论的材料；
7. 主 session 已经负责 Reader、Structure、Topic、Source 中两个以上上游阶段，继续承担取象会使程序状态与语义判断混在同一上下文；
8. 准备使用脚本、模板、字典或批量循环生成 directional verdict、claim kernel、main scene 或 finding 正文。

只有同时满足以下全部条件，主 session 才可处理一个窄增量 kernel：单一 topic、单一 process phase、最多两个 mandatory dimensions、selected units 不超过 12、无路线竞争、无 L4 载体比较、无 timing／synastry／歧义、未接触经历或预期答案，且仍须完成本协议的全量 unit disposition ledger 和独立审计。无法确定时按“必须调用”处理。

环境没有可创建全新上下文 agent 的能力时，复杂象核标记 `AGENT_ISOLATION_UNAVAILABLE` 并停止在 Imagery 之前。不得由主 session 代写，不得把旧报告改写、批量脚本或更长自检当作隔离替代。

## 二、角色与文件边界

### Orchestrator

主 session 只负责：

- 计算复杂度触发项；
- 生成不含结论的 `scene-kernel-jobs/<topic>/job-packet.json`；
- 以全新上下文调用 producer；
- 调用另一个全新上下文 auditor；
- 在 audit PASS 后合并 canonical artifacts 并向下游传播。

主 session 不得在 job packet、脚本、模板、文件名、字段默认值或 agent 消息中预写 directional verdict、preferred carrier、预期职业／学历／事件或命主反馈。

### Producer agent

producer 使用全新上下文；在支持时固定 `fork_turns: none`。它只能读取 job packet 明列的输入，不继承总 session 历史，不读取旧 finding、composition、report、subject context、known facts、用户纠错或预期答案。

一个 producer agent turn 只处理一个 `job_id／topic_id`，写完即结束。不得用 follow-up task 让同一 agent 连续处理下一个 topic；否则第二个 topic 已继承前题结论，不再是 fresh producer。多个 topic 可并行，但必须使用不同隔离目录，且只有 orchestrator 可以在全部独立审计通过后合并。

每个 agent 只写自己的隔离目录：

```text
scene-kernel-jobs/<topic>/producer-output/
  material-disposition-ledger.json
  scene-kernel.json
  producer-receipt.json
```

不得直接改 `bazi-scene-kernels.yaml`、canonical findings 或其他 agent 的目录。

### Auditor agent

auditor 必须与 producer 和 orchestrator 分离，并使用另一全新上下文。它只读取 job packet、原始输入、producer output 与审计规则；不得读取 producer 的对话推理、总 session 诊断、预期答案或命主经历。auditor 只写 PASS／FAIL 证据，不替 producer 改结论。

一个 auditor turn 同样只审一个 job；不得用已审过其他 topic、已经看过 known facts 或参与过生产的 agent 继续审计。

```text
scene-kernel-jobs/<topic>/independent-audit/
  audit-state.json
  semantic-audit.md
```

FAIL 后废弃该 producer output，另开新的 producer turn；不得把 auditor 的建议连同原答案交回原 producer 反复缝补并称为独立重做。

## 三、Job Packet 最小合同

`job-packet.json` 至少包含：

```json
{
  "schema_version": "1.0",
  "job_id": "SKJ-...",
  "case_id": "...",
  "topic_id": "...",
  "task": "produce-one-process-anchored-scene-kernel",
  "complexity_triggers": [],
  "fresh_context_required": true,
  "allowed_inputs": [
    {"role": "structure_freeze", "path": "...", "sha256": "..."},
    {"role": "process_handoff", "path": "...", "sha256": "..."},
    {"role": "topic_lens", "path": "...", "sha256": "..."},
    {"role": "runtime_packet", "path": "...", "sha256": "..."},
    {"role": "manifestation_receipts", "path": "...", "sha256": "..."}
  ],
  "forbidden_inputs": [
    "subject-context",
    "known-facts",
    "old-findings",
    "old-composition",
    "old-report",
    "user-correction-or-expected-answer"
  ],
  "output_directory": ".../producer-output"
}
```

timing／synastry 追加相应已冻结 diff、retention、transition 与 expiry 输入。packet 只指定判断对象和材料，不指定判断方向。

## 四、Producer 固定提示词

调用 producer 时使用以下固定任务说明，只替换方括号内路径：

> 你是八字十神—干支象核生产者。你不知道命主经历，也不得猜测委托者期待的答案。你的目标不是填写 schema，而是仅凭 `[job-packet.json]` 允许的冻结材料，判断 `[topic_id]` 在现实中更可能形成什么、较不支持什么、怎样成事、代价在哪里、什么现实门使结果兑现、何时反转。
>
> 先完整读取 job packet 及其全部 allowed inputs。不得读取目录中未列入 allowed inputs 的文件。写任何 directional verdict 前，必须完成每个 runtime selected unit 的 disposition：`used / counterevidence / context-only / excluded-with-reason`，并使四类并集严格等于 runtime packet 的 selected units；不得截前 N 项，不得自行填写“已全部覆盖”。
>
> 认识顺序固定为：冻结 process 与 phase → 领域十神关系链 → 天干显性动作 → 地支关系后场景 → 藏干参与层 → 柱位范围 → 同柱／跨柱限制 → 竞争路线与相反证据 → L1–L4 现实载体竞争。对每个 mandatory judgment dimension 单独建立推导链和 claim kernel，先拆分，后合成主象、次象、切换象与未显化层。
>
> 每条 directional claim 必须引用实际 support unit IDs、counterevidence unit IDs（没有时说明经过了哪些相反材料检查）、process／axis、干支柱位组合、结果门与反转条件。十神标签、单个干支、通用五行机制或问题措辞不能单独推出结论。不得把多个维度按数组位置套入预写句子。
>
> 只写 `[output_directory]`。完成 `material-disposition-ledger.json`、`scene-kernel.json` 与 `producer-receipt.json` 后停止；不要生成 finding、composition 或 reader 报告。

producer receipt 必须声明实际读取的路径与 hash、未读取的 forbidden inputs、是否存在 prior exposure、是否使用脚本生成判断文本。判断文本若来自预写字典、模板循环或上游答案字段，receipt 必须 FAIL。

## 五、材料全量处置

`material_spread_receipt` 必须保存：

- `runtime_packet_ref`；
- runtime packet 全部 `selected_unit_ids`，顺序可不同但集合必须相等；
- 每个 unit 唯一一条 `unit_dispositions`；
- `disposition` 为 `used / counterevidence / context-only / excluded-with-reason`；
- `used` 与 `counterevidence` 必须回链一个或多个 claim kernel；
- `context-only` 与 `excluded-with-reason` 必须给出本题为何不进入结论的具体理由；
- runtime unit 总数、处置总数与 validator 计算结果。

`all_chain_links_covered` 只能作为 validator 输出，producer 不得凭布尔值自证。canonical kernel 中如保留该字段，其值必须由 validator receipt 回填，并同时引用 validator receipt。

## 六、独立验收固定任务

auditor 必须回答：

1. runtime selected unit 集与 disposition ledger 是否严格相等，有无静默截断、重复或无理由排除；
2. 每个 mandatory dimension 是否有独立 claim，正文是否真的回答该 dimension；
3. 每条 claim 能否由所引 process、十神链、天干动作、地支／藏干状态与柱位共同推出；
4. 干支材料是否实际收窄、加强、限制或反转了十神含义，而不是报告末尾的装饰；
5. 支持材料、相反材料、竞争路线与最强替代是否都被处理；
6. 是否存在预写答案、数组位置映射、固定前 N units、跨 topic 通用句、批量模板或生产／审计共享答案源；
7. 主象是否在独立 claims 成立后才合成，强度是否与 L1–L5 及现实结果门一致。

任一项失败即 BLOCKER。字段齐全、字数、judgment 数、路径存在或 producer 自报 PASS 均不能替代上述验收。

## 七、盲测资格

已经向某个 session 透露命主经历、错误方向、期望答案或修复目标后，该 session 及其 fork 不再具有该命例的 blind first-pass 资格。它可以做故障复现和回归修复，但不能作为泛化证据。正式 forward test 必须使用未讨论的新命例、全新上下文 producer、独立 auditor，并在第一次输出冻结后才解封 known facts。
