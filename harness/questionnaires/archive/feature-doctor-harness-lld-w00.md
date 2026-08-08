---
mode: feature
wave: 0
stage: lld
created: 2026-08-08
status: archived
---
# 问卷 lld W00 · Preview(决策默认值 yes/no 速答)

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
> **设计背景**(供作答参考):doctor-for-harness 的 vision + hld 已定稿([VISION](../design/doctor-harness/VISION.md) + [HLD](../design/doctor-harness/HLD.md),W00/W01 全采纳 + [ADR-0012](../../adr/0012-harness-layering-rule.md) / [ADR-0013](../../adr/0013-harness-layering-migration.md))。本阶段 = 分阶段实现规格:拆几个阶段、每步做什么、DoD 怎么验。已核实:两套 skill 位置(仓库 `skills/` + `~/.claude/skills/`)、命名模式 confirm/feature/grill/retro 齐备、现存 feature-skill-* vs feature-skills-* 近似前缀(作豁免清单)。

## 决策默认值清单

### 阶段拆分

- [X]  **1 阶段拆分(4 阶段)** = ① P1 规则权威(HARNESS-RULES.md 起草 + SKILL.md 引用);② P2 校验脚本(scripts/harness-check.py 实现 + 现状跑通);③ P3 分层迁移(本仓库 design/ 重组 + 链接重算 + 断链回归);④ P4 双副本同步 + 家族表述(仓库 + ~/.claude + CLAUDE.md/CONTEXT 第 9 个表述)。〔HLD 四模块 → 实现阶段映射〕
- [X]  **2 依赖链** = P1 → P2 → P3 → P4(校验脚本依赖规则权威定义;迁移依赖校验脚本验证;家族表述依赖迁移验证通过)。〔HLD 数据流:规则权威是唯一 source〕
- [X]  **3 每阶段独立 DoD** = P1:grep 规则文档在位 + SKILL.md 引用句;P2:脚本对现状跑出真实违规 / 无违规 0 输出;P3:design/ 重组完成 + 断链 0 新增;P4:双副本 diff 0(仅脱敏差)+ 家族表述同步。〔HLD 验收 + 迁移先例 DoD 参照〕

### 详细设计

- [X]  **4 HARNESS-RULES.md 结构** = 四节:① 分层定义(design/<feature></feature>/ 判定句 + 裸放规则);② 归属判据(一句:独立 CLAUDE.md/git/发布边界 → 独立 harness);③ 命名规范(init/feature/grill/retro/confirm 各模式正则 + 豁免清单);④ 归档规则(新归档子目录 + 存量不挪 + README 索引)。〔HLD 模块①内容 + ADR-0012〕
- [X]  **5 校验脚本结构** = 单文件 `harness-check.py`:主函数扫描 harness_root → 三个检查函数(命名正则 / ADR 编号连续 / 归档位置)→ 输出违规清单;`--json` 可选。纯标准库(pathlib/re)。〔HLD 模块③ + 接口契约〕
- [X]  **6 迁移流程文档** = MIGRATION-FLOW(SKILL.md 节或独立):设计新布局 → 挪文件(必做档 design/ 重组)→ 相对链接重算 → 跑校验 → 断链回归 → 规格同步。逐步可跟随,不自动化。〔HLD 模块② + ADR-0013 迁移方式〕

### 接口规格

- [X]  **7 校验脚本接口** = `python3 scripts/harness-check.py [harness_root]` → stdout 违规清单(逐条「路径: 违规类型」)+ exit 0;`--json` 输出 JSON。入参:harness_root(默认 ./harness);出参:违规清单;异常:目录不存在 → 提示 + exit 1。〔HLD 接口契约 #9〕
- [X]  **8 规则引用接口** = 各 SKILL.md 落盘路径句保持硬编码 `harness/`(ADR-0011),只在 HARNESS-RULES.md 声明分层规则,SKILL.md 加一句「分层见 HARNESS-RULES.md」。〔HLD 接口契约 #10 + 反漂移〕

### DoD

- [X]  **9 脚本事实 DoD** = 对当前仓库跑:能准确报出真实违规(ADR 编号跳号 / 命名偏离 / 归档位置)——现状核实:ADR 0001–0011 连续(无跳号)、命名有 feature-skill-* vs feature-skills-* 近似(豁免清单)、归档全在 archive/;分层迁移后跑:0 违规 + 0 断链。误报门 = 无违规时 0 输出。〔VISION Q7 + 已核实现状〕
- [X]  **10 迁移 DoD** = 必做档 design/ 重组完成(methodology 裸放保留、feature 系列已建目录保留、逐条核对归属);相对链接全部重算;断链回归 0 新增;SKILL.md 引用同步;可选档(questionnaires/adr)标 TBD。〔ADR-0013 DoD〕
- [X]  **11 家族回归 DoD** = 新增 skill 不破坏既有 8 skill 触发/落盘/引擎机制;两套副本同步后 diff 0(仅脱敏差);CLAUDE.md 家族图 / CONTEXT skill 家族节 / 落盘速查表同步(pending——Q9 先 dogfood 后入家族,迁移验证通过后落)。〔VISION 验收 + 家族先例〕

### 依赖与预估

- [X]  **12 外部依赖** = 无(纯 Markdown + 纯 Python 标准库脚本,不涉编译/运行);校验脚本与 desensitize.py 并列 scripts/。〔已核实:scripts/ 现有 desensitize.py 纯标准库〕
- [X]  **13 工作量排序** = P1(规则起草,最轻)> P3(迁移 + 断链回归,最重)> P2(校验脚本,中)> P4(双副本 + 家族表述,中)。〔参照 skill-spec-revamp 实现排序〕
- [X]  **14 实现方式** = long-running-agent 驱动(feature_list 从 P1–P4 反推)或手动按阶段推进;本次设计完成后的实现由用户决定是否衔接 long-running。〔design-Q lld 收尾惯例〕

## 补充声明

> 用户作答:14/14 全采纳(文件勾选,大写 [X]),无留空、无补充声明。

---

## 处理报告摘要(W00,2026-08-08)

- **preview 统计**:勾选采纳 14 / 留空不采纳 0 / 转 W01 正式题 0;取消默认率 0/14 = 0%。
- **落盘**:LLD [`harness/design/doctor-harness/LLD.md`](../../design/doctor-harness/LLD.md)(新建,14 条采纳落盘);无新增 ADR(ADR-0012/0013 已在 hld 阶段立)。
- **下一阶段**:lld 收尾——覆盖清单 + 阶段闸门 + 设计完成清单(dogfood/压测/实现衔接提议)。
