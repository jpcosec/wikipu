---
identity:
  node_id: "doc:wiki/concepts/what_to_preserve_from_the_matrix_model.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/methodology_synthesis_graph_routing.md", relation_type: "documents"}
compliance:
  status: "planned"
  failing_standards: []
source:
  source_path: "raw/methodology_synthesis_graph_routing.md"
  source_hash: "f3dc9e1e39adb5e4a5de79310c1d485370d2a57b60fefe5d804c156f6e25fe2e"
  compiled_at: "2026-04-14T16:50:28.664247"
  compiled_from: "wiki-compiler"
---

The matrix's real contribution is not the coordinate system — it is the **separation of temporal state**. `runtime` vs. `plan` as a navigation axis is valuable regardless of graph or matrix. A node in the graph should carry a temporal facet: is this current truth, a plan, a deferred item, or historical?

## Details

The matrix's real contribution is not the coordinate system — it is the **separation of temporal state**. `runtime` vs. `plan` as a navigation axis is valuable regardless of graph or matrix. A node in the graph should carry a temporal facet: is this current truth, a plan, a deferred item, or historical?

Translated to the graph model:
- Current truth nodes → `ComplianceFacet.status = "implemented"` + no `plan/` prefix in node_id
- Plan nodes → `doc:plan_docs/...`
- Deferred nodes → `doc:future_docs/...`
- Historical nodes → ADR nodes with `adr.status = "superseded"`

The Librarian agent can then scope queries by temporal state as a facet filter, not a coordinate axis. Same separation, graph-native representation.

Generated from `raw/methodology_synthesis_graph_routing.md`.