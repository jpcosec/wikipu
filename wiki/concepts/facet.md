---
identity:
  node_id: "doc:wiki/concepts/facet.md"
  node_type: "concept"
edges: []
compliance:
  status: "implemented"
  failing_standards: []
---

A Facet is a strongly typed data dimension attached to a `KnowledgeNode` within the Knowledge Graph. Facets carry the structured attributes that give meaning to a node beyond its basic identity and edges.

## Definition

Instead of defining an enormous, monolithic schema for every node, Wikipu uses a facet-based architecture. A node's schema is a composition of optional facets (Pydantic models) such as `SemanticFacet` (intent, docstrings), `ASTFacet` (code structure, signatures), `IOFacet` (file reads/writes), and `ComplianceFacet` (status, failing standards). 

This orthogonal design ensures that new analytical dimensions can be added to the graph without breaking existing node parsing or querying logic.

## Examples

- **ASTFacet:** Records that a Python function has the signature `def build_wiki(source_dir: Path) -> BuildResult`.
- **ComplianceFacet:** Marks a node as having `status: "implemented"` but missing its `Abstract`.
- **IOFacet:** Notes that a specific module uses `Path.read_text()` to read `knowledge_graph.json`.

## Related Concepts

- `[[topology]]`