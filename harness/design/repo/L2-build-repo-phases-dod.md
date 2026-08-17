# LLD · repo 级设计(分阶段落地规格)
>
> **导览块**(LN 制,2026-08-17 doctor 层级改造演练迁入;原 LLD.md)
> - 本层位置:L2-build 构建层;上游 L0(验收)+ L1(契约:三区/术语/优先级)
> - 覆盖:P1–P6 阶段拆分 / 依赖链 / 每阶段 DoD / 回归验证
> - 上下游:受 L1 契约约束;阶段拆分为 long-running feature 反推源
> - 契约项声明:每阶段 DoD(含回归三项)= 验收硬约束

> 来源:design-questionnaire lld 阶段 W00(16/16 全采纳,2026-08-05);grill-Q 压测 12 项修订回灌(2026-08-05,正文标注「压测 Qn」)。上游:[L0-vision](L0-vision-repo-design.md) + [L1-contract](L1-contract-repo-architecture.md)。
> 本文 = 落地规格;执行时每阶段按 DoD 验证,全部完成后走 P6 发布门。

## L1 阶段计划(6 阶段,可独立交付/验证)

依赖链:P1 结构迁移独立前置 → P2 术语 → P3 内容 → P4 入口 → P5 归档 → P6 发布门。

| 阶段 | 目标 | 关键动作 | DoD |
|---|---|---|---|
| **P1** | harness 区迁移 + 链接改造 | `git mv` harness/design/ → harness/design/、harness/questionnaires/ → harness/questionnaires/;全部引用方更新 + **skill 落盘路径同步(5 skill 规格 + CLAUDE.md 落盘速查表)** + **方法论 §4.2 路径引用断链豁免登记(并入 P3 一并改)** | 统一回归三项 + P1 专项 |
| **P2** | 术语判定表 + CONTEXT 更新 | 8 术语逐词判定表落 CONTEXT;新词三条件门槛落 CONTEXT + **ADR-0005 四处一致核心子串同步修订(保留原措辞作历史,压测 Q2)** | 统一回归三项 + 术语表完整 |
| **P3** | 方法论 + 哲学 v4 内容修订 | §零 受众(个人,机制内容保留重述为个人 × AI)+ §2.2 第二支柱机制层对称化(**只补机制层,不建度量/症状层**)/ 哲学学科化(§一 人因、§六 软工、新增运筹节)/ 全文术语替换 / 附录 C 更新 | 统一回归三项 + 受众表述全库一致(DoD-5) |
| **P4** | 入口改造 | **实操术语联动(若有,已并入 P3 处理)** + CLAUDE.md 瘦身(规范优先级节含协调注)+ AGENTS.md 零内容路由创建 + README 更新 | 统一回归三项 + 入口收敛(DoD-2) |
| **P5** | ADR + 归档 | ADR-0008/0009/0010 落地 + **ADR-0005 更新(记修订历史)**;v3 移 docs/methodology/archive/ + **归档链接改造清单(P1 工具链复用)**;文件头谱系更新 | 统一回归三项 + 3 ADR 存在 |
| **P6** | 发布门 + dogfood | OD-4 母本同步(其他位置副本标注)+ 脱敏门 + 语义人审 + **README 发布说明注明术语版本**;产物期 dogfood(**验收 = 用户实际执行 + AI 记录**) | P6 发布门专项 |

## L2 详细设计

### harness 区结构(镜像迁移,不重组)

```
harness/
├── design/              # ← harness/design/ 整体迁入
│   ├── VISION.md        # methodology v3 设计套(文件头标注归属)
│   ├── hld_v1.md / hld_v2.md / hld-methodology-separation.md
│   ├── lld_v1.md / lld_v2.md
│   └── repo/            # 本次 repo 级设计套(VISION/HLD/LLD)
└── questionnaires/      # ← harness/questionnaires/ 整体迁入
    └── archive/         # 已处理问卷(含本次 4 份 feature-repo-design-*)
```

迁移方式:`git mv`(保留历史);原位置不留占位;迁移后 docs/ 仅剩:methodology/(+archive/)、CONTEXT.md、OPEN-DECISIONS.md、adr/、LICENSE。

### v4 文件头谱系格式(沿 v3 惯例)

```
# <标题> v4

> **版本谱系**:v1 单支柱 → v2 双支柱 → v3 补全第一支柱机制层 → **v4 受众收窄 + 第二支柱对称化 + 学科化**(本次)。
> **v4 演进推导链**:<受众过宽/术语膨胀/第二支柱缺立论 → 学科视角引入(人因/软工/运筹)>
> **本文独立成文** 声明保留。
> **三块拆分说明** 更新为 v4 表述。
```

### AGENTS.md 内容骨架(零内容路由,<30 行,压测 Q10)

1. 项目状态一句话(方法论 + skill 仓库,无构建工具链)
2. 启动顺序:读 CLAUDE.md(Claude Code 入口)→ 按 CLAUDE.md 关键文档导航选读 → 检查规范优先级
3. 指向 docs 的链接(方法论三块 / CONTEXT / ADR / OPEN-DECISIONS)
4. Codex 专属约束(少量,如脱敏门检查)
5. **不放任何清单/表**(选读表只在 CLAUDE.md 一处——双入口零内容 = 零漂移)

### CLAUDE.md 新结构(6 节)

1. 仓库定位(压缩,方法论摘要指向方法论文件)
2. **规范优先级**(新增,唯一权威处)
3. 关键文档导航(收敛,含 harness 区新路径)
4. skill 家族协作(压缩指向方法论 §5.3)
5. 编辑铁律(保留)
6. 仓库状态(更新至 v4)

### 术语判定表结构(落 CONTEXT 附录)

| 术语 | 学科对应(人因/软工/运筹/无) | 判定(保留/合并/换学科词/删除) | 理由 |
|---|---|---|---|
| 信息断层 | 人因 | 待判 | … |
| …(8 术语) | | | |

判定方向(HLD H2 + hld W01 Q4 C):保留有独立含义的核心词(无学科对应或学科词语义偏移,如 (a)(b) 盲区)、合并语义重叠词、可替换学科标准词者优先替换;新词引入过三条件门槛(学科无对应 + 方法论必需 + 定义清晰)。

## L3 接口规格

### 路径契约

| 旧路径 | 新路径 | 引用方 |
|---|---|---|
| harness/design/** | harness/design/** | CLAUDE.md / README / TODO / ADR / CONTEXT / 方法论三块 / skill DESIGN.md / 归档问卷互引 / 本项目设计产物 |
| harness/questionnaires/** | harness/questionnaires/** | 同上 |

引用格式:相对路径;方法论三块 § 互引沿用现有约定(17 处跨文件 § 引用先例,ADR-0007)。

## L4 DoD

### 统一回归三项(每阶段)

1. 脱敏门 0 命中(`python3 scripts/desensitize.py .`)
2. 断链检查 0(链接检查工具链,81 链接基线)
3. 方法论关键内容不丢(章节清单 22 项 + 核心子串 grep 14 项)

### P1 迁移专项

- harness/ 区文件齐备,docs/ 原位置无残留(grep 无旧路径)
- 引用全更新(grep 旧路径 design/questionnaires 全库 0 命中;豁免项除外——见下)
- **5 skill 规格无旧路径残留**(design-Q / grill-Q / retro-Q / action-Q / long-running 的 SKILL.md + DESIGN.md)
- **断链豁免清单登记**:方法论 §4.2 路径引用(并入 P3 一并改)——豁免项显式登记,不静默
- git mv 历史保留(git log 可追踪)

### P6 发布门专项

- OD-4 母本同步完成(其他位置副本标注「开发副本,以 v4 为准」,仓库外证据)
- 脱敏报告(改了什么)
- 语义人审通过
- dogfood 任务跑通记录(实操文件轻量修订按新规范走完)

## L5 依赖与预估

- **外部依赖**:无新外部依赖(纯文档仓库);OD-4 母本同步涉及作者其他位置副本(仓库外动作,需用户配合)。
- **工作量排序**:P3(内容修订)> P1(迁移 + 链接)> P4(入口)> P2(术语表)> P5(ADR + 归档)> P6(发布门)。
- **前置**:本设计产物(4 份问卷)归档后,落地执行可由 long-running-agent 或手动按阶段推进。
