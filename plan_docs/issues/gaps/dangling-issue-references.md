# Dangling Issue References

**Explanation:** Seven issue files reference two issue files that no longer exist — they were decomposed into the current 22-issue set (commit `d615977`) but the `Reference:` fields were not updated. Agents reading these issues will hit dead links.

Missing files referenced:
- `plan_docs/issues/unimplemented/cross-session-memory.md` — referenced by `history-command.md`, `session-log-schema.md`, `session-log-storage.md`, `session-resume-from-log.md`, `trail-collect-session-log.md`
- `plan_docs/issues/unimplemented/autopoiesis-loop-coordinator.md` — referenced by `cycle-record-persistence.md`, `session-resume-from-log.md`

**Reference:** `plan_docs/issues/unimplemented/history-command.md`, `plan_docs/issues/unimplemented/session-log-schema.md`, `plan_docs/issues/unimplemented/session-log-storage.md`, `plan_docs/issues/unimplemented/session-resume-from-log.md`, `plan_docs/issues/unimplemented/trail-collect-session-log.md`, `plan_docs/issues/unimplemented/cycle-record-persistence.md`

**What to fix:** Replace each dangling reference with the actual replacement issues from the current index.

**How to do it:**
1. In the five files referencing `cross-session-memory.md`: replace with the relevant subset of `session-log-schema.md`, `session-log-storage.md`, `trail-collect-session-log.md` depending on what each issue actually needs.
2. In the two files referencing `autopoiesis-loop-coordinator.md`: replace with `run-skeleton.md` and/or `coordinator-gate-resume-flow.md` as appropriate.
3. No tests needed — this is a docs-only fix.

**Depends on:** `none`
