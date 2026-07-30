# CONTEXT — 术语表

> 纯术语表:只放概念定义,不放决策(见 [docs/adr/](adr/))与实现细节。
> 首次创建:2026-07-28。

## 双支柱

方法论的核心理念,相乘缺一为零(详见 [methodology_v3 §二](methodology/methodology_v3.md)):

- **第一支柱 · 以信息为核心**:与 AI 协作的本质是信息流转;瓶颈在有效上下文的质与量,以及对抗 AI 在信息真空中的幻觉式自作主张决策。
- **第二支柱 · 驾驭工程 = AI × 软件工程**:AI 是加速器,软件工程纪律(设计先行 / TDD / Code Review / ADR / 复盘)是骨架。

## 第一支柱术语分层(v3)

第一支柱相关术语的层级归属(详见 [methodology_v3 §2.1 / §1.2 / §5.1](methodology/methodology_v3.md)):

- **信息断层** = 返工的根源框架,分两类:人与人断层(由 AI 替代角色解决)、人与 AI 断层(由问答对齐解决);返工是其可见症状。
- **信息流转** = 过程模型:上下文进入模型,模型产出结果,结果沉淀为新的信息。
- **有效上下文** = 质量度量(度量层):不易产生幻觉、精准命中当前任务的信息量;经验值 200k 模型约 120k,1m 模型约 400k。
- **背景缺失** = 幻觉根因(机制层诱因):分 (a)(b) 两类(见下)。
- **信息真空** = 背景缺失的形象别名:AI 在其中自作主张的真空地带。
- **机制层 / 度量层 / 症状层** = 三层立论模型(因果链,非同级分类):机制层(AI 幻觉式自作主张决策,根因)→ 度量层(有效上下文)→ 症状层(返工)。
- **vibe coding** = 不交代背景、不设约束、AI 自由发挥的编程方式;方法论的首要治理场景。
- **(a)(b) 盲区** = 背景缺失两类:(a) 知道但没写 → preview / 问卷捕获;(b) 自己也不知道(隐含假设)→ grill 对抗逼出。

## 5 环节闭环

开发工作流主路径(详见 [methodology_v3 §四](methodology/methodology_v3.md)):design-Q → grill-Q → dogfood → long-running → retro;delegate 横切。grill-Q / dogfood / retro / delegate 是正交方法论,可任意环节插入,不锁死在线性阶段。

## Grill 家族

决策引擎,分两族(详见 [methodology_v3 §5.3](methodology/methodology_v3.md)):

- **批量问卷族**:design-Q / grill-Q / retro-Q(多波次问卷,离线作答)。
- **单点深钻族**:grill / grill-with-docs(一问一答,逐轮等待)。

## skill 家族

方法论的可执行载体,7 个核心 skill:design-questionnaire / grill-questionnaire / grill / grill-with-docs / retro-questionnaire / long-running-agent / delegate。本仓库为其唯一 source of truth([ADR-0001](adr/0001-source-of-truth.md))。

## Claude Code(在本仓库的定位)

定语,指方法论的首个实践载体;非仓库品牌、非「专属」。方法论理念(双支柱 / 5 环节 / Grill)工具无关、可迁移;skill 直接运行依赖 Claude Code 的 AskUserQuestion / subagent / SKILL.md([OD-2](OPEN-DECISIONS.md))。

## 脱敏

本仓库内容已去除作者项目名 / 路径 / 个人标识(发布门槛见 [OD-1](OPEN-DECISIONS.md),检查脚本 [scripts/desensitize.py](../scripts/desensitize.py))。归档问卷中的「项目A / 项目B …」为脱敏占位。
