# Context Active Work Intersection

**Explanation:** The context issue asks for open work items, but the current command does not intersect results with active issues. Agents need the current work surface, not just graph neighbors.

**Reference:** `plan_docs/issues/Index.md`, `src/wiki_compiler/context.py`, `src/wiki_compiler/workflow_guard.py`

**What to fix:** Add active-issue intersection to context bundles using the repo's current issue surface.

**How to do it:**
1. Decide the canonical active-work source for routing.
2. Add issue matching/intersection logic.
3. Add tests for context bundles that include relevant active issues.

**Depends on:** `plan_docs/issues/unimplemented/context-router-contract.md`, `plan_docs/issues/unimplemented/context-graph-aware-routing.md`
