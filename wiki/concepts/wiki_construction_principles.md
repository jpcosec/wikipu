---
identity:
  node_id: "doc:wiki/concepts/wiki_construction_principles.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/wiki_construction_principles.md", relation_type: "documents"}
  - {target_id: "doc:wiki/standards/00_house_rules.md", relation_type: "depends_on"}
compliance:
  status: "implemented"
  failing_standards: []
---

A set of core disciplines that ensure the Knowledge Graph remains unit-tested, atomic, and composable. These principles apply the rigor of clean code to human-AI documentation.

## Definition
The same discipline that makes code clean applies to documentation. A wiki node is a unit of knowledge with one responsibility, a clear interface, and composition properties.

## Examples
- **Mandatory Abstract:** Every node starts with a 1-3 sentence paragraph that defines the node's intent.
- **Transclusion:** Instead of duplicating content, use `![[node_name]]` to embed concepts.
- **Node Templates:** Using specific sections for `concept`, `how_to`, `standard`, etc.

## Related Concepts
- **Law of Atomicity:** Ensuring nodes answer exactly one question.
- **Deterministic Navigation:** Using MOCs instead of blind searches.
