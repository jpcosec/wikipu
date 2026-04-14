---
identity:
  node_id: doc:wiki/concepts/routing_matrix_vs_graph.md
  node_type: concept
edges:
- target_id: raw:raw/methodology_synthesis_graph_routing.md
  relation_type: documents
compliance:
  status: implemented
  failing_standards: []
source:
  source_path: raw/methodology_synthesis_graph_routing.md
  source_hash: f3dc9e1e39adb5e4a5de79310c1d485370d2a57b60fefe5d804c156f6e25fe2e
  compiled_at: '2026-04-14T16:50:28.664147'
  compiled_from: wiki-compiler
---

The context router (doc_methodology) uses a 4D matrix (domain × stage × layer × temporal state). This works for pipeline projects where the structure is genuinely regular — a linear sequence of stages across orthogonal domains. Coordinates are a natural fit when every document has a clean home in the grid.

## Definition

The context router (doc_methodology) uses a 4D matrix (domain × stage × layer × temporal state).

## Examples

- A standard applies across multiple domains and stages
- A concept is relevant to several unrelated modules
- Cross-cutting concerns (logging, error contracts, observability) have no natural domain×stage cell
- Decisions have arbitrary dependencies, not grid coordinates

## Related Concepts

- [[Index]]
- [[core_philosophy]]

## Details

The context router (doc_methodology) uses a 4D matrix (domain × stage × layer × temporal state). This works for pipeline projects where the structure is genuinely regular — a linear sequence of stages across orthogonal domains. Coordinates are a natural fit when every document has a clean home in the grid.

Reality is not always a matrix. It is closer to a graph:
- A standard applies across multiple domains and stages
- A concept is relevant to several unrelated modules
- Cross-cutting concerns (logging, error contracts, observability) have no natural domain×stage cell
- Decisions have arbitrary dependencies, not grid coordinates

Forcing graph-shaped knowledge into a matrix produces gaps (cross-cutting items with no home) and distortions (items assigned to the nearest cell rather than their true location).

Generated from `raw/methodology_synthesis_graph_routing.md`.
