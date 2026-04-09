# Run Skeleton

**Explanation:** There is no `wiki-compiler run` command yet, so the autopoietic loop has no executable coordinator surface. The first slice should orchestrate only safe, non-gated steps instead of bundling the full pause/resume and trail logic.

**Reference:** `src/wiki_compiler/main.py`, `src/wiki_compiler/perception.py`, `src/wiki_compiler/builder.py`, `src/wiki_compiler/ingest.py`

**What to fix:** Add a `wiki-compiler run` skeleton that performs status, classifies safe actions, runs non-structural steps, and rebuilds the graph.

**How to do it:**
1. Add the CLI command and coordinator entrypoint.
2. Execute only non-gated actions in the first version.
3. Add tests for a no-op cycle and a safe auto-response cycle.

**Depends on:** `plan_docs/issues/unimplemented/perception-gates-and-classification.md`
