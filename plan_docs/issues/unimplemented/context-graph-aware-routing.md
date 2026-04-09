# Context Graph-Aware Routing

**Explanation:** The current context command does basic heuristic seeding plus neighborhood expansion. It does not yet route by graph role such as direct matches, ancestors, dependents, and related how-to nodes.

**Reference:** `src/wiki_compiler/context.py`, `src/wiki_compiler/query_server.py`, `src/wiki_compiler/query_language.py`, `wiki/how_to/use_the_graph.md`

**What to fix:** Upgrade context routing from heuristic seed matching to graph-aware routing with ranking reasons.

**How to do it:**
1. Distinguish direct matches, ancestors, descendants, and related docs.
2. Return score and reason metadata.
3. Add routing tests for each relation type.

**Depends on:** `plan_docs/issues/unimplemented/context-router-contract.md`
