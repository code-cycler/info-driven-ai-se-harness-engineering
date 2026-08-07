# ADR-0011: 放弃方案 R(落盘根配置化),回归硬编码 `harness/`

- 状态:accepted
- 日期:2026-08-07

## 背景

方案 R(落盘根配置化)在 skill-spec-revamp(`harness/design/skill-spec-revamp/`)设计:让 4 个问卷 skill(design-Q / grill-Q / retro-Q / action-Q)+ long-running 的落盘目录由「读项目 CLAUDE.md 声明 → 默认 `harness/` → 落盘前确认」动态决定,而非硬编码,以便 skill 通用化(别的项目可声明别的根)。

方案 R 于 2026-08-07 在 `~/.claude/skills/` 落地(feature_list F007–F010 标 passes:true),但:
- 本仓库 `skills/`(发布镜像)未同步,两套漂移约 30 文件;
- feature_list 的 passes 标记对应 `~/.claude` 版,对本仓库读者构成误导(违反 long-running「passes 必须端到端测试通过」铁律);
- 用户审查后决策:不需要配置化通用性,要求所有 harness 文件硬编码放 `项目根/harness/`。

用户决策来源:`confirm-skill-harness-sink-w00` 补充声明 + hld W00 D1–D8 全采纳(归档 `harness/questionnaires/archive/`)。

## 决策

1. **放弃方案 R**:撤销「读 CLAUDE.md 声明 → 默认 → 落盘前确认」的落盘根配置化机制;4 问卷 skill + long-running 的落盘路径回归硬编码 `项目根/harness/`(design/ + questionnaires/ + adr/)。
2. **保留 F007 骨架改造**:design-Q STAGE-SKELETONS 的判别法则 / 反简化 / 最小必含 / 分档节与路径无关,**不在本撤销范围**,保留并回灌仓库(见 LLD P2)。
3. **固有文件不动**:CONTEXT.md / OPEN-DECISIONS.md / TODO.md / docs·retro/ 维持 ADR-0009 三区模型的项目固有位置。
4. **善后**:feature_list F008/09/10 标撤销(passes=false)、skill-spec-revamp 设计文档顶部标注「路径配置化部分放弃」,不删历史(原始信息不丢失)。

## 替代方案

- **保留方案 R,回灌仓库**:维持配置化通用性。否决——用户明确不需要(个人开发者单仓库,无多项目不同根场景),配置化的读声明/确认开销无收益,且两套漂移已造成 passes 标记误导。
- **方案 R + 仓库同步**:技术上可消除漂移,但用户决策是放弃机制本身(不要运行时配置化),非同步问题。

## 后果

- (+) skill 落盘路径简单确定(硬编码 `harness/`),无运行时确认开销;消除仓库 vs `~/.claude` 的方案 R 漂移源。
- (+) feature_list passes 标记回归真实(本仓库文件即被测对象)。
- (−) skill 不再「入乡随俗」——若将来用于声明非 harness 根的项目,需改 skill 或重新引入配置化(双向门,可逆)。
- (−) 方案 R 的设计投入(skill-spec-revamp 设计套)成为废弃分支,留历史标注不删。
