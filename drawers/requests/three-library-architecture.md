---
status: open
priority: p1
assigned_to: sldb-team + wikipu-team
created: 2026-04-22
labels:
  - feature-request
  - architecture
  - three-libraries
  - modular
---

# Feature Request: Three-Library Architecture

## Context

We have three concerns that are currently coupled:

1. **Document management** — contracts, templates, roundtrip validation, federation
2. **Graph reasoning** — nodes, edges, traversal, OWL, energy, context
3. **Wiki topology** — zones, autopoietic cycle, CLI orchestration

These concerns should be **separated into three independent libraries**.

## Current State

```
wikipu
├── src/wiki_compiler/  ← mixed concerns
│   ├── contracts.py   ← graph edges + facets
│   ├── energy.py      ← energy audit
│   ├── owl_reasoner.py ← OWL reasoning
│   ├── context.py     ← context routing
│   ├── cleanser.py   ← structural optimization
│   └── graph_utils.py ← graph operations
│
├── .sldb/            ← sldb store
└── sldb             ← external dependency
```

**Problem:** Everything is coupled to wikipu. Neither sldb nor the graph layer are independently useful.

## Proposal: Three Libraries

```
┌──────────────────────────────────────────────────────────┐
│                     wikipu                              │
│              (orchestrates both)                          │
│                                                         │
│  zones: raw/, desk/, wiki/, drawers/, src/               │
│  wiki-compiler CLI                                       │
│  autopoietic cycle                                     │
└──────────────────────────────────────────────────────────┘
         │                              │
         ▼                              ▼
┌─────────────────┐         ┌──────────────────────────┐
│      sldb       │         │          kgdb            │
│                 │         │                          │
│ documents       │         │ relations                │
│ contracts       │         │ semantics                │
│ templates       │         │ reasoning                │
│ validation      │         │ query                    │
│ document index  │         │ graph-native reports     │
│ federation      │         │                          │
└─────────────────┘         └──────────────────────────┘
         │                              │
         ▼                              ▼
   indexed facts                 horizontal relations + meaning
```

## Library Responsibilities

### 1. sldb — Document Facts + Index

**What it owns:**
- documents and models
- `StructuredNLDoc` base class
- Roundtrip validation
- Hash cascade (Merkle-style integrity)
- Federation (cross-repo stores)
- document index

**What it provides:**
- `sldb doc add/track/validate`
- `sldb model add/update`
- `sldb store init/check/sync`

**What it does NOT own:**
- Graph relationships between docs
- OWL reasoning
- Energy audit
- Context routing

**No dependency:** Can be used standalone.

### 2. kgdb — Relation Graph + Semantic Layer

**What it owns:**
- cross-document relations
- semantic overlays above facts
- graph-native query and traversal
- OWL ontology + reasoner
- graph-side reports derived from relation structure

**What it provides:**
- Graph traversal (`get_ancestors`, `get_descendants`)
- Structured queries (`StructuredQuery`)
- semantic interpretation over indexed facts
- reasoning outputs

**What it does NOT own:**
- Document format
- Templates
- Roundtrip validation

**No dependency:** Can be used standalone with any indexed factual source.

### 3. wikipu — Curator of Both Layers

**What it owns:**
- `wiki/` (current truth)
- `raw/` (ore)
- `desk/` (work surface)
- `drawers/` (deferred)
- `src/` (motor)
- `wiki-compiler` CLI
- Autopoietic cycle

**What it provides:**
- Zone-based organization
- wiki-compiler commands that curate the document and relation layers together
- Autopoietic self-maintenance

**What it consumes:**
- sldb for document management
- kgdb for relation and semantic reasoning

## Dependency Graph

```
wikipu
├── sldb              (required)
│   └── (no deps)
│
└── kgdb             (required)
    └── (no deps)

sldb        ← independent
kgdb ← independent
```

Neither sldb nor kgdb should depend on wikipu.

## Interface: Document ↔ Graph

The key interface is **linking indexed `sldb` facts to `kgdb` relation nodes**:

```python
# In kgdb
class KGNode(BaseModel):
    node_id: str
    sldb_ref: str | None  # Optional link to sldb document
    facets: dict

# In sldb
class DocumentEntry(BaseModel):
    name: str
    path: str
    kg_ref: str | None  # Optional link to KG node
```

**Cross-library edges:**

```python
# kgdb stores this:
class Edge(BaseModel):
    target_id: str
    relation_type: Literal[
        "extends", "contains", "documents",
        "transcludes", "implements", ...
    ]
    source: Literal["kg", "sldb"]

# If source is "sldb", kgdb
# looks up the kg_ref in sldb store
```

## Commands After Separation

### sldb (standalone)

```bash
sldb doc add --model FooDoc data.yaml
sldb model add foo:FooDoc
sldb store check
sldb store sync analyzer/
```

### kgdb (standalone)

```bash
kg query "extends:Document AND compliance: implemented"
kg energy --report
kg context --task "review architecture"
kg cleanse --dry-run
```

### wikipu (orchestrates both)

```bash
wiki-compiler build         # Builds graph from wiki/ + sldb store
wiki-compiler query      # Queries graph
wiki-compiler energy    # Energy audit
wiki-compiler audit   # Compliance check
sldb doc add          # Delegates to sldb
kg context           # Delegates to kgdb
```

## Migration Path

### Phase 1: isolate kgdb from wiki_compiler

Extract from `src/wiki_compiler/`:
- `graph_utils.py` → `kgdb.graph`
- `owl_reasoner.py` → `kgdb.reasoning`
- `energy.py` → `kgdb` core + `wikipu` adapter split
- `context.py` → `kgdb` core + `wikipu` adapter split
- `cleanser.py` → `kgdb.cleansing`
- `contracts.py` → `kgdb` graph contracts + `wikipu` schema split

Create: sibling repo/package `kgdb`

### Phase 2: Refactor sldb

Current: `wiki_compiler/contracts/tasks.py`, `wiki_nodes.py` use sldb
Target: These are the primary sldb use cases

### Phase 3: Refactor wikipu

Current: wikipu embeds both
Target: wikipu curates sldb + kgdb

```python
# In wikipu/src/wikipu/build.py
from sldb import StructuredNLDoc
from kgdb import Graph, Query, EnergyAudit

def build_knowledge_graph():
    graph = Graph()
    
    # Ingest from sldb store
    for doc in sldb_store.documents():
        node = kg_node_from_sldb_doc(doc)
        graph.add_node(node)
    
    # Ingest from sldb model inheritance
    for model in sldb_store.models():
        for parent in model.__bases__:
            graph.add_edge(model.node_id, parent.node_id, "extends")
    
    # Reason
    EnergyAudit(graph).run()
    
    return graph
```

## Questions for the Teams

### For sldb Team

1. Would you accept `sldb` staying responsible only for documents and their index?
2. Should sldb add **optional `kg_ref` field** to `DocumentEntry`?
3. What's your stance on cross-library edges?

### For wikipu Team (us)

1. Can we extract `kgdb` as a separate repo?
2. Should `wikipu` remain only the curator/orchestrator of both layers?
3. License: same as sldb?

### For Both

1. **Protocol:** How do sldb docs link to KG nodes?
2. **Federation:** Does sldb store federate with KG, or KG federate with sldb?
3. **Versioning:** Use rp-style contracts instead of semver

---

## How rp Solves Versioning

**rp (repopackage)** uses typed contracts instead of version numbers.

Reference: `/home/jp/proyectos/repopackage/docs/ARCHITECTURE.md`

### The Pattern

```yaml
# sldb compose.yaml
kind: package
name: sldb
exports:
  - DocumentContract   # What sldb provides
  - ModelContract      # What sldb provides
  - StoreContract     # What sldb provides
consumes: []         # sldb has no dependencies

# kgdb compose.yaml
kind: package
name: kgdb
exports:
  - GraphContract    # What KG provides
  - QueryContract   # What KG provides
  - EnergyContract  # What KG provides
  - ContextContract # What KG provides
consumes: []       # KG has no dependencies

# wikipu compose.yaml
kind: project
name: wikipu
consumes:
  - DocumentContract  # Requires sldb
  - GraphContract     # Requires KG
```

### How It Works

1. **Solver validates:** Every `consumes` in the graph is satisfied by an `exports` from a descendant node
2. **No version numbers:** Just contract matching
3. **Development lines:** Projects can pin to specific branches, not just versions
4. **Parallel evolution:** Each library evolves independently; solver ensures compatibility

### Benefits for Three Libraries

| Traditional (semver) | rp-style (contracts) |
|---|---|
| "sldb v2.1 depends on nothing" | "sldb exports DocumentContract" |
| "kgdb v1.0 depends on nothing" | "kgdb exports GraphContract" |
| "wikipu v3.0 depends on sldb v2.1" | "wikipu consumes DocumentContract + GraphContract" |

**No "which versions are compatible?"** The contracts define the interface.

---

## Alternative Considered

| Alternative | Pros | Cons |
|---|---|---|
| Keep coupled (current) | Simpler now | Harder to evolve |
| Two libraries (sldb+kg) | Simpler | Still coupled to wikipu |
| **This proposal (three)** | Full modularity | More repos to maintain |
| One library (merged) | One repo | Loss of focus |

We believe **three libraries + rp contracts** is the right balance.

---

Submitted by: wikipu team
Date: 2026-04-22
Affected repos: sldb, wikipu, (new: kgdb)
