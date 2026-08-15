# HARNESS-RULES · harness 文件组织权威规则

> harness 区(`项目根/harness/`)文件组织的**唯一权威源**。各 skill SKILL.md 落盘路径不再内联复制本规则,只引用「分层见 HARNESS-RULES.md」。
> 权威性:[ADR-0012](../../harness/adr/0012-harness-layering-rule.md)(分层规则)+ [ADR-0013](../../harness/adr/0013-harness-layering-migration.md)(迁移执行)+ [ADR-0011](../../harness/adr/0011-abandon-plan-r-hardcode-harness.md)(硬编码 harness/)。
> 修订:改本文件 = 改 harness 组织规则,须同步 [CHANGELOG](CHANGELOG.md) 留痕。

## 一、分层定义(design/)

`harness/design/` 下的设计文档按是否「feature 级设计」分层:

**判定句**:该设计是否会被独立引用 / 与其它 feature 冲突?
- **是 → `design/<feature-slug>/` 子目录**(feature 级设计:有独立设计套 VISION/HLD/LLD,可独立引用);
- **否 → 裸放 `design/` 根下**(全局/单文件设计,如方法论修订)。

示例判例(本仓库现状):
- feature 级(子目录):`repo/`、`skill-spec-revamp/`、`feature-skills-harness-consistency/`、`doctor-harness/`;
- 全局设计(裸放):`VISION.md`(methodology v3 设计套)、`hld_v2.md`、`lld_v2.md`、`hld-methodology-separation.md`。

## 二、归属判据(哪个根建 harness)

一句判据:**子模块有独立 CLAUDE.md / 独立 git / 独立发布边界 → 子模块根建自己的 `harness/`;否则归主根。**

- 默认:单仓库场景归主根 `项目根/harness/`;
- 多子项目仓库:子模块满足上面任一条件才独立建 harness,否则与主项目共用;
- 落盘前轻量校验(pwd 是否在含 harness/ 的项目根),防工作目录错位误落。**归属校验由各 skill 落盘前执行**(grill-Q Q6 回灌:doctor-harness 只提供判据,不提供校验工具);多项目场景的真实落地待 dogfood(触发时各 skill 补 pwd 检查)。

## 三、命名规范(questionnaires/)

问卷命名模式(各 skill 生成问卷时遵守):

| 模式 | 命名 | 示例 |
|---|---|---|
| init | `<stage>-w<NN>.md`(stage ∈ vision/hld/lld) | `vision-w01.md` |
| feature | `feature-<slug>-<stage>-w<NN>.md` | `feature-repo-design-hld-w00.md` |
| grill | `grill-<slug>-w<NN>.md` | `grill-repo-design-w01.md` |
| retro | `retro-<主题>-w<NN>.md` | `retro-repo-design-w01.md` |
| confirm | `confirm-<slug>-w00.md` | `confirm-skill-harness-sink-w00.md` |

**slug 规范**:来源 = feature 名 / 主题名 kebab-case;去重(生成前自查同 prefix 已有文件);禁通用词(skill/design 等易混淆词)。

**活跃区子目录**(2026-08-14 增补):活跃问卷默认可按 feature/主题建 `questionnaires/<feature>/` 子目录(与 `archive/<feature>/` 对称,便于同 feature 多份活跃问卷归拢);归档时移入对应 `archive/<feature>/`,子目录空了即删。

**豁免清单**(存量已偏离,不清扫,作已知项):`feature-skill-*` vs `feature-skills-*` 近似前缀(历史遗留,读文件时注意区分)。

## 四、归档规则(archive/)

- **归档按 feature/主题**建 `archive/<feature>/` 子目录(新归档 + 存量整批迁移,2026-08-08 用户裁决由「存量不挪」修订为「允许整批迁移」,走 MIGRATION-FLOW 断链回归);
- 非单一 feature 归属的散件(如 confirm-list)入 `archive/_misc/`;
- **归档 README 索引**:列出子目录与归档问卷,便于检索;
- 只移不删,文件名不变。
- **superseded(作废)问卷**(2026-08-14 增补):未答完即被问卷外路径取代的问卷,按 superseded 处置——status 改 `archived`、文件尾部加作废注记(日期 + 取代路径 + 「不作为设计决策依据」),迁入对应 `archive/<feature>/`;不删除、不留在活跃区。status 定义见各问卷引擎 QUESTIONNAIRE-FORMAT.md。

## 五、布局合规校验

`python3 scripts/harness-check.py [harness_root]` 检查:问卷命名正则 / ADR 编号连续(0001 起无跳号)/ 归档位置(processed/archived 问卷在 archive/)。违规清单输出,0 违规时无输出。分层迁移后跑 0 违规 + 0 断链。

**「布局合规」定义**(grill-Q Q10 回灌):= 命名/ADR 编号/归档位置三检查(**脚本可查**,harness-check.py 覆盖)+ design/ 分层(**人工判据**,脚本 report 模式列出供人审,判定句见第一节)。分层判定句需语义判断(可独立引用/冲突),非纯格式,故脚本不强校验分层对错,只报告现状。

## 六、治理文件归属(OPEN-DECISIONS / TODO / CONTEXT / ADR)

2026-08-14 用户裁决(openorbbecsdk dogfood 触发):

- 项目已建 `harness/` 的:**OPEN-DECISIONS.md / TODO.md / CONTEXT.md 归 `harness/` 根**;ADR 归 `harness/adr/`(懒创建,0001 起编号)。治理文件是 harness 内部组织形态,不污染项目根 `docs/`(与 ADR-0011/0012 同一精神)。
- 项目无 `harness/` 的:沿用各 skill 原约定(grill-with-docs:`docs/OPEN-DECISIONS.md` 或 CONTEXT 旁)。
- 各 skill 文档不内联复制本条路径,引用「治理文件归属见 HARNESS-RULES.md」。