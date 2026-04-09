# Coordinator Gate Resume Flow

**Explanation:** The coordinator must stop cleanly when an action crosses the topology boundary, write gates, and resume only after explicit resolution. Without that pause/resume loop, `run` cannot safely handle cleansing apply or other gated actions.

**Reference:** `wiki/standards/artifacts/gate.md`, `src/wiki_compiler/main.py`, `wiki/reference/protocols/gate_loop.md`

**What to fix:** Add gate writing, pause messaging, rerun inspection, and resume/apply flow to the coordinator.

**How to do it:**
1. Write open gates when approval is required.
2. Detect resolved gates on rerun.
3. Continue only for approved items and stop on pending or rejected ones.

**Depends on:** `plan_docs/issues/unimplemented/gate-table-runtime.md`, `plan_docs/issues/unimplemented/run-skeleton.md`, `plan_docs/issues/unimplemented/cleansing-apply-and-advanced-detectors.md`
