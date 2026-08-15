# P5(long-running 双模式)变更清单

| 变更 | 位置 |
|---|---|
| description:单 agent 默认 + 准备/执行模式 + 多 worktree + SendMessage 触发词 | frontmatter |
| §5.3 feature 反推 LN 制(最低构建语义层 + L0 兜底;旧三件别名) | 反推规则 |
| §5.4 停点两分支(单线程直接实现/多线程转准备模式) | 衔接 |
| §5.5 新节:准备模式(任务包五字段+人审查确认)/执行模式(后台 agent 各驻 worktree+SendMessage+合并三层防线+线程失败回退);模式切换由人确认 | 新节 |
| §6/§8/§10 三处禁令限定式(provisional:多 worktree 首次真实使用复核) | 禁令调和 |
