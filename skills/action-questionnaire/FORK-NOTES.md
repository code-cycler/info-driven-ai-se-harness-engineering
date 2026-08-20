# FORK-NOTES · action-questionnaire 有意分叉声明

> 仅含有意分叉条目(相对 design-Q canonical 引擎);完整设计决策见项目仓库 skills/action-questionnaire/DESIGN.md。分叉为永久分叉,不在四方同步范围内(OD-11)。

- W00 = **confirm-list(细节确认清单)**:语义从「决策默认值 + AI 默认倾向」(生成式)改为「行动细节 + AI 的理解」(确认式:AI 汇报理解,人核对);要点数建议 10–25 → **5–20**(行动轻量从简)
- 文件命名 `confirm-<slug>-w<NN>.md`,frontmatter `stage` 恒 `confirm`、`mode` 恒 `feature`
- 小波阈值 ≤2 → ≤4(创建期经验估值)→ **≤3**(四副本统一收紧;原估值待真实数据校准)
- 落盘无阶段文档;常规留痕 = 归档问卷(三条件升格 ADR/OD 照常)
- FORMAT 规则 7 强化:涉代码事实/外部依赖必须附核实证据(本 skill 铁律 2 的格式侧落地)
- 补充声明**第四类**:「用户先验结论 → 待验证假设」(分析中显式检验,不预设为结论,处理报告标注)——**仅本副本**(dogfood D-1 回修,用户裁决「只改 action-Q」)
