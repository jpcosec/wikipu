---
identity:
  node_id: "doc:wiki/standards/contracts.md"
  node_type: "doc_standard"
edges:
  - target_id: "file:src/wiki_compiler/contracts/__init__.py"
    relation_type: documents
  - target_id: "code:src/wiki_compiler/contracts/base.py:Edge"
    relation_type: documents
  - target_id: "code:src/wiki_compiler/contracts/base.py:SystemIdentity"
    relation_type: documents
  - target_id: "code:src/wiki_compiler/contracts/facets.py:IOFacet"
    relation_type: documents
  - target_id: "code:src/wiki_compiler/contracts/facets.py:ASTFacet"
    relation_type: documents
  - target_id: "code:src/wiki_compiler/contracts/facets.py:SemanticFacet"
    relation_type: documents
  - target_id: "code:src/wiki_compiler/contracts/facets.py:ADRFacet"
    relation_type: documents
  - target_id: "code:src/wiki_compiler/contracts/facets.py:TestMapFacet"
    relation_type: documents
  - target_id: "code:src/wiki_compiler/contracts/facets.py:ComplianceFacet"
    relation_type: documents
  - target_id: "code:src/wiki_compiler/contracts/node.py:KnowledgeNode"
    relation_type: documents
  - target_id: "code:src/wiki_compiler/contracts/proposals.py:AuditFinding"
    relation_type: documents
  - target_id: "code:src/wiki_compiler/contracts/proposals.py:FacetProposal"
    relation_type: documents
  - target_id: "code:src/wiki_compiler/contracts/proposals.py:FacetOrthogonalityReport"
    relation_type: documents
  - target_id: "code:src/wiki_compiler/contracts/proposals.py:TopologyProposal"
    relation_type: documents
  - target_id: "code:src/wiki_compiler/contracts/proposals.py:CollisionReport"
    relation_type: documents
---

Canonical Pydantic models and contracts for the Knowledge Graph ecosystem. Defines the schema for nodes, edges, and facets like ADR, compliance, and I/O.

## Rule Schema

```python
class KnowledgeNode(BaseModel):
    identity: SystemIdentity
    edges: list[Edge]
    semantics: SemanticFacet | None
    ast: ASTFacet | None
    io_ports: list[IOFacet]
    compliance: ComplianceFacet | None
    adr: ADRFacet | None
    test_map: TestMapFacet | None
```

## Fields

- `KnowledgeNode.identity`: The unique ID and type.
- `KnowledgeNode.edges`: Directed relationships to other nodes.
- `KnowledgeNode.io_ports`: Input/Output dimensions.
- `KnowledgeNode.compliance`: House rules status.

## Usage Examples

```python
from wiki_compiler.contracts import KnowledgeNode, SystemIdentity

node = KnowledgeNode(
    identity=SystemIdentity(node_id="file:src/main.py", node_type="file"),
    edges=[]
)
print(node.identity.node_id)
```
