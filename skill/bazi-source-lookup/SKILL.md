---
name: bazi-source-lookup
description: 为四柱八字建立可追溯的结构规则包与完整取象包：根据 chart-stage1、冻结结构、report-scope、Topic Lens 和追问范围，路由《千里命稿》《子平真诠》原本、徐乐吾评注、课程全文及干支十神身体职业场所等展开材料；完整原局分别覆盖家庭、学业、财运、事业和求测者加选专题，记录实际读取范围、imagery units、来源层、流派差异、OCR疑点、延后覆盖和证据缺口。用户判断旺衰格局刑冲合害墓库合化，或首次／增量补充具体取象并审计原书依据时使用。本技能不代替结构或生活判断。
---

# 八字 Source Lookup

根据盘面触发项加载本轮真正需要的完整材料，产出可审计的 Source Packet。结构规则包与取象包分开；后续追问允许增量加载，不要求首次报告穷尽一个干支的全部象意。

## 必读输入

- case-manifest.yaml
- chart-stage1.yaml
- 待判断的问题或来自 Structure Core 的 source_queries
- 取象阶段另需 `use-kernel.md`、`report-scope.yaml`、`topic-lens-index.yaml` 与对应 per-topic lens

缺少 Stage 1 时停止，先调用 $bazi-reader。

## 来源层

从现有总技能的 reference 库读取：

- 《千里命稿》原典与高保真整理：基础旺衰、干支、人元、刑冲合害、墓库等。
- 《子平真诠》原本：月令格局、成败救应、变化、纯杂、相神、生克先后。
- 徐乐吾评注：仅作为评注层，不能署为沈孝瞻原意。
- 若境清课程全文：干支和十神取象、课程扩展；不得倒灌成韦千里原文。
- 其他流派：单列规则，不与子平或韦千里静默混用。

总索引入口：

- ../bazi-structure-dynamics/references/source-index.md
- ../bazi-structure-dynamics/references/ziping-zhenquan-source-map.md
- ../bazi-structure-dynamics/references/ruojing-course-source-map.md
- ../bazi-structure-dynamics/references/source-ingestion-fidelity.md

## 路由规则

1. 先从 Stage 1 提取触发项：月令、司令、强弱争议、透藏、合冲刑害、墓库、重支、空亡、调候和岁运层。
2. 再从问题提取所需层：结构、格局、取象、健康、职业、关系、神秘学、岁运或合盘。
3. 对每个关键判断列 source_query_id，读取完整相关章节，不只读搜索命中的单句。
4. 记录本轮实际读取的文件、章节或时间段、来源身份和版本。
5. 原典冲突时建立分流矩阵；不得私自拼成一条“综合古法”。
6. 缺少完整取象展开时标 SOURCE_GAP，禁止凭缩略口诀补故事。
7. full-reading 按 topic-lens-index 分别生成 family-home、education-learning、wealth-resource、career-work 与全部 selected optional topics 的 imagery packet；逐条读取 `body_use_axis` 两端及生用、损用、去处、日主关系所需的完整 imagery units。允许共享同一完整来源读取收据，但每个 packet 的 coverage registry 必须独立，不能用一个 general packet 伪装覆盖全部领域。

### Packet roles

- `structure`：旺衰、司令、格局、合冲刑害、墓库、通关和路线条件。
- `imagery`：本 topic 涉及的干、支、十神、柱位、藏干、身体、场所、动作和领域取象。
- `supplemental-imagery`：追问时为同一冻结结构补充首次未展开的象意。

取象包中的每个 `imagery_unit` 必须保留来源展开的层次、适用条件、正反表现和边界，不得只存一句“某干像什么”。同一材料里的例子不能升级为固定行业或事件。

## Source Packet 最低字段

按 [Source Packet schema](references/source-packet-schema.md) 输出：

- case、framework lock、question scope
- source query
- triggering chart facts
- files and exact sections read
- extracted decision rules
- provenance：原典／评注／课程／现代模型
- conflicts and unresolved gaps
- allowed claims and forbidden overreach
- packet role、imagery unit registry 与 deferred coverage
- full-reading 另记录 report-scope ref、topic slug、topic body、use pivot、relation axis IDs、baseline required 与 topic-lens ref

## 硬门槛

- 声称“原书说”但没有实际读取记录：FAIL。
- 用徐评代替沈孝瞻、用课程代替韦千里：FAIL。
- 用索引摘要或搜索片段代替完整取象卡：FAIL。
- 流派规则冲突但未分栏：BLOCKER。
- full-reading 缺任一基础 topic 或已选专题的 imagery coverage registry：BLOCKER。
- 本轮所需原文缺失：允许继续结构枚举，但相关结论上限为低置信度。

## 输出边界

结构阶段产出 `source-packet.md`；取象阶段产出 `imagery-source-packet-<topic>.md`，追问可产 `imagery-source-packet-<turn-id>.md`。可以整理证据和分歧，不得决定谁旺、谁可用、是否成局、格局最终成立或事件必然发生。
