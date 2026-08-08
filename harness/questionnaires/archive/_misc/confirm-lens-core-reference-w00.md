---
mode: confirm
wave: 0
stage: confirm
created: 2026-08-05
status: archived
---
# 问卷 confirm W00 · 定界转出记录(action-Q,未生成 confirm-list)

> **行动**:参考同级项目「项目A」的现有架构(除了非追踪项),优化本项目的哲学和具体的架构。(「项目A」为脱敏占位,映射见本地 desensitize_map.local.json,本文件不复述真实名。)
>
> **本记录不是 confirm-list**:定界检查判定该行动为 feature 级,按 action-Q 定界规则「不启动本 skill,提醒转专用 skill」直接转出。本文件 = 调研发现 + 定界结论 + 路线决策留痕,作为 design-Q 的输入留档(action-Q 升级转出协议)。

## 一、触发与定界

- **触发**:用户显式调用 /action-questionnaire,参数「参考同级项目『项目A』的现有架构(除了非追踪项),我想要优化本项目的哲学和具体的架构」。(原话中的真实名已按映射表替换为占位,语义未变。)
- **定界结论:feature 级行动** —— ①「优化哲学」触及 canonical(methodology_v3 / philosophy_v1,ADR-0007 + OD-4 母本标注);②「优化架构」 = 多文件结构性变更(CLAUDE.md / README / docs 布局 / 可能新增 AGENTS.md);③ 需要设计先行。依据 action-Q SKILL.md 定界:「是 → 不启动本 skill,提醒转 design-Q(需设计)/ grill-Q(有工件要压测)/ long-running(跨会话实现)」。

## 二、调研发现(铁律 2:先核实再定界;证据 = git status / 文件读取实测)

### 「非追踪项」界定

- 「项目A」git 实测(`git status --short`):非追踪项 = `.claude/`(kimi settings.local.json)、`.codex/`、`dist/`(构建产物)。**「非追踪项」理解 = git untracked 三件,参考时排除**。〔代码实测〕
- 「项目A」的 `.gitignore` 含 waste/ 不入忽略的注释(「waste/ 不在此忽略 —— 废弃文件需入库归档并记 waste.log,绝不直接删除」)——与本项目 waste 纪律同源。

### 「项目A」可参考架构要素(排除非追踪项后)

| 要素 | 「项目A」做法 | 本项目现状 | 对照结论 |
|---|---|---|---|
| 规则单源 | AGENTS.md 全量规则(Codex 入口,「完整项目规则只维护在 AGENTS.md」) | 无 AGENTS.md | ❌ 缺失 |
| 入口文件 | CLAUDE.md 极简(启动顺序 + 规范顺序 + 约束,明言「不复制 AGENTS.md 全部规则」) | CLAUDE.md 9.5KB 长篇(方法论摘要 + skill 家族 + 铁律 + 状态 + 导航全塞) | ⚠️ 篇幅/职责可对照 |
| 分级架构 | L1 端到端总览 / L2 行为·不变量·验收边界 / L3 实现分册×8;冲突时 L2 优先,其他冲突必须说明不得静默选择 | 方法论三块(methodology_v3 自包含 + philosophy + practical)+ ADR 体系(ADR = source of truth) | ⚠️ 分级与冲突优先级可对照 |
| 术语表 | CONTEXT.md 统一术语 | CONTEXT.md 已有(纯术语表) | ✅ 已具备 |
| 导航 | README「文档入口」表 + AGENTS「按改动选读」表 | 导航散在 CLAUDE.md / README / 方法论三处 | ⚠️ 入口不统一 |
| 状态声明 | README 明言「架构基线,尚无可运行实现」 | CLAUDE.md 状态节 | ✅ 已具备 |
| 约束清单 | AGENTS.md「架构硬约束」不得做清单 | 编辑铁律散在 CLAUDE.md | ⚠️ 可对照 |
| 文档头标记 | 各文档头 `<!-- Hallmark · pre-emit critique: P5 H5 E5 S5 R5 V4 -->` 自我审查标记 | 无 | ℹ️ 可讨论 |

### 本项目相关现状(已核实)

- TODO「⏳ design-questionnaire 正式设计:vision → HLD → LLD」长期未跑;本行动本质上 = 该待办 + 「项目A」参考输入。
- 仓库自身 repo 级 design-Q 未跑(design-Q / grill-Q / retro-Q 目录内 docs/ 是 dogfood 产物,不构成本仓库自身设计文档)。
- 方法论 canonical 母本标注(OD-4):methodology + philosophy 文件改动受四处锁定保护;实操文件走轻量流程。
- ADR-0007:方法论三块拆分(methodology_v3 自包含 / philosophy_v1 / practical_v1 非 canonical)。
- 仓库已脱敏(OD-1):「项目A」= 同级项目真实名的映射占位(映射表本地存放,见 scripts/desensitize_map.local.json);本文档全程按占位书写。

## 三、路线决策(AskUserQuestion 逐字转写,2026-08-05)

**问题**:「参考『项目A』优化本项目哲学与架构」是 feature 级行动(动 canonical + 多文件结构性变更),需转专用设计流程。走哪条路线?
- 选项:A. 转 design-Q 正式设计(推荐);B. 先 grill-Q 压测再设计;C. 先出 confirm-list 对齐范围。
- **用户答(单选)**:「转 design-Q 正式设计(推荐)」

## 四、下一步

1. 归档本文件(只移不删,已入 harness/questionnaires/archive/)。
2. 转 design-Q:调用 design-questionnaire skill,输入 = 本记录 + 行动描述 + 「项目A」参考面。
3. design-Q 完成后,方法论/仓库架构修订遵守 OD-4 母本标注与 ADR 体系。

---

## 处理报告摘要(归档时追加,2026-08-05)

- 流程:定界(第 0 步)→ 调研(第 1 步,实测「项目A」结构 + git 非追踪项)→ 定界结论 feature 级 → 升级转出(第 5 步)→ 用户选「转 design-Q 正式设计」。
- 未生成 confirm-list(W00 定界直接转出,非「跳过作答」)。
- 落盘:本归档文件;无 ADR / OD / CONTEXT 升格(设计决策留待 design-Q 产出)。
- 脱敏门:写入后全仓库扫描 0 命中(2026-08-05 验证)。
- 覆盖度:隐式骨架六要素中,目标/输入/依赖已调研确认;输出/约束/边界为 design-Q 的设计对象,不在本 skill 深挖。
