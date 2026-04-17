---
pill_type: pattern
scope: component
language: en
nature: implementation
bound_to: owl-phase1-parallel-run
created: 2026-04-17
lifecycle: current
---

# Owlready2 Usage Patterns

## Pattern 1: World Setup

```python
from owlready2 import *

# Single world per session
default_world.set_backend(filename="wikipu.sqlite3")
onto = default_world.get_ontology("http://wikipu.org/ontology/")
```

## Pattern 2: Creating Classes

```python
with onto:
    class contains(ObjectProperty):
        domain   = [Thing]
        range    = [Thing]
```

## Pattern 3: Creating Individuals

```python
wiki_node = Knowledge("node_id")
wiki_node.contains = [other_node]
```

## Pattern 4: Querying

```python
# Simple search
onto.search(iri="*energy*")

# SPARQL
list(default_world.sparql("""
    SELECT ?s ?p ?o 
    WHERE { ?s ?p ?o }
    LIMIT 10
"""))
```

## Pattern 5: Export

```python
onto.save(file="wikipu.owl", format="rdfxml")
```

## Pattern 6: Observable Changes

```python
from owlready2.observe import default_world

def observer(triples):
    # Validate each triple
    pass

default_world.observer.append(observer)
```

## Reference

- `wiki/adrs/003_owl_integration.md` (Core Mechanism section)
- `owlready2.readthedocs.io/en/v0.50/intro.html`
