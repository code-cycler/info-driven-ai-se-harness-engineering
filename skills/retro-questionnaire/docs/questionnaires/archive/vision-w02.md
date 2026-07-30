---
mode: init
wave: 2
stage: vision
created: 2026-07-23
status: archived
---
# 问卷 vision W2 · 复盘问题的修正跟踪

> 填写规则:
>
> 1. 每题勾选 `[x]`;默认单选,标「(多选)」可勾多个,选项数不限
> 2. ★ = 推荐选项,附推荐理由
> 3. 每题末尾 🤔 是逃生舱:勾了 = 我定不了 → agent 走降风险协议,绝不重问
> 4. 选项都不合适 → 在 ✍️ 自定义 后自由书写
> 5. 标「条件:Qn 选 X 才答」的是内联浅分支,条件不满足直接跳过

项目:retro-questionnaire(复盘问卷 skill)
出题依据:W1-Q7 自定义答案「复盘时发现的问题没有及时修正」——风险已落盘 VISION#风险与约束,但缓解机制未定,本波追问。

## Q1. 为避免「复盘发现的问题没有及时修正」,retro 产物怎么跟踪问题修正?   [落盘: VISION#核心场景]

- [ ]  A. retro 文档固定含「Action Items」节:每项 = 问题 → 行动 → 核验时机;下一阶段 DoD 核验时先核上阶段 action items  ★推荐 —— 闭环嵌入现有 DoD 流程,不引入新系统;与「阶段末触发」(W1-Q2)正好衔接
- [ ]  B. Action items 转入 OPEN-DECISIONS 或任务系统跟踪 —— OD 记的是未决决策不是行动项;引入外部依赖
- [ ]  C. 只记录不跟踪,接受风险 —— 诚实,但你在 W1 主动提出这条风险,说明不接受
- [ ]  🤔 我定不了 → 推迟/降风险

- ✍️ 自定义: __________在design-questionnaire中补充设计一个TODOmd文档，及时阅读

### Q1.1 (条件: Q1 选 A 才答) Action items 的核验结果(已修/未修)记在哪?   [落盘: VISION#核心场景]

- [ ]  A. 下一份 retro 文档开头设「上阶段 Action Items 回顾」节  ★推荐 —— 复盘链自包含,跨文档可追溯,原文档不动
- [ ]  B. 更新原 retro 文档(出 _vN+1 新版本) —— 符合版本命名规范,但回顾时要翻旧版,链路易断
- [ ]  🤔 我定不了 → 推迟/降风险

- ✍️ 自定义: __________


补充声明：在questionnaire系列skill中，问卷模版中末尾添加一个补充声明项；当新一波问题数不超过2个时，使用提问skill

---

## 处理报告摘要(2026-07-23)

- 落盘:Q1 ✍️自定义「TODO.md 文档 + 及时阅读」→ [../../VISION.md](../../VISION.md)#核心场景(行动项跟踪机制);Q1.1 条件未满足,不重出
- 更新文件:retro-questionnaire/docs/VISION.md
- 异常:无(Q1 未勾选但有自定义,有效;Q1.1 条件不满足未答,忽略)
- 逃生舱:无
- 补充声明处理(两条规格反馈,已即时修规格):
  1. 问卷模板末尾加「补充声明」区 → 已改 design-questionnaire/QUESTIONNAIRE-FORMAT.md
  2. 新一波问题数 ≤ 2 时改用提问(AskUserQuestion),不出问卷文件 → 已改 design-questionnaire/SKILL.md 与 PROCESSING-RULES.md
- 覆盖度:骨架 V1–V6 全覆盖,动态盲点清零 → 本阶段再无可盘问的信息,进入阶段闸门
