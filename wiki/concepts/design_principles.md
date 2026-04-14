---
identity:
  node_id: "doc:wiki/concepts/design_principles.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/graph_construction_process.md", relation_type: "documents"}
compliance:
  status: "planned"
  failing_standards: []
source:
  source_path: "raw/graph_construction_process.md"
  source_hash: "5cce04b66b0ac2624ccae799d5a8d22e00e6b9dd15ccc31cb63eb7dcb12cfaa9"
  compiled_at: "2026-04-14T16:50:28.660927"
  compiled_from: "wiki-compiler"
---

1. **Separation of concerns** — topology is built once; semantics are layered on top independently.

## Details

1. **Separation of concerns** — topology is built once; semantics are layered on top independently.
2. **Extensibility** — new facets can be added without touching the graph structure or existing passes.
3. **Auditability** — every quality finding is a graph query with a deterministic result.
4. **Code as ground truth** — facets are extracted from code, not written by hand. The graph
   reflects reality, not intention.

Generated from `raw/graph_construction_process.md`.