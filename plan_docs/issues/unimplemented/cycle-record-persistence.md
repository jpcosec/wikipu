# Cycle Record Persistence

**Explanation:** The coordinator needs a durable record of each run even before the full cross-session memory system lands. A narrow cycle record lets later history and session logic build on an existing runtime output instead of inventing it later.

**Reference:** `plan_docs/issues/unimplemented/run-skeleton.md`, `wiki/reference/protocols/autopoiesis_coordinator.md`

**What to fix:** Add a minimal `CycleRecord` model and write one JSON file per coordinator run under `desk/autopoiesis/cycles/`.

**How to do it:**
1. Define a narrow cycle record schema.
2. Write one record per `run` invocation.
3. Add tests for path creation and persisted fields.

**Depends on:** `plan_docs/issues/unimplemented/run-skeleton.md`
