# How-To Wiki Section

**Explanation:** The system has no canonical how-to documentation for its own core operations. Two flat files exist (`wiki/how_to_use.md`, `wiki/how_to_add_component.md`) but they are not structured as a proper wiki section and do not cover the full set of operations agents and humans need to perform. Without these, every new session must rediscover workflows from first principles.

**Reference:** `wiki/standards/00_house_rules.md` (WK-4 defines the `how_to` node template), `wiki/how_to_use.md`, `wiki/how_to_add_component.md`

**What to fix:** Create `wiki/how_to/` as a structured section with an `Index.md` and one node per operation. Migrate and rewrite the two existing flat files into the new structure.

**Nodes to create:**
1. `how_to/plan.md` — how to scope and structure a plan before touching code or wiki
2. `how_to/design.md` — how to design a new module or topology change (TopologyProposal flow)
3. `how_to/document.md` — how to write and maintain wiki nodes (WK rules applied)
4. `how_to/research.md` — how to ingest external sources into raw/ and process them
5. `how_to/use_the_graph.md` — how to query, traverse, and interpret the knowledge graph
6. `how_to/use_the_cli.md` — how to use wiki-compiler commands (migrate from how_to_use.md)
7. `how_to/use_socratic_methodology.md` — what Socratic method means here and why the system uses it
8. `how_to/use_autopoiesis.md` — how the autopoietic cycle works and when to trigger it

**Each node must follow the `how_to` template:** Abstract → Prerequisites → Steps → Verification

**Depends on:** none (pure documentation work)
