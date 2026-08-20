# MIGRATION-FLOW · harness 目录迁移流程

> harness 区(design/ + questionnaires/ + adr/)目录重组的**可跟随执行流程**。逐步手动执行 + 校验脚本验证,不自动化。
> 依据:[ADR-0013](../../harness/adr/0013-harness-layering-migration.md)(迁移执行)+ [ADR-0012](../../harness/adr/0012-harness-layering-rule.md)(分层规则)+ 历次迁移先例(见下表与 CHANGELOG)。

## 何时用

- 引入新分层规则(如 design/<feature>/ 聚合)后,重组既有目录;
- harness 组织混乱(裸放/子目录混用、归档平铺膨胀)需要治理;
- 任何将移动/重命名 harness 文件的场景。

## 流程(7 步)

### 1. 设计新布局

按 [HARNESS-RULES.md](./HARNESS-RULES.md) 判定句逐条核对现有文件归属:

- **design/**:feature 级设计(会被独立引用/与其它 feature 冲突)→ 建 `design/<feature-slug>/`;全局/单文件设计裸放根下;
- **questionnaires/**:新归档按 feature/主题建子目录;存量不挪;
- **adr/**:编号平铺是硬约束,不因 feature 分组破坏。

产出:**迁移清单**(文件 → 目标位置),人审确认。

### 2. 挪文件

- 用 `git mv` 保持 rename 历史(可追踪);
- **只移不删,文件名不变**(原始信息不丢失铁律);
- 存量不挪原则:仅被判定句要求重组的文件动,其余原样。

### 3. 相对链接重算

- 列出受影响文件(尤其**归档问卷的跨目录引用**——从 `questionnaires/` 移入 `archive/` 时,`../design/` 变 `../../design/`,层级加深一层);
- grep 修正:`grep -rn '\.\./' ` 受影响目录,核对每个链接目标;
- 常见错误:归档问卷 `../design/` → 应为 `../../design/`(移入 archive/ 后多一层)。

### 4. 断链回归

- 全库相对链接检查(脚本扫描 `](...)` 且非 http/# 目标,解析目标存在性);
- 本次迁移引入的断链必须 **0**;
- 存量断链(历史遗留,如中文短语误渲染)登记豁免,不修。

### 5. 跑校验

```bash
python3 scripts/harness-check.py ./harness
```

- 0 违规(无输出)+ 0 断链 ✓;
- 违规清单 → 人决定是否修。

### 6. 规格同步

- 若各 SKILL.md 引用的路径变化(如分层后子目录层级),同步引用句;
- 分层规则本身在 HARNESS-RULES.md,SKILL.md 只引用不复制。

### 7. 留痕

- 迁移记录追加到 doctor-harness [CHANGELOG.md](./CHANGELOG.md)(日期 + 变更 + 原因);
- 若迁移发现规则缺口(未覆盖场景),更新 HARNESS-RULES.md。

## 先例参考

| 迁移 | 范围 | 结果 |
|---|---|---|
| 2026-08-05 harness 区物理分离 | docs/design + docs/questionnaires → harness/ | 96 断链 → 7 豁免 |
| 2026-08-08 分层落地 | design/ 天然分层确认 + 归档链接修复 | 9 处层级链接修复,存量 3 豁免 |

## DoD(迁移完成判据)

- [ ] 迁移清单全部执行(git mv 可追踪);
- [ ] 相对链接全部重算,本次引入断链 0;
- [ ] `harness-check.py` 0 违规;
- [ ] SKILL.md 引用同步(若路径变化);
- [ ] CHANGELOG 留痕