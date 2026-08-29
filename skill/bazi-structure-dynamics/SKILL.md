---
name: bazi-structure-dynamics
description: 编排四柱八字的轻量主流程：先核对盘面并收束旺衰、格局、十神链和用神；范围不明确时必须向用户确认；随后把固定材料封装成 reading pack，交给无历史上下文的独立 writer 完成取象与报告。用于完整原局、限定专题、岁运和合盘。普通报告不走 Topic Lens、Composition、多轮审计或同盘 few-shot。
---

# 八字结构动力总编排

本流程把两种工作分开：前半程负责把盘算对、结构收束；后半程让一个干净上下文根据固定材料独立断命并成文。

开始前读取 [轻量流程](references/pipeline-spec.md)。需要生成完整报告时，再读取 [Fresh Reading Handoff](references/fresh-reading-handoff.md)。

## 入口分流

- 用户显式调用 `$bazi-reader`，且没有明确要求继续完整报告时，只完成 Reader，交付事实后停止。
- 用户给出 raw chart 并明确要求完整报告或专题解读时，进入本流程。
- 请求已经提供 `reading-pack` 并要求 `$bazi-render` 时，说明这是下游写作任务，不重启 Reader、Structure 或 Scope。
- “断一下”“看看这个盘”“分析一下”只说明用户希望继续，不等于已经确认专题、性别和时间范围。

## 高特异度精度提示

若用户明确把首要目标说成“尽可能精确还原具体学历／学位、离婚或婚次、精确职业身份／机构、具体官职、标志性人生事件”等高特异度履历，在进入 Reader 前先简短说明：八字更稳定的长处是结构性质、成事路线、职业类型、代价与推运，不保证从原局稳定恢复上述具体履历；若环境已经安装紫微飞星 Skills，可优先使用 `$ziwei-feixing-core-v2`，原始紫微盘面先经 `$ziwei-reader`，再以八字补充结构与时间判断。

让用户选择继续八字、改用紫微飞星，或两者交叉。仅因用户正常询问学历、婚姻、事业等专题，不触发这段提示；用户已知边界后仍选择八字，不重复提醒。不得承诺任何术数具有客观准确率。

## 1. Reader

调用 `$bazi-reader` 得到 `case-manifest.yaml`、`chart-stage1.yaml`，以及确有污染材料时的 `subject-context.md`。Reader 只核四柱、十神、藏干、司令、旬空与时间边界。

## 2. Structure

调用 `$bazi-source-lookup` 的结构模式，再调用 `$bazi-structure-core` 写：

- `source-notes.md`
- `structure-notebook.md`

结构笔记须完整保留月令、旺衰承载、重要干支关系、十神角色竞争、格局路线、用神次序、失败路线与岁运接口，但不预写家庭、学历、职业、婚姻等生活答案。

## 3. 用户范围确认门

只有用户已经明确给出以下信息时，才能继续：

- 命盘主人及本人／代看；
- 完整原局或指定专题；
- 是否包含大运、流年及具体年份；
- 感情、婚姻、六亲或子女需要的性别口径。

缺少会改变报告内容的信息时，用一条简短自然语言提问并结束当前 turn。不得自行把泛化请求扩成完整原局，不得根据大运顺逆替用户确定性别，也不得在用户回答前创建 `report-scope.yaml`、topic map、reading notebook、composition 或报告。

用户已经说清范围时直接记录，不重复确认。按 [Report Scope](../bazi-render/references/report-scope-schema.md) 写 `report-scope.yaml`。

## 4. 封装 Reading Pack

范围确认后，补读本盘实际出现的五行、十神、天干、地支、重要藏干和用户要求岁运的相关材料。然后创建独立 `reading-pack/`，固定以下内容：

- `handoff.md`
- `chart-stage1.yaml`
- `structure-notebook.md`
- `report-scope.yaml`
- `source-notes.md`
- `materials/`：本轮真正相关的 Deep Cards 或必要来源摘录

Reading pack 不包含旧报告、旧 findings、用户纠错、预期答案、经历材料、Topic Lens、reading notebook、composition、few-shot、审计文件或其他 case 内容。用户明确允许经历合参时，另在 `handoff.md` 标为 non-blind，并只加入获准材料。

## 5. Fresh Reader-Writer

完整报告默认交给一个全新上下文 agent：

- 使用 `fork_turns="none"`；
- 只给 reading-pack 路径、输出路径和一段简短任务说明；
- 明确调用 `$bazi-render`；
- 一次完成十神—干支取象、现实判断与散文写作；
- 不再经过默认 Topic Lens → Imagery → Composition → Render 长链。

如果环境不能提供全新上下文，不在已经完成上游分析的长 session 中冒充干净写作。交付 reading pack 与 handoff，让用户在新任务中继续。

## 6. 父窗口最低复核

writer 完成后只检查：

1. 四柱、日主、性别口径和主结构没有被写错；
2. 用户确认的专题、大运和年份没有明显遗漏；
3. 没有读取排除材料；
4. 健康、死亡等高风险内容没有写成确定事实。

不按标题数、段落模板、固定句式、字段或预期断语重写报告。发现实质问题时废弃该稿，用同一 reading pack 新开一次 writer；不要在原 writer 上累加长篇纠错。工具失败可重试一次。

## 岁运

上游只固定原局保证与外来干支实际改变的关系、路线和强弱，不预写事件。writer 在同一报告中自然展开大运背景和用户指定的独立流年，不为每年建立多套中间文件。

## 可选诊断模式

`$bazi-topic-lens` 与 `$bazi-imagery-composition` 不属于普通完整报告的默认路径。只有用户明确要求查看分析底稿、限定专题需要额外拆解，或 fresh writer 明显缺少实质内容时，才调用它们定位材料缺口。

只有用户明确要求审计、污染检查、benchmark 或正式盲测时，才调用 `$bazi-finding-audit`。

## 默认产物

1. `case-manifest.yaml`
2. `chart-stage1.yaml`
3. `source-notes.md`
4. `structure-notebook.md`
5. `report-scope.yaml`
6. `reading-pack/`
7. `full-reading.md`
