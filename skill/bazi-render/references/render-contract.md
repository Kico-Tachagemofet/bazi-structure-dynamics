# 八字 Render Contract

## 报告结构

完整原局先读取 `report-scope.yaml`。报告一级领域章节使用稳定 topic marker：

```markdown
## 家庭与生活环境
<!-- topic_id: family-home -->
```

full-reading 必须且只能各出现一次：

- `family-home`
- `education-learning`
- `wealth-resource`
- `career-work`

`selected_optional_sections` 中每个 slug 也必须各有一个 topic marker。限定问题报告可以不含基础四项，但标题与交付说明必须明确“限定问题分析”，并列出未覆盖板块。

每条 finding 对应一个独立小节，并含：

```markdown
### [生活语言标题]

<!-- finding_id: F-XXX-001 -->

**[直接、可核验的核心判断]**

[原象 + 十神 + 柱位的复合解释]

[同柱互染 + 藏干 + 全局结构修正]

[基线／受压／良性／反向版本]

生活判断：……

条件与代价：……

技术依据：finding ID；pillar/node/edge/route IDs；source unit IDs；confidence
```

不设机械字数下限。详细度以 finding 的 `render obligations` 是否 100% 保留为准；复杂 finding 可以很长，简单 finding 不为凑字数灌水。

## 一一覆盖

- 一条 finding 不得与另一条合并后只留一个标题。
- 同一 finding 可在别处交叉引用，但完整展开只保留一处，避免重复。
- finding 中的 mandatory imagery、conditions、costs、counterevidence、source gap 必须进入正文或明确的技术依据。
- `do_not_render` 不得泄漏到正文。

## 生活语言与术语

八字读者可能需要看见“壬寅、偏印、食神制杀”等术语，因此不采用紫微 Render 的术语全禁规则。要求是：

- 首次出现术语时立刻说明它在此盘承担什么功能；
- 不把术语本身当结论；
- 技术 ID 放在“技术依据”行；
- 正文始终能由不熟悉完整模型的命主判断是否符合。

## Confidence

- high：直接陈述，但仍保留适用条件。
- medium：使用“更容易／倾向于／在……时”。
- low：明确说证据不足，只给候选表现。
- gap：不产肯定断语；说明还缺哪份材料。

## 领域例子

职业、行业、关系角色或神秘学实践均先写性质，再写例子。不得把例子反过来当结构证据。

## Q&A 与完整报告的差别

- 完整报告要求 findings 一一展开。
- Q&A 只回答当前问题涉及的 findings，可引用而不重写无关章节。
- Q&A 若新增经审计 finding，应写入增量 composition 与 conversation state，供后续继续引用。
- Q&A 不得因追求即时性跳过必要的 Source、Topic 或 Audit 回退。

## 经历映射与验证边界

- 家庭、职场、关系等都只是领域载体；不得把 family-home 设为唯一或强制校准入口。
- 显化映射只能在 findings 审计后运行，只调整表达带、呈现顺序、措辞、领域载体或追问方向，并明确 `non-evidentiary`。
- 报告若声称验证，必须引用有效的 timing hypothesis freeze、verbatim response、scorecard 与 score audit；否则只能说“经历合参”或“显化映射”。
- 默认只收“准／部分准／不准／记不清”的 quick feedback，可自愿补一句；不自动追问、不计分。详细验证必须由用户主动说“展开验证”等意图后启用。
- 详细模式每次只用一个自然问题处理一个时间窗，不把事件数量、月份、先后、领域和返工一次性列成必填表格。
- 流运回应以自由叙事为主，不用宽泛关键词和逐条认同制造命中；“说得通”不增加置信度。
- 用户不提供经历时写“未做经历映射／验证”，不得降低结构审计结论，也不得声称已经回验。

## Render Audit

至少检查：

- finding 覆盖是否一一对应；
- 形成层次是否被压成十神标签；
- 同柱互染是否双向且未伪造成作用边；
- 藏干的可用条件是否保留；
- 全局修正、反向表现和最强替代解释是否保留；
- 行业是否先性质后例子；
- 经历是否被正确区分为显化映射或预注册验证；
- 对话是否发生 scope creep；
- 前后结论冲突时是否先审计。
- report-scope、基础四板块、已选专题与 topic markers 是否完整；
- 相关经历是否在 blind finding 或 timing hypothesis 冻结前污染生成；已知先验是否排除／降权。
