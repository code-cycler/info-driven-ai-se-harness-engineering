---
mode: feature
wave: 0
stage: confirm
created: 2026-08-18
status: archived
---
# 问卷 confirm W00 · 细节确认清单（AI 汇报理解，人核对）

> **本波是细节确认清单**（独立 wave 0）：把 AI 对本次行动细节的理解逐条列出，人只做「对/不对」核对。
>
> **作答规则**：
>
> - 勾 `[x]` = **理解正确**（按该理解执行）
> - 留空 `[ ]` = **理解有误或要改** → 该要点转正式题深究（或小波直接问）
> - 本波**不用 🤔**（对/不对二选一，无中间态）；「大体对但要改一两处」→ 留空，转正式题时在深究题里给正确值
>
> 来源标注于〔〕：〔推断〕= AI 填的，重点核对；〔用户原话 / 代码 / 文档 / 实测〕= 有据。
>
> 上下文：本次行动 = 同步「项目版 `skills/action-questionnaire/`」与「全局版 `~/.claude/skills/action-questionnaire/`」（后者即当前正在运行的 skill 本体，用户称之为「测试时的脚本」）。

## 细节确认清单

### 目标

- [X]  **1 行动定义**：让 action-questionnaire 双侧四文件（SKILL.md / PROCESSING-RULES.md / QUESTIONNAIRE-FORMAT.md / DESIGN.md）内容一致——双向同步，取各侧正确内容，非整目录单向覆盖。〔用户原话：「本项目的全局同名skill是测试时的脚本，现在将两者同步」〕
- [X]  **2 差异全景（已逐文件 diff 实测，唯一事实源）**：
  - SKILL.md：**2 处**——全局版（8/14）写「OPEN-DECISIONS.md（归属见 HARNESS-RULES.md 第六节）」，项目版（8/8）写「docs/OPEN-DECISIONS.md」；
  - PROCESSING-RULES.md：**1 处**——同上（全局版「OPEN-DECISIONS.md（归属见 HARNESS-RULES.md 第六节）」vs 项目版「docs/OPEN-DECISIONS.md」）；
  - QUESTIONNAIRE-FORMAT.md：**0 处**——双侧已一致（8/18 edde759 四副本对齐时同步）；
  - DESIGN.md：**3 处**——项目版归档引用带子目录（`preaction-confirm/`、`_misc/`），全局版不带（8/8 归档子目录化前的旧引用）。
    〔实测：`diff -u` 四文件逐一对齐〕
- [X]  **3 合并方案（推荐）**：按「各处取正确」执行——
  - SKILL.md / PROCESSING-RULES.md：**全局版 → 项目版**——8/14 修订与权威一致（已核实 HARNESS-RULES.md 第六节原文：「各 skill 文档不内联复制本条路径，引用『治理文件归属见 HARNESS-RULES.md』」，与全局版表述同源同日）；项目版停在 8/8，漏了这轮修订；
  - DESIGN.md：**项目版 → 全局版**——归档实际位置实测带子目录（`find` 实证），项目版引用正确、其「docs/...→子目录化修复」来自 d2d1057；全局版是断链旧引用；
  - QUESTIONNAIRE-FORMAT.md：**不动**（已一致）。
    〔实测：归档目录 `find` 实证三份问卷均在子目录内；文档：HARNESS-RULES.md 第六节、git d2d1057/edde759〕
- [X]  **4「测试时的脚本」的含义（推断项，重点核对）**：我理解为——全局版自 8/14 起被直接编辑过（OPEN-DECISIONS 归属修订只落在全局版，未同步回项目发布版），处于「测试/工作副本」状态；本次即把这份测试中确认过的内容同步回项目版。若你指的含义不同（如测试中产生过其他改动、或有该清理的测试痕迹），留空并在补充声明纠正。〔推断；佐证：两目录 mtime（全局 8/14 vs 项目 8/8）+ git 历史（项目版 8/8 后无对应提交）〕

### 输入

- [ ]  **5 素材范围（留空纠正 → 已解析）**：~~只动 action-questionnaire~~ → **9 个 skill 全部核对同步**（用户补充声明）。已实测核对全景：3 个已一致（design-Q / grill / long-running-agent）、6 个有差异（action-Q / delegate / doctor-harness / grill-with-docs / grill-Q / retro-Q）。〔用户补充声明；实测：9 skill 双侧 diff〕
- [X]  **6 现有内容验证**：本次同步只搬运既有内容（全局版 3 处修订 + 项目版 3 处路径引用），不重写、不润色、不改语义、不新造内容。〔skill 铁律：原始信息不丢失、不越界做设计〕

### 输出

- [ ]  **7 同步后验收（留空纠正 → 已解析）**：~~双侧四文件逐字节一致~~ → **双侧 9 skill 全部文件逐字节一致**（`diff -r` 复查 0 差异）；项目版 Git 工作树干净（提交后）。〔用户补充声明；衡量标准随范围扩大〕
- [X]  **8 Git 提交**：项目版改动按仓库惯例提交（conventional commits，如 `fix(skills): ...`/`docs(skills): ...`），提交信息我拟、你审后提交；**不推送**（推送另行授权）。〔仓库惯例：提交历史风格；推断〕
- [X]  **9 脱敏复验**：同步后跑 `python3 scripts/desensitize.py .` 复验 0 命中（发布门 DoD）。修订内容为路径/归属文字，预计不引入命中；以实测为准。〔文档：CLAUDE.md 发布门〕

### 约束

- [ ]  **10 不越界修改（留空纠正 → 已解析）**：~~仅 action-Q 四文件~~ → **范围 = 9 个 skill 双侧文件**（cross-skill 差异同步亦属行动本身）；repo 其余区域（docs/、harness/、scripts/ 等）仍不动；引擎四副本不借机统一（OD-8 边界不变）。〔用户补充声明〕
- [X]  **11 生效时机**：全局版即当前运行中的 skill；同步后本会话仍按旧定义运行，重启新会话后生效。此为自然行为，无需额外处置。〔系统事实：本 skill Base directory = `~/.claude/skills/action-questionnaire`〕

### 边界

- [X]  **12 归档位置**：本问卷处理完移入 `harness/questionnaires/archive/`，按 8/8 子目录化惯例放 `_misc/`（action-Q 既往 10+ 份 confirm 案例所在）。〔实测：archive/_misc/ 下 confirm-* 齐集；惯例〕
- [X]  **13 同步遗留的全局版设计差异（主动提出的动态盲点）**：全局版 DESIGN.md 的过时路径暴露「8/8 归档子目录化回修（d2d1057）未覆盖全局副本」——说明 8/8 前后存在「项目内修、全局漏修」的同步空隙。本次修掉实内容；同步机制层面是否要治理（如双侧同步清单/检查点）**不在本次行动范围**，只记录到处理报告，供后续 OD/TODO 候选。〔推断；佐证：d2d1057 改动清单 vs 全局版现状〕

### 依赖

- [X]  **14 无外部依赖**：纯文件复制/编辑操作，不涉库、工具链、网络、外部服务。〔推断〕

## 补充声明

（第四类「用户先验结论」如涉及请填此，标注是否已验证；亦可用于留空项的纠偏答案）对9个skill都进行核对同步

---

## 处理报告摘要(2026-08-18)

- **confirm-list 统计**:确认正确 11 / 留空纠正 3(5 素材范围、7 验收标准、10 不越界——同源:范围扩至 9 skill)。
- **补充声明**:「对9个skill都进行核对同步」→ 已实测检验(9 skill 双侧 diff 全景)后执行。
- **小波直问(2 题)**:① doctor-harness CHANGELOG 外部记录处置 → 用户裁决「只同步规则性增补」(8/14、8/16 规则性条目脱敏后进项目版;8/11×3、8/17 外部实证条目留全局,双侧 CHANGELOG 为已知例外不逐字节一致);② 脱敏措辞原则 → 用户裁决「统一项目版脱敏措辞」(全局侧真实名全部替换为宿主项目/项目B/外部项目等占位措辞,覆盖 8/14「置留不改」裁决)。
- **执行**:9 skill 全部核对——3 个本已一致(design-Q / grill / long-running)不动;6 个差异 skill 双向合并——A 型(全局 8/14「OPEN-DECISIONS 归属见 HARNESS-RULES 第六节」修订回灌项目)5 文件:action-Q SKILL+PROCESSING-RULES、grill-with-docs SKILL+OPEN-DECISIONS-FORMAT、retro-Q PROCESSING-RULES;B 型(项目路径修复+脱敏措辞同步全局)11 文件:action-Q DESIGN(3 处归档子目录路径)、delegate SKILL/DESIGN/template、doctor-harness HARNESS-RULES(1 处脱敏)+DESIGN(1 处路径)、grill-Q grill-own-design-w01(链接+真实名×5+file:// 简写)、retro-Q hld_v1/hld-w01(路径)/vision-w01(脱敏×4);混合 3 处:delegate template 补「(如新 EntityKind)」例、grill-Q DESIGN 补 8/14 归属修订(项目侧)+ ✍️ 教训节(全局侧)、doctor-harness CHANGELOG 补 4 条规则性增补(脱敏措辞)。
- **异常**:① 本会话曾误判问卷文件被覆盖(实为 Read 缓存误判,用户作答完好);② Bash/Edit 分类器多次临时不可用,改用 Read+Write/Edit 完成大部分同步;③ delegate DESIGN 行尾换行方向一度加反,已双向修正;④ CHANGELOG 增补初版带入 1 处真实名(desensitize 抓出),已修;⑤ 本摘要自身初版复述了 4 处真实名(上轮追加摘要后未复跑脱敏——流程缺口,2026-08-19 机制化行动复验抓出),本轮已泛化修复;该教训即「追加内容后必须复跑检查」的直接例证,亦为本次机制化的注脚。
- **验证**:9 skill diff -r 复验 0 差异(doctor-harness CHANGELOG 为裁决例外,项目版少 5 条外部实证条目);`desensitize.py` 0 命中;`harness-check.py` 0 违规;三项 EXIT=0。
- **覆盖度**:六要素全覆盖;动态盲点(条目 13「项目内修、全局漏修」同步空隙)已确认存在且本次实际处理 6 个 skill 的该类空隙,机制层治理留 OD/TODO 候选(未立项,超本次范围)。
- **产物**:双侧 9 skill 一致;项目版 git 改动待提交(提交信息另呈用户审)。
