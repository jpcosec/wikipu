# Trail Collect Session Log Writing

**Explanation:** Cross-session memory needs a write path from trail collect into durable session logs. Without that bridge, session models and storage exist but no runtime populates them.

**Reference:** `raw/trail_collect.md`, `wiki/reference/protocols/trail_collect.md`, `plan_docs/issues/unimplemented/cross-session-memory.md`

**What to fix:** Implement trail-collect-to-session-log writing as a library/runtime surface.

**How to do it:**
1. Convert closeout artifacts into a `SessionLog`.
2. Write append-only logs at session close.
3. Add tests for artifact typing and append behavior.

**Depends on:** `plan_docs/issues/unimplemented/session-log-schema.md`, `plan_docs/issues/unimplemented/session-log-storage.md`, `plan_docs/issues/unimplemented/trail-collect-closeout.md`
