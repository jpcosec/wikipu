# Session Resume From Log

**Explanation:** The real value of cross-session memory is resuming with the latest session context. That requires loading the most recent session log before a new coordinator cycle begins.

**Reference:** `plan_docs/issues/unimplemented/cross-session-memory.md`, `plan_docs/issues/unimplemented/autopoiesis-loop-coordinator.md`, `src/wiki_compiler/perception.py`

**What to fix:** Restore coordinator context from the latest session log at startup.

**How to do it:**
1. Load the latest session log before new perception/detection work.
2. Surface unresolved gates and recurrent anomalies into the new cycle.
3. Add tests for cold start vs resumed start.

**Depends on:** `plan_docs/issues/unimplemented/session-log-schema.md`, `plan_docs/issues/unimplemented/session-log-storage.md`, `plan_docs/issues/unimplemented/trail-collect-session-log.md`, `plan_docs/issues/unimplemented/run-skeleton.md`
