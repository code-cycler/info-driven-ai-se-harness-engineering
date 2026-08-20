# delegate · CHANGELOG

> 本 skill 治理历史。本 skill 不复用问卷引擎,无规则本体级分叉,故无 FORK-NOTES。追加式,只增不改。

## 2026-08-20 · P1 治理历史迁移(governance-history-split F040)

- **变更**:SKILL.md 4 处日期剥离(来源行/preview 迁移节压缩为现行规则/full 模式出处/实测条款)+ 头部索引行;DESIGN.md 表内日期剥为 round 出处、round 1 详录压缩、漂移声明历史更新条迁本 CHANGELOG。
- **原因**:ADR-0024 治理历史分离 P1。
- **影响**: SKILL.md、DESIGN.md
- **出处**: [L1 契约](../../harness/design/governance-history-split/L1-contract-gov-history-split.md) + ADR-0024

## 2026-08-01 · full 模式 + 实测条款(grill-Q ai-autonomy 压测)

- **变更**:① `mode: full` 全权模式(delegation.md 开关,白名单语义反转排除集;供「AI 全权自治」双轨对照 OD-13 使用;底线与留痕不变);② 实测条款新纪律:「AI 先实测(只读)可自主执行;实测后的决策归类仍交人,或归入 full 排除集」——解决「AI 先实测再判定」与「AI 无自分类权」的张力;③ delegation-template.md 加 mode 字段。
- **出处**: grill-Q ai-autonomy W01/W02(archive/ai-autonomy/)+ OD-13

## 2026-07-27 · dogfood round 2(项目B 实现期)

- **变更**:G11(D7 工程判断作模板候选行默认 disabled——项目B D7 stage0 单点未偏离但无留痕证据、无边界事件;待 round 3 定性)+ G12(log 存在性检查机制:init 同创空 log + 回顾检查条数,零条目须显式说明——项目B「规范完好、执行失效」实证);G6 注同步为 W00 语义(round 1 漂移声明描述的旧版 preview 已过时)。
- **出处**: 项目B dogfood round 2(宿主项目归档)

## 2026-07-25 · 创建 + dogfood round 1(项目C 设计期)

- **变更**:① 创建:宿主项目 grill-questionnaire W01 压测用户提案「下放部分简单决策权给 AI」的产物——G1–G5(白名单机制/治理文件与日志分离/项目根位置/双层收回/禁区优先);② round 1 关键发现:delegation-log 0 条(根因 = 决策面错位:设计期判断在问卷作答,白名单覆盖实现期,尚未被真正测试)/「触发流程不确定」属实(design-Q 0 处 delegate 引用 → G9 契约化 + G10 放权时机定 vision 闸门)/preview 全程零触发(→ G6 superseded,迁移为 design-Q 强制步骤)/design-Q 缺环境现实验证步骤(→ design-Q 增补);③ 下轮度量四项(判断轮次数/preview 预答率/log 条数/逃生舱使用率)。
- **出处**: 宿主项目归档问卷 + 「决策下放」OD 条目
