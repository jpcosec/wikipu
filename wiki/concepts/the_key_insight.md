---
identity:
  node_id: "doc:wiki/concepts/the_key_insight.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/graph_construction_process.md", relation_type: "documents"}
compliance:
  status: "planned"
  failing_standards: []
source:
  source_path: "raw/graph_construction_process.md"
  source_hash: "5cce04b66b0ac2624ccae799d5a8d22e00e6b9dd15ccc31cb63eb7dcb12cfaa9"
  compiled_at: "2026-04-14T16:50:28.660887"
  compiled_from: "wiki-compiler"
---

The raw graph gives you **reachability** — what can find what.

## Details

The raw graph gives you **reachability** — what can find what.
Facets give you **semantics** — what things mean.
Quality checking is asking: where do these two layers disagree?

Every gap between "this node exists" and "this node is fully understood and documented"
is a documentation debt. The system does not check docs by reading prose —
it checks them by looking for missing structure in the graph.

---

Generated from `raw/graph_construction_process.md`.