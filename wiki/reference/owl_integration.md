---
identity:
  node_id: "doc:wiki/reference/owl_integration.md"
  node_type: "reference"
edges:
  - {target_id: "doc:wiki/adrs/003_owl_integration.md", relation_type: "documents"}
  - {target_id: "doc:wiki/concepts/topology.md", relation_type: "documents"}
compliance:
  status: "implemented"
  failing_standards: []
---

# OWL Integration Reference

This document explains how the OWL integration works in wikipu, with practical examples.

## Overview

The OWL integration uses a dual-library approach:
- **rdflib** for extraction, export, and querying (flexible, simple API)
- **owlready2** for reasoning (HermiT/Pellet reasoners)

The wiki graph is exported to an OWL file (`wikipu.owl`) which is gitignored (derived artifact).

## Architecture

```
wiki/*.md  →  markdown_to_rdf()  →  rdflib Graph  →  wikipu.owl
                                           ↓
                                     SPARQL queries
                                           ↓
                                   owlready2 + HermiT
                                           ↓
                                   Inferred triples
```

## Modules

| Module | Purpose |
|--------|---------|
| `owl_backend/extractor.py` | Markdown → RDF triples |
| `owl_backend/export.py` | Graph → RDF/XML |
| `owl_backend/import_export.py` | RDF → Markdown |
| `owl_reasoner.py` | HermiT reasoning |
| `sync_gate.py` | Pydantic ↔ OWL sync |

## Commands

### Build with OWL Export

```bash
wiki-compiler build --owl
```

Extracts all wiki nodes to RDF and saves `wikipu.owl`.

**Output:**
```
[OK] Graph saved to knowledge_graph.json
[OK] OWL ontology saved to wikipu.owl
```

### Query with SPARQL

```bash
wiki-compiler query --owl "SELECT ?s ?p ?o WHERE { ?s ?p ?o } LIMIT 10"
```

**Example output:**
```json
{
  "results": [
    ["https://wikipu.ai/ontology/energy", "https://wikipu.ai/ontology/status", "implemented"],
    ["https://wikipu.ai/ontology/autopoiesis", "https://wikipu.ai/ontology/node_type", "concept"]
  ],
  "count": 2
}
```

### Energy with Reasoning

```bash
wiki-compiler energy --reasoning
```

Runs HermiT reasoner and includes inferred relationships.

**Output:**
```
### OWL Reasoning
- **Consistency**: CONSISTENT
- **Reasoner**: ['HermiT reasoner completed']
```

### Audit with Sync Check

```bash
wiki-compiler audit --sync-check
```

Checks for conflicts between Markdown edges and OWL triples.

## SPARQL Examples

### Find all concepts
```bash
wiki-compiler query --owl "SELECT ?s WHERE { ?s <https://wikipu.ai/ontology/node_type> 'concept' }"
```

### Find all implemented nodes
```bash
wiki-compiler query --owl "SELECT ?s WHERE { ?s <https://wikipu.ai/ontology/status> 'implemented' }"
```

### Find references to a node
```bash
wiki-compiler query --owl "SELECT ?s WHERE { ?s <https://wikipu.ai/ontology/references> 'energy' }"
```

### Count all triples
```bash
wiki-compiler query --owl "SELECT (COUNT(*) as ?cnt) WHERE { ?s ?p ?o }"
```

## Extraction Details

The extractor parses Markdown frontmatter and body:

### Frontmatter → RDF

```yaml
---
identity:
  node_id: "doc:wiki/concepts/energy.md"
  node_type: "concept"
compliance:
  status: "implemented"
---
```

Becomes:
```rdf
<wikipu:energy> a wikipu:KnowledgeNode .
<wikipu:energy> wikipu:node_id "doc:wiki/concepts/energy.md" .
<wikipu:energy> wikipu:node_type "concept" .
<wikipu:energy> wikipu:status "implemented" .
```

### Wiki-links → References

```markdown
See [[autopoiesis]] and [[topology]] for details.
```

Becomes:
```rdf
<wikipu:energy> wikipu:references "autopoiesis" .
<wikipu:energy> wikipu:references "topology" .
```

## Programmatic Usage

### Extract Wiki to OWL

```python
from pathlib import Path
from wiki_compiler.owl_backend.extractor import extract_all, get_world
from wiki_compiler.owl_backend.export import export_to_rdfxml

# Extract all wiki files
graph = extract_all(Path("wiki"))

# Save to file
output = export_to_rdfxml(graph)
print(f"Exported {len(graph)} triples to {output}")
```

### Query the Graph

```python
from wiki_compiler.owl_backend.extractor import get_world

graph = get_world()

# SPARQL query
results = graph.query("""
    SELECT ?node ?type
    WHERE {
        ?node <https://wikipu.ai/ontology/node_type> ?type .
    }
    LIMIT 20
""")

for row in results:
    print(f"{row.node} -> {row.type}")
```

### Run Reasoning

```python
from wiki_compiler.owl_reasoner import OwlReasoner

reasoner = OwlReasoner()

# Run HermiT reasoner
inferred = reasoner.sync_reasoner()

# Check consistency
consistency = reasoner.consistency_check()
print(f"Ontology is: {consistency['consistency']}")
```

### SyncGate (Bidirectional)

```python
from wiki_compiler.sync_gate import SyncGate

gate = SyncGate()

# Export Pydantic node to OWL
violations = gate.export_to_owl("energy", {
    "node_type": "concept",
    "status": "implemented"
})

if violations:
    print(f"SHACL violations: {violations}")

# Import from OWL
node_data = gate.import_from_owl("energy")
print(node_data)
```

## Node Naming

Nodes are named by file stem:

| File | Node URI |
|------|---------|
| `wiki/Index.md` | `wikipu:Index` |
| `wiki/concepts/energy.md` | `wikipu:concepts_energy` |
| `wiki/selfDocs/WhoAmI.md` | `wikipu:selfDocs_WhoAmI` |

Special characters (slashes, spaces) are replaced with underscores.

## OWL Properties

| Property | Description | Example |
|----------|-------------|---------|
| `wikipu:node_id` | Canonical node ID | `"doc:wiki/concepts/energy.md"` |
| `wikipu:node_type` | Node type | `"concept"`, `"reference"`, `"selfDoc"` |
| `wikipu:status` | Compliance status | `"implemented"`, `"planned"` |
| `wikipu:references` | Wiki-links | `"autopoiesis"`, `"topology"` |

## Validation

### SHACL Shapes

The `shacl/` module defines shapes for KnowledgeNode validation:

```python
from wiki_compiler.shacl import validate_node, validate_ontology

# Validate a single node
violations = validate_node(my_node)

# Validate entire ontology
all_violations = validate_ontology()
```

### Real-time Validation

Enable with owlready2.observe:

```python
from wiki_compiler.shacl.validator import enable_realtime_validation

enable_realtime_validation()
```

## Troubleshooting

### "rdflib not installed"
```bash
pip install rdflib
```

### "Java not found" (reasoning)
HermiT requires Java runtime:
```bash
java -version  # Must be installed
```

### Empty wikipu.owl
Ensure frontmatter has proper YAML:
```yaml
---
identity:
  node_id: "doc:wiki/X.md"
  node_type: "concept"
---
```

## Files

- **Derived:** `wikipu.owl` (gitignored, regenerated on build)
- **Source:** `wiki/*.md` (authoritative)
- **Config:** `pyproject.toml` (dependencies)

## Related

- [[wiki/adrs/003_owl_integration.md]] — ADR for OWL integration
- [[wiki/concepts/topology.md]] — Topology concepts
- [[wiki/reference/cli/query.md]] — Query command
- [[wiki/reference/cli/energy.md]] — Energy command
