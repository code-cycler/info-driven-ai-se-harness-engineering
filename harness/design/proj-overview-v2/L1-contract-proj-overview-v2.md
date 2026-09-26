# L1-contract-proj-overview-v2.md · proj-overview-v2 feature

> 导览:① 位置与职责 = **契约层**(产物规格契约 + skill 修订契约 + 实现步骤与 DoD;两层形态下吸收构建层动作)② 覆盖 = SKILL.md 五处修订 / 产物八段式规格 / en 回译与同步 / 治理收尾五件 ③ 上下游 = 继承 [L0-vision](L0-vision-proj-overview-v2.md) 验收六条(全链硬约束)与「派生性质即约束 + 超源即删」全程约束;基线 = [human-project-view 设计套](../human-project-view/)(v1,历史层,其未被子项显式重裁的裁决继续有效)④ **契约项声明(L1 内实现硬约束)**:本文「输出规格」「实现四步 DoD」「联动清单」全部为硬约束;偏离须走治理性偏差路径(ADR-0021 语义)。
> 状态:L1 W00 已处理(10/10 全采纳,无转正式题);2026-09-25。
> 修订注记(2026-09-26):产物落点由 `harness/PROJECT-OVERVIEW.md` 改**项目根** `PROJECT-OVERVIEW.md`(用户裁决:认读第一入口可发现性优先,与 README/CLAUDE/TODO 同级;HARNESS-RULES §六/方法论 §3.3.1/README/CLAUDE/en 镜像同步——本文「落点」相关条款以本注记为准)。

## 模块与边界

### 修改

| 模块 | 动作 | 职责 |
|---|---|---|
| `skills/proj-overview/SKILL.md` | 五处修订(见下) | 唯一规格载体,<100 行守住 |
| `skills/proj-overview/DESIGN.md` | 启用「v2 修订」节 | 裁决摘要 + 设计套指针 |
| `harness/PROJECT-OVERVIEW.md` | 八段式覆盖重生成 | 人重载上下文认读第一入口 |
| `harness/adr/0026-…md` | 版本内修订注记行 | 受众/行数/summary 三点参数演进留痕 |
| `philosophy-v7-challenge-report_2026-09-08.md` | #三 反馈行追加 v2 注记 | 动机链完整 |

**SKILL.md 五处修订清单**(grill W01 Q2/Q3/Q4/Q5 回灌;现 53 行 → 预计 65–70 行,守 <100):
① 输出规格加图方向硬约束(所有图 `flowchart TD`;subgraph 内禁 `direction LR`);② 加 summary 职责规格(ADR/OD 全量每条一行带源链接、TODO/STATUS-LOG/CHANGELOG 头部转述、表格行数 = 源条目数;**ADR 摘要取材约束** = 「决策」节首句直引或紧缩转述、禁跨节综合,生成时抽 3 条人快审——Q3;**OD 状态列直读 OD 状态字段、禁 AI 归纳**——Q4,依赖 OD 源文件修复);③ 行数条款替换(删「≤250 行超限即精简」→「行数随源文件面线性增长,禁止自由发挥;**分型自检**——事实段(summary/快照/脉络)逐段溯源,结构段(定位/导读/索引)核段规格」——Q2);④ 加导读段规格(三档读法,头部 3–5 行);⑤ frontmatter description 加「认读第一入口:人重载上下文从此开始」。项目侧 DESIGN.md 加「v2 修订」节(裁决摘要 + 设计套指针 + **dogfood 反馈模板三问**——Q5:15 分钟档走读后 ① 能否画出项目结构组织方式 ② 能否定位「落盘根为什么硬编码」在哪个 ADR ③ 信息密度合适还是过载)。

### 不动

- HARNESS-RULES §六「人读派生视图」类目四条特性(只读派生/手动重生成/宽松漂移/三件套自声明)——行数上限不在特性内,无需修订。
- README 新增入口指引行 / CLAUDE.md 新增导航行 / 实操会话恢复链(新增暂缓,L0 裁决,失忆测试通过后另议;**既有 v1 规格描述的同步不暂缓**,见联动清单第 0 条)。
- 原 human-project-view 设计套三件(历史层)与已归档问卷。

## 接口契约

### 输出(硬约束)

- **八段固定序**:① 定位(一句话 + 三入口分工声明)/ ② 导读(三档读法)/ ③ 结构全景(BFS 竖向总图 + 区块索引表)/ ④ 治理文件 summary / ⑤ 决策脉络(精选叙事时间线)/ ⑥ 当前状态快照 / ⑦ DFS 深链 / ⑧ 检索索引(「我想找 X → 去 Y」按问题组织)。段序 = 新人通读认知递进;失忆快路径由导读承载,不重排。
- **导读格式**:3–5 行,三档各一行指到段号(3 分钟恢复 = §1→§6→§5;15 分钟框架 = 前四段 + summary 表浏览;检索 = §8/§7/图旁索引)。
- **summary 段规格**:ADR 表 3 列(编号·带源链接 / 标题 / 一句话决策摘要——取材 = 「决策」节首句直引或紧缩转述,禁跨节综合,生成时抽 3 条人快审)行数 = ADR 实数;OD 表 3 列(编号·带源链接 / 主题 / 状态——直读 OD 状态字段,禁 AI 归纳;源字段随 ⚠-2 修复就位)行数 = OD 实数;TODO/STATUS-LOG/CHANGELOG 头部用叙述 + bullet;summary 段头置顶警示行(「以源文件为准,禁止按过期 summary 做单向门决策」);文件头信息源清单按 summary 段分列源文件。
- **图规格**:所有图 `flowchart TD`,subgraph 内禁 `direction LR`;BFS 四层分解(理念/流程/执行/治理)继承 v1,三入口分工不进图(写 §1 文字);DFS 动态选取 = 主线链 1 条(v2 生成时 = 本 feature 自身,自指深度 1)+ 高风险/挂账链 1–2 条 + 刚收口链可选 1 条,共 3–5 条;图数 ≥2 且 ≤12,每图 ≤30 节点;链接走图旁索引表。
- **行数**:无硬上限(派生性质即约束);**超源即删自检**为生成必经步骤,自检结果留痕(DESIGN.md「v2 修订」节或产物头部信息源清单注记)。
- **头部三件套不变**(时间戳/信息源清单/派生声明——声明句升级含「认读第一入口」);不标规格版本。

### 处理(继承 v1 + 两处升级)

- 扫描分级三档继承;**治理类升级**:ADR/OD 从「头读」升为「全量条目读」(每条读标题 + 状态/决策节首段,支撑一行摘要)。
- 快照数据源 = TODO 头部唯一权威源,直接引用转述,AI 不新增判断;漂移自检义务(头部与 git 近况明显不一致 → 提示人先更新)——均继承不变。

## 全局选型(含被否决项)

| 决策点 | 选型(已决) | 被否决项(理由) | 裁决处 |
|---|---|---|---|
| 段序 | 八段认知递进 + 导读载快路径 | 为三分钟档重排(破坏通读递进) | L1 W00 #1 |
| 三入口呈现 | §1 定位段文字 | 进 BFS 图(入口是读者路由非项目结构) | L1 W00 #4 |
| DFS 选取 | 动态规则(主线+挂账+收口,3–5 链) | 静态三链(不随主线演进) | L1 W00 #5 |
| 行数约束 | 派生性质即约束 + 超源即删 | 500 硬上限 / 软目标+分段上限(W00 #8 已否) | L0 W01 Q1 |
| en 范围 | 仅 SKILL.md 回译 + stamp | 产物也译(harness 不在翻译面,en 16 件实测无 harness 零件) | L1 W00 #8 |
| 实现载体 | feature_list F052 单条 + progress 条目 | 不登记轻实现(破坏留痕纪律一致性) | L1 W00 #10 |
| ADR | 不另立;ADR-0026 版本内修订注记 | 另立新 ADR(路线本体未变) | L0 W00 #13 |

## 实现四步与 DoD(F052,单会话串行)

| 步 | 动作 | DoD(全部可 grep/命令验证) |
|---|---|---|
| ① skill 侧 | SKILL.md 五处修订 + DESIGN.md v2 节(含反馈模板三问)+ en 回译 + `--stamp` + 双侧同步(全局侧 cp SKILL.md) | `wc -l` <100;五处修订 grep 在位(「flowchart TD」「分型自检」「认读第一入口」「禁跨节综合」等);i18n-check 0;sync-check 0 |
| ② 治理注记 | ADR-0026 修订注记行 + 挑战报告 #三 v2 注记 | 两处 grep 命中 |
| ③ 产物重生成 | 八段式 v2 全量重写 PROJECT-OVERVIEW.md + 分型自检留痕(事实段溯源 / 结构段对规格)+ ADR 摘要抽 3 条人快审 + 逐图渲染验证(临时 HTML + mermaid@11 CDN,验后删) | 八段标题 grep 齐;`direction LR` 0 命中;summary 表行数 = 源目录实数(生成时实测 N=26/29 作注记——grill W01 Q9 抽象化);每条 summary 行含相对链接;渲染验证全图通过;自检与快审留痕在位 |
| ④ 治理收尾 | 联动清单五件 + 四门终验 + F052 passes:true + progress 条目 | CHANGELOG 中英双落;skill CHANGELOG / TODO 子条目 / STATUS-LOG grep 在位;四门全绿(desensitize 0 / sync 0 / i18n 0 / harness-check exit=0) |

## 联动清单(治理收尾;grill W01 Q1 扩容 = 第 0 条既有描述同步 + 原五件)

0. **既有 v1 规格描述同步(+3 zh + 2 en)**:[README.md](../../README.md):129 卡片行 / [CLAUDE.md](../../CLAUDE.md):68 速查行 / [methodology_v5.md](../../docs/methodology/methodology_v5.md) §3.3.1 路由表行(canonical 版本内修订,⚠ 已单独呈报确认)+ en/README.md:137 / en/docs/methodology/methodology_v5.md:330(随 zh 回译);CHANGELOG 历史条目不改(append-only,由 v2 新条目自然形成演进时间线)。
1. 根 [CHANGELOG.md](../../CHANGELOG.md):「proj-overview v2:认读第一入口 + 治理文件 summary 职责」一条,**中英双落**(ADR-0025 增量协议)。
2. `skills/proj-overview/CHANGELOG.md`:v2 规格升级条目(仅项目侧,ADR-0024 历史层)。
3. [TODO.md](../../TODO.md):human-project-view 块内追加 v2 子条目——失忆测试窗口改「自 v2 生成日 ≥3 天」(v1 的 09-28 预约作废)+ 新人视角测试观察项登记;不另开块。
4. [harness/STATUS-LOG.md](../STATUS-LOG.md):v2 升级条目一条。
5. 全局侧 DOGFOOD-LOG:**失忆测试完成后**追加 v2 结果(人过目后写入,同 v1 惯例;不在本 feature 实现四步内)。
