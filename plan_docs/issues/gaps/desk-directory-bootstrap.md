# Desk Directory Bootstrap

**Explanation:** Several Phase 3 issues write to paths under `desk/` (`desk/Gates.md`, `desk/autopoiesis/`, `desk/autopoiesis/cycles/`), but the `desk/` directory does not exist in the repository. The house rules define it as the active operational zone (OP-1), distinct from `plan_docs/` which holds issue files. Without the directory and a minimal seed structure, `gate-table-runtime`, `session-log-storage`, and `cycle-record-persistence` will all write to a missing path.

**Reference:** `wiki/standards/00_house_rules.md` (OP-1, OP-2, ID-4), `plan_docs/issues/unimplemented/gate-table-runtime.md`, `plan_docs/issues/unimplemented/session-log-storage.md`, `plan_docs/issues/unimplemented/cycle-record-persistence.md`

**What to fix:** Create the `desk/` directory with the minimal structure required by the house rules before any runtime code writes to it.

**How to do it:**
1. Create `desk/Gates.md` with an empty gate table header matching `wiki/standards/artifacts/gate.md`.
2. Create `desk/autopoiesis/` with a placeholder or `Board.md` stub.
3. Verify `wiki-compiler build` and `wiki-compiler audit` still pass after adding the new paths.

**Depends on:** `none`
