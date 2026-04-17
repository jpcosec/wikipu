---
pill_type: decision
scope: domain
language: en
nature: context
bound_to: owl-phase2-quadstore-primary, owl-phase3-reasoning
created: 2026-04-17
lifecycle: current
---

# Phase 2-3 Design Decisions

## SyncGate Architecture

```python
class SyncGate:
    def __init__(self, onto):
        self.onto = onto
        self.shacl_validator = SHACLValidator()
    
    def export_to_owl(self, node: KnowledgeNode) -> bool:
        """Pydantic → OWL. Returns False if rejected."""
        # 1. Validate with Pydantic
        if not node.model_validate(node):
            return False
        
        # 2. Convert to RDF
        individual = self._pydantic_to_owl(node)
        
        # 3. SHACL gate
        if not self.shacl_validator.validate(individual):
            return False
        
        # 4. Add to quadstore
        self.onto.add(individual)
        return True
    
    def import_from_owl(self, uri: str) -> KnowledgeNode | None:
        """OWL → Pydantic. Returns None if rejected."""
        individual = self.onto[uri]
        raw = self._owl_to_pydantic(individual)
        try:
            return KnowledgeNode.model_validate(raw)
        except ValidationError:
            return None
    
    def sync(self) -> SyncReport:
        """Full bidirectional sync with conflict detection."""
        # Compare Pydantic nodes with OWL individuals
        # Report conflicts for human review
        pass
```

## Conflict Resolution Strategy

| Situation | Resolution |
|-----------|-----------|
| Pydantic valid, OWL invalid | Reject OWL, keep Pydantic |
| Pydantic invalid, OWL valid | Reject Pydantic, regenerate |
| Both valid, different | Flag for ADR gate |

## SPARQL Query Patterns

### Find Node by ID
```sparql
SELECT ?s WHERE {
    ?s wikipu:node_id "doc:wiki/concepts/energy.md"
}
```

### Find References
```sparql
SELECT ?target WHERE {
    ?source wikipu:references ?target .
    FILTER(CONTAINS(STR(?source), "energy"))
}
```

### Find by Edge Type
```sparql
SELECT ?target WHERE {
    ?source wikipu:implements ?target .
}
```

### Find Inferred Relationships (Phase 3)
```sparql
SELECT ?class WHERE {
    ?individual a ?class .
    ?class a owl:Class
}
```

## Reasoner Integration (Phase 3)

```python
def run_reasoner():
    """Run HermiT, store inferences separately."""
    inferences = get_ontology("http://wikipu.org/inferences/")
    with inferences:
        sync_reasoner()
    return inferences
```

## Reference

- `wiki/adrs/003_owl_integration.md` (Gatekeeping section)
- `owlready2.readthedocs.io/en/v0.50/reasoning.html`
