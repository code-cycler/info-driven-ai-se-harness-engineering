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
- 落盘前轻量校验(pwd 是否在含 harness/ 的项目根),防工作目录错位误落。

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

**豁免清单**(存量已偏离,不清扫,作已知项):`feature-skill-*` vs `feature-skills-*` 近似前缀(历史遗留,读文件时注意区分)。

## 四、归档规则(archive/)

- **新归档**按 feature/主题建 `archive/<feature>/` 子目录;
- **存量不挪**(原始信息不丢失铁律 + 不破坏既有链接);
- **归档 README 索引**作为过渡:列出已归档问卷,便于检索;
- 只移不删,文件名不变。

## 五、布局合规校验

`python3 scripts/harness-check.py [harness_root]` 检查:问卷命名正则 / ADR 编号连续(0001 起无跳号)/ 归档位置(processed/archived 问卷在 archive/)。违规清单输出,0 违规时无输出。分层迁移后跑 0 违规 + 0 断链。