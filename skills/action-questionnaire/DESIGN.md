# DESIGN — action-questionnaire 设计决策记录

> 本 skill 的设计决策记录(定位 / 压测裁决 Q1–Q15+W02 / 被否决项 / 已知限制);治理历史(创建起源/dogfood 案例/引擎同步时间线)见 [CHANGELOG.md](./CHANGELOG.md);有意分叉见 [FORK-NOTES.md](./FORK-NOTES.md)。
> 工件性质:它不是独立拍脑袋产物,是 grill-questionnaire 对「行动前细节确认 skill」提案 15 题压测的裁决落地(归档问卷见 CHANGELOG 创建条 + OD-11)。

## 定位(一句话)

非正式行动前的批量细节确认:AI 把对行动细节的理解写成「细节确认清单(confirm-list)」,人核对后执行——对齐信息以规避 AI 在信息真空中的幻觉式自作主张(方法论 §2.1 机制层的直接对策,(a) 类盲区的捕获器)。

## 压测裁决全录(W01 15 题 + W02 提问波 1 题)

| # | 问题 | 裁决 | 落实位置 |
|---|---|---|---|
| Q1 | 独立新 skill vs 扩展现有 | 独立新 skill | 本目录;被否决项见下节 |
| Q2 | 问卷族 × 一问一答保留场景 | 不矛盾:阈值 ≤3 兜小波,≥4 题批量省串行 | SKILL.md 第 2 步小波阈值 |
| Q3 | 阈值依据 | 经验估值,双向门,待真实使用数据校准 | FORK-NOTES 分叉 3 |
| Q4 | preview × 阈值涌现形态 | 预期形态:confirm-list 为主、正式题波兜底,反形式主义 | SKILL.md 第 2 步;FORMAT 文件结构节 |
| Q5 | 环境现实验证 | 含:涉代码事实/外部依赖先核实,证据入出题依据 | SKILL.md 铁律 2 + 第 1 步;FORMAT 规则 7 |
| Q6 | 第 4 份引擎副本 × OD-8 | 不触发重议:从 design-Q canonical 复制(含 W00 节),声明有意分叉 | OD-11;FORK-NOTES.md |
| Q7 | 落盘形态 | 归档问卷唯一常规留痕 + 三条件升格 ADR/OD | PROCESSING-RULES.md 落盘映射 |
| Q8 | 触发范围 | 与设计无关的非正式 action、通用行为,避免 design-Q 式重决策 | SKILL.md 第 0 步 |
| Q9 | 与 delegate 边界 | 确认优先:写操作默认确认,除非**显式声明**继承 delegate 白名单 | SKILL.md 铁律 3 + 第 0 步豁免检查 |
| Q10 | 终止判据 | 隐式骨架六要素:目标/输入/输出/约束/边界/依赖 | SKILL.md 第 1/5 步;FORMAT W00 模板 |
| Q11 | 与 long-running 接口 | 不嵌入;行动升级到 feature 级 → 提醒转专用 skill;ADR/OD 正常记录 | SKILL.md 铁律 7 + 第 5 步升级转出 |
| Q12 | dogfood | 不做正式 dogfood(≥2 案例) | 见「dogfood 范围决策」节 |
| Q13 | canonical 同步时机 | 先过门槛后同步(7→8 六文件七处) | 仓库 TODO.md |
| Q14 | 命名 | 定 `action-questionnaire`(action 前缀 + 问卷族后缀) | 本目录名 |
| Q15 | preview 术语漂移 | 更名「细节确认清单(confirm-list)」,语义改确认式 | FORK-NOTES 分叉 1 |
| W02 | Q12×Q13 矛盾(不做 dogfood 但门槛是 dogfood 过关) | 补 1 个轻量 dogfood 案例作 canonical 同步门槛 | 下节 |

## 被否决项(Q1,为什么不是扩展现有 skill)

| 被否决项 | 否决理由 |
|---|---|
| design-Q 加 confirm 模式 | design-Q 是设计期生成式(阶段坍缩/闸门/preview=决策默认值);确认是行动前对齐式,混入要分叉其阶段机制,且触发词互相污染 |
| grill-Q 阈值参数化 | grill-Q 是对抗压测(D1–D8 找漏洞),本 skill 是生成式对齐,目标相反,硬合并语义混乱 |
| grill / grill-with-docs 扩展批量模式 | 破坏单点深钻族「一问一答、即时反馈」定位 |

## dogfood 范围决策(Q12 + W02)

- **不做正式 dogfood**(≥2 真实案例 + 计数)。
- **canonical 同步门槛 = 1 个轻量 dogfood 案例**(W02 裁决,解 Q12×Q13 矛盾):用一个真实非正式行动完整走一遍本 skill 流程,记录缺口即时回修规格。**门槛已过关**(首案例 = skill 家族生态位重叠分析,过程与发现见 CHANGELOG);canonical 同步(7→8)已解锁并执行。

## 已知限制(设计期自认)

1. 只对齐 (a) 类幻觉的一半:用户确认对齐用户脑中的背景;AI 误读现实靠铁律 2 兜,核实深度有限(SKILL.md「已知限制」节)。
2. 阈值现值 ≤3 无数据支撑(Q3),可能在真实使用中调整。
3. 与 delegate 的「显式声明继承」豁免机制尚无具体声明格式——首个使用项目需在 delegation.md 里给出写法(届时回修 SKILL.md 第 0 步)。
