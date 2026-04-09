# Coordinator Identity Preflight

**Explanation:** The coordinator should not execute actions blindly. It needs a reusable preflight that checks identity rules, topology boundaries, and minimal-energy routing before deciding whether work stays automatic, becomes gated, or turns into a question.

**Reference:** `wiki/standards/00_house_rules.md`, `src/wiki_compiler/query_executor.py`, `src/wiki_compiler/validator.py`, `wiki/reference/protocols/socratic.md`

**What to fix:** Add a coordinator preflight layer for identity-rule checks and minimal-energy action selection.

**How to do it:**
1. Evaluate relevant ID and OP rules before action execution.
2. Route violating actions to gates or Socratic follow-up instead of executing them.
3. Add focused tests for rule-triggered downgrades.

**Depends on:** `plan_docs/issues/unimplemented/run-skeleton.md`
