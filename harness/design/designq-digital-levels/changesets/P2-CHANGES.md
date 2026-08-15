# P2(doctor 拓展先行)变更清单

| 变更 | 侧 | 文件 | patch |
|---|---|---|---|
| HARNESS-RULES 增补七/八节(LN 规则 + 存量改造 + 迁移映射表) | 全局版 | ~/.claude/skills/doctor-harness/HARNESS-RULES.md | P2-doctor-HARNESS-RULES.patch |
| SKILL.md 触发词 + 场景⑤⑥ + 规则清单两行 | 全局版 | ~/.claude/skills/doctor-harness/SKILL.md | P2-doctor-SKILL.patch |
| CHANGELOG 留痕(私有不入库) | 全局版 | ~/.claude/skills/doctor-harness/CHANGELOG.md | —(指纹豁免) |
| harness-check.py LN 校验(命名/L0 缺失/裸放/存量豁免) | 项目侧 | scripts/harness-check.py | git diff 自身 |

自测:五场景(合法/无L0/L0非vision/存量豁免/裸放)全符合 + 本仓库回归 0 违规。
