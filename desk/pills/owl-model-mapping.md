---
pill_type: model
scope: global
language: en
nature: implementation
bound_to: owl-phase1-parallel-run, owl-phase2-quadstore-primary
created: 2026-04-17
lifecycle: current
---

# Pydantic → OWL Model Mapping

## Core Classes

| Pydantic | OWL |
|----------|-----|
| `KnowledgeNode` | `owl:NamedIndividual` |
| `SystemIdentity.node_id` | `wikipu:node_id` (annotation) |
| `SystemIdentity.node_type` | `rdf:type` |
| `Edge.target_id` | Object property value |
| `Edge.relation_type` | `owl:ObjectProperty` |

## Facets → Annotations

| Facet | OWL Property |
|-------|-------------|
| `SemanticFacet.intent` | `rdfs:comment` |
| `SemanticFacet.raw_docstring` | `wikipu:raw_docstring` |
| `ComplianceFacet.status` | `wikipu:has_compliance_status` |
| `ComplianceFacet.failing_standards` | `wikipu:failing_standards` |
| `ADRFacet.decision_id` | `wikipu:decision_id` |
| `ADRFacet.status` | `wikipu:has_decision_status` |
| `GitFacet.blob_sha` | `wikipu:blob_sha` |
| `GitFacet.status` | `wikipu:has_git_status` |

## Relation Types → ObjectProperties

```python
RELATION_TYPES = {
    "contains":     "wikipu:contains",
    "depends_on":   "wikipu:dependsOn",
    "reads_from":   "wikipu:readsFrom",
    "writes_to":    "wikipu:writesTo",
    "documents":    "wikipu:documents",
    "transcludes":  "wikipu:transcludes",
    "extends":      "wikipu:extends",
    "implements":   "wikipu:implements",
}
```

## Node Types → Classes

```python
NODE_TYPES = {
    "directory":     "wikipu:Directory",
    "file":          "wikipu:File",
    "code_construct": "wikipu:CodeConstruct",
    "doc_standard":  "wikipu:DocStandard",
    "concept":       "wikipu:Concept",
    "index":         "wikipu:Index",
    "how_to":        "wikipu:HowTo",
    "adr":           "wikipu:ADR",
    "reference":     "wikipu:Reference",
    "faq":           "wikipu:FAQ",
    "selfDoc":       "wikipu:SelfDoc",
}
```

## Compliance Status → Individuals

```python
COMPLIANCE_STATUS = {
    "planned":     "wikipu:Planned",
    "scaffolding": "wikipu:Scaffolding",
    "mocked":      "wikipu:Mocked",
    "implemented":  "wikipu:Implemented",
    "tested":      "wikipu:Tested",
    "exempt":      "wikipu:Exempt",
}
```

## Reference

- `src/wiki_compiler/contracts/node.py`
- `src/wiki_compiler/contracts/base.py`
- `wiki/adrs/003_owl_integration.md` (Pydantic Schema Integration)
