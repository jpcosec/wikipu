# History Command

**Explanation:** Session logs will not help agents unless there is a read surface for them. A read-only `history` command is independently useful and does not require the full coordinator runtime.

**Reference:** `src/wiki_compiler/main.py`, `plan_docs/issues/unimplemented/session-log-schema.md`, `plan_docs/issues/unimplemented/session-log-storage.md`, `wiki/reference/cli/status.md`

**What to fix:** Add `wiki-compiler history` as a read-only session-log aggregator.

**How to do it:**
1. Add the CLI command and aggregation logic.
2. Summarize open gates, recurring perturbations, and routed artifacts.
3. Add tests and a CLI reference doc.

**Depends on:** `plan_docs/issues/unimplemented/session-log-schema.md`, `plan_docs/issues/unimplemented/session-log-storage.md`
