# HLD · doctor-for-harness

> 来源:design-questionnaire feature 模式 hld 阶段 W00(2026-08-08,12/14 采纳;#13/#14 转 W01)。
> 上游:[VISION](VISION.md)(W00 20 条 + W01 10 条全采纳)+ [OD-15](../../../docs/OPEN-DECISIONS.md) + [ADR-0011](../../adr/0011-abandon-plan-r-hardcode-harness.md)。
> 本文件 = 架构层;落地规格见 LLD(分阶段实现)。

## 系统架构

### 模块划分(W00 #1)

doctor-for-harness 四模块:

| 模块 | 职责 | 载体 |
|---|---|---|
| ① 规则权威模块 | 分层规则 + 归属判据 + 命名规范,一处权威 | HARNESS-RULES.md |
| ② 迁移流程模块 | 目录重组 + 相对链接重算 + 断链回归 | MIGRATION-FLOW 文档(或 SKILL.md 节) |
| ③ 校验模块 | 布局合规检查(命名 / ADR 编号 / 归档位置) | scripts/harness-check.py |
| ④ 演进留痕模块 | 组织变更记录,可回溯 | CHANGELOG(DESIGN.md 节) |

### 数据流(W00 #2)

```
规则权威模块(HARNESS-RULES.md) ← 唯一 source
   ├─→ 被 SKILL.md 引用(「分层见 HARNESS-RULES.md」)
   ├─→ 迁移流程按其执行
   └─→ 校验脚本按其检查
校验脚本输出违规清单 → 人决定是否迁移
迁移流程 → 触发演进留痕记录
```

## 技术选型

| 选型项 | 决策 | 被否决项 |
|---|---|---|
| 校验脚本实现(W00 #5) | 纯 Python 单文件 `scripts/harness-check.py`,标准库 pathlib/re,无第三方依赖 | 否决:第三方校验库(引入依赖,杀鸡用牛刀) |
| 脚本检查项(W00 #6) | 三合一:① 问卷命名正则 ② ADR 编号连续 ③ 归档位置;保守实现只报格式偏离;**+ design/ 分层 report 模式**(grill-Q Q1/Q8:列出裸放/子目录现状供人审,不判对错) | 否决:① 内容语义判断(误报风险高,非脚本职责);② 分层强校验(判定句需语义,report 模式已覆盖人工核对) |
| 迁移工具形态(W00 #7) | 不写自动化迁移脚本;手动 + 文档流程 + 校验脚本验证 | 否决:自动化迁移工具(一次性工作,过度工程) |
| 断链回归手段(W00 #8) | 复用既有方法:grep 相对链接 + 校验脚本 + 人工抽查 | 否决:新造链接检查工具(先例已有成熟做法) |

## 接口契约

| 接口 | 规格 |
|---|---|
| 校验脚本(W00 #9) | `python3 scripts/harness-check.py [harness_root]` → stdout 违规清单(逐条「路径: 违规类型」)+ exit 0(违规存在也 0,人读输出决定);`--json` 可选结构化输出 |
| 规则引用(W00 #10) | HARNESS-RULES.md 是唯一权威源;各 SKILL.md 落盘路径句保持硬编码 `harness/`(ADR-0011),不内联复制分层规则,只引用「分层见 HARNESS-RULES.md」 |

## 部署与运维

| 项 | 决策 |
|---|---|
| 触发时机(W00 #11) | 手动触发为主(「分层一下」「校验 harness」);迁移作独立行动项带 DoD;校验发布前/定期可选;不进任何 skill 每次流程 |
| 演进留痕(W00 #12) | 组织变更记录在 `harness/design/doctor-harness/CHANGELOG.md`(或 DESIGN.md 节)——每次迁移/规则修订追加一条(日期 + 变更 + 原因) |

## 架构决策识别(H5)

| 候选决策 | ADR 三条件(难逆转 + 会困惑 + 真权衡) | 结论 |
|---|---|---|
| 分层规则是否 ADR(W00 #13) | 「平铺 vs 分层」真权衡 + 会困惑(现状混用无规则)+ 影响长期 | **已立 [ADR-0012](../../adr/0012-harness-layering-rule.md)**(W01 裁定) |
| 迁移行动项是否 ADR(W00 #14) | 迁移破坏既有链接(不可逆影响)+ 执行决策背景值得记录 | **已立 [ADR-0013](../../adr/0013-harness-layering-migration.md)**(W01 裁定) |