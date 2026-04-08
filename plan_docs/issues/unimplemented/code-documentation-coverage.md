# Code Documentation Coverage

**Explanation:** Source code nodes exist in the graph but are not linked to their corresponding wiki documentation nodes. Without `documents` edges, the graph cannot answer "what wiki node explains this module?" and the audit tool cannot flag undocumented code.

**Reference:** `src/wiki_compiler/builder.py`, `src/wiki_compiler/auditor.py`, `wiki/reference/`

**What to fix:** Add `documents` edges from wiki reference nodes to their corresponding code nodes during the build pass. The audit tool should then report any code node with no incoming `documents` edge.

**How to do it:**
1. In `builder.py` or `facet_injectors.py`, after scanning wiki nodes, match each `doc:wiki/reference/*.md` node to its corresponding `file:src/` node by convention (e.g. `wiki/reference/builder.md` → `file:src/wiki_compiler/builder.py`).
2. Add a `documents` edge for each match found.
3. Add an `AuditCheck` in `auditor.py` that surfaces code nodes with no incoming `documents` edge.

**Depends on:** none
