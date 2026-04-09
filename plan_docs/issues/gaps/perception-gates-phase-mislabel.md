# Perception Gates Phase Mislabel

**Explanation:** `perception-gates-and-classification` is listed under "Phase 4 — Autopoietic loop" in `plan_docs/issues/Index.md`, but the dependency map in that same file records `Phase 4[21] → Phase 3[16]`, meaning `run-skeleton` (Phase 3) depends on it. The parallelization map also correctly places it in Phase 3 (`Phase 3 [10][12][15] then [13][21]...`). The section heading is wrong and could cause an agent to defer a Phase 3 prerequisite.

**Reference:** `plan_docs/issues/Index.md`, `plan_docs/issues/unimplemented/perception-gates-and-classification.md`, `plan_docs/issues/unimplemented/run-skeleton.md`

**What to fix:** Move the `perception-gates-and-classification` entry from the "Phase 4" section into the "Phase 3 — Runtime and protocol" section of `Index.md`, keeping its dependency relationships and numbering consistent.

**How to do it:**
1. In `Index.md`, remove item #21 from the Phase 4 block.
2. Insert it into the Phase 3 block before `run-skeleton` (#16), since #16 depends on it.
3. Verify the dependency summary and parallelization map still read correctly after the move.

**Depends on:** `none`
