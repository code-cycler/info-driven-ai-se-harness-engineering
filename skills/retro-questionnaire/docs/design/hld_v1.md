# retro-questionnaire · HLD(全局设计) v1

> 2026-07-23 由 design-questionnaire 的 hld W1 问卷落盘生成。
> 问卷归档:[../questionnaires/archive/hld-w01.md](../questionnaires/archive/hld-w01.md)
> 覆盖 VISION:[../VISION.md](../VISION.md)(2026-07-23 闸门定稿)

## 架构(H1)

```
~/.claude/skills/retro-questionnaire/
├── SKILL.md                  # 触发条件 + 复盘主流程
├── RETRO-SKELETONS.md        # retro 骨架模板(本 skill 唯一特有物)
├── QUESTIONNAIRE-FORMAT.md   # 引擎副本(复制自 design-questionnaire,见「选型」)
├── PROCESSING-RULES.md       # 引擎副本(同上)
└── docs/
    ├── VISION.md
    ├── design/hld_v1.md
    └── questionnaires/archive/
```

职责边界:SKILL.md 只管触发与流程编排(阶段 DoD 核验后主动提议 / 用户手动);RETRO-SKELETONS.md 承载全部 retro 特有内容;引擎两文件与 design-questionnaire 同构。

**作用对象**:retro 作用于「宿主项目」(被复盘的项目)。出题依据从宿主项目读取,retro 文档落盘宿主项目 `docs/retro/`,行动项写宿主项目 `TODO.md`,已用问卷归档宿主项目 `docs/questionnaires/archive/`——不落在 skill 目录。

数据流:五源读取(见接口契约)→ 生成 retro 问卷 → 用户作答 → 落盘 retro 文档 + TODO.md → 问卷归档。

## 选型(H2)

- 引擎复用:**复制两份**(hld-W1-Q1 选 B)。retro 持有自己的引擎副本,各自独立演进。
- 防漂移声明机制(hld-W1-Q1 ✍️自定义):
  1. 两个 skill 各自声明:改动引擎时需考量是否同步另一个;
  2. 若两副本已存在漂移,必须声明该漂移「是否为设计」(intentional divergence 还是待修)。
- 同步规则(hld-W1-Q4 选 A):任何引擎修改,在两个 skill 的 DESIGN.md 各记一笔,并检查另一方是否受影响。
- 被否决:相对路径引用(断裂风险)、抽取共享目录(回改成本 + 游离目录)、版本依赖(过度工程)。

## retro 骨架结构(H1 补充,hld-W1-Q2 选 A)

按方法论四节 + Action Items:

1. **进展顺利**(What went well)
2. **出问题与原因假设**(What went wrong;反思题选项 = 常见原因假设清单)
3. **架构偏离**(实现 vs 设计文档不一致;只记录,后续动作由人发起)
4. **学到什么**
5. **Action Items**(固定节:问题 → 行动 → 核验时机;同时写入宿主项目 TODO.md)

## 接口契约(H3)

出题依据数据源(hld-W1-Q3 选 A + ✍️自定义),硬约束,实现阶段不得偏离:

1. 阶段设计文档(HLD / LLD / DoD)
2. `git log`(本阶段提交)
3. `TODO.md` 未完成项
4. 上一份 retro 的 Action Items(→ 新 retro 文档开头设「Action Items 回顾」节)
5. 与用户交流中的有价值内容(反馈、决定、洞察;✍️自定义补充)

格式契约:retro 问卷 = QUESTIONNAIRE-FORMAT.md;解析、降风险、归档 = PROCESSING-RULES.md。

## 部署与运维(H4)

- 位置:`~/.claude/skills/retro-questionnaire/`(用户级)
- 触发:agent 检测到宿主项目阶段 DoD 核验通过 → 主动提议,人确认;或用户手动触发
- 防漂移运维:见「选型」声明机制 + 同步规则

## ADR 识别(H5)

hld-W1-Q1(复制两份):双向门——改回引用只需改 SKILL.md 并删除副本,未达 ADR 门槛。决策与权衡记录于本文档「选型」。本阶段无 ADR。

## 遗留(2026-07-24 已全部完成)

- LLD / 实现:~~写 SKILL.md、RETRO-SKELETONS.md,复制引擎两文件,在 design-questionnaire 的 DESIGN.md 登记引擎复制声明~~(已完成:SKILL.md、RETRO-SKELETONS.md、DESIGN.md 决策索引、引擎副本含标记注释)。
