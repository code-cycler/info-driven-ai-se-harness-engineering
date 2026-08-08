---
mode: feature
wave: 0
stage: hld
created: 2026-08-08
status: archived
---
# 问卷 hld W00 · Preview(决策默认值 yes/no 速答)

> **本波是 preview 预答层**(独立 wave 0):把 AI 有明确默认倾向的决策点逐条列出,人只做 yes/no 速答。
>
> **作答规则**:
>
> - **预勾选 = opt-in 开关**(默认关,本次未启用):全部 `[ ]`,人逐条作答
> - **勾 `[x]` = 采纳默认** → 按该默认落盘; **取消(留空)= 不采纳** → 该要点转入 W01 单独拷问
> - **单向门要点(发布 / 删除 / 花钱 / 脱敏等不可逆)永不预勾**,强制人逐条显式勾选确认
> - 本波**不用 🤔**(yes/no 二选一,无中间态);真定不了 → 留空即可,转 W01 深究
> - 若"大体同意但要改一两处" → 留空,转 W01 时在深究题里给自定义值
>
> 默认来源标注于〔〕。
>
> **设计背景**(供作答参考):doctor-for-harness 的 vision 已定稿([VISION](../../design/doctor-harness/VISION.md,W00 20 条 + W01 10 条全采纳)。本阶段 = 架构设计:分层规则 / 归属判据 / 校验机制 / 模块划分 / 接口契约 / ADR 识别。已核实:44 处 SKILL.md/引擎 harness 路径句、ADR 0001–0011 连续、2026-08-05 迁移先例(96 断链 → 7 豁免)。

## 决策默认值清单

### 架构

- [X]  **1 模块划分** = doctor-for-harness 四模块:① 规则权威模块(分层规则 + 归属判据 + 命名规范,HARNESS-RULES.md);② 迁移流程模块(重组 + 链接重算 + 断链回归,MIGRATION-FLOW 文档或 SKILL.md 节);③ 校验模块(scripts/harness-check.py);④ 演进留痕模块(变更记录,CHANGELOG 或 DESIGN.md 节)。〔VISION 四项职责 → 模块映射〕
- [X]  **2 数据流** = 规则权威模块是唯一 source → 被 SKILL.md 引用 / 迁移流程按其执行 / 校验脚本按其检查;校验脚本输出违规清单 → 人决定是否迁移;迁移流程 → 触发演进留痕记录。〔VISION「规则一处权威」+ 场景 A–D〕
- [X]  **3 HARNESS-RULES.md 内容** = 分层定义(design/<feature></feature>/ 判定句 + 裸放规则)+ 归属判据一句 + 命名规范(S2 各模式正则)+ 归档规则(新归档子目录 + 存量不挪 + README 索引)。〔VISION Q2/Q3/Q4 + 压测 S2–S5〕
- [X]  **4 归属判据落点** = 轻量规则入 HARNESS-RULES.md 一节(非独立文件)——个人单仓库不触发,子模块独立时另建。〔VISION Q4 下沉轻量规则〕

### 技术选型

- [X]  **5 校验脚本实现** = 纯 Python 单文件 `scripts/harness-check.py`(无第三方依赖,标准库 pathlib/re)——与 desensitize.py 同风格;输出:违规清单(文件 + 违规类型)+ 0 违规时无输出。〔已核实:scripts/ 现有 desensitize.py 纯标准库〕
- [X]  **6 脚本检查项** = 三合一:① 问卷命名正则(init/feature/grill/retro/confirm 各模式);② ADR 编号连续(0001 起,无跳号);③ 归档位置(processed/archived 状态的问卷在 archive/)。保守实现:只报格式偏离,不报内容语义。〔VISION Q7〕
- [X]  **7 迁移工具形态** = 不写自动化迁移脚本(一次性工作,手动 + 文档流程 + 校验脚本验证);迁移流程 = MIGRATION-FLOW 文档步骤(设计新布局 → 挪文件 → 链接重算 → 跑校验 → 断链回归)。〔VISION Q1 最小可用:不预设自动化框架〕
- [X]  **8 断链回归手段** = 复用既有方法(2026-08-05 迁移先例):grep 相对链接 + 校验脚本 + 人工抽查;不新造链接检查工具。〔已核实:迁移先例有成熟做法〕

### 接口契约

- [X]  **9 校验脚本接口** = `python3 scripts/harness-check.py [harness_root]` → stdout 违规清单(逐条「路径: 违规类型」)+ exit 0(违规存在也 0,人读输出决定);`--json` 可选输出结构化。〔与 desensitize.py 接口风格对齐〕
- [X]  **10 规则引用接口** = HARNESS-RULES.md 是唯一权威源;各 SKILL.md 落盘路径句保持硬编码 `harness/`(ADR-0011),不内联复制分层规则,只引用「分层见 HARNESS-RULES.md」。〔反漂移 + ADR-0011〕

### 部署与运维

- [X]  **11 触发时机** = 手动触发为主(「分层一下」「校验 harness」);迁移作为独立行动项带 DoD;校验在发布前/定期可选跑。不进任何 skill 的每次流程(不增加确认负担)。〔VISION Q5 独立脚本 + 迁移时强制 + 之后可选〕
- [X]  **12 演进留痕落点** = harness 组织变更记录在 `harness/design/doctor-harness/CHANGELOG.md`(或 DESIGN.md 节)——每次迁移/规则修订追加一条(日期 + 变更 + 原因)。〔VISION 场景 D + 原始信息不丢失〕

### ADR 识别

- [ ]  **13 分层规则是否 ADR** = 暂不立 ADR(分层是 harness 内部组织形态,双向门可逆;难逆转性不足 ADR 三条件);记 HARNESS-RULES.md + DESIGN.md。若迁移实际破坏既有链接(不可逆影响),再补 ADR。〔已核实:ADR 三条件 = 难逆转 + 会困惑 + 真权衡;分层不满足难逆转〕
- [ ]  **14 迁移行动项是否 ADR** = 分层迁移作为独立行动项带 DoD(进 TODO),不立 ADR——迁移是执行不是决策,决策(分层规则)已记 HARNESS-RULES。〔design-Q 惯例:行动项进 TODO〕

## 补充声明

> **用户作答(2026-08-08,文件圈选)**:#1–#12 勾选采纳;#13 #14 留空(不采纳默认 → 转 W01 深究)。agent 于 2026-08-08 处理时重读文件确认(User 提示「重读问卷文件」)。

---

## 处理报告摘要(W00,2026-08-08)

- **preview 统计**:勾选采纳 12 / 留空不采纳 2(#13 #14)/ 转 W01 正式题 2;取消默认率 2/14 = 14.3%。
- **落盘**:HLD [`harness/design/doctor-harness/HLD.md`](../../../design/doctor-harness/HLD.md(新建,12 条采纳落盘;#13/#14 标「待 W01」);无 ADR。
- **读取教训**:grep `[x]` 小写未匹配用户大写 `[X]`、Read 缓存误报未变化——处理问卷以**cat 直接读文件字节**为准,不以 grep/Read 缓存结论作废用户编辑。
- **下一波**:W01 = #13 #14 深究(分层规则 / 迁移行动项是否 ADR)+ 若引出的开放题。
