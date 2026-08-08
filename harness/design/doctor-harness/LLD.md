# LLD · doctor-for-harness

> 来源:design-questionnaire feature 模式 lld 阶段 W00(2026-08-08,14/14 全采纳)。
> 上游:[VISION](VISION.md) + [HLD](HLD.md) + [ADR-0012](../../adr/0012-harness-layering-rule.md) + [ADR-0013](../../adr/0013-harness-layering-migration.md)。
> 本文 = 落地规格;执行时每阶段按 DoD 验证,全部完成后走 dogfood 自检 + 衔接实现期。

## L1 阶段计划(4 阶段,可独立交付/验证)

依赖链:**P1 → P2 → P3 → P4**(校验脚本依赖规则权威定义;迁移依赖校验脚本验证;家族表述依赖迁移验证通过)。

| 阶段 | 目标 | 关键动作 | 独立 DoD |
|---|---|---|---|
| **P1 规则权威** | HARNESS-RULES.md 起草 + SKILL.md 引用 | 起草五节规则(分层定义/归属判据/命名规范/归档规则/布局合规校验)+ 各 skill SKILL.md 加「分层见 HARNESS-RULES.md」 | grep 规则文档在位(五节标题)+ SKILL.md 引用句 |
| **P2 校验脚本** | scripts/harness-check.py 实现 + 现状跑通 | 单文件三检查函数 + 接口 | 脚本对现状跑出真实违规 / 无违规 0 输出 |
| **P3 分层迁移** | 本仓库 design/ 重组 + 链接重算 + 断链回归 | 必做档 design/ 按 feature 聚合 + 相对链接重算 | design/ 重组完成 + 断链 0 新增 |
| **P4 双副本 + 家族** | 仓库 + ~/.claude 同步 + 家族表述 | 双副本同步 + CLAUDE.md/CONTEXT 第 9 个表述 | 双副本 diff 0(仅脱敏差)+ 家族表述同步 |

## L2 详细设计

### 2.1 HARNESS-RULES.md 结构(P1)

五节:

1. **分层定义**:design/<feature>/ 判定句(feature 级设计 = 会被独立引用 / 与其它 feature 冲突 → 建子目录)+ 裸放规则(全局/单文件设计裸放根下);
2. **归属判据**一句:子模块有独立 CLAUDE.md / git / 发布边界 → 子模块根建自己的 harness/;否则归主根;
3. **命名规范**:init/feature/grill/retro/confirm 各模式正则 + 豁免清单(feature-skill-* vs feature-skills-* 近似前缀);
4. **归档规则**:新归档按 feature/主题建 archive/<feature>/ 子目录;存量不挪;归档 README 索引。

### 2.2 校验脚本结构(P2)

单文件 `scripts/harness-check.py`:

```
main(harness_root) → 扫描目录
  ├─ check_naming(): 问卷命名正则(init/feature/grill/retro/confirm)
  ├─ check_adr_sequence(): ADR 编号连续(0001 起,无跳号)
  └─ check_archive_location(): processed/archived 问卷在 archive/
输出违规清单(逐条「路径: 违规类型」);--json 可选
纯标准库(pathlib/re)
```

### 2.3 迁移流程文档(P3)

MIGRATION-FLOW(SKILL.md 节或独立):设计新布局 → 挪文件(必做档 design/ 重组)→ 相对链接重算 → 跑校验 → 断链回归 → 规格同步。逐步可跟随,不自动化。

## L3 接口规格

| 接口 | 规格 |
|---|---|
| 校验脚本 | `python3 scripts/harness-check.py [harness_root]` → stdout 违规清单 + exit 0;`--json` 输出 JSON。入参:harness_root(默认 ./harness);出参:违规清单;异常:目录不存在 → 提示 + exit 1 |
| 规则引用 | 各 SKILL.md 落盘路径句保持硬编码 `harness/`(ADR-0011),只在 HARNESS-RULES.md 声明分层规则,SKILL.md 加一句「分层见 HARNESS-RULES.md」 |

## L4 DoD

### 统一回归(每阶段必跑)

1. **机制回归**:新增 skill 不破坏既有 8 skill 触发/落盘/引擎机制;
2. **脱敏门**:`python3 scripts/desensitize.py .` 0 命中(skill 改动若复制进本仓库则扫)。

### 各阶段 DoD

- **P1**:HARNESS-RULES.md 在位(grep 五节标题:分层定义/归属判据/命名规范/归档规则/布局合规校验)+ 各 skill SKILL.md 引用句在位;
- **P2**:脚本对当前仓库跑出真实违规(ADR 编号跳号 / 命名偏离 / 归档位置);无违规时 0 输出(误报门);`--json` 可用;
- **P3**:必做档 design/ 重组完成(methodology 裸放保留、feature 系列已建目录保留、逐条核对归属);相对链接全部重算;断链回归 0 新增;SKILL.md 引用同步;可选档(questionnaires/adr)标 TBD;**F019 实证:design/ 已天然分层,无需物理重组,本次实为确认 + 9 处归档链接修复**(grill-Q Q3 回灌);
- **P4**:两套副本 diff 0(仅脱敏差);CLAUDE.md 家族图 / CONTEXT skill 家族节 / 落盘速查表同步第 9 个(pending——先 dogfood 后入家族,迁移验证通过后落)。

## L5 依赖与预估

- **外部依赖**:无(纯 Markdown + 纯 Python 标准库脚本,不涉编译/运行);校验脚本与 desensitize.py 并列 scripts/。
- **工作量排序**:P1(规则起草,最轻)> P3(迁移 + 断链回归,最重)> P2(校验脚本,中)> P4(双副本 + 家族表述,中)。
- **实现方式**:long-running-agent 驱动(feature_list 从 P1–P4 反推)或手动按阶段推进;本次设计完成后的实现是否衔接 long-running 由用户定。