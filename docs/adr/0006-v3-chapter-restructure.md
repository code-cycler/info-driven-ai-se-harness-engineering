# ADR-0006: v3 章节彻底重排(推翻 HLD#1 保编号)

- 日期:2026-07-29
- 状态:accepted
- 来源:grill-Q W01 压测 v3 设计(Q3),用户定夺选「彻底重排」

## 背景

[HLD#1](../design/hld_v1.md) 原定 v3「保 v2 编号 + 小节注入」(锚点稳定)。grill-Q W01 [Q3](../questionnaires/archive/grill-methodology-v3-design-w01.md) 压测:第三选项「彻底重排」被隐含否决、理由不充分——v3 是 canonical 立论重构,章节顺序应服务新立论(机制层先行 + 双靶子);保编号让 v3 背 v2 章节顺序包袱。窗口期(v2 未广泛引用,VISION#16)正是重排成本最低时。用户定夺选「彻底重排」。

## 决策

1. v3 章节**彻底重排**,按新立论重新组织(主线:vibe coding 失败 → 机制层 → 双支柱 → 落地)。
2. CONTEXT / README / CLAUDE 的方法论链接锚点**全量重写**(不再保 v2 §2/§4/§5.3 编号)。
3. v3 新章节顺序作为 **P1 实现期首个设计任务**定稿(方向:§一 重定位为「vibe coding 失败模式」开篇,机制层主线前置);可经 grill-with-docs 深究章节顺序。

## 替代方案(被否决)

- **保编号 + 小节**(HLD#1 原):否——v3 背 v2 顺序包袱,窗口期浪费重排机会;立论重构值得配套章节重构。
- **部分重排**(立论章重排、非立论保编号):否——折中增加复杂度,锚点半新半旧更乱。

## 后果

- (+) v3 章节最优适配新立论,读者从开篇就建立「vibe coding → AI 幻觉 → 问答对齐」主线。
- (−) 锚点全量重写:CONTEXT/README/CLAUDE 所有方法论链接重写;LLD P4 发布清单加「锚点全量重写」步骤。
- (−) v3 章节顺序需重新设计(P1 首个任务),增加 P1 工作量。
- (−) [ADR-0004](0004-methodology-v3-hallucination-thesis.md) / [ADR-0005](0005-pillar-standard-wording.md) 中「保锚点」相关表述需同步(锚点不再保,改全重写)。
- (−) HLD#1/#10、LLD#13 等「锚点稳定 / 结构不变」条款全部失效,已升 [HLD_v2](../design/hld_v2.md) / [LLD_v2](../design/lld_v2.md) 修订。
