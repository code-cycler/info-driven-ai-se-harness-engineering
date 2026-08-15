---
mode: feature
wave: 0
stage: lld
created: 2026-08-15
status: processed
---
# 问卷 feature-designq-digital-levels lld W00 · Preview(决策默认值 yes/no 速答)

> **本波是 preview 预答层**(独立 wave 0):AI 有明确默认倾向的决策点逐条列出,人只做 yes/no 速答。
>
> **作答规则**:勾 `[x]` = 采纳默认;留空 = 不采纳转 W01 深究;单向门要点永不预勾;本波不用 🤔;「大体同意但要改」→ 留空转 W01。

**lld 阶段目标**:把 VISION/HLD 定案的架构转成**构建路径**——阶段拆分(依赖链)、每阶段详细设计与 DoD、文件级改动清单。对应骨架 L1 阶段拆分 / L2 详细设计 / L3 接口规格 / L4 DoD / L5 依赖与预估。

## 决策默认值清单

**阶段拆分(L1,依赖链序)**

- [X]  **1 八阶段拆分**:P0 双向同步(全局⇄项目一致起点,压测 Q2-C)→ P1 backup(同步后三 skill 目录 diff 存档 `global-backup/`)→ P2 design-Q 主改造(STAGE-SKELETONS 重写 + SKILL.md 定模/闸门/停点)→ P3 引擎四副本同步(stage 枚举 + 命名两处 × 四 skill,Q1-C)→ P4 long-running 双模式改造 → P5 doctor 拓展三件套(HARNESS-RULES 增补 + SKILL.md 触发词 + harness-check.py)→ P6 装载 + DOGFOOD 双案例 → P7 回灌 + 收尾 retro。每阶段独立可验证(依赖:P2–P5 依赖 P0/P1;P6 依赖 P2–P5 全完成;P7 依赖 P6 人确认) 〔HLD §6 流程 + L1 判据「不能独立验证 = 粒度太粗」〕
- [X]  **2 P2–P5 的落盘侧**:规格改造全部在**全局版**进行(实验语义),每阶段变更清单 + 全量 diff 记录到本 feature 目录 `changesets/P<n>.patch`;本项目 skills/ 全程不动(P0 同步例外——双向同步本身就是要动项目版) 〔OD-24 + W00 #17〕

**详细设计要点(L2)**

- [X]  **3 P2 STAGE-SKELETONS 重写范围**:四部分(总则/最小必含总览/模板库/协议集)按 HLD §2–§3 已定案结构;旧三档坍缩表替换为「最小 1 层 + L0 自检」;判别法则升级三问;**头部导览块**;旧术语(VISION/HLD/LLD)保留为别名注记 〔HLD 契约 + W00 #12/#16〕
- [X]  **4 P4 long-running 改动清单**:SKILL.md——§3 补「任务包」字段规范;§5.3 反推规则改 LN 制(最低构建语义层 + L0 兜底);§5.4 衔接节补停点语义;新增「准备模式 / 执行模式」节(含多 worktree);§6/§8/§10 三处禁令限定式改写(provisional);description 触发词补「准备模式/执行模式/多 worktree」 〔HLD §4 全部裁决〕
- [X]  **5 P5 doctor 改动清单**:HARNESS-RULES——增补「六、层级设计文档规则」(LN 命名/布局/豁免清单)+「七、存量结构改造流程」(盘点→映射→标待补→人确认成档)+ 旧档迁移映射表;SKILL.md 触发词补「层级改造/迁移/存量规范化」;harness-check.py 加 LN 命名校验 + L0 缺失提示 + 存量豁免 〔HLD §2 + W00 #10–#13〕
- [X]  **6 design-Q SKILL.md 停点实现**:§5 收尾节新增「多线程开工询问」步骤(AskUserQuestion:单线程/多线程),与既有 grill-Q/long-running 衔接提议串联为固定收尾链(压测→停点→衔接) 〔补充声明 3 + HLD §4〕

**DoD 与回归(L4)**

- [X]  **7 每阶段 DoD**:P0 = diff -rq 三 skill 两侧一致;P1 = backup 目录三套 patch 齐全;P2–P5 = 各文件改动 grep 锚点核验 + 变更清单记录;P6 = DOGFOOD 双案例走通三要素(VISION V4 判据)+ 过程信号即时留痕;P7 = 回灌后 harness-check exit=0 + 脱敏 0 + OD-24 关闭 + retro-Q 完成 〔L4 可脚本化优先〕
- [X]  **8 回归验证每阶段跑**:harness-check.py + 脱敏门(P2–P5 全局侧改动也要跑——全局版无脱敏要求但项目侧记录变更时要过一遍防带入) 〔L4 回归 + OD-1〕

**依赖与预估(L5)**

- [X]  **9 工作量排序与并行性**:P0/P1 一次会话可完成(轻);P2 最重(骨架重写 + 模板库);P3 轻(两处 × 四副本);P4 中;P5 中(含脚本);P6 跨会话(DOGFOOD 案例实际跑);P7 轻。总预估 3–4 个工作会话(P6 需真实案例不可压缩) 〔L5〕
- [X]  **10 DOGFOOD 案例载体**:案例 1(小,2 层)= DOGFOOD 沙盒下一个 skill/脚本级小工具;案例 2(中,3 层含插层)= DOGFOOD 沙盒下一个中型功能;两案例均人确认可用为收口;具体题材 P6 时人选题 〔OD-24 + VISION V4〕

## 补充声明

<任何想补充的话:阶段拆分调整、DoD 修正、案例偏好……没有就留空。agent 处理时必读>long-running-agent 默认还是单agent，多agent作拓展能力，最好是利用Claude code 多agent的相互通信的能力。我会优先测试docter H的能力

---

## 处理摘要(2026-08-16)

- **采纳**:10/10 全采纳,0 留空,0 转 W01。
- **补充声明 2 条裁决**:① **long-running 默认单 agent,多 agent = 拓展能力**,实现优先利用 Claude Code 原生多 agent 相互通信能力(主会话 spawn 后台 agent 各驻 worktree + SendMessage 通信 + task-notification 收结果)——HLD §4 与架构图已同步修正;② **doctor-H 优先测试**——执行序调整为 P0→P1→**P2 doctor 先行(含用户优先能力测试)**→P3 design-Q→P4 引擎→P5 long-running→P6 DOGFOOD→P7 回灌。
- **落盘**:[HLD](../../design/designq-digital-levels/HLD.md) §4 单/多 agent 定位 + 执行模式改多 agent 通信实现;[LLD](../../design/designq-digital-levels/LLD.md) 全文(八阶段 doctor 优先序 + 文件级清单 + LN/任务包 schema + DoD + 预估 3–4 会话)。
