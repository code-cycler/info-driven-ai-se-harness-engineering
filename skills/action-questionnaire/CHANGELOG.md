# action-questionnaire · CHANGELOG

> 本 skill 治理历史(创建起源/dogfood 案例/引擎同步时间线)。追加式,只增不改;规则现值见 SKILL.md 与引擎文件,设计决策见 [DESIGN.md](./DESIGN.md),有意分叉见 [FORK-NOTES.md](./FORK-NOTES.md)。

## 2026-08-20 · P1 治理历史迁移(governance-history-split F040)

- **变更**:① SKILL.md 8 处日期注记剥离(含 description 内 1 处)+ 头部索引行 + 分工表阈值过时值 ≤4→≤3 顺手修正;② DESIGN.md 收敛(定位/裁决表 Q1–Q15+W02/被否决项/dogfood 范围决策/已知限制)——dogfood 案例两例详录、引擎同步记录 ×3、skill-spec-revamp 同步(superseded)、复用前重验扩散叙述迁本 CHANGELOG;③ 有意分叉清单(6 条)从 DESIGN 迁 FORK-NOTES.md(双侧一致);④ 引擎 FORMAT/PROCESSING 日期剥离 + 头部拆分。
- **原因**:ADR-0024 治理历史分离 P1。
- **影响**: SKILL.md、DESIGN.md、QUESTIONNAIRE-FORMAT.md、PROCESSING-RULES.md、FORK-NOTES.md(新)
- **出处**: [L1 契约](../../harness/design/governance-history-split/L1-contract-gov-history-split.md) + ADR-0024

## 2026-08-18 · 引擎规则 4 修正(✍️ 位置)

- **变更**:FORMAT 规则 4——「✍️ 自定义」改为「紧跟所有选项之后、固定为题目最后一位」,消除与规则 13 排序矛盾;本副本模板本已合规,仅规则 4 措辞统一;四副本 × 双侧同批同步。
- **出处**: grill-Q first-principles W01 补充声明

## 2026-08-08 · 小波阈值收紧(≤4 → ≤3)

- **变更**:有意分叉 #3 的阈值由 ≤4 收紧为 ≤3(四副本统一,grill-harness-file-mgmt-w01 压测补充声明用户裁决);DESIGN 裁决表 Q2/Q3 与 FORMAT/SKILL 同步。
- **出处**: grill-harness-file-mgmt-w01(archive/harness-file-mgmt/)

## 2026-08-07 · 复用前重验扩散 + skill-spec-revamp 同步与撤销

- **变更**:① 「复用前重验」从 design-Q 未验证假设生命周期管理(D30)扩散到本 skill(confirm-list 引用之前确认过但从未实测的信息先重验;落 SKILL 第 1 步,与分叉 #6 衔接);② skill-spec-revamp 落盘路径配置化(方案 R)同步到本 skill——**2026-08-07 撤销**(ADR-0011),路径回归硬编码 `harness/`;HLD/LLD 判别法则不扩散到本 skill(无内容骨架)。
- **出处**: confirm-design-q-unverified-assumptions-w00 小波裁决 + ADR-0011

## 2026-08-03 · 预勾开关化 + 实测前置同步

- **变更**:预勾选 opt-in 开关默认关 + 选项排序统一 + 单向门永不预勾(OD-14 修订,confirm-pregou-switch-w00 全确认);「实测与调研前置」标准流程入 SKILL(confirm-testing-preflight-w00 全确认)。四副本同步(OD-8 重访触发①命中)。
- **出处**: OD-14 + 归档确认清单(archive/_misc/)

## 2026-07-31 · dogfood 两个案例(门槛过关)

- **变更**:① **首案例 = skill 家族生态位重叠分析**(confirm-skill-niche-overlap-w00):流程全走(定界→核实 8 份 SKILL→W00 14 条→全勾一轮终结→处理报告→执行→归档→小波 2 题);发现 **D-1 规格缺口**(补充声明第四类「用户先验结论」原三类去向未覆盖 → 回修为本副本分叉 #6)、D-2 顺畅(confirm-list 形态对「先核实再动手」有效)、D-3 轻摩擦(全勾零异常 W00 的两次串行等待,是否优化留使用数据)——门槛过关,canonical 同步(7→8)解锁;② **第二案例 = 生态位区分**(confirm-grill-niche-distinguish-w00):新观察 = 补充声明作「留空项纠偏答案」通道有效 / 小波直问处理开放型确认项有效 / 类目边界校准(第四类未误伤既有规则)。
- **出处**: 归档问卷(archive/_misc/)

## 2026-07-30 · 创建(15 题压测裁决落地)

- **变更**:grill-Q 对「行动前细节确认 skill」提案 15 题压测(11 勾选 + 4 自定义)→ 独立新 skill 创建:SKILL.md + 引擎副本 ×2(含 W00 节改 confirm-list)+ DESIGN.md;15 题裁决见 DESIGN「压测裁决全录」;第 4 份引擎副本分叉治理定 OD-11(不触发 OD-8 重议,有意分叉声明);canonical 同步(7→8)先过门槛后执行。
- **出处**: [grill-preaction-confirm-skill-w01](../../harness/questionnaires/archive/preaction-confirm/grill-preaction-confirm-skill-w01.md) + OD-11
