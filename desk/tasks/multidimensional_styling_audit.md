# Implement Multidimensional Styling (Cross-Ruling) Audit

With the shift towards highly granular, atomic files, we need the ability to enforce "multidimensional styling." Currently, rules are applied individually. We need a mechanism where composite rules (cross-ruling) can intersect and enforce standards across distributed, granular code and text nodes. 

For instance, if Rule A dictates patterns for a specific library, and Rule B dictates patterns for I/O writing, the intersection of those rules should dynamically standardize cross-patterned styling for any code that uses both.

## Explanation
Our atomic files mean that a single concept might be composed of many small, orthogonal fragments. The `wiki-compiler audit` must be upgraded to perform intersectional rule checks across these fragments. Instead of checking a single massive file against a single standard, the compiler must evaluate how overlapping rules apply to a composed AST node or document section. 

## Reference
- `src/wiki_compiler/auditor.py`
- `wiki/concepts/wiki_construction_principles.md`
- `wiki/standards/house_rules.md` (ID-3, OP-5)

## What to fix
1. Upgrade the `wiki-compiler audit` to support "Rule Intersection" (cross-ruling).
2. The auditor should be able to query the graph for multiple intersecting properties (e.g., uses Library X AND performs Disk I/O) and apply a composite styling constraint.
3. If the AST or Markdown fails the composite check, it should flag a `cross_ruling_violation` specifying which two (or more) dimensions are clashing.

## Depends on
- `plan_docs/issues/unimplemented/replace_node_count_heuristic.md`