# Fresh Reading Handoff

Reading pack 的作用是把“上游已经确定什么”完整固定下来，同时把旧报告、用户反馈和长 session 历史留在外面。

## 目录

```text
reading-pack/
├── handoff.md
├── chart-stage1.yaml
├── structure-notebook.md
├── report-scope.yaml
├── source-notes.md
└── materials/
```

`materials/` 只复制本盘实际出现并参与结构的五行、十神、天干、地支、重要藏干，以及用户要求岁运的相关卡片或必要来源摘录。不要把整个 Skill、全部原典、其他命例或 archive 打包进去。

## handoff.md 只写

- case 路径与输出路径；
- 命盘主人、性别口径与本人／代看；
- 用户确认的专题、大运、流年和原始问题；
- 必须完整读取的 pack 文件；
- 是否为 blind／non-blind；
- 明确排除的目录和材料。

不写预期答案、旧稿评价、用户曾纠正什么，也不规定每章必须有哪些小标题或固定句型。

## Fresh agent 提示

```text
Use $bazi-render for a downstream reading task. Read every file inside <reading-pack-path> completely. The chart facts and structure notebook are fixed upstream conclusions; do not restart Reader or Structure. Independently combine the ten-god chains, stems, branches, hidden stems, pillars and timing material into a detailed Chinese Bazi reading covering exactly the confirmed scope. Organize the report naturally and write it to <output-path>. Do not read archive, .archive, other case folders, prior reports, findings, composition, user history or any few-shot.
```

使用 `fork_turns="none"`，不要把父 session 的对话摘要附在提示后面。
