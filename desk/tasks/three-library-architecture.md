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
│      sldb       │         │      knowledgeGraph       │
│                 │         │                          │
│ .sldb/          │         │ knowledge_graph.json     │
│ Documents       │         │ Nodes + Edges            │
│ Contracts       │         │ Facets                   │
│ Templates       │         │ OWL Reasoning            │
│ Roundtrip valid │         │ Energy Audit             │
│ Hash cascade    │         │ Context Routing          │
│ Federation      │         │ Cleansing                 │
└─────────────────┘         └──────────────────────────┘
         │                              │
         ▼                              ▼
   Document contracts              Graph operations
   are graph nodes               inform document lifecycle
```

## Library Responsibilities

### 1. sldb — Document Management

**What it owns:**
- `.sldb/` store (documents, models, store_index)
- `StructuredNLDoc` base class
- Roundtrip validation
- Hash cascade (Merkle-style integrity)
- Federation (cross-repo stores)

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

### 2. knowledgeGraph — Graph Reasoning

**What it owns:**
- `knowledge_graph.json` (or equivalent)
- Nodes, edges, facets
- OWL ontology + reasoner
- Energy audit
- Context routing
- Cleansing

**What it provides:**
- Graph traversal (`get_ancestors`, `get_descendants`)
- Structured queries (`StructuredQuery`)
- Energy report
- Context bundle
- Cleansing proposals

**What it does NOT own:**
- Document format
- Templates
- Roundtrip validation

**No dependency:** Can be used standalone with any data source.

### 3. wikipu — Wiki Topology + Orchestration

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
- wiki-compiler commands (build, query, audit, etc.)
- Autopoietic self-maintenance

**What it consumes:**
- sldb for document management
- knowledgeGraph for graph reasoning

## Dependency Graph

```
wikipu
├── sldb              (required)
│   └── (no deps)
│
└── knowledgeGraph   (required)
    └── (no deps)

sldb        ← independent
knowledgeGraph ← independent
```

Neither sldb nor knowledgeGraph depend on each other or on wikipu.

## Interface: Document ↔ Graph

The key interface is **linking sldb documents to knowledgeGraph nodes**:

```python
# In knowledgeGraph
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
# knowledgeGraph stores this:
class Edge(BaseModel):
    target_id: str
    relation_type: Literal[
        "extends", "contains", "documents",
        "transcludes", "implements", ...
    ]
    source: Literal["kg", "sldb"]

# If source is "sldb", knowledgeGraph
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

### knowledgeGraph (standalone)

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
kg context           # Delegates to knowledgeGraph
```

## Migration Path

### Phase 1: Extract knowledgeGraph from wiki_compiler

Extract from `src/wiki_compiler/`:
- `graph_utils.py` → `knowledgeGraph.graph`
- `owl_reasoner.py` → `knowledgeGraph.owl`
- `energy.py` → `knowledgeGraph.energy`
- `context.py` → `knowledgeGraph.context`
- `cleanser.py` → `knowledgeGraph.cleansing`
- `contracts.py` (edges + facets) → `knowledgeGraph.contracts`

Create: https://github.com/sldb-team/knowledge-graph

### Phase 2: Refactor sldb

Current: `wiki_compiler/contracts/tasks.py`, `wiki_nodes.py` use sldb
Target: These are the primary sldb use cases

### Phase 3: Refactor wikipu

Current: wikipu embeds both
Target: wikipu consumes sldb + knowledgeGraph

```python
# In wikipu/src/wikipu/build.py
from sldb import StructuredNLDoc
from knowledgeGraph import Graph, Query, EnergyAudit

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

1. Would you accept **extracting the graph layer** as a separate `knowledgeGraph` library?
2. Should sldb add **optional `kg_ref` field** to `DocumentEntry`?
3. What's your stance on cross-library edges?

### For wikipu Team (us)

1. Can we **extract knowledgeGraph** to a separate repo?
2. Should it be `knowledge-graph` (hyphen) or `knowledgegraph` (no hyphen)?
3. License: same as sldb?

### For Both

1. **Protocol:** How do sldb docs link to KG nodes?
2. **Federation:** Does sldb store federate with KG, or KG federate with sldb?
3. **Versioning:** Lock-step releases or independent?

---

## Alternative Considered

| Alternative | Pros | Cons |
|---|---|---|
| Keep coupled (current) | Simpler now | Harder to evolve |
| Two libraries (sldb+kg) | Simpler | Still coupled to wikipu |
| **This proposal (three)** | Full modularity | More repos to maintain |
| One library (merged) | One repo | Loss of focus |

We believe **three libraries** is the right balance.

---

Submitted by: wikipu team
Date: 2026-04-22
Affected repos: sldb, wikipu, (new: knowledge-graph)