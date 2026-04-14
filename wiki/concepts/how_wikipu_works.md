---
identity:
  node_id: doc:wiki/concepts/how_wikipu_works.md
  node_type: concept
edges:
- target_id: doc:wiki/standards/house_rules.md
  relation_type: contains
- target_id: doc:wiki/reference/knowledge_node_facets.md
  relation_type: contains
compliance:
  status: implemented
  failing_standards: []
---

Wikipu works by compiling code, documentation, and decisions into a shared knowledge graph that both humans and agents can navigate. The wiki is not just prose; it is structured input to a graph-shaped system that enforces architectural rules and preserves traceable context.

## Definition

Wikipu works by compiling code, documentation, and decisions into a shared knowledge graph that both humans and agents can navigate.

## Examples

- wiki nodes under `wiki/`, which declare identity, status, and explicit relationships
- scanned source code under `src/`, which yields semantic, AST, I/O, and testing facets

## Related Concepts

- [[house_rules]]
- [[knowledge_node_facets]]

The build loop combines two sources of truth:

- wiki nodes under `wiki/`, which declare identity, status, and explicit relationships
- scanned source code under `src/`, which yields semantic, AST, I/O, and testing facets

This lets the system answer structural questions such as what depends on a node, which docs describe a module, or where a proposal would collide with existing topology.
