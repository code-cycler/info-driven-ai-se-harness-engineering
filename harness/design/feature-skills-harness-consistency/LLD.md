# LLD · 撤销方案 R + 重建 skills/ 一致性(分步执行规格)

> 来源:hld W00(D1–D8 全采纳)+ [HLD.md](./HLD.md)。本文 = 实现期 source of truth;long-running-agent 据此执行。
> dogfood 声明:本 LLD 按 design-Q lld 骨架写(L1–L5 最小必含),坍缩 vision(hld 已合并目标)。

## L1 阶段拆分(执行批次,给 long-running 的 features)

依赖链:**P1 → P2/P3(可并行)→ P4 → P5 → P6**。P1 决策先行;P2(仓库回灌)与 P3(~/.claude 撤销)操作不同文件可并行;P4/P5 善后;P6 验证收口。

| 阶段 | 目标 | 关键动作 | 独立 DoD |
|---|---|---|---|
| **P1** | 立 ADR-0011 | 落「放弃方案 R 回归硬编码 harness/」决策(背景/决策/替代/后果);hld D1–D8 + 本 LLD 引用 | ADR-0011 存在 + 三条件论证在位 |
| **P2** | 仓库 `skills/` 回灌 | 从 `~/.claude/skills/` 合并**非路径改动**(F007 骨架 + dogfood 修订)到仓库,**路径保持硬编码 `harness/`**;真实名→占位脱敏 | 仓库 skills/ grep「落盘根\|`<根>`\|确定落盘\|声明命中」0 命中 + 脱敏门 0 + F007 内容在位 |
| **P3** | `~/.claude/skills/` 撤销方案 R | design-Q/grill-Q/retro-Q/action-Q 的 PROCESSING-RULES 落盘映射 `<根>`→`harness/`、SKILL「确定落盘根」子步删除、QUESTIONNAIRE-FORMAT 文件约定、long-running §5.3、design-Q DESIGN D23/D26 撤销;**保留真实名** | ~/.claude grep「落盘根\|`<根>`\|确定落盘\|声明命中」0 命中 + F007/dogfood 保留 |
| **P4** | feature_list 标注 | F008/F009/F010 标「方案 R 已放弃,撤销」+ passes 改回 false(不删 notes);F007 标「保留、已回灌」;追加 F011–F016 本 feature | F008/09/10 passes=false + 撤销标注在位 + 历史notes 留存 |
| **P5** | 设计文档标注 | `harness/design/skill-spec-revamp/` 三件(LLD/HLD/VISION)顶部加「路径配置化(方案 R)部分 2026-08-07 放弃,回归硬编码;骨架(F007)部分保留」;**不删** | 三文件顶部标注在位 |
| **P6** | 同步验证 + 脱敏门 | 仓库 `skills/` vs `~/.claude/skills/` 全量 diff:仅剩脱敏差异(真实名 vs 占位);`python3 scripts/desensitize.py .` 0 命中 | diff 仅脱敏差异 + 脱敏门 0 + 8 skill 路径硬编码 harness/ |

## L2 详细设计(判定规则 · 每处差异怎么处理)

逐文件 diff 时,按差异性质套规则(非文件级 cp,是改动级合并):

| 差异性质 | 判据(grep) | 处理 |
|---|---|---|
| 方案 R 路径配置化 | `落盘根`/`<根>`/`确定落盘`/`声明命中`/`CLAUDE.md 声明优先` | **撤销**(P2 仓库无此问题;P3 ~/.claude 改回硬编码 `harness/`) |
| F007 骨架内容 | `判别法则`/`最小必含`/`坍缩.*分档`/`反简化` | **回灌仓库**(P2,~/.claude 已有) |
| dogfood/内容增强 | 各 skill 修订(逐文件人审) | **回灌仓库**(P2,脱敏) |
| 项目名脱敏 | 真实项目名(脱敏脚本命中项) | **保留差异**(仓库用占位 项目A/B/C/某库/某种类;~/.claude 用真实名) |

关键文件清单(P3 撤销操作的目标):
- design-questionnaire:SKILL.md(删「确定落盘根」子步)、PROCESSING-RULES.md(落盘映射)、QUESTIONNAIRE-FORMAT.md(文件约定)、DESIGN.md(D23 路径/D26)
- grill-questionnaire / retro-questionnaire / action-questionnaire:PROCESSING-RULES.md + SKILL.md + QUESTIONNAIRE-FORMAT.md
- long-running-agent:SKILL.md §5.3

## L3 接口规格

无外部接口(纯 skill Markdown 规格)。同步契约见 HLD「同步契约」:仓库(脱敏)= 权威,~/.claude(真实名)= 副本,改仓库后对 ~/.claude 做同样撤销操作(非 cp,因脱敏不同)。

## L4 DoD(可脚本化)

每步必跑:
1. **路径硬编码回归**:目标 skill 文件 grep「落盘根\|`<根>`\|确定落盘\|声明命中\|CLAUDE.md 声明优先」**0 命中**(P2 查仓库、P3 查 ~/.claude)
2. **F007 保留**:design-Q STAGE-SKELETONS grep「判别法则\|最小必含\|坍缩.*分档」**>0**(P2 后仓库也有)
3. **脱敏门**:`python3 scripts/desensitize.py .` **0 命中**(P2/P6)
4. **同步一致**(P6):仓库 vs ~/.claude diff 仅脱敏差异(真实名/占位),无内容分歧
5. **feature_list 真实**(P4):F008/09/10 passes=false(不再误导)

## L5 依赖与预估

- **外部依赖**:无(纯 Markdown;~/.claude 是本地文件可直接改)
- **工作量排序**:P3(~/.claude 撤销,8 skill 多文件)> P2(仓库回灌,逐文件脱敏合并)> P1/P4/P5(善后)> P6(验证)
- **执行驱动**:long-running-agent(feature_list 从 P1–P6 反推,追加 F011–F016 到现有 feature_list.json);P2 逐文件脱敏合并需人审样本
- **单向门**:无(P3 ~/.claude 改动可逆;P2 回灌有 git 历史);ADR-0011 立案 = 决策记录,双向门

## long-running 衔接

lld 完成 → feature_list.json 追加 F011–F016(P1–P6 对应)→ long-running-agent 从落盘文件重建(feature_list + 本 LLD + HLD),逐阶段执行,每阶段 DoD 全绿才 passes:true。P2(脱敏合并)与 P6(脱敏门)涉及 OD-1 发布门槛,执行时人审。
