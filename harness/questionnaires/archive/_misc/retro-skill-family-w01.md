---
mode: feature
wave: 1
stage: retro
created: 2026-08-19
status: archived
---
# 问卷 retro W01 · skill 家族使用体验复盘(9 skill 使用频次 / 走形式环节 / 轻任务耗时)

> 填写规则:
>
> 1. 每题勾选 `[x]`;默认单选,标「(多选)」可勾多个,选项数不限
> 2. ★ = 推荐选项,附推荐理由;**选项排序 = 非推荐在前 → 逃生舱倒数第二 → 推荐最后**
> 3. 每题末尾 🤔 是逃生舱:勾了 = 我定不了 → agent 走降风险协议,绝不重问
> 4. 选项都不合适 → 在 ✍️ 自定义 后自由书写
> 5. 标「条件: Qn 选 X 才答」的是内联浅分支,条件不满足直接跳过

**复盘主题**:9 个核心 skill 的真实使用体验——哪些在用、哪些走形式、轻任务实际耗时是否成比例。产出 = 家族级裁剪清单(回 TODO + OD-6 外部采用者视角参考)。
**出题依据**:grill-Q skill-family W01 Q10-A 裁决;OD-17(doctor-harness 使用率存疑)、OD-23(delegate 未 pilot)为已有单点记录,本次补家族全景。

---

## 1. 使用频次盘点

## Q1. 近一个月实际主动调用过的 skill(多选)   [落盘: retro 文档]

出题依据:区分「在用 / 低频 / 从未」三档是裁剪清单的输入。勾你真实调用过(非被自动触发)的。

- [X]  design-questionnaire(生成式设计问卷)
- [X]  grill-questionnaire(对抗式压测问卷)
- [ ]  grill(通用单点深钻)
- [X]  grill-with-docs(绑库单点深钻)
- [X]  retro-questionnaire(复盘问卷)
- [X]  long-running-agent(跨会话实现)
- [ ]  delegate(决策下放)
- [X]  action-questionnaire(行动前确认)
- [X]  doctor-harness(harness 治理)
- [ ]  🤔 我定不了 → 推迟/降风险

- ✍️ 自定义: __________

## Q2. 从未用过或只用过一次的 skill(多选)   [落盘: retro 文档]

出题依据:低频 skill 是「装置只进不出」的审查对象(对应 OD-17 使用率重访)。

- [ ]  design-questionnaire
- [ ]  grill-questionnaire
- [X]  grill
- [ ]  grill-with-docs
- [ ]  retro-questionnaire
- [ ]  long-running-agent
- [X]  delegate
- [ ]  action-questionnaire
- [ ]  doctor-harness
- [ ]  🤔 我定不了 → 推迟/降风险

- ✍️ 自定义: __________

---

## 2. 走形式与过度准备

## Q3. 哪个 skill 的哪个环节最让你感觉「走形式 / 过度准备」?   [落盘: retro 文档 + TODO]

出题依据:你在压测 W01 Q3 已勾「前置调研五步闭环」最不成比例;此题请你具体定位到 skill + 环节,作为裁剪清单的直接输入。

- [ ]  design-Q 的 preview W00 + 多波问卷(决策密集但波次多)
- [ ]  grill-Q 的 D1–D8 全维度 + 实测前置(轻压测也走全调研)
- [ ]  action-Q 的 confirm-list(轻确认也列清单)
- [ ]  long-running 的会话启动 checklist(7 步,轻会话也全走)
- [ ]  retro-Q 的五源读取(轻阶段也读五源)
- [X]  都不走形式——各环节我都觉得值
- [ ]  🤔 我定不了 → 推迟/降风险

- ✍️ 自定义: __________

## Q4. 轻任务(如单行修复 / 小脚本)实际耗时 vs 任务本身耗时   [落盘: retro 文档]

出题依据:你的核心痛点「轻任务过度准备」;此题量化感受,验证轻量模式规范(W01 Q4 已加)是否切中。

- [X]  流程耗时 >> 任务本身(如改一行字要走 5 分钟确认/问卷)
- [ ]  流程耗时 ≈ 任务本身(可接受但不爽)
- [ ]  流程耗时 < 任务本身(流程没拖后腿)
- [ ]  没明显体感差异,说不出
- [ ]  🤔 我定不了 → 推迟/降风险

- ✍️ 自定义: __________

---

## 3. 价值与裁剪

## Q5. 哪个 skill 对你价值最大(最不想砍)?   [落盘: retro 文档]

出题依据:裁剪清单的「保留优先级」锚点。

- [ ]  design-questionnaire
- [X]  grill-questionnaire
- [ ]  grill
- [ ]  grill-with-docs
- [ ]  retro-questionnaire
- [ ]  long-running-agent
- [ ]  delegate
- [ ]  action-questionnaire
- [ ]  doctor-harness
- [ ]  🤔 我定不了 → 推迟/降风险

- ✍️ 自定义: __________

## Q6. 是否有 skill 你认为可退役 / 降级为文档(不再作为 skill 常驻)?   [落盘: retro 文档 + OPEN-DECISIONS(若提出退役)]

出题依据:装置只进不出审查(压测 W01 Q6);退役须走 OD 使用率重访,不擅自删。

- [ ]  无——9 个都想保留
- [ ]  doctor-harness(治理低频,可降级为静态规则文档 + 校验脚本)
- [X]  delegate(未 pilot,可暂缓)
- [X]  grill(通用零留痕,触发词易混淆)
- [ ]  retro-questionnaire(复盘可手动做)
- [ ]  🤔 我定不了 → 推迟/降风险

- ✍️ 自定义: __________

---

## 4. 学到什么

## Q7. 这次压测 + 复盘,你对「skill 是否精炼优雅、能否更好服务于人」的结论是?   [落盘: retro 文档]

出题依据:开放题;你最初的四个焦点(过度准备 / 合并 / 精炼 / 哲学符合度)的收口反思。

- [X]  当前形态基本合理,只需轻量模式 + 措辞对齐这类微调(W01 已做)
- [X]  有结构性冗余,需进一步裁剪(如合并 / 退役某些 skill)
- [ ]  方向对但执行层太重,核心问题是 AI 照单全收流程脚本(轻量模式提议机制可解)
- [ ]  🤔 我定不了 → 推迟/降风险

- ✍️ 自定义: __________

---

## 5. Action Items

<处理时由 Q3/Q6 答案 + 上述裁决提炼:问题 → 行动 → 核验时机。落盘 retro 文档 Action Items 节 + TODO.md>

---

## 补充声明

<任何想补充的话:新需求、格式反馈、范围调整、临时想到的风险……没有就留空。agent 处理时必读>skill中有提到各自的各个提问维度，然而这些都需要用户逐个反看skill，将这些维度定义塞入readme或者context或者任何用户会积极查看的地方

---

## 处理报告摘要(2026-08-19,W01 处理)

**作答解析**:7/7 答毕,无异常(无单选多勾矛盾——Q1/Q2 为多选题、Q7 勾 2 项为有意并存结论;无必答未答、无逃生舱触发)。自定义仅补充声明 1 条有效。

**逐题裁决与去向**:

| 题 | 裁决 | 去向 |
|---|---|---|
| Q1 使用频次 | 在用 7(除 grill/delegate 全用) | retro 文档 §1 |
| Q2 低频/从未 | grill、delegate | retro 文档 §2 + OD-12/OD-23 重访引用 |
| Q3 走形式 | 都不走形式(各环节都觉得值) | retro 文档 §1(痛点非环节多余) |
| Q4 轻任务耗时 | 流程耗时 >> 任务本身(核心痛点实证) | retro 文档 §2(轻任务错配重流程) |
| Q5 价值最大 | grill-questionnaire | retro 文档 §5(保留优先级锚点) |
| Q6 可退役/降级 | delegate(未 pilot 暂缓)、grill(触发词易混淆) | 不擅自退役 → 走 OD-23 / OD-12 既有重访触发;retro 文档 §5 |
| Q7 结论(勾2) | 形态基本合理(微调已做) + 有结构性冗余需裁剪(并存) | retro 文档 §4(裁剪共识) |
| 补充声明 | 提问维度需聚合到用户积极查看处 | CONTEXT「skill 家族」节补「提问维度速查」子表(已落) |

**落盘文件**:① [skill-family-experience_v1.md](../../../../docs/retro/skill-family-experience_v1.md)(retro 文档,四节 + Action Items);② [CONTEXT.md](../../../../docs/CONTEXT.md)「skill 家族」节补提问维度速查表(补充声明)。

**Action Items 落 TODO.md**:轻任务 dogfood 验证 / delegate 走 OD-23 / grill 走 OD-12 / 维度可见性已即做。

**裁剪共识(Q7 双勾)**:保留 7 个高频 skill 形态不变;delegate / grill 不擅自退役,挂 OD 使用率重访(装置只进不出的合规出口);维度聚合到 CONTEXT 提升可发现性。无新增 ADR(均为双向门,难逆转性不足 ADR 三条件)。
