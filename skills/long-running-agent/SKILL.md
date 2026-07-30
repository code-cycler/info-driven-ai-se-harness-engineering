---
name: long-running-agent
description: "长时间运行、跨多会话复杂项目的约束系统。增量工作(一次只处理一个功能)、feature_list.json 功能列表、claude-progress.txt 进度记录、端到端测试验证(只有通过测试才标记 passes:true)、Git 整洁状态、约定式提交。触发:多会话/长周期项目、需要 feature_list 跟踪、长期工程任务、跨上下文窗口的工作、design-questionnaire LLD 收尾后衔接实现期。Use when a project enters long-running implementation spanning multiple sessions / context windows, or after design-questionnaire LLD hands off to implementation."
---

# long-running-agent (长时间运行代理约束系统)

> 基于 Anthropic 官方文章《Effective harnesses for long-running-agents》
> **原文链接**: https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents
>
> 本 skill 是**通用开发工具**,不绑定任何特定项目。术语用 Claude Code 语境:文中「压缩上下文」指 Claude Code 的 `/compact`,不是任何产品级的 Compression 概念。

## 1. 解决什么问题

跨多个上下文窗口的复杂任务里,AI 代理容易:

1. **一次性做太多** → 半成品堆积
2. **过早宣布完成** → 部分功能完成就当项目完成
3. **未测就标完成** → 功能标记 `passes:true` 但没跑端到端测试
4. **会话间失忆** → 新会话没有前一会话的记忆(本 skill 用**落盘文件**对抗失忆,不依赖会话上下文)

### 核心理念

- **增量工作**:一次只处理一个功能
- **清晰工件**:为下一会话留下清晰的进度记录(写进文件,不是上下文)
- **整洁状态**:代码始终处于可合并到主分支的状态
- **端到端验证**:只有通过完整测试才标记功能完成

## 2. 项目文件

长时间运行项目应包含以下核心文件:

```
project/
├── .claude/
│   ├── feature_list.json      # 功能需求列表
│   └── claude-progress.txt    # 进度记录文件
├── src/                       # 源代码
├── tests/                     # 测试文件
└── .git/                      # Git 仓库
```

| 文件 | 用途 |
|------|------|
| `feature_list.json` | 所有功能需求及其状态;首会话创建,后续会话更新状态 |
| `claude-progress.txt` | 每个会话的工作记录;会话结束时更新 |

> **不再使用初始化脚本**(init.sh / init.bat)。环境启动由项目既有的工具链(README / Makefile / package.json / build 脚本等)承担,本 skill 不创建启动脚本。

## 3. 功能列表规范 (feature_list.json)

### JSON 格式

```json
{
  "project_name": "项目名称",
  "created_at": "2026-03-03T10:00:00Z",
  "features": [
    {
      "id": "F001",
      "category": "functional",
      "priority": "high",
      "description": "功能描述",
      "steps": ["测试步骤1", "测试步骤2", "测试步骤3"],
      "passes": false,
      "last_tested": null,
      "notes": ""
    }
  ]
}
```

### 字段说明

| 字段 | 类型 | 说明 |
|------|------|------|
| `id` | string | 功能唯一标识符(如 F001) |
| `category` | string | 类别:`functional` / `ui` / `api` / `performance` / `security` |
| `priority` | string | 优先级:`high` / `medium` / `low` |
| `description` | string | 功能的清晰描述 |
| `steps` | array | 验证此功能的测试步骤 |
| `passes` | boolean | 功能是否通过端到端测试 |
| `last_tested` | string | 最后测试时间(ISO 8601) |
| `notes` | string | 备注或已知问题 |

> 若项目经过 design-questionnaire 设计,`features` 优先从 LLD 的**阶段拆分**与 DoD 反推,而非凭空列举——见 §5.3。

## 4. 进度文件规范 (claude-progress.txt)

### 格式

```
================================================================================
SESSION: <会话编号>
时间: <ISO 8601 时间戳>
================================================================================

## 完成的任务
- <任务描述>

## 修改的文件
- <文件路径>: <简要说明>

## Git 提交
- <commit hash>: <提交信息>

## 遇到的问题
- <问题描述及解决方案>

## 下一步计划
- <下一个待处理的功能 ID>

================================================================================
```

新会话写入文件**顶部**(最新在上),历史会话向下堆叠。

## 5. 会话启动检查(单一流程)

> 不再区分「初始化代理」与「编码代理」。首会话与后续会话共用一份启动 checklist,区别只在 feature_list.json 是否已存在。

### 5.1 启动 checklist

```
1. 确认工作目录
   [ ] pwd 确认工作目录,只能在此目录编辑文件

2. 重建上下文(从落盘文件,不依赖会话上下文)
   [ ] 读 claude-progress.txt 了解最近工作
   [ ] git log --oneline -10 查看最近提交
   [ ] 读 feature_list.json 了解功能状态
   [ ] (若存在)读 design-Q 产出的 VISION / HLD / LLD 与归档问卷

3. 验证基础环境
   [ ] 用项目既有工具链(README / Makefile / build 脚本)启动环境
   [ ] 执行基础测试确认环境正常;发现问题优先修复

4. 选择下一个功能
   [ ] 从 feature_list.json 选优先级最高且未完成(passes:false)的功能
   [ ] 一次只处理一个功能

5. 实现功能
   [ ] 编写代码
   [ ] 编写测试
   [ ] 执行端到端测试

6. 更新状态
   [ ] 只有通过所有测试才设 passes:true
   [ ] 更新 claude-progress.txt(写顶部)
   [ ] Git 提交(遵循项目既有提交约定)

7. 会话结束检查
   [ ] 代码处于整洁状态
   [ ] 所有测试通过
   [ ] 进度文件已更新
```

### 5.2 首会话额外步骤

feature_list.json 不存在时,先创建它:

```
[ ] 分析需求,提取所有功能点
[ ] 编写 feature_list.json,所有功能 passes:false,每个含详细测试步骤
[ ] 创建 claude-progress.txt,记录初始设置完成
[ ] git init(若未初始化)+ 初始提交
```

### 5.3 从落盘文件重建上下文(关键机制)

**会话上下文可能被压缩(Claude Code `/compact`)而丢失设计期决策细节**。本 skill 不依赖会话上下文重建项目认知,而是从落盘文件:

- **有 design-Q 产物**:读 VISION / HLD / LLD + `docs/questionnaires/archive/` 归档问卷,从 LLD 阶段拆分反推 feature_list 的 features。
- **无 design-Q 产物**:读 claude-progress.txt + feature_list.json + git log,从历史会话与代码现状重建。

机制自洽:无论上下文是否被压缩,落盘文件都是 source of truth。

### 5.4 与 design-questionnaire 的衔接

design-Q 在 LLD 阶段收尾、grill-questionnaire 压测之后,会提议触发本 skill(衔接实现期)。衔接时:

- design-Q 产出的 VISION / HLD / LLD 是 feature_list 的 source of truth。
- 用户可拒绝衔接,随后随时手动调用本 skill(见 §7 触发契约)。

## 6. 增量工作原则

### 一次只处理一个功能

**必须严格遵守**:

```
[OK] 正确
1. 选一个功能 → 完整实现 → 编写并运行测试 → 通过则更新状态 → 提交 → 下一个

[X] 错误
1. 同时开始多个功能
2. 留下多个半成品
3. 未测试就标记完成
```

### 代码整洁状态

每个会话结束时,代码应处于:

- 无重大 Bug,现有功能正常
- 代码有序、易理解
- 测试全过
- 可合并到主分支

### Git 提交规范

**优先遵循项目既有约定**(项目的 AGENTS.md / CLAUDE.md / contributing guide)。若项目无约定,默认使用约定式提交:

```
<type>(<scope>): <description>
```

type:`feat` / `fix` / `refactor` / `test` / `docs` / `chore`。

示例:`feat(student): 添加 ID 验证功能` / `fix(course): 修复学生计数错误`。

> 本 skill 不重写项目的提交规则——项目级约定优先,skill 只在缺省时给默认。

## 7. 触发契约

- design-Q LLD 收尾、经 grill-Q 之后**提议一次**,可拒绝。
- grill-Q 被拒时紧接提议;grill-Q 被接受时压测完成后再提议。
- 拒绝后实现期不再自动提议;用户随时可手动调用(`/skill` 或自然语言「启动 long-running-agent」)。
- 手动触发不受上下文压缩影响——从落盘文件重建(§5.3)。

## 8. 测试验证要求

### 端到端原则

**核心原则**:只有通过端到端测试才能将功能标记为 `passes: true`。

```
1. 实现功能代码
2. 编写测试用例
3. 运行单元测试 + 集成测试
4. 手动验证(如适用)
5. 全部通过 → passes:true
6. 任一失败 → 保持 passes:false,继续修复
```

### 功能标记规则

```json
// [OK] 全部测试通过
{ "passes": true, "last_tested": "2026-03-03T15:00:00+08:00", "notes": "所有测试通过" }

// [X] 未测试就标 true —— 禁止
{ "passes": true, "last_tested": null }

// [OK] 测试失败保持 false
{ "passes": false, "last_tested": "2026-03-03T15:30:00+08:00", "notes": "用例 3 失败,需修复边界条件" }
```

### 禁止行为

| 禁止 | 原因 |
|------|------|
| 删除或修改测试步骤 | 可能导致功能缺失或 Bug |
| 未测试就标记 passes:true | 产生不可靠的功能状态 |
| 跳过失败的测试 | 隐藏潜在问题 |
| 删除功能项以减少工作量 | 功能永久丢失 |
| 一次处理多个功能 | 容易产生半成品代码 |

## 9. 失败模式与恢复

### 问题-对策

| 问题 | 对策 |
|------|------|
| 过早宣布项目完成 | 会话开始读 feature_list,选未完成功能继续 |
| 留下有 Bug 或未记录的代码 | 会话开始读 progress + git log + 跑基础测试;会话结束提交 Git 并更新 progress |
| 过早标记功能完成 | feature_list 定义详细测试步骤;只有端到端通过才 passes:true |
| 尝试一次性做太多 | 一次只处理一个功能,完成才继续下一个 |

### 恢复策略

代码处于不良状态时:

```
1. 识别问题
   [ ] 跑测试确认哪些功能失败
   [ ] git log 找到最后稳定版本
   [ ] 读 progress 了解最近变更

2. 恢复稳定状态
   [ ] git revert 撤销问题提交
   [ ] 或 git reset --hard <commit> 回到稳定版本(谨慎使用)
   [ ] 重新跑测试确认恢复

3. 重新开始
   [ ] 更新 progress 记录恢复操作
   [ ] 重新选功能,这次用更小更安全的步骤
```

## 10. 快速参考

### 会话启动检查清单

```
[ ] 1. pwd 确认工作目录
[ ] 2. 读 claude-progress.txt(最近工作)
[ ] 3. 读 feature_list.json(功能状态)
[ ] 4. (若存在)读 VISION/HLD/LLD(design-Q 产物)
[ ] 5. git log --oneline -10(最近提交)
[ ] 6. 项目既有工具链启动环境 + 基础测试
[ ] 7. 选下一个功能
```

### 会话结束检查清单

```
[ ] 1. 所有测试通过
[ ] 2. 代码整洁状态
[ ] 3. 更新 feature_list.json(若有功能完成)
[ ] 4. 更新 claude-progress.txt(写顶部)
[ ] 5. Git 提交(项目既有约定)
[ ] 6. 向用户报告
```

### 强制执行

**这是长时间运行项目的核心规则,必须严格遵守:**

- 任何时候都不跳过会话启动流程
- 任何时候都不一次处理多个功能
- 任何时候都不未测试就标记完成
- 任何时候都不留下不整洁的代码状态
- 必须始终为下一会话留下清晰的工件
