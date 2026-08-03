# Bazi Structure Dynamics

一个以结构动力和原典证据分析四柱八字的 Codex skill。

它不把十神压缩成固定吉凶标签，也不先验地用“身强／身弱”覆盖整盘；而是逐一检查天干与藏干的得令、根气、透藏、生扶、克泄、位置与引动，再比较月令格局、用神／相神和多条竞争作用链。

## 主要能力

- 校验四柱、藏干和十神映射；
- 建立逐节点力量表与全局作用网络；
- 区分格神、功能用神、相神、喜神和忌神；
- 比较食神制杀、杀印相生、财生杀、财制枭、枭夺食、通关等竞争路线；
- 结合《千里命稿》《子平真诠》原本及评注、课程逐段资料提取完整上下文；
- 审计一份既有命理解读是否跳步、混淆来源或把局部作用误写成全局结论。

## 安装

仓库中的可安装 skill 位于：

```text
skill/bazi-structure-dynamics
```

将这个目录复制到 Codex 的个人 skills 目录后重启 Codex。也可以使用支持 GitHub 路径的 skill 安装器，指定本仓库中的上述子目录。

## 使用

示例提示：

```text
Use $bazi-structure-dynamics to analyze this 八字 through source-grounded strength, 格局, competing 生克制化 pathways, and full-context 象义.
```

完整原局分析至少需要年月日时四柱。涉及真太阳时、月令司令、大运或应期时，还需核对出生地、节气和起运资料。

## 仓库结构

```text
skill/bazi-structure-dynamics/
├── SKILL.md
├── agents/openai.yaml
├── references/
└── scripts/
```

`references/` 保存结构方法、来源路由和完整证据材料；`scripts/` 是新增 DOCX、EPUB、文本和媒体资料时使用的摄取工具，不是日常解盘的必需依赖。

## 边界

- 本项目用于传统命理文本研究与结构化分析，不构成医疗、法律、财务或其他专业建议。
- 课程转录存在听写待核内容；关键干支、术语、命例与断语应回听原始材料。
- 原文、评注、课程观点和当前模型必须分层引用，不得互相冒名。
- 本仓库未授予统一的开源许可证；来源材料的权利归各自作者或权利人所有。详见 [NOTICE.md](NOTICE.md)。
