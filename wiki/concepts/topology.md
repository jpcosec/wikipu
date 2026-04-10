---
identity:
  node_id: "doc:wiki/concepts/topology.md"
  node_type: "concept"
edges: []
compliance:
  status: "implemented"
  failing_standards: []
---

Topology in Wikipu refers to the entire internal boundary, structure, and arrangement of the repository's Knowledge Graph, codebase, and informational zones.

## Definition

A Topology is the complete, typed network of connections between the system's files, modules, wiki nodes, and operational surfaces. It is bounded by the repository itself. Any element that is tracked by git and processed by `wiki-compiler` is part of the internal topology. External codebases, web APIs, or unversioned local state exist outside the topology boundary. 

Operations that mutate the internal topology (adding a module, deleting a core node) are safe if reversible, but require a formal `TopologyProposal` when initiating new architectural changes to guarantee ID-1 Orthogonality.

## Examples

- **Inside Topology:** The `src/wiki_compiler/` code, `wiki/` directory, the `knowledge_graph.json` artifact.
- **Outside Topology:** A remote REST API called by a script, an untracked local developer scratchpad.
- **Topology Change:** Adding a new scanner plugin that requires a new module file and corresponding `wiki/reference` documentation.

## Related Concepts

- `[[facet]]`
- `[[wiki_construction_principles]]`