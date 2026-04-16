---
identity:
  node_id: doc:wiki/concepts/topology.md
  node_type: concept
edges:
  - {target_id: "doc:wiki/concepts/pirate.md", relation_type: "contains"}
compliance:
  status: implemented
  failing_standards: []
---

Topology in Wikipu refers to the entire internal boundary, structure, and arrangement of the repository's Knowledge Graph, codebase, and informational zones.

## Definition

Topology in Wikipu refers to the entire internal boundary, structure, and arrangement of the repository's Knowledge Graph, codebase, and informational zones.

## Zones

| Zone | Purpose |
|------|---------|
| `wiki/` | Knowledge graph and documentation |
| `src/` | Source code |
| `src/looting/` | Looted/stolen external projects for experimentation (see [[looting_protocol]]) |
| `src/looting/gems/` | Local LLM CLI tool via Ollama - prompt templates and JSON processing |
| `src/looting/pirate/` | Fork of pi coding agent - used for autopoietic self-experimentation |
| `src/looting/pirate/` | Fork of pi coding agent - used for autopoietic self-experimentation |

## Examples

- Implementation of this concept within the Wikipu workflow.
- Application of these principles in current documentation.

## Related Concepts

- [[facet]]
- [[wiki_construction_principles]]
- [[pirate]]

Operations that mutate the internal topology (adding a module, deleting a core node) are safe if reversible, but require a formal `TopologyProposal` when initiating new architectural changes to guarantee ID-1 Orthogonality.
