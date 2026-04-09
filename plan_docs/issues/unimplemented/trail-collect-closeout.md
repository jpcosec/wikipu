# Trail Collect Closeout

**Explanation:** The coordinator still needs a closeout step that classifies outcomes into durable artifacts such as decisions, gaps, and rule patches. Without trail collect, the cycle can run but cannot explain what it learned.

**Reference:** `raw/trail_collect.md`, `wiki/reference/protocols/trail_collect.md`, `wiki/standards/00_house_rules.md`

**What to fix:** Add a trail-collect closeout step that classifies resolved gates and produced artifacts into structured outputs.

**How to do it:**
1. Classify cycle outcomes into trail artifact categories.
2. Return or persist structured trail output.
3. Add tests for the routing and classification decisions.

**Depends on:** `plan_docs/issues/unimplemented/coordinator-gate-resume-flow.md`, `plan_docs/issues/unimplemented/cycle-record-persistence.md`
