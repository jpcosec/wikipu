# Raw to Wiki Ingestion Pipeline (Karpathy Gap)

**Explanation:** The "Karpathy vision" (Raw -> Compile -> Query) is currently missing its automated "Compile" (from raw notes into wiki nodes) step. `wiki-compiler ingest` is a stub that doesn't effectively refine "ore" from `raw/` into structured, atomized wiki nodes.

**Reference:** `plan_docs/issues.md` (Karpathy Perspective Gap 2), `plan_docs/2026-04-08-three-phase-graph.md` (Task 5-6)

**What to fix:** 
1. Implement "Wiki Construction Discipline" (Task 5): templates, abstracts, and the `compose` command.
2. Upgrade `ingest` to propose atomic node decompositions from raw text rather than just generating stubs.
3. Integrate an LLM-backed extraction mechanism if possible for refinement of notes in `raw/` into `wiki/`.

**How to do it:** 
Follow the steps in Task 5 of `plan_docs/2026-04-08-three-phase-graph.md`.
1. Build `node_templates.py`.
2. Upgrade `src/wiki_compiler/ingest.py`.
3. Add `compose` subcommand to `main.py`.

**Depends on:** `plan_docs/issues/unimplemented/facet-system-foundation.md`
