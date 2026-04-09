# Session Log Storage

**Explanation:** Once the schema exists, the runtime still needs stable paths and helpers for reading and writing logs. Storage policy should be isolated before `history` or coordinator resume logic depends on it.

**Reference:** `src/wiki_compiler/main.py`, `src/wiki_compiler/scaffolder.py`, `plan_docs/issues/unimplemented/cross-session-memory.md`

**What to fix:** Add storage helpers and canonical path conventions for session logs under `desk/autopoiesis/`.

**How to do it:**
1. Define canonical paths and discovery helpers.
2. Add create/load/list/latest-session helpers.
3. Add tests for empty, missing, and multi-session cases.

**Depends on:** `plan_docs/issues/unimplemented/session-log-schema.md`
