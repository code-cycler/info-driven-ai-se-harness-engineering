# ADR-0002: License 混合协议——方法论文字 CC-BY 4.0,skill 配置 MIT

- 日期:2026-07-28
- 状态:accepted
- 来源:建仓前 grill-questionnaire 压测(Q2A)

## 背景

本仓库内容性质混合:方法论文章是文字(适合 CC-BY 4.0);skill 的 SKILL.md + 引擎副本(QUESTIONNAIRE-FORMAT.md / PROCESSING-RULES.md)更偏可执行配置 / 规则(适合 MIT / Apache-2.0)。License 一旦发布、被人引用后很难改——单向门。方法论文章附录引用了 Nygard / Beck / Anthropic 等外部来源(灵感来源,非直接引用,标注即可)。

## 决策

**混合协议**:方法论文字(docs/methodology)用 **CC-BY 4.0**,skill 配置(SKILL.md、引擎副本、归档示例、scripts)用 **MIT**,README 顶部明确声明分区。

## 替代方案

- **全 MIT(含文章)**:MIT 对纯文字不贴切,不利转载归属。
- **全 CC-BY 4.0**:skill 配置用 CC 不合开发者习惯,阻碍「直接拷进 `~/.claude/skills` 复用」。
- **Apache-2.0(skill)+ CC-BY 4.0(文章)**:Apache 带专利条款,本仓库无专利场景,偏重。

## 后果

- (+) 文字可署名转载、skill 可自由复用,各得其所。
- (+) skill 的 MIT 与常见 harness / agent 项目协议一致,降低复用摩擦。
- (−) 混合协议需 README 明确分区。
- (−) skill 引擎副本(QUESTIONNAIRE-FORMAT / PROCESSING-RULES 自标「design-Q 引擎复用件」)版权:本仓库作者原创,MIT 化无障碍(见 [OD-8](../OPEN-DECISIONS.md))。
