# 归档问卷索引(harness/questionnaires/archive/)

> 已处理问卷归档区,按 feature/主题子目录组织(HARNESS-RULES 第四节)。只移不删,文件名不变。
> 子目录化迁移:2026-08-08(doctor-harness 治理,用户裁决「存量不挪 → 允许整批迁移」)。

## 子目录一览

| 子目录 | 内容 | 份数 |
|---|---|---|
| `methodology/` | methodology v2/v3 设计 + 三块拆分 + 哲学 v4 压测(W01+W02)+ 学科挂接压测 | 10 |
| `repo-design/` | repo 级设计(repo 级设计落地) | 6 |
| `skill-spec-revamp/` | design-Q skill 规格整理(方案 R + 骨架改造) | 7 |
| `doctor-harness/` | doctor-for-harness 设计套 + 压测 | 5 |
| `skills-harness-consistency/` | 方案 R 撤销 / skill 一致性 | 1 |
| `ai-autonomy/` | AI 双轨照 pilot 压测(OD-13) | 2 |
| `preaction-confirm/` | action-Q 立项压测 | 1 |
| `merge-grill-family/` | grill 家族合并压测(作废框架) | 1 |
| `harness-file-mgmt/` | harness 文件管理规格压测 | 1 |
| `_misc/` | confirm 散件(非单一 feature 归属的行动确认) | 10 |
| `philosophy-v5/` | philosophy_v5 design-Q(feature,vision/hld/lld)+设计压测 | 4 |

## 检索说明

- long-running 重建上下文时,按 feature/主题定位归档问卷(而非平铺 grep);
- 新归档按 feature/主题入对应子目录;无对应子目录 → 建新子目录或入 `_misc/`(非 feature 归属);
- 归档文件保持「只移不删」,文件名不变。