# global-backup 清单(P1,2026-08-16)

备份对象:全局版三 skill(同步后一致起点,F027 完成态)——改造(P2–P5)前快照,回滚基准。

| skill | 文件 | sha256(前16) |
|---|---|---|
| design-questionnaire | DESIGN.md | 339c5a9e137487e2 |
| design-questionnaire | PROCESSING-RULES.md | fe7a6aa70a6515b5 |
| design-questionnaire | QUESTIONNAIRE-FORMAT.md | 9142bbaf1bb02657 |
| design-questionnaire | SKILL.md | 6d4bdd2405a7fd96 |
| design-questionnaire | STAGE-SKELETONS.md | 257a5a649de956e9 |
| doctor-harness | DESIGN.md | 8d140807cc11c367 |
| doctor-harness | HARNESS-RULES.md | 7043ecc4f295a001 |
| doctor-harness | MIGRATION-FLOW.md | 0ba46ddfff15a6c3 |
| doctor-harness | SKILL.md | 0e54db8a074d4e12 |
| long-running-agent | SKILL.md | 060de7f0d7c2fc85 |

豁免(不入库):见 EXEMPT-fingerprints.txt(doctor CHANGELOG = 用户私有日志含真实名,脱敏防火墙;且不在 P2–P5 改造范围)。
回滚:cp 本目录对应文件回 ~/.claude/skills/<skill>/ 即可(逐文件可回滚)。
