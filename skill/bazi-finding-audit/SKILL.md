---
name: bazi-finding-audit
description: 以独立检察官模式审计八字结构、格局、路线、取象、composition、render、对话追问、岁运和合盘判断：验证上游产物与结构冻结，检查司令事实、节点关系覆盖、路线端点漂移、通量与治疗优先级混淆、合化开库、支局竞争、伪闭环、同柱取象漏层、完整来源、经历污染、报告压缩和聊天越界。用户要求复核命理解读、Structure Core 或取象阶段完成、前后说法矛盾、或历史判断反复漏项时使用。发现 BLOCKER 必须返工，不作圆场。
---

# 八字 Finding Audit

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

Topic、timing、synastry、composition 或 render 审计还必须读取对应上游文件。

full-reading 的 topic／composition／render 审计另必须读取：

- `report-scope.yaml`；
- `topic-lens-index.yaml` 与全部 per-topic lens；
- 基础四板块和已选专题的 imagery coverage、source packets、findings；
- family blind finding audit、family calibration state 与回应引用（若有）。

## A 层：程序完整性

- Stage 1 是否 PASS 或明确 PARTIAL；
- 节点是否覆盖四干及全部逐位置藏干；
- 每一重复支是否保留独立节点；
- 关系枚举是否含合、冲、刑、自刑、害、破、方会、三合和共享支；
- 地支关系是否从普通候选边中独立出来，并含全部 negative scan；
- Branch State 是否把裁决逐节点写入 Post-Branch Node Ledger；
- Post-Branch Node Ledger 是否覆盖全部原始节点；
- Edge Map 是否只引用 post-branch state，而没有绕回 pre-branch availability；
- 每个结构结论能否追溯到 node／edge／source ID；
- Reader 已知司令是否被结构化记录；司令修正后是否重跑全部下游；
- route 是否只引用 Edge Map 的 edge ID，端点、action、layer 和 distance 是否完全继承；
- problem state 是否先于救应／出口；actual throughput、net effect 与 therapeutic priority 是否分开；
- conditions matrix 是否覆盖每条主路线；
- 本轮声称使用的原文是否出现在 Source Packet；
- subject context 是否在结构审计前被隔离。
- full-reading 是否先交付启动说明，结构冻结后才生成 report-scope；
- report-scope 是否明确 chart owner、querent role、reading center、基础四板块与已选专题；
- family blind findings 是否在详细家庭事实与校准回应进入生成上下文前完成。

任一缺失为 BLOCKER。

## B 层：内容可靠性

逐项扫描 [Audit checklist](references/audit-checklist.md)，重点包括：

- 有根是否被写成畅通；
- 字面相生是否忽略火熔、土埋、寒湿燥烈和下游承接；
- 合是否未经条件直接化；
- 冲是否直接开库；
- 藏干是否被同等冲出；
- 藏干存在、根气、直接做功和格用资格是否混为一层；
- 同支藏干是否仅凭五行关系自动生成 active 边；
- 是否反向把所有未透藏干统一降为 weak／conditional，漏掉原典允许的人元作用、root support 或 environmental feed；
- 旬空降力是否被误写成“不自动开库”的原因；
- 自刑是否漏掉或被夸大；
- 方会、三合和共享支是否只按口诀裁决；
- 图上闭环是否被写成真实周流；
- 同一节点是否同时被多条路线重复占用；
- 是否只看日主而漏掉自治子系统；
- 是否把系统运行等同于日主受益或控制；
- 是否把最强实际通道当成最佳救应，或把加重主问题的路线列为 outlet；
- 格局是否先定后证；
- 不同流派是否被混成一套；
- 用户经历、杯卦或灵体反馈是否被当成普遍规则证据。

任一主结构错误为 BLOCKER；仅影响权重或表述者为 WARNING。

## C 层：输出保真

- topic finding 必须引用已审计结构路线；
- full-reading 是否分别覆盖 family-home、education-learning、wealth-resource、career-work；
- selected optional topics 是否逐项有 lens、source、finding、composition 与 render；
- 每个 topic 是否有明确 taiji center，且技术中心由 Topic Lens 选择而非要求求测者自选十神；
- 取象覆盖是否包含相关柱的天干、地支、十神、柱位和全部藏干；
- 是否逐层完成同柱双向着色，并明确其为 composition-only；
- 每条 finding 是否做 full-chart sweep、表达带和显化层；
- composition 不得加入 finding 没有的新判断，也不得压掉形成层次；
- render 不得删掉关键原象、限制、代价和反证；
- 取象必须读取完整来源展开；
- 职业行业是否先推导性质，再给行业／岗位／任务／收入／可见度例子；
- 回验是否只校准已有分支；
- 健康、精神和超自然断语必须标明边界，不替代现实诊断或本体论证明。

## D 层：报告入口与对话边界

对首次报告入口与 Q&A 额外检查：

- qa-route 是否先识别 clarification、new imagery、new domain、timing、synastry、structural challenge 或 contradiction；
- 直接回答是否确有已审计 finding 与完整 imagery unit；
- 新领域是否增量回到 Topic／Source／Imagery，而非 Render 自由发挥；
- 新时间层、合盘接口或结构争议是否退回对应上游；
- 前后矛盾是否先审计；
- conversation state 是否把用户叙述误写成结构事实。
- 首次完整原局缺 report-scope 时是否错误 direct-render；
- 家庭校准提示是否只引用已审计判断，拒绝校准时是否明确 uncalibrated。

## 裁决

- 任一 BLOCKER：FAIL，列明应回退的阶段，修复后重审。
- 无 BLOCKER、有 WARNING：PASS_WITH_WARNINGS。
- 全部通过：PASS。

结构审计 PASS 后产出 `structure-freeze-receipt.yaml`，记录所有结构输入的路径、hash、schema version 与审计报告 ID。任一结构文件改变即失效。

机械检查优先运行：

- `scripts/validate_route_integrity.py`：从 Edge Map 展开路线端点，检查端点漂移、链条连续性与 aggravating／outlet 冲突。
- `scripts/make_structure_freeze.py`：只在结构审计 PASS 后为必需结构文件生成 SHA-256 冻结收据。

禁止 force pass。审计输出按 [Audit report schema](references/audit-report-schema.md) 生成，并对每个问题列：证据、影响、修复阶段、复验条件。
