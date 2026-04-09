# Self-Inclusion: System Processes as Graph Nodes

**Explanation:** The knowledge graph currently contains nodes for code, docs, and wiki content — but not for the system's own processes. The CLI commands, agent protocols (Socratic, trail collect, gate loop), and the hausordnung itself are not nodes in the graph they govern. This violates the operational closure requirement for autopoiesis: a system cannot maintain itself if it does not model its own components. Any query about "what does this system do?" cannot be answered from the graph.

**Reference:** `raw/autopoiesis_system.md`, `src/wiki_compiler/main.py`, `agents/librarian/intro.md`

**What to fix:**
1. Add wiki nodes for each CLI command (`build`, `ingest`, `scaffold`, `query`, `cleanse`, `curate`) in `wiki/reference/cli/`, each with a `SemanticFacet` describing its role and an `IOFacet` describing its inputs and outputs.
2. Add wiki nodes for each agent protocol (Socratic, trail collect, gate loop, autopoiesis coordinator) in `wiki/reference/protocols/` once those protocols are implemented.
3. Add edges from each CLI node to the source modules it calls (e.g. `wiki-compiler build` → `code:src/wiki_compiler/builder.py:build_wiki`).
4. Add a node for the hausordnung (`wiki/standards/00_house_rules.md`) with edges to every node it governs — establishing the identity rules as first-class graph citizens.
5. Ensure `scan_python_sources()` in `builder.py` picks up `src/wiki_compiler/main.py` so CLI entry points are auto-scanned.

**How to do it:**
- CLI nodes can be hand-authored in `wiki/reference/cli/` — one file per command, YAML frontmatter with `node_type: "doc_standard"` and explicit `io_ports`.
- The hausordnung node exists once `gaps/missing-house-rules.md` is resolved. Its edges to governed nodes should be declared in its own frontmatter.
- Protocol nodes are stubs until the protocols are implemented; create them with `compliance.status: "planned"` and promote when implemented.

**Depends on:** `gaps/duplicate-docs-cleanup.md` (hausordnung must exist before it can be a node)
