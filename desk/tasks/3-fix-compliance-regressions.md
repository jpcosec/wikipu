# Fix Compliance Regressions

**Explanation:** The wiki-compiler audit reports 107 undocumented code nodes, 21 missing docstrings, and 122 compliance violations (mostly in drafts).
**Reference:** `wiki-compiler audit` output.
**What to fix:** Address the documentation gaps by adding docstrings and linking code to wiki nodes.
**How to do it:** Systematically add missing docstrings to `src/wiki_compiler/` and ensure each symbol is documented in a corresponding wiki node with a `documents` edge.
**Depends on:** plan_docs/issues/gaps/2-resolve-cleansing-gate.md
