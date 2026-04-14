---
identity:
  node_id: "doc:wiki/standards/seed_rule.md"
  node_type: "doc_standard"
edges:
  - {target_id: "raw:raw/methodology_synthesis_graph_routing.md", relation_type: "documents"}
compliance:
  status: "planned"
  failing_standards: []
source:
  source_path: "raw/methodology_synthesis_graph_routing.md"
  source_hash: "f3dc9e1e39adb5e4a5de79310c1d485370d2a57b60fefe5d804c156f6e25fe2e"
  compiled_at: "2026-04-14T16:50:28.664288"
  compiled_from: "wiki-compiler"
---

**Abstract:** The knowledge graph is the routing system. Agents navigate by traversal and facet query, not by coordinate lookup.

> The knowledge graph is the routing system. Agents navigate by traversal and facet query, not by coordinate lookup. Temporal state is a facet, not an axis.

## Details

> The knowledge graph is the routing system. Agents navigate by traversal and facet query, not by coordinate lookup. Temporal state is a facet, not an axis.

Generated from `raw/methodology_synthesis_graph_routing.md`.

## Rule Schema

- Graph is the routing system
- Navigation via traversal and facet query
- Temporal state is a facet, not an axis

## Fields

- `node_id`: Unique graph identifier
- `edges`: Relationships between nodes
- `temporal`: Time-based facet

## Usage Examples

- Query by traversal: `wiki-compiler query --type get_node`
- Query by facet: `wiki-compiler query --type get_facet`