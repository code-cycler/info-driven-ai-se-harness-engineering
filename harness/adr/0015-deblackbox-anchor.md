# ADR-0015:去黑盒作第五学科视角独立锚点(正交第一支柱)

> 状态:accepted(2026-08-10,design-Q philosophy-v5 hld W00 #15 采纳)
> 决策日期:2026-08-10
> **更名注记(2026-08-13)**:「第五学科视角」更名「**第四学科视角**」——原命名计数口径从未落盘,与本 ADR「后果」节「学科数 3→4」矛盾;grill-Q philosophy-v5 W01 Q1 用户裁决全仓改名(否决「保留第五 + 补口径注记」方案)。本文原文(含标题)保留历史措辞不改;living 文档(philosophy_v5 / CONTEXT / CLAUDE / README)已同步新名。

## 背景

philosophy_v4 顶部挂三学科(人因 / 软工 / 运筹)。grill-Q discipline-mapping W01 发现:项目建桥研究(~/notes,2026-07-28)通篇证明实践根植**安全科学**(STAMP / Reason / HRO / Safety-II),但哲学 0 处承认(D7 矛盾)。grill-with-docs 深钻「去 AI 黑盒」(6 点结晶,落 [CONTEXT AI 黑盒节](../../docs/CONTEXT.md))确立:

- **黑盒 = 三层次合一**(决策过程不透明 + 依据不可追溯 + 结果不可独立验证)
- **与第一支柱(AI 幻觉式自作主张)正交**:第一支柱治「决策错」(信息维度);去黑盒治「过程不可见」(审计维度)。独立——信息给够仍可能黑盒,过程留痕仍可能决策错。

## 决策

philosophy_v5 新增 **§八「安全科学视角:去 AI 黑盒」**,作为**第五学科视角的独立立论锚点**(与第一支柱正交,**非子集、非第三支柱**)。

- 去黑盒 = 独立风险维度(三层次 × 三坏后果:潜伏沉积 / 失控放大 / 信任劫持)
- 对策 = 统合已有可审计装置(delegation-log / ADR / 人审 / dogfood)+ 形式化 V&V 缺口留 [OD-19](../../docs/OPEN-DECISIONS.md)
- 度 = 弹性边界(WAI 定底线:关键 / 单向门强制留痕;WAD 留空间:纯执行灵活)
- **双支柱结构不动**(信息核心 + 驾驭工程);第五视角是横切学科挂接,不改立论骨架

## 替代方案(被否决)

- **第一支柱子集**:黑盒是信息缺失的一种 → **否决**(grill-with-docs Q2 用户裁决:正交独立,非子集)
- **第三支柱**:双支柱 + 安全 = 三支柱 → **否决**(立论结构变更过重;学科视角足以承载;用户澄清「第五学科视角」非「第三支柱」)
- **因果前提**:黑盒是幻觉根因之一 → **否决**(虽相关但 Q2 选「正交独立维度」)

## 后果

- **正面**:消除「建桥研究安全科学 vs 哲学 0 处」的内部矛盾;安全科学在 canonical 层正名;去黑盒有独立立论锚点(非附庸于第一支柱)。
- **负面**:哲学加第五学科视角(学科数 3→4,守 [ADR-0014](0014-discipline-mapping-strategy.md) 软边界 < 6);§八 新增章节(哲学篇幅增);哲学↔方法论双向引用维护成本。
- **关联**:[ADR-0014](0014-discipline-mapping-strategy.md)(分层策略)、[CONTEXT AI 黑盒节](../../docs/CONTEXT.md)(6 点结晶)、[OD-19](../../docs/OPEN-DECISIONS.md)(V&V 缺口)。

## 关联

- 深钻来源:grill-with-docs「去 AI 黑盒」单点深钻(2026-08-10,6 点结晶落 CONTEXT)
- hld 来源:[feature-philosophy-v5-hld-w00](../questionnaires/archive/philosophy-v5/feature-philosophy-v5-hld-w00.md) #15
- 前序压测:[grill-discipline-mapping-w01](../questionnaires/archive/methodology/grill-discipline-mapping-w01.md)(发现安全科学缺口)
