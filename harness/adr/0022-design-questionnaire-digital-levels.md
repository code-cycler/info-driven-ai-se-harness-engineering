# ADR-0022: design-questionnaire 数字层级制(LN)改造

- 状态:accepted(2026-08-17,feature-designq-digital-levels 全流程:design-Q 设计套 + grill-Q 压测 10 题回灌 + long-running F027–F034 实施)
- 决策日期:2026-08-14(立项)至 2026-08-17(回灌)

## 背景

design-Q 原产物为 VISION/HLD/LLD 三时间阶段(坍缩三档),层次被阶段锁死:小项目被迫多文档、层次不可独立演进、HLD/LLD 边界靠判别法则补丁维持(越界实证)。用户裁决(grill-Q methodology-improvement W01 Q3-A + 自定义):改为数字层级,「第 0 层 design、第 1 层 design……根据实际项目动态调整」;参照同级对标仓库 Level 1/2/3(阅读视角,可独立维护,非时间阶段)。

## 决策

1. **混合制职责模型**:L0-vision 固定(目标/范围/验收,恒在不可坍缩);L1+ 浮动(职责自声明 + 常用模板 L1-contract/L2-build 作默认参照)。
2. **最小 1 层 + L0 自检**:小项目/小 feature/小 action 单层交付合法;L0 闸门内置五信号自检(⑤ AI 判定为建议信号,须附具体缺失理由,增层决策由人拍板——与「AI 自评不能单独证明」对齐)。
3. **契约优先裁决**:上层契约优先于下层细节;改上层契约走 ADR-0021 治理性偏差路径。双落点:STAGE-SKELETONS 总则 + 各层导览块契约项声明。
4. **插层/回退协议**:插层(深度不足,默认底层追加)/ 回退(上游失效,只重过受影响层)互补。
5. **引擎随层级制修订**(压测 Q1-C,推翻原「不动」裁决):stage 枚举改层名语义,四副本联动。
6. **范围扩容**:long-running 双模式(默认单 agent;准备/执行模式为拓展,多 worktree 用 Claude Code 原生 SendMessage 通信,模式切换由人确认);doctor-harness 拓展(LN 布局规则/存量改造/构想直生/旧档迁移映射);design-Q 收尾必停询问多线程开工。
7. **双副本实验路径**(OD-24):全局 = 实验版,项目 = backup;实测**双向漂移**(任一侧领先先同步再实验);doctor CHANGELOG 类私有日志单向防火墙(全局→项目禁止,防脱敏事故)。

## 替代方案(被否决)

- 固定语义层级制(L0=目标/L1=契约/L2=构建强制):与「不严格限定、可只有 L0」冲突,小项目被迫套模板。
- 最小 2 层底线 / 全浮动制 / 单文档档(第 4 坍缩档):分别被最小 1 层裁决、L0 恒在基线、Q3-A 全面改造吸收。
- AI 自动开工多线程:违反铁律 1(模式切换必须人确认)。
- 「全局=实验/项目=稳定 backup」单向假设:被双向漂移实证推翻。

## 后果

- (+) 层次与阶段解耦,小项目单文件合法,大项目按需增层;一条决策一个家;裁决规则一眼可判。
- (+) 三 skill 能力闭环:doctor 管布局/迁移/存量改造(含构想直生),long-running 支持多 worktree 拓展,design-Q 收尾停点接实现期分流。
- (−) 引擎四副本维护面 +1 处(stage 枚举);导览块/契约项声明是新增写作义务。
- (−) 动态插层协议未经真实案例验证(F033 案例 2 用户裁决跳过:低频难自然触发)——留待首个自然触发案例回访。

## 关联

- 来源:[grill-methodology-improvement-w01](../questionnaires/archive/_misc/grill-methodology-improvement-w01.md) Q3-A;设计套 [designq-digital-levels/](../design/designq-digital-levels/);压测 [grill-designq-digital-levels-design-w01](../questionnaires/archive/designq-digital-levels/)。
- 相关:[ADR-0021](0021-design-implementation-deviation-governance.md)(偏差治理 = 契约变更路径)、[ADR-0020](0020-cross-skill-minimum-governance-contract.md)、[OD-24](../../docs/OPEN-DECISIONS.md)(实验路径,已随回灌关闭该轮)。
