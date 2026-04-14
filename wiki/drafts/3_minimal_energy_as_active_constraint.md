---
identity:
  node_id: "doc:wiki/drafts/3_minimal_energy_as_active_constraint.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/unimplemented_from_sourcetalk.md", relation_type: "documents"}
compliance:
  status: "planned"
  failing_standards: []
source:
  source_path: "raw/unimplemented_from_sourcetalk.md"
  source_hash: "1a7f8c9ba485c0342c7bddb0d133479345f1edd3e7047103e0544db195914f61"
  compiled_at: "2026-04-14T16:50:28.666258"
  compiled_from: "wiki-compiler"
---

**Idea:** Before any TopologyProposal is generated, first query the graph to see if a simpler structure already exists that satisfies the requirement. If a match exists, extend it rather than creating new elements.

## Details

**Idea:** Before any TopologyProposal is generated, first query the graph to see if a simpler structure already exists that satisfies the requirement. If a match exists, extend it rather than creating new elements.

**Current state:** Not implemented as an automated check. The orthogonality validator checks for I/O collisions but doesn't query for existing nodes with overlapping intent.

**Reference (autopoiesis_system.md line ~196):**
> "Minimal energy is not just a design principle — it must be an active check in the coordinator. Before any proposal is generated, the coordinator asks: is there a simpler structure that satisfies this requirement? This is a graph query (find nodes with overlapping intent or IO), not a heuristic."

---

Generated from `raw/unimplemented_from_sourcetalk.md`.