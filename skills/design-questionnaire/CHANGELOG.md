# design-questionnaire · CHANGELOG

> 本 skill 治理历史(创建起源/裁决时间线/引擎同步/压测修订)。追加式,只增不改;规则现值见 SKILL.md 与各引擎文件,设计决策见 [DESIGN.md](./DESIGN.md)。

## 2026-08-20 · P1 治理历史迁移(governance-history-split F040)

- **变更**:① SKILL.md 17 处带日期治理注记剥离(规则现值保留;无日期判例论证保留);头部加索引行;② DESIGN.md 收敛为「定位/设计决策 D1–D38/已知限制」三节——引擎同步记录 ×3、SKILL.md 分层迁移评估、引擎复制声明内同步事件、格式反馈事件叙述迁本 CHANGELOG;③ 无 FORK-NOTES(本 skill 为引擎 canonical,自身无规则本体级分叉)。
- **原因**:ADR-0024 治理历史分离 P1。
- **影响**: SKILL.md#全部、DESIGN.md#全部
- **出处**: [L1 契约](../../harness/design/governance-history-split/L1-contract-gov-history-split.md) + ADR-0024

## 2026-08-20 · grill-design-q 三透镜压测修订(D31–D38)

- **变更**:W00 价值定位(防漏优先)/ 入口校准闸门(D32)/ 收尾面板化(D33)/ 处理报告全文归档(D34)/ 推理句分级(D35)/ delegate 白名单接口(D36)/ 形态×协议交叉表(D37)/ 规格同步修复(D38)——9 项修订全执行(⚠ 两项草案另行确认后落地);残余张力落 OD-27 / OD-28。决策表留 DESIGN.md。
- **原因**:grill-Q 三透镜(软件工程/第一性原理/项目哲学)压测 design-Q 规格。
- **影响**: SKILL.md(入口闸门/时序/delegate 接口/收尾面板)、STAGE-SKELETONS(交叉表)、FORMAT/PROCESSING
- **出处**: [grill-design-q-w01](../../harness/questionnaires/archive/_misc/grill-design-q-w01.md)

## 2026-08-19 · SKILL.md 分层迁移评估:全量缓行(**后被推翻**)

- **变更**:样板迁移(design-Q 第 92 行 dogfood 过程叙述收拢)+ 评估结论「全量分层迁移低收益缓行」——扫描实测 9 skill 日期注记多为规则出处与原值(纯过程叙述 <5%);ADR-0023 主要价值 = 升格机制 + 教训归位纪律,而非存量一次性大迁移。
- **原因**:grill-Q skill-family W01 Q8-A(ADR-0023)。
- **⚠ 后续(2026-08-20)**:本评估的「缓行」结论被 [ADR-0024](../../harness/adr/0024-governance-history-split-dual-form.md) 推翻(用户立项治理历史分离,Q1-C 裁决注记全迁)——评估的事实判断(注记多为出处型)仍成立,执行判断被新裁决取代。ADR-0023 已补「后续演进」注记。
- **影响**: (评估结论,无文件变更;推翻后由本 CHANGELOG 首条执行)
- **出处**: ADR-0023 + [grill-skill-family-w01](../../harness/questionnaires/archive/_misc/grill-skill-family-w01.md)

## 2026-08-18 · 引擎规则 4 修正(✍️ 自定义位置)

- **变更**:QUESTIONNAIRE-FORMAT 规则 4——「✍️ 自定义」由「紧跟 🤔 之后」改为「紧跟所有选项(含 ★推荐)之后、固定为题目最后一位」,消除与规则 13(推荐居末)的顺序矛盾(该矛盾是「✍️ 行结构性遗漏」的根源,grill-Q first-principles W01 曾 10 题全漏);grill-Q / retro-Q 模板示例同步;四副本 × 双侧同批同步,无新有意分叉。
- **影响**: 四份 QUESTIONNAIRE-FORMAT
- **出处**: grill-Q first-principles W01 补充声明

## 2026-08-08 · 格式参数统一(题量 10 / 小波 ≤3)

- **变更**:题量上限 10–15 → 10;小波阈值四份统一 ≤3(action-Q ≤4 → ≤3 为有意分叉修订,不撤销 confirm-list 语义分叉)。
- **原因**:grill-harness-file-mgmt-w01 压测补充声明用户裁决 + 后续确认「四份统一 ≤3」。
- **影响**: 四份 FORMAT 规则 8 + 四份 SKILL.md 第 2 步
- **出处**: [grill-harness-file-mgmt-w01](../../harness/questionnaires/archive/harness-file-mgmt/grill-harness-file-mgmt-w01.md)

## 2026-08-07 · 未验证假设生命周期管理(D27–D30)

- **变更**:SKILL.md §1 补台账维护 + 复用前重验;§5 闸门汇报;扩散 action-Q(复用前重验)。决策表留 DESIGN.md。
- **原因**:action-Q 确认清单(confirm-design-q-unverified-assumptions-w00,15 条确认 + 小波裁决)发现验证纪律锚定「出题时」的缺口。
- **影响**: SKILL.md#探索与验证、#循环与终止
- **出处**: confirm-design-q-unverified-assumptions-w00(archive/_misc/)

## 2026-08-06/07 · skill-spec-revamp(D23–D26 + 四副本落盘映射同步 + Q7 深钻)

- **变更**:① 骨架增强(HLD/LLD 判别法则 + 最小必含 H1–H5/L1–L5 + 坍缩分档,仅 design-Q 不扩散);② 方案 R(落盘路径配置化)设计后**放弃**,回归硬编码 `harness/`(ADR-0011,D23 superseded);③ 引擎同步:canonical 落盘映射改后四副本落盘映射节同步(仅该节 diff 0,不含各副本有意分叉区),long-running §5.3 读归档路径同步;④ Q7 深钻结论:retro 文档落点 = 项目固有 `docs/retro/`;四副本同步只改「描述宿主项目落盘路径」的字符串,不改 skill 自身目录内部相对引用(判据:`./docs/...` 指 skill 内部 vs `docs/...` 描述宿主)。设计套 harness/design/skill-spec-revamp/。
- **影响**: STAGE-SKELETONS/PROCESSING-RULES/QUESTIONNAIRE-FORMAT + 四副本 + long-running §5.3
- **出处**: [grill-skill-spec-revamp-w01](../../harness/questionnaires/archive/skill-spec-revamp/grill-skill-spec-revamp-w01.md) + ADR-0011

## 2026-08-03 · 预勾开关化 + 实测前置(OD-14 修订 + 标准流程)

- **变更**:① 预勾选 = opt-in 开关默认关;选项排序(非推荐在前 → 逃生舱倒数第二 → 推荐最后)= 默认行为;单向门永不预勾;预勾设防开关开启时适用;四份副本同步(OD-8 重访触发①命中),问题级排序仅 design-Q 保留;② SKILL.md「生成问卷」前新增「实测与调研前置」标准流程(调研现状/不假设/多实测/多获取信息/及时保存)。
- **原因**:OD-14 默认勾选试点修订(confirm-pregou-switch-w00 全确认)+ action-Q 确认(confirm-testing-preflight-w00 全确认)。
- **影响**: 四份 FORMAT/PROCESSING + SKILL.md
- **出处**: OD-14 + 归档确认清单(archive/_misc/)

## 2026-07-24 · 引擎修改三方同步(D22)+ grill-Q 复制引擎(D21)

- **变更**:① PROCESSING-RULES 降风险协议 step 1 + 落盘映射——双向门逃生舱由「采用推荐项,不进 OD」改为「采用推荐项 + 进 OD 标注」,三份同步无漂移;② grill-questionnaire 建立并复制引擎(D18 机制扩为三方)。
- **影响**: 三份 PROCESSING-RULES + 三份 DESIGN
- **出处**: grill-Q dogfood W01 补充声明

## 2026-07-23/24 · dogfood 修订(D13–D22)+ 创建起源

- **变更**:① 创建:grill-with-docs 11 轮串行问答设计定稿(D1–D12,2026-07-23)——动机 = 一问一答交互延迟拖垮启动前完整设计,解法 = 多波次 Markdown 问卷;② dogfood 修订(D13–D22,retro-questionnaire vision W1/W2 + hld W1 实跑产出):补充声明区/小波阈值/TODO 四时机/dogfood 可选步骤/坍缩选项/引擎复用改复制/坍缩细化/降噪撤回(D20)/引擎三方(D21)/逃生舱进 OD(D22)。
- **影响**: (创建期全文件;修订落 FORMAT/PROCESSING/SKILL/STAGE-SKELETONS)
- **出处**: retro vision/hld 归档问卷(skills/retro-questionnaire/docs/questionnaires/archive/)+ grill-with-docs 会话
