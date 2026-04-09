# Context Prose Bundles

**Explanation:** Current context output is mostly schema and abstract data. A real context router should hydrate bundles with the actual prose snippets that an LLM or human needs to act.

**Reference:** `src/wiki_compiler/context.py`, `wiki/reference/context.md`, `wiki/how_to/use_the_cli.md`

**What to fix:** Render LLM-ready context bundles with relevant wiki prose, ranked explanations, and structured JSON.

**How to do it:**
1. Load prose snippets for selected doc nodes.
2. Improve markdown and JSON rendering for direct consumption.
3. Add snapshot-style tests for representative bundles.

**Depends on:** `plan_docs/issues/unimplemented/context-router-contract.md`, `plan_docs/issues/unimplemented/context-graph-aware-routing.md`, `plan_docs/issues/unimplemented/context-checklists-and-rules.md`, `plan_docs/issues/unimplemented/context-active-work-intersection.md`
