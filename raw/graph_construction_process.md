# The Three-Phase Graph Construction Process

## Core Idea

The knowledge graph is built in three independent, composable phases.
Each phase adds a layer of meaning on top of the previous one.
The raw graph captures existence. Facets capture semantics. Queries capture quality.

---

## Phase 1 — Build the Raw Graph (Structure)

The raw graph answers only: **what exists, and what points to what.**

Every file, directory, code construct, and doc becomes a node.
Every detectable reference between them becomes an edge — imports, file includes,
transclusions, co-mentions. No meaning is assigned yet. NetworkX holds this as a
pure topology: a skeleton of the system.

```
dir:src  --contains-->  file:src/scanner.py
file:src/scanner.py  --depends_on-->  file:src/contracts.py
doc:wiki/how_it_works.md  --transcludes-->  doc:wiki/standards/00_house_rules.md
```

At this stage the graph is a map of existence and reference only.
An LLM could walk it but couldn't understand what anything does.

**Sources for the raw graph:**
- Directory tree walk → `contains` edges
- Python `import` statements → `depends_on` edges
- Markdown `![[transclusion]]` syntax → `transcludes` edges
- YAML frontmatter `edges:` declarations → any relation type

---

## Phase 2 — Inject Facets (Semantics)

Facets are independent passes over the raw graph. Each pass visits relevant nodes
and enriches them with a new dimension. They do not change the topology — they annotate it.

| Pass | What it reads | What it injects |
|---|---|---|
| AST scanner | `.py` files | `ASTFacet` — signatures, construct type, imports |
| Docstring extractor | `.py` files | `SemanticFacet` — intent, raw docstring |
| IO detector | AST + docstring annotations | `IOFacet` — medium, path, schema |
| Compliance checker | node completeness rules | `ComplianceFacet` — status, failing standards |
| Test mapper | test files + decorators | `TestMapFacet` — type, coverage |
| ADR linker | `wiki/adrs/` | `ADRFacet` — decision history |

After this phase the same node `file:src/scanner.py` is no longer just an ID.
It carries intent, signatures, known I/O ports, and a compliance status.

**Key property:** facet passes are orthogonal. They can be run in any order,
added independently, and extended without touching the core graph structure.

---

## Phase 3 — Query for Documentation Quality

The structured graph can now be interrogated as a cross-reference engine.
Quality gaps appear as structural anomalies — places where the two layers disagree.

**Coverage gaps** — code that exists but has no documentation edge:
```
code nodes  WHERE  no incoming edge WITH relation_type="documents"
→ undocumented modules
```

**Semantic gaps** — nodes that exist but have no meaning attached:
```
code nodes  WHERE  SemanticFacet IS NULL  OR  raw_docstring IS NULL
→ missing docstrings
```

**I/O gaps** — data flowing without a type contract:
```
IOFacet nodes  WHERE  schema_ref IS NULL  AND  medium != "network"
→ untyped disk I/O
```

**Compliance violations** — nodes failing specific house rules:
```
nodes  WHERE  ComplianceFacet.failing_standards IS NOT EMPTY
→ standards breaches
```

**Stale documentation** — docs pointing to code that no longer exists:
```
edges WITH relation_type="documents"  WHERE  target_id NOT IN graph.nodes
→ dead references
```

**Orphaned plans** — future_docs entries with no corresponding code node:
```
doc nodes in future_docs/  WHERE  no outgoing edge to any code node
→ forgotten backlog items
```

---

## The Key Insight

The raw graph gives you **reachability** — what can find what.
Facets give you **semantics** — what things mean.
Quality checking is asking: where do these two layers disagree?

Every gap between "this node exists" and "this node is fully understood and documented"
is a documentation debt. The system does not check docs by reading prose —
it checks them by looking for missing structure in the graph.

---

## Design Principles

1. **Separation of concerns** — topology is built once; semantics are layered on top independently.
2. **Extensibility** — new facets can be added without touching the graph structure or existing passes.
3. **Auditability** — every quality finding is a graph query with a deterministic result.
4. **Code as ground truth** — facets are extracted from code, not written by hand. The graph
   reflects reality, not intention.
