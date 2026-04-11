---
identity:
  node_id: "doc:wiki/drafts/the_implication_for_wikipu.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/methodology_synthesis_graph_routing.md", relation_type: "documents"}
compliance:
  status: "planned"
  failing_standards: []
source:
  source_path: "raw/methodology_synthesis_graph_routing.md"
  source_hash: "f3dc9e1e39adb5e4a5de79310c1d485370d2a57b60fefe5d804c156f6e25fe2e"
  compiled_at: "2026-04-10T17:47:33.733589"
  compiled_from: "wiki-compiler"
---

The Librarian agent should not navigate by coordinates. It should navigate by graph traversal and facet queries. The infrastructure already exists:

## Details

The Librarian agent should not navigate by coordinates. It should navigate by graph traversal and facet queries. The infrastructure already exists:

- `get_node` — retrieve a node by ID
- `get_ancestors` / `get_descendants` — traverse relationships
- `StructuredQuery` + `FacetFilter` — find nodes by facet properties
- `GraphScope` — scope a query to a subgraph

The routing matrix is a special case of a graph — a regular, structured subgraph where every node has orthogonal coordinates. For a general knowledge system, the graph is the routing matrix. The "coordinates" are node IDs and edge types, not domain×stage tuples.

Generated from `raw/methodology_synthesis_graph_routing.md`.