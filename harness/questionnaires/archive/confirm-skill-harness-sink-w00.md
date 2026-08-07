---
mode: feature
wave: w00
stage: confirm
created: 2026-08-07
status: archived
slug: skill-harness-sink
title: 对齐「skill 生成文件落 harness / 方案 R」的现状理解
---
# 细节确认清单(confirm-list)

> 触发:审查发现「本仓库 skills/ 缺方案 R、与 ~/.claude/skills/ 漂移」后,用户提出「没理解方案 R,构想是所有 skill 生成文件放 harness,先对齐现状再定修复方案」。
> 本轮**只对齐现状理解**,不确定修复方案。勾 `[x]` = AI 理解正确,留空 = 理解有误或要改(留空项转深究)。
> AI 的理解依据:skill-spec-revamp LLD、~/.claude 版 design-Q SKILL.md、本仓库 CLAUDE.md、feature_list.json、全量 diff 实测。

## A. 方案 R 是什么(核对你的理解)

- [ ]  **A1. 方案 R =「落盘根配置化」**——skill 运行时生成的文件(问卷/设计文档/ADR)放宿主项目的哪个目录,不写死,而是读项目 CLAUDE.md 的声明来定。(`落盘根` = design/ + questionnaires/ + adr/ 共用的前缀)
  - 来源:skill-spec-revamp/LLD.md §2.2/§2.3
- [ ]  **A2. 方案 R 三步**:① 读项目 CLAUDE.md,匹配声明关键词(「落盘速查/harness 区/设计产物落」等);② 没声明则默认 `harness/`;③ 落盘前用 AskUserQuestion 跟用户确认一次「放 X 对吗」。
  - 来源:~/.claude/skills/design-questionnaire/SKILL.md:54-59(含方案 R 版)
- [ ]  **A3. 方案 R ≠「改放别处」**。本仓库 CLAUDE.md 速查表声明了 harness/,方案 R 命中后**结果就是放 harness/**——与你的构想「所有 skill 文件放 harness」一致。
  - 来源:本仓库 CLAUDE.md「落盘路径速查表」节
- [ ]  **A4. 方案 R 的意义是「通用化 + 可确认」**——让 skill 在别的项目也能入乡随俗(别的项目可声明别的根),并在落盘前给你一次确认机会;**不是**改变本仓库「放 harness」的结果。
  - 来源:skill-spec-revamp/LLD.md §L3(路径决定接口)

## B. 现状(核对事实)

- [ ]  **B1. 你实际运行的是 `~/.claude/skills/`**(含方案 R);本仓库 `skills/` 是**发布镜像**(硬编码 harness/、**无方案 R**)。本次 /action-questionnaire 加载的 base directory 就是 `~/.claude/skills/action-questionnaire`。
  - 来源:command 元信息 + diff 实测(仓库版 grep「落盘根」0 处,~/.claude 版 6 处)
- [ ]  **B2. 两套系统性漂移**:8 个 skill 中 6 个不同(action-Q/delegate/design-Q/grill-Q/grill-with-docs/retro-Q),约 30 个文件。design-Q 差最多(STAGE-SKELETONS.md 75 行 = 方案 R 骨架改造)。
  - 来源:全量 diff 扫描
- [ ]  **B3. 漂移有两个独立来源**:① 方案 R 只落在 ~/.claude、未回灌本仓库;② 脱敏差异——本仓库是脱敏版(项目A/B/C/宿主项目),~/.claude 是未脱敏开发版(真实项目名)。
  - 来源:delegate/DESIGN.md diff(项目名对照)
- [ ]  **B4. feature_list.json F007–F010 标 `passes:true`,但行号(SKILL:56 / PROCESSING-RULES:28 / DESIGN:99-102)对应的是 ~/.claude 版,不是仓库版**。即「测试通过」的是 ~/.claude 版;本仓库 skills/ 既无方案 R,这个 passes 标记对仓库读者构成误导。
  - 来源:feature_list.json notes + git show 9d870bf --stat(未碰 skills/)

## C. 你的构想 vs 方案 R

- [ ]  **C1. 你的构想「所有 skill 生成文件放 harness」= 本仓库的落盘策略 = 方案 R 在本仓库命中后的运行结果**。两者**不矛盾**——方案 R 在本仓库就是放 harness。
  - 来源:A3 + 本仓库 CLAUDE.md 声明

> **本轮不答(留到对齐后定修复方案时)**:你要的是「结果放 harness」即可(硬编码 harness/ 也达成),还是「机制配置化」(方案 R,通用 + 落盘前确认)?这是修复方案的关键分叉,核对完现状我们再定。

---

## 补充声明(✍️ 自由书写,agent 处理时必读) 放弃此方案，硬性要求所有harness文件放到 项目根/harness/ 文件夹下

<!--
(你对方案 R 的疑问、现状描述需要纠正的地方、构想里我没领会到的点,写在这里)
-->

---

## 处理报告(2026-08-07,agent 解析)

- **作答**:A1–A4 / B1–B4 / C1 全部留空(未逐条勾选);补充声明 = 「放弃此方案,硬性要求所有 harness 文件放到 项目根/harness/ 文件夹下」。
- **解读**:用户不对齐方案 R 的机制细节(A 节),直接给决策——**放弃方案 R(配置化),回归硬编码 `<项目根>/harness/`**。即 C 节「本轮不答」的分叉,用户选了「结果放 harness」并进一步放弃方案 R 机制本身。
- **现状含义**:本仓库 `skills/`(硬编码 `harness/`)符合用户要求;`~/.claude/skills/`(方案 R 配置化)+ feature_list F007–F010(passes:true)+ skill-spec-revamp 设计文档 = 待撤销/修订。
- **去问**:
  1. **[已转 AskUserQuestion]**「所有 harness 文件」范围:仅 design/questionnaires/adr(三区模型 harness 区),还是连 CONTEXT/OD/TODO/retro 也挪进 harness/?
  2. 撤销方案 R 的执行:跨 `~/.claude` 8 skill + feature_list + 设计文档,属多文件结构性变更 → 建议转 long-running-agent 驱动。
- **落盘**:本 confirm-list 归档(决策留痕);harness 范围确认后启动撤销执行。
