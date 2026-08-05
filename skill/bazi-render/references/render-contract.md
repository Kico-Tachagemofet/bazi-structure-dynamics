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

## 家庭校准边界

- 家庭 blind findings 必须先于详细家庭经历生成并通过审计。
- 校准提示只能逐条展示 finding 已有的可核验判断，不能现场补故事。
- `confirmed／conditional／disconfirmed` 只可调整表达带、呈现顺序、措辞或领域载体。
- 用户不校准时报告写“家庭板块未做经历校准”，不得降低结构审计结论，也不得声称已经回验。

## Render Audit

至少检查：

- finding 覆盖是否一一对应；
- 形成层次是否被压成十神标签；
- 同柱互染是否双向且未伪造成作用边；
- 藏干的可用条件是否保留；
- 全局修正、反向表现和最强替代解释是否保留；
- 行业是否先性质后例子；
- 经历是否只作校准；
- 对话是否发生 scope creep；
- 前后结论冲突时是否先审计。
- report-scope、基础四板块、已选专题与 topic markers 是否完整；
- 家庭事实是否在 blind finding 审计前污染生成。
