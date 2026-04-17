---
identity:
  node_id: "doc:wiki/adrs/003_owl_integration.md"
  node_type: "adr"
adr:
  decision_id: "003"
  status: "proposed"
  context_summary: "Knowledge is currently declared manually via YAML frontmatter with no inference engine. Owlready2 provides an OWL 2.0 quadstore with automatic reasoning, replacing manual relationship auditing with HermiT/Pellet inference."
edges:
  - {target_id: "doc:wiki/adrs/Index.md", relation_type: "documents"}
  - {target_id: "doc:wiki/concepts/knowledge.md", relation_type: "supersedes"}
  - {target_id: "doc:wiki/selfDocs/WhatAmI.md", relation_type: "implements"}
  - {target_id: "doc:wiki/standards/house_rules.md", relation_type: "constrains"}
compliance:
  status: "proposed"
  failing_standards: []
---

# ADR 003: Integrate OWL 2.0 via Owlready2

## Context

Knowledge in wikipu is currently declared via YAML frontmatter with typed edges:

```yaml
edges:
  - {target_id: "doc:wiki/something.md", relation_type: "contains"}
```

This approach has two fundamental limitations:

1. **No inference** — Relationships must be manually declared. The system cannot deduce that `A contains B` and `B contains C` implies `A transitively contains C`.

2. **No reasoning** — The wiki-compiler scanner/auditor can detect drift, but cannot automatically reclassify nodes based on their properties.

OWL (Web Ontology Language) 2.0 is the W3C standard for knowledge representation. Owlready2 is a Python library that:
- Stores knowledge in an optimized SQLite3 quadstore
- Exposes ontologies as Python objects (transparent access)
- Includes HermiT/Pellet reasoners for automatic classification
- Supports SPARQL queries for complex graph traversal

Given our topology definition — "knowledge is typed relationships between concepts" — OWL is a formalization of exactly that pattern.

## Decision

Integrate Owlready2 as the knowledge graph engine, replacing YAML frontmatter edges with OWL axioms.

### Mapping

| Current Wikipu | OWL Equivalent |
|----------------|----------------|
| Markdown + YAML frontmatter | OWL files (RDF/XML or NTriples) |
| `edges[].target_id` + `relation_type` | RDF triples (Subject, Predicate, Object) |
| Scanner/Auditor for drift | `sync_reasoner()` for consistency + inference |
| Manual hierarchical auditing | Automatic class reparenting via reasoner |
| wiki-compiler `.search()` | SPARQL or owlready2 `.search()` |

### Core Mechanism

```python
from owlready2 import *

# Quadstore replaces wiki/ directory
default_world.set_backend(filename="wikipu.sqlite3")

# Ontology IRI replaces node_id namespace
onto = default_world.get_ontology("http://wikipu/")

# Typed edges become OWL ObjectProperties
with onto:
    class contains(ObjectProperty):
        domain   = [Thing]
        range    = [Thing]
    
    class implements(ObjectProperty):
        domain   = [Thing]
        range    = [Thing]

# Knowledge nodes become OWL Classes
class Knowledge(Thing):
    namespace = onto

# Concrete nodes become Individuals
wiki_node = Knowledge("knowledge_node_1")
wiki_node.contains = [other_node]
```

### Integration Phases

**Phase 1 — Parallel Run**
- Add `owlready2` to dependencies
- Export current wiki graph to OWL (RDF/XML)
- Quadstore lives alongside Markdown files
- `wiki-compiler` gains `--owl` flag for OWL-backed queries
- Define SHACL shapes for `KnowledgeNode` schema
- Implement `markdown_to_owl()` content extraction pipeline

**Phase 2 — Quadstore Primary**
- Parse Markdown files into quadstore on load
- YAML frontmatter edges become OWL triples
- Wiki-link content becomes `:references` properties
- Deprecate `.search()` in favor of SPARQL
- Implement `SyncGate` class for bidirectional sync

**Phase 3 — Reasoning Integration**
- Add `sync_reasoner()` to energy/audit cycle
- Replace manual drift detection with consistency checking
- Inferred relationships stored in separate inference ontology
- Activate SHACL validation as gatekeeper
- Tables extracted as enumerated classes where applicable

**Phase 4 — Full Migration**
- Markdown files become human-readable OWL export
- YAML frontmatter edges removed
- Narrative prose stays in Markdown; structured content in OWL
- Owlready2 is the single source of truth
- Pydantic models become read-only views of OWL state

## Pydantic Schema Integration

Our current `KnowledgeNode` Pydantic models define validation schemas. These map directly to OWL constructs:

| Pydantic Model | OWL Equivalent |
|----------------|----------------|
| `KnowledgeNode` | `owl:NamedIndividual` |
| `node_type` | `rdf:type` (class) |
| `edges[].relation_type` | `owl:ObjectProperty` |
| `semantics.intent` | `rdfs:comment` annotation |
| `compliance.status` | Data property or class membership |
| `git.blob_sha` | Annotation property |
| `adr.status` | Data property + inference |

### Facet → Annotation Mapping

```python
# SemanticFacet → rdfs:comment
:wiki_concepts_knowledge rdfs:comment "Typed relationships between concepts"@en .

# ComplianceFacet → Custom annotation property
:wiki_concepts_knowledge :compliance_status :Implemented ;
                          :failing_standards [] .

# ADRFacet → Structured annotations
:ADR_003 :decision_id "003" ;
          :decision_status :Proposed ;
          :context_summary "Knowledge declared via YAML lacks inference..." .
```

### Constraint Validation

```python
# Pydantic Literal enums become OWL enumerated classes
:ADRStatus  a        owl:Class ;
            owl:oneOf  ( :Proposed :Accepted :Deprecated :Superseded ) .
```

## Gatekeeping: Bidirectional Sync

Since Pydantic schemas define our write-side validation and OWL defines our reasoning-side truth, we need a gatekeeper to synchronize both.

### Architecture

```
┌─────────────────┐     Gatekeeper      ┌─────────────────┐
│   Pydantic      │◄──────────────────►│      OWL         │
│   (Write-side)  │    SHACL + Rules    │   (Read-side)   │
│                 │                     │                 │
│  • Validation   │   Pydantic → OWL    │  • Reasoning    │
│  • API schemas  │   Pydantic ← OWL    │  • Inference    │
│  • Type safety  │   Conflict detect   │  • SPARQL       │
└─────────────────┘                     └─────────────────┘
```

### SHACL Shapes (OWL-Native Gatekeeping)

SHACL validates RDF data against structural shapes before acceptance:

```turtle
@prefix sh:   <http://www.w3.org/ns/shacl#> .
@prefix owl:  <http://www.w3.org/2002/07/owl#> .
@prefix rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
@prefix wikipu: <http://wikipu.org/ontology/> .

:KnowledgeNodeShape
    a sh:NodeShape ;
    sh:targetClass owl:NamedIndividual ;
    
    sh:property [
        sh:path wikipu:node_id ;
        sh:minCount 1 ;
        sh:maxCount 1 ;
        sh:datatype xsd:string ;
    ] ;
    
    sh:property [
        sh:path rdf:type ;
        sh:in (
            wikipu:Directory wikipu:File wikipu:CodeConstruct 
            wikipu:Concept wikipu:ADR wikipu:Index 
            wikipu:HowTo wikipu:Reference wikipu:FAQ wikipu:SelfDoc
        ) ;
    ] ;
    
    sh:property [
        sh:path wikipu:has_compliance_status ;
        sh:in ( wikipu:Planned wikipu:Scaffolding wikipu:Mocked 
                wikipu:Implemented wikipu:Tested wikipu:Exempt ) ;
    ] ;
    
    sh:property [
        sh:path wikipu:compiled_at ;
        sh:datatype xsd:dateTime ;
    ] ;
.
```

### Pydantic Gate (Python-Side)

When syncing from OWL back to the system:

```python
from pydantic import BaseModel, ValidationError

def owl_to_pydantic(individual) -> KnowledgeNode | None:
    """OWL → Pydantic. Returns None if validation fails (rejected)."""
    raw = {
        "identity": {
            "node_id": str(individual.node_id),
            "node_type": extract_rdf_type(individual),
        },
        "edges": extract_edges(individual),
        "semantics": extract_semantics(individual),
        "compliance": extract_compliance(individual),
        # ... other facets
    }
    
    try:
        return KnowledgeNode.model_validate(raw)
    except ValidationError:
        return None  # Sync rejected
```

### SyncGate Class

```python
class SyncGate:
    """
    Bidirectional gate between Pydantic schemas and OWL quadstore.
    Enforces consistency between write-side validation and read-side inference.
    """
    
    def export_to_owl(self, node: KnowledgeNode) -> bool:
        """Pydantic → OWL. Reject if SHACL validation fails."""
        if not node.model_validate(node):
            return False  # Pydantic rejected
        
        # Convert to RDF
        individual = pydantic_to_owl(node)
        
        # SHACL gate before commit
        if not self._shacl_validate(individual):
            return False  # SHACL rejected
        
        default_world.add(individual)
        return True
    
    def import_from_owl(self, individual) -> KnowledgeNode | None:
        """OWL → Pydantic. Gate on return to Python consumers."""
        raw = extract_rdf_triples(individual)
        try:
            return KnowledgeNode.model_validate(raw)
        except ValidationError:
            return None  # Rejected
    
    def sync(self) -> SyncReport:
        """Full bidirectional sync with conflict detection."""
        conflicts = []
        
        for pydantic_node in self._all_pydantic_nodes():
            owl_node = default_world[uri(pydantic_node.identity.node_id)]
            
            if owl_node:
                if not self._consistent(pydantic_node, owl_node):
                    conflicts.append(Conflict(
                        source="pydantic",
                        target="owl",
                        node=pydantic_node.identity.node_id,
                    ))
        
        return SyncReport(conflicts=conflicts)
    
    def _shacl_validate(self, individual) -> bool:
        """Run SHACL validation before OWL commit."""
        # Implementation uses pyshacl or owlready2-shacl
        pass
```

### Real-Time Observation (Optional)

Owlready2's observe framework can block invalid triples at insertion time:

```python
from owlready2.observe import default_world

def gatekeeper(triples):
    for s, p, o in triples:
        if not shacl_validates((s, p, o)):
            raise SyncRejected(
                f"Triple violates SHACL: {s} {p} {o}"
            )

default_world.observer.append(gatekeeper)
```

### Conflict Resolution

| Conflict Type | Resolution Strategy |
|---------------|-------------------|
| Pydantic valid, OWL invalid | Reject OWL state, keep Pydantic |
| Pydantic invalid, OWL valid | Reject Pydantic, regenerate from OWL |
| Both valid but different | Flag for human review (ADR gate) |

## Markdown Content Integration

The frontmatter is not the only content in wiki nodes. The markdown body has structured sections that map to OWL annotations and constructs.

### Wiki-Links → Typed References

```python
# Current markdown body
See [[autopoiesis]] and [[facet]].

# OWL equivalent
:wikipu:energy  :references  :autopoiesis ;
                 :references  :facet .
```

### Markdown Sections → Annotation Properties

```turtle
# ## Definition section
:wikipu:energy  rdfs:comment  "Energy in Wikipu is the conceptual and structural cost..."@en .

# ## Examples section
:wikipu:energy  :hasExample  "Energy Score Heuristic: Energy = (New Nodes * 10)..." .

# ## Related Concepts section
:wikipu:energy  rdfs:seeAlso  :facet , :topology .
```

### Tables → Enumerated Classes or Restrictions

```python
# Current in house_rules.md:
# | Autopoiesis | the how | How does the system maintain itself? |
# | Wiki        | the what | What does the system currently know? |

# OWL equivalent:
:wikipu:FiveElements  a           owl:Class ;
                      owl:oneOf  ( :Autopoiesis :Wiki :KnowledgeGraph :Git :CLI ) .

:wikipu:Autopoiesis  a             :FiveElements ;
                     :serves_as    "the how" ;
                     :answers      "How does the system maintain itself?".
```

### Rule IDs → Annotation Properties

```turtle
# ID-1, ID-2 from house_rules.md become OWL axioms
:ID1_Orthogonality  a           :IdentityRule ;
                     :rule_id     "ID-1" ;
                     :rule_name   "Orthogonality" ;
                     :enforced_by :TopologyProposalValidation ,
                                 :FacetProposalOrthogonalityCheck ;
                     rdfs:comment "No two elements do the same thing..." .
```

### "Enforced by:" → SWRL Rules

```python
# Current: "Enforced by: TopologyProposal validation"
# OWL/SWRL: Inference rule

# If a proposal has no orthogonality_check_passed
# Then it violates ID-1
swrl_rule = """
ID1_Enforcement(?p) :- 
    :proposal(?p),
    :violates_orthogonality(?p)
"""
```

### Energy Formula → OWL Restriction or Annotation

```turtle
# Energy = (New Nodes * 10) + (New Edges * 2) + (Violations * 100)
# Stored as annotation (complex math not natively OWL)

:wikipu:energy_formula  :energy_equation  
    "Energy = (New Nodes * 10) + (New Edges * 2) + (Orthogonality Violations * 100)" ;
    :threshold           50 ;
    :meaning             "score > 50 suggests rejection or refactoring" .
```

### Node Type Templates → OWL Class Hierarchies

WK-4 defines body structures per node_type:

```turtle
# concept structure: Abstract → Definition → Examples → Related
:wikipu:Concept  a           owl:Class ;
                 :hasSection :Definition , :Examples , :RelatedConcepts .

# adr structure: Abstract → Context → Decision → Rationale → Consequences
:wikipu:ADR  a           owl:Class ;
             rdfs:subClassOf :Document ;
             :hasSection :Context , :Decision , :Rationale , :Consequences .
```

### Content Extraction Pipeline

```python
def markdown_to_owl(node_path: Path) -> Individual:
    """Extract structured content from markdown to OWL individual."""
    content = node_path.read_text()
    frontmatter, body = parse_yaml_frontmatter(content)
    
    # 1. Wiki-links → :references property
    wiki_links = extract_wikilinks(body)
    for link in wiki_links:
        individual.references.append(get_individual(link))
    
    # 2. Sections → Annotation properties
    sections = parse_markdown_sections(body)
    if "## Definition" in sections:
        individual.comment = [sections["## Definition"]]
    if "## Examples" in sections:
        individual.hasExample = sections["## Examples"]
    
    # 3. Tables → Class assertions or annotations
    tables = extract_tables(body)
    for table in tables:
        if is_enumeration(table):
            create_enumerated_class(table)
        else:
            for row in table.rows:
                individual.annotate(row)
    
    # 4. Rule IDs → Annotation properties
    rules = extract_rules(body)
    for rule in rules:
        rule_individual = create_rule(rule)
        individual.enforces = rule_individual
    
    return individual
```

### What Stays as Prose

Not everything should be formalized:

| Content Type | OWL? | Reason |
|-------------|-------|--------|
| Definitions | ✅ Yes | `rdfs:comment` |
| Examples | ✅ Yes | `:hasExample` |
| Rule prose | ✅ Partial | Just annotations |
| Tables (enumerations) | ✅ Yes | `owl:oneOf` |
| Tables (data) | ❌ No | Keep as annotation |
| Narrative prose | ❌ No | Keep as markdown |
| Mathematical formulas | ✅ Yes | As string annotations |
| Code blocks | ❌ No | Keep as literal |

## Consequences

**Positive:**
- Automatic inference of transitive, symmetric, and inverse relationships
- Consistency checking catches contradictory knowledge
- SPARQL enables complex graph queries impossible with current wiki-compiler
- HermiT/Pellet reasoners provide machine-checkable logic
- OWL is an open standard with tooling (Protégé, etc.)

**Negative:**
- Dependency on Java runtime for HermiT/Pellet
- Learning curve for OWL semantics
- SQLite backend is not human-editable like Markdown
- Migration of existing wiki/ content is non-trivial

**Neutral:**
- Git remains the commit boundary (OWL files are commit-able)
- raw/ ingestion unchanged
- src/ wiki-compiler becomes owlready2 wrapper

## Alternatives Considered

1. **Keep current YAML frontmatter** — No inference, manual maintenance. Does not align with topology definition of knowledge as typed relationships.

2. **Use RDFlib only** — Stores triples but no reasoning. owlready2 builds on RDFlib with additional OWL support.

3. **Use graph database (Neo4j)** — owlready2 benchmarks faster; also requires separate tooling.

4. **Build custom reasoner** — Reinventing wheel; HermiT/Pellet are proven, maintained reasoners.

## References

- [OWL 2.0 W3C Specification](https://www.w3.org/TR/owl2-overview/)
- [Owlready2 Documentation](https://owlready2.readthedocs.io/)
- [Great Table of Description Logics](http://www.lesfleursdunormal.fr/static/_downloads/great_ontology_table.pdf)
- [SHACL W3C Specification](https://www.w3.org/TR/shacl/)
- [pyshacl (Python SHACL validator)](https://github.com/RDFLib/pySHACL)
- [SKOS (Simple Knowledge Organization System)](https://www.w3.org/TR/skos-reference/)
