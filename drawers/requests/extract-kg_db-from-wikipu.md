---
status: open
priority: p1
assigned_to: wikipu-team
created: 2026-04-22
labels:
  - feature-request
  - architecture
  - extraction
  - modular
---

# Feature Request: Extract kg_db from wikipu

## Context

wikipu's `wiki_compiler/` contains two distinct concerns that should be separated:

1. **Graph reasoning** — nodes, edges, OWL, energy, context, cleansing
2. **Wiki orchestration** — zones, build, CLI, autopoietic cycle

This proposal extracts the graph layer into `kg_db` (Knowledge Graph Database), leaving wikipu as a thin orchestrator.

## Clarification: Relationship with sldb

**IMPORTANT:** This request and `sldb-knowledge-graph-integration.md` are **complementary, not contradictory**.

| Library | Scope |
|---|---|
| **sldb** | Document management, templates, validation, federation + **minimal graph** |
| **kg_db** | Full graph reasoning (OWL, energy, context, cleansing) |

**kg_db does NOT replace sldb.** kg_db consumes sldb for document management. sldb provides minimal graph (edges, links) to kg_db.

```
kg_db (consumes sldb)
├── graph/             ← uses sldb documents as nodes
├── reasoning/         ← OWL (NOT in sldb)
├── energy/           ← audit (NOT in sldb)
├── context/          ← routing (NOT in sldb)
└── cleansing/        ← proposals (NOT in sldb)

sldb (standalone, now with minimal graph)
├── .sldb/documents/    ← documents
├── .sldb/models/      ← contracts
└── .sldb/graph/       ← edges + links ONLY
```

## Current State

```
wikipu/
└── src/wiki_compiler/      ← mixed concerns
    ├── graph_utils.py   ← graph ops
    ├── contracts.py     ← edges + facets
    ├── energy.py       ← energy audit
    ├── owl_reasoner.py ← OWL reasoning
    ├── owl_backend/     ← OWL backend
    ├── shacl/         ← SHACL validation
    ├── context.py      ← context routing
    ├── query_executor.py
    ├── query_language.py
    ├── cleanser.py
    ├── registry.py
    ├── facet_validator.py
    ├── coordinator.py
    ├── perception.py
    │
    ├── main.py          ← CLI entry (mixed)
    ├── builder.py      ← builds graph
    ├── commands/      ← delegates to graph + sldb
    ├── scaffolder.py
    ├── curate.py
    └── ...rest
```

## Proposal: Extract kg_db

### kg_db (Knowledge Graph Database)

```python
# kg_db/ structure
kg_db/
├── contracts/
│   ├── edges.py        # Edge model
│   ├── facets.py       # ComplianceFacet, GitFacet, ...
│   └── knowledge_node.py  # KnowledgeNode
├── graph/
│   ├── graph_utils.py
│   ├── builder.py
│   └── types.py       # DiGraph wrapper
├── query/
│   ├── executor.py
│   └── language.py
├── reasoning/
│   ├── owl_reasoner.py
│   └── shacl/
├── energy/
│   └── audit.py
├── context/
│   └── routing.py
├── cleansing/
│   └── proposals.py
├── registry/
│   └── facets.py
└── compose.yaml
```

### What kg_db Gets (Full Reasoning)

### From wiki_compiler

kg_db extracts the **full reasoning layer** from wikipu:

| Feature | Source | In kg_db |
|---|---|---|
| OWL reasoner | `owl_reasoner.py` | `reasoning/owl.py` |
| SHACL validation | `shacl/` | `reasoning/shacl/` |
| Energy audit | `energy.py` | `energy/audit.py` |
| Context routing | `context.py` | `context/routing.py` |
| Cleansing | `cleanser.py` | `cleansing/` |
| Graph ops | `graph_utils.py` | `graph/ops.py` |
| Query executor | `query_executor.py` | `query/executor.py` |

### What kg_db Does NOT Get (belongs to sldb)

- Document format (`StructuredNLDoc`)
- Templates (`__template__`)
- Roundtrip validation
- Hash cascade
- Federation

These belong to sldb.

## What kg_db Exports (compose.yaml)

```yaml
kind: package
name: kg_db
version: "0.1.0"
exports:
  - GraphContract      # DiGraph, nodes, edges, add/get operations
  - QueryContract    # StructuredQuery, query executor
  - EnergyContract   # run_energy_audit() → EnergyReport
  - ContextContract  # build_context_bundle() → ContextBundle
  - OWLContract     # OWL reasoning + SHACL validation
  - CleansingContract  # CleansingProposal detection + application
  - FacetContract    # ComplianceFacet, GitFacet, SourceFacet
  - RegistryContract  # facet registry
consumes: []
```

### What wikipu Consumes

```yaml
kind: project
name: wikipu
version: "0.1.0"
consumes:
  - GraphContract     # from kg_db
  - QueryContract   # from kg_db
  - DocumentContract  # from sldb
  - StoreContract     # from sldb
```

## Files to Extract

| File | → | New Module |
|---|---|---|
| `contracts.py` | → | `kg_db/contracts/` |
| `graph_utils.py` | → | `kg_db/graph/graph_utils.py` |
| `energy.py` | → | `kg_db/energy/audit.py` |
| `owl_reasoner.py` | → | `kg_db/reasoning/owl_reasoner.py` |
| `owl_backend/` | → | `kg_db/reasoning/owl_backend/` |
| `shacl/` | → | `kg_db/reasoning/shacl/` |
| `context.py` | → | `kg_db/context/routing.py` |
| `query_executor.py` | → | `kg_db/query/executor.py` |
| `query_language.py` | → | `kg_db/query/language.py` |
| `cleanser.py` | → | `kg_db/cleansing/proposals.py` |
| `registry.py` | → | `kg_db/registry/facets.py` |
| `facet_validator.py` | → | `kg_db/registry/validator.py` |
| `coordinator.py` | → | `kg_db/coordination/` |
| `perception.py` | → | `kg_db/perception/` |

## Files to Keep in wikipu

| File | Purpose |
|---|---|
| `main.py` | CLI entry, delegates to kg_db + sldb |
| `builder.py` | Orchestrates build using kg_db |
| `commands/` | CLI commands (build, query, audit → kg_db; scaffold, curate → sldb) |
| `scaffolder.py` | Uses sldb for doc templates |
| `curate.py` | Uses sldb for draft curation |
| `node_templates.py` | SLDB node templates |
| `manifest.py` | Raw source manifest |
| `drafts.py` | Draft tracking |
| `session_storage.py` | Session logs |
| `trails.py` | Trail artifacts |
| `gates.py` | Gate tracking |
| `workflow_guard.py` | Workflow enforcement |

## Migration Path

### Phase 1: Extract kg_db

```bash
# Create kg_db repo
git clone wikipu kg_db
cd kg_db

# Remove wikipu-specific files
rm -rf wiki/ raw/ desk/ drawers/ src/wikipu/ .sldb/

# Remove wikipu orchestration files
rm -rf src/wiki_compiler/main.py
rm -rf src/wiki_compiler/commands/
rm -rf src/wiki_compiler/scaffolder.py
rm -rf src/wiki_compiler/curate.py

# Move to new structure
mkdir -p kg_db/{contracts,graph,query,reasoning,energy,context,cleansing,registry,coordination,perception}
# ... move files accordingly

# Update imports
sed -i 's/wiki_compiler.contracts/kg_db.contracts/g' kg_db/**/*.py
sed -i 's/wiki_compiler.graph_utils/kg_db.graph.graph_utils/g' kg_db/**/*.py

# Add compose.yaml
cat > kg_db/compose.yaml << 'EOF'
kind: package
name: kg_db
version: "0.1.0"
exports:
  - GraphContract
  - QueryContract
  - EnergyContract
  - ContextContract
  - OWLContract
  - CleansingContract
  - FacetContract
  - RegistryContract
consumes: []
EOF
```

### Phase 2: Refactor wikipu to consume kg_db

```python
# wikipu/src/wiki_compiler/main.py (AFTER extraction)
from kg_db import Graph, QueryExecutor, EnergyAudit, ContextRouter
from sldb import doc_add, model_add, store_check

def main():
    if args.command == "build":
        graph = Graph()
        builder = GraphBuilder(graph)
        builder.scan_wiki()
        builder.scan_sldb()
        graph.save()

    elif args.command == "query":
        executor = QueryExecutor(graph)
        results = executor.execute(args.query)

    elif args.command == "energy":
        audit = EnergyAudit(graph)
        report = audit.run()
```

### Phase 3: Add sldb integration

```python
# wikipu/src/wiki_compiler/commands/scaffold.py
import sldb

def handle_scaffold(args):
    sldb.model_add(args.model, pythonpath=args.pythonpath)
    sldb.doc_add(args.model, args.data, output=args.output)
```

## What kg_db Gains

| Benefit | Description |
|---|---|
| **Independence** | kg_db can be used without wikipu |
| **Clean API** | Contracts define the interface |
| **Tests** | kg_db has its own test suite |
| **Evolution** | kg_db evolves at its own pace |

## What wikipu Gains

| Benefit | Description |
|---|---|
| **Simplicity** | wikipu is a thin orchestrator |
| **Focus** | Zones, CLI, autopoietic cycle only |
| **Composability** | Can swap kg_db for another graph library |
| **Size** | Much smaller codebase |

## Commands After Separation

### kg_db (standalone)

```bash
kg_db build --source my_docs/
kg_db query "extends:ConceptDoc AND compliance: implemented"
kg_db energy --report
kg_db context --task "review architecture"
kg_db cleanse --dry-run
```

### wikipu (orchestrates kg_db + sldb)

```bash
wiki-compiler build         # delegates to kg_db + sldb
wiki-compiler scaffold     # delegates to sldb
wiki-compiler curate      # delegates to sldb
wiki-compiler audit       # delegates to kg_db
```

## Questions

1. **Name:** `kg_db` or `knowledge-graph` or `knowledgegraph`?
2. **Location:** New repo or subdirectory of wikipu?
3. **Tests:** Extract with files or extract after?
4. **OWL:** Keep owlready2, or make it optional?

---

Submitted by: wikipu team
Date: 2026-04-22
Affected repos: wikipu, (new: kg_db)