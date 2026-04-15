# Multidimensional Styling (Cross-Ruling) Audit

**Explanation:** With the shift towards highly granular, atomic files, we need the ability to enforce "multidimensional styling." Rules should be able to intersect and enforce standards across distributed, granular code and text nodes.

**Reference:**
- `src/wiki_compiler/auditor.py`
- `wiki/standards/house_rules.md` (ID-3, OP-5)

**What to fix:**
1. Upgrade `wiki-compiler audit` to support "Rule Intersection" (cross-ruling)
2. Query graph for multiple intersecting properties (e.g., uses Library X AND performs Disk I/O)
3. Flag `cross_ruling_violation` when dimensions clash

**How to do it:**
1. Add composite rule checking in auditor.py
2. Add intersection query capability
3. Add cross_ruling_violation audit finding type

**Depends on:** 7 (replace node count heuristic)
