# AGENTS.md

本文件是 Codex / GitHub 的仓库入口(路由文件,零内容 = 零漂移)。Claude Code 会话请读 [CLAUDE.md](./CLAUDE.md)。

## 启动顺序

1. 读 [CLAUDE.md](./CLAUDE.md)(仓库定位 / 规范优先级 / 关键文档导航)
2. 按 CLAUDE.md「关键文档导航」选读本次改动相关文档
3. 文档冲突时按 CLAUDE.md「规范优先级」节裁决(方法论主张 > ADR > CONTEXT > skill 规格 > 实操)

## 指向 docs 的链接

- 方法论三块:[methodology_v5.md](docs/methodology/methodology_v5.md) / [philosophy_v7.md](docs/methodology/philosophy_v7.md) / [practical_v1.md](docs/methodology/practical_v1.md)
- 术语表:[docs/CONTEXT.md](docs/CONTEXT.md) / 决策记录:[harness/adr/](harness/adr/) / 待决事项:[docs/OPEN-DECISIONS.md](docs/OPEN-DECISIONS.md)
- AI 流程产物:[harness/design/](harness/design/) / [harness/questionnaires/](harness/questionnaires/)

## Codex 专属约束

- 发布前脱敏门:`python3 scripts/desensitize.py .` 必须 0 命中(映射表在本地 gitignored,不提交;不要在 .md 中复述映射表真实名)
- 本仓库无 build / test 工具链,验证以断链检查 + 脱敏为主
