# long-running-agent · CHANGELOG

> 本 skill 治理历史。本 skill 无 DESIGN.md;无规则本体级双侧分叉,故无 FORK-NOTES。追加式,只增不改。

## 2026-08-20 · P1 治理历史迁移(governance-history-split F040)

- **变更**:SKILL.md 4 处日期注记剥离(「2026-08-16 P5」系出处)+ 头部索引行;新建本 CHANGELOG;维持无 DESIGN.md。JSON 示例中的时间戳字面量非治理注记,保留。
- **原因**:ADR-0024 治理历史分离 P1。
- **影响**: SKILL.md
- **出处**: [L1 契约](../../harness/design/governance-history-split/L1-contract-gov-history-split.md) + ADR-0024

## 2026-08-16/17 · P5 双模式拓展 + LN 制衔接(designq-digital-levels)

- **变更**:① §5.4 与 design-Q 的衔接(末层收尾、grill-Q 之后、多线程停点询问两分支);② §5.3 从落盘文件重建上下文(LN 制:层文件 + 归档问卷;feature 反推规则 = 最低构建语义层,无构建层从 L0 验收反推);③ §5.5 准备模式与执行模式(多 worktree 多 agent 拓展,优先 Claude Code 原生多 agent 通信;任务包五字段;三层合并防线;线程失败回退);④ 「一次只处理一个功能」收窄为限定式(单 worktree 会话内;多 worktree 并行 = 执行模式 + 人确认任务包边界,provisional 待首次真实使用复核);⑤ §2 初始化脚本废止(环境启动归项目工具链)。F027–F034 全链落地(commit 80a18c3…a9086be)。
- **出处**: [ADR-0022](../../harness/adr/0022-design-questionnaire-digital-levels.md) + designq-digital-levels HLD/LLD + retro-designq-digital-levels_v1

## 2026-03(初版)· 创建

- **变更**:基于 Anthropic《Effective harnesss for long-running-agents》建 skill——增量工作/清晰工件/整洁状态/端到端验证四理念;feature_list.json + claude-progress.txt 两核心文件;会话启动 checklist;测试验证要求(passes:true 只在端到端通过后)。
- **出处**: Anthropic 工程文章(文首链接)
