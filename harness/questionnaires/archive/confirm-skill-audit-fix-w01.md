---
mode: feature
wave: 1
stage: confirm
created: 2026-09-27
status: archived
---
# 问卷 confirm W01 · 修复方案决策点

> **与 W00 的关系**:W00(confirm-list)中**留空(理解有误/要改)**的要点,处理后会作为正式题**追加到本波尾部**逐个深究(≤3 题则不生成文件,小波直接问)。本波另列**开放型确认项**(多选/方向型,不适合 W00 的对/不对)。

> **填写规则**:
>
> 1. 每题勾选 `[x]`;默认单选,标「(多选)」可勾多个,选项数不限
> 2. ★ = 推荐选项,附推荐理由;**选项排序 = 非推荐在前 → 逃生舱倒数第二 → 推荐最后**(规则 14)
> 3. 每题末尾 🤔 是逃生舱:勾了 = 我定不了 → agent 走降风险协议,绝不重问
> 4. 选项都不合适 → 在 ✍️ 自定义 后自由书写
> 5. 标「条件:Qn 选 X 才答」的是内联浅分支,条件不满足直接跳过
> 6. **预勾选 = opt-in 开关**(默认关):你启动本 skill 时明确说「预勾选」才预勾推荐选项,否则全部 `[ ]`(规则 15;confirm-list 无选项,不适用)

## Q1. 高4 · D34 归档规则漂移(全文 vs 摘要)怎么收口?   [落盘: 四方 PROCESSING-RULES + 三副本 SKILL + 四方 CHANGELOG/DESIGN 留痕]

出题依据:主会话实测——design-Q `PROCESSING-RULES.md:82` 为「追加处理报告**全文**」(2026-08-20 D34 修订),grill/retro/action 三副本(如 `grill-questionnaire/PROCESSING-RULES.md:80`)仍为「追加处理报告**摘要**(落盘文件链接列表)」;三副本 FORK-NOTES 均无「归档粒度」分叉声明 → 不是有意分叉,是 D34 单方修订未走 OD-8 四方考量。铁律 6「原始信息不丢失」四 skill 同权。

- [ ] A. 保持三副本「摘要」不动,仅在四方 DESIGN.md 各记一笔「D34 为 design-Q 专属差异」 —— 零改动风险,但「摘要」丢失每题去向细节,跨会话回溯(提问波追加、long-running 反推)在 grill/retro/action 侧只有链接表
- [ ] B. 三副本保持「摘要」,但摘要内容扩为「每题去向一览」(折中粒度) —— 需新定义中间粒度,规则复杂化
- [ ] 🤔 我定不了 → 推迟/降风险
- [X] C. 四方同步为「追加处理报告全文,顶部保留摘要节」(design-Q 现行写法整体扩散),四方 DESIGN/CHANGELOG 各记同步一笔 ★推荐 —— 理由:三副本无有意分叉记录,属遗漏非设计;「单文件可回溯」语义四 skill 一致;且这是「内容同步」不是「抽共享文件」,不触 OD-8 禁令

- ✍️ 自定义: __________

## Q2. 高5 · LN 制词汇残留在 grill/retro 副本怎么清?   [落盘: grill/retro QUESTIONNAIRE-FORMAT + retro PROCESSING-RULES + 两方 FORK-NOTES]

出题依据:主会话实测——grill `QUESTIONNAIRE-FORMAT.md` L4 头注「LN 层名是 design-Q 词汇本 skill 不用」vs L12 命名行却写 `stage ∈ L0-vision | L1-contract | L2-build`(同文件自相矛盾);retro `PROCESSING-RULES.md:30-32` 落盘映射仍是「vision 阶段题 → VISION.md」旧词且零免责声明;retro FORMAT L11 同有 LN 命名行。action-Q 副本已彻底本地化(confirm- 命名,无此问题),是三副本中唯一干净的参照。

- [ ] A. 保留 LN 行,统一加与 grill 头注同款的免责注(「此行是 design-Q 词汇,本 skill 实际命名为 X」) —— 改动最小,但规则行仍写着他 skill 的词,读者需拼合两处理解
- [ ] B. 只修 grill 的 L4/L12 自相矛盾,retro 的 LN 旧词进 OD 待决 —— 半吊子,retro 侧漂移依旧
- [ ] 🤔 我定不了 → 推迟/降风险
- [X] C. 各副本改为本 skill 实际命名(grill FORMAT 命名行 → `grill-<slug>-w<NN>`;retro FORMAT 命名行 → `retro-<主题>-w<NN>`、PR 映射表 LN 旧词行改为 retro 实际产出物映射),两方 FORK-NOTES 登记此分叉 ★推荐 —— 理由:规则行写对而非打补丁;action-Q 已示范此形态;FORK-NOTES 登记 = OD-8 声明义务履行

- ✍️ 自定义: __________

## Q3. 高6 · grill-with-docs 文件结构示例的 ADR/OD 落点统一为哪套?   [落盘: grill-with-docs/SKILL.md + ADR-FORMAT.md(+OPEN-DECISIONS-FORMAT.md)]

出题依据:主会话实测——SKILL.md L117-130 单 context 示例画 `docs/adr/` + `docs/OPEN-DECISIONS.md`;L134-146 多 context 示例画 `docs/adr/`(系统级)+ 各 context `src/<ctx>/harness/adr/`;而同文件 L148 懒创建与 `ADR-FORMAT.md:3`「ADRs live in `harness/adr/`」均为 harness 制,OPEN-DECISIONS-FORMAT 引 HARNESS-RULES 第六节。两套并存,疑为 mattpocock 上游原文适配未清干净。

- [ ] A. 保留 `docs/adr/` 通用示例(适配无 harness/ 的普通仓),加注「harness 项目见 ADR-FORMAT 的 harness/adr/」 —— 示例与规则两处并存依旧,读者需自行仲裁
- [ ] B. 单/多 context 示例全删,只留 ADR-FORMAT 一处规则 —— 丢掉「目录长什么样」的直觉引导
- [ ] 🤔 我定不了 → 推迟/降风险
- [X] C. 示例统一为 harness 制:单 context = 根 `CONTEXT.md` + `harness/adr/` + OPEN-DECISIONS(位置按 HARNESS-RULES 第六节);多 context = `CONTEXT-MAP.md` + 各 context `<ctx>/harness/adr/`,并在示例旁注明「本 skill 默认绑库模式」 ★推荐 —— 理由:规则本体(ADR-FORMAT/L148/第六节)已选边 harness 制,示例跟上即消除双说;与 doctor-harness 布局权威一致

- ✍️ 自定义: __________

## Q4. 根因拷问产出之一:家族计数/主线状态「五处双写」怎么治理?   [落盘: docs/OPEN-DECISIONS.md]

出题依据:Agent C 发现+主会话证实——「skill 数量/主线状态」在 CLAUDE.md 状态节与 L41、TODO 头部、philosophy_v7:299、practical_v1:10、README:160 与目录树等多处双写,F051 十处联动清单仍漏哲学文件与状态节;本次 41 条中至少 7 条直接由此产生。结构性变更(收敛单源)是单向门级动作,不宜夹在修复批里。

- [ ] A. 本批直接收敛单源:TODO 头部为唯一权威,CLAUDE/README/philosophy/practical 全部改指针 —— 动 canonical 哲学文件表述结构,影响面大,与 41 条修复混批风险高
- [ ] B. 保持五处双写,仅把五处固定进联动清单(补全 F051 式清单) —— 仍是人记忆维护清单,已证会漏
- [ ] 🤔 我定不了 → 推迟/降风险
- [X] C. 本批落 OPEN-DECISIONS 记录该待决项(重访触发 = 下次家族规模变化/下次联动修订),结构性变更留给专门 feature;本批仅修既有 7 条失真条目 ★推荐 —— 理由:单向门决策不混批;OD 留痕即完成「拷问沉淀」;修复与治理分层

- ✍️ 自定义: __________

## Q5. 预防治理包:哪些机制项本批一并落地?(多选)   [落盘: 视所选项 = scripts/ 或 skill 文件或 OPEN-DECISIONS]

出题依据:根因分析(详见于处理报告)——「双侧同步有脚本所以 0 违规,计数/状态没脚本所以漂移」:有可执行断言的地方不漂移,靠人记忆清单的地方必漏。以下各项相互独立,可多选。**★推荐组合 = ①+③+④**(理由:直接对应你的「预防和治理」诉求,低成本机器可执行;②涉 skill 规则本体修改、⑤属归档位置偏好,均可再议)。

- [X] ① 计数/状态断言脚本:并入 harness-check.py 或新增 scripts(如 audit-check.py),机器断言「全仓 skill 计数一致 + TODO 头部状态 vs feature_list passes 一致」 —— 直接防住本批 6 条高危中的 3 条复发
- [X] ② 治理收尾 DoD 固定项:long-running SKILL/方法论补「治理收尾必含 TODO 勾销 + CHANGELOG 追加」—— 防 F052 式滞后复发(涉 skill 规则本体修改 + 双侧同步)
- [X] ③ 引擎前置检查步骤:四方 PROCESSING-RULES 各加「改引擎文件前强制 grep 其余三副本比对差异,同步或声明二选一并留痕」 —— 把 OD-8 协议从「自觉」变「步骤」
- [X] ④ sync-check 双向扫描:scripts/skills-sync-check.py 增「全局侧独有 skill 目录 → warning(登记 pilot 例外后不报)」 —— 堵主会话自查发现的方向性盲区
- [X] ⑤ 审查报告沉淀:本批三份 subagent 报告全文归档进 docs/(如 docs/retro/ 或 harness/design/skill-audit/) —— 知识不随对话消失(若不选,则仅随问卷归档附录)
- [ ] 🤔 我定不了 → 推迟/降风险
- [ ] ⑥ 全不做,只修 41+1 条,机制项仅停留在 Q4 的 OD 记录 —— 修复批最小化,但同类漂移无机器防线,可能复发

- ✍️ 自定义: __________

## Q6. 41+1 条修复的 CHANGELOG 记法?   [落盘: 各 skill CHANGELOG + 根 CHANGELOG]

出题依据:修复横跨 9 skill + 全局文档,CHANGELOG 是治理历史(追加式)不是问题清单;逐条记会产生大量碎片条目。

- [ ] A. 逐发现一条(41+1 条各一条) —— 最细粒度,但 CHANGELOG 膨胀,与「治理历史」定位不符
- [ ] B. 只在根 CHANGELOG 记一条总条目,skill CHANGELOG 不动 —— 违反「改 skill 必记该 skill CHANGELOG」惯例(且 design/retro 还有欠账要补)
- [ ] 🤔 我定不了 → 推迟/降风险
- [X] C. 每 skill CHANGELOG 一条汇总条目(列该 skill 修复点编号 + 指向归档问卷的处理报告全文),根 CHANGELOG 一条总条目,STATUS-LOG 一条 ★推荐 —— 理由:粒度与 CHANGELOG 定位匹配;逐条明细由问卷处理报告承载(附录含三份报告全文),CHANGELOG 链过去

- ✍️ 自定义: __________

---

## 补充声明

<任何想补充的话:新需求、格式反馈、范围调整、临时想到的风险……没有就留空。agent 处理时必读>是否有机制或流程可以强制跨会话信息传递或Handoff，使得每次会话不留尾巴，或能及时稳健的擦屁股？

---

# 处理注记(2026-09-27)

六题裁决已全执行:Q1=C/Q2=C/Q3=C/Q4=C(OD-30)/Q5=①②③④⑤全落/Q6=C。补充声明新需求(跨会话 handoff)→ 分析回应见 [04-root-cause-and-governance.md](../../design/skill-audit/04-root-cause-and-governance.md) §五,决策风险落 **OD-31**(候选方向 A 钩子/B 清单/C pre-commit,倾向 A+C,重访触发三条)。完整处理报告与逐条去向见 [confirm-skill-audit-fix-w00.md](./confirm-skill-audit-fix-w00.md) 尾部。
