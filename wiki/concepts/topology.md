---
identity:
  node_id: doc:wiki/concepts/topology.md
  node_type: concept
edges: []
compliance:
  status: implemented
  failing_standards: []
---

Topology in Wikipu refers to the entire internal boundary, structure, and arrangement of the repository's Knowledge Graph, codebase, and informational zones.

## Definition

Topology in Wikipu refers to the entire internal boundary, structure, and arrangement of the repository's Knowledge Graph, codebase, and informational zones.

## Examples

- Implementation of this concept within the Wikipu workflow.
- Application of these principles in current documentation.

## Related Concepts

- [[facet]]
- [[wiki_construction_principles]]

Operations that mutate the internal topology (adding a module, deleting a core node) are safe if reversible, but require a formal `TopologyProposal` when initiating new architectural changes to guarantee ID-1 Orthogonality.
