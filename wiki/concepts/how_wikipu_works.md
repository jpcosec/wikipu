---
identity:
  node_id: "doc:wiki/concepts/how_wikipu_works.md"
  node_type: "concept"
edges:
  - {target_id: "doc:wiki/standards/house_rules.md", relation_type: "contains"}
  - {target_id: "doc:wiki/reference/knowledge_node_facets.md", relation_type: "contains"}
compliance:
  status: "implemented"
  failing_standards: []
---

Wikipu works by compiling code, documentation, and decisions into a shared knowledge graph that both humans and agents can navigate. The wiki is not just prose; it is structured input to a graph-shaped system that enforces architectural rules and preserves traceable context.

## Definition

At the center of Wikipu is the `KnowledgeNode`: a typed unit representing a directory, file, code construct, or wiki artifact. Nodes are connected by typed edges such as `contains`, `documents`, and `transcludes`, which gives the repository navigable meaning instead of just file placement.

The build loop combines two sources of truth:

- wiki nodes under `wiki/`, which declare identity, status, and explicit relationships
- scanned source code under `src/`, which yields semantic, AST, I/O, and testing facets

This lets the system answer structural questions such as what depends on a node, which docs describe a module, or where a proposal would collide with existing topology.

## Examples

- `wiki-compiler build` compiles wiki Markdown plus scanned Python into `knowledge_graph.json`.
- `wiki-compiler query --type get_descendants --node-id file:src/wiki_compiler/main.py` traverses the graph instead of searching manually.
- A reference page in `wiki/reference/` can `documents`-link a code file while a concept page explains why that area exists.

## Related Concepts

- `wiki/reference/knowledge_node_facets.md` defines the facet vocabulary used by the graph.
- `wiki/standards/house_rules.md` defines the rules the graph helps enforce.
- `wiki/how_to/use_the_graph.md` explains the operational workflow for graph-first navigation.
