# Librarian Agent Query Server and Tool Runtime

**Explanation:** The "Librarian Agent" needs a way to query the knowledge graph and submit proposals through a functional runtime. Currently, the `query_server.py` and tools like `submit_topology_proposal` have no functional backend. This blocks the AI-human collaboration cycle.

**Reference:** `agents/librarian/intro.md`, `src/wiki_compiler/query_server.py`, `plan_docs/issues.md` (Librarian perspective)

**What to fix:** 
1. Build out the query server in `src/wiki_compiler/query_server.py`.
2. Implement the tools described in the Librarian Agent protocol (`query_knowledge_graph`, `submit_topology_proposal`).
3. (Stretch) Ensure the server can serve the NetworkX graph or a derived SQLite database for efficient querying.

**How to do it:** 
1. Define the API or tool interface for the Librarian agent.
2. Wire the `StructuredQuery` (from Facet System Foundation) into the query server.
3. Build the `TopologyProposal` validation logic (this is related to but distinct from `FacetProposal` — see `src/wiki_compiler/validator.py`).

**Depends on:** `plan_docs/issues/unimplemented/facet-system-foundation.md`
