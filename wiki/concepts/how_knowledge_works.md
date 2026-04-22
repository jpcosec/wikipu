---
identity:
  node_id: "doc:wiki/concepts/how_knowledge_works.md"
  node_type: "concept"
edges:
  - {target_id: "doc:wiki/concepts/wiki_construction_principles.md", relation_type: "extends"}
  - {target_id: "doc:wiki/standards/house_rules.md", relation_type: "documents"}
compliance:
  status: "implemented"
  failing_standards: []
---

Knowledge in this system is not stored — it is structured. A fact lives only in the relationship between nodes, not inside any single file.

## The Atom of Knowledge

Every unit of knowledge is a `KnowledgeNode`. It has three layers:

1. **Identity** — who this node is (node_id + node_type)
2. **Edges** — typed relationships to other nodes
3. **Facets** — dimensions that answer specific questions (semantics, ast, compliance, git, source...)

A node without edges is a silence. An edge without a type is noise. The truth lives in the typed relationship.

## Typed Contracts at Every Boundary

ID-3 requires every boundary to be typed. This means:
- No raw dicts pass between modules
- No strings carry untyped data
- Pydantic `Field(description=...)` is mandatory on every field

The contract IS the documentation. LLMs read field descriptions.

## The Graph Is the Knowledge

```
raw/  →  wiki-compiler ingest  →  knowledge_graph.json
                                           ↓
                                      wiki/
```

The graph is the canonical knowledge. The wiki/ folder is a human-readable projection of it.

## Six Zones

| Zone | Role |
|---|---|
| `raw/` | Immutable seed ore (never written) |
| `exclusion/` | Non-self infrastructure (untouchable) |
| `wiki/` | Current truth |
| `desk/` | Active operational surface |
| `drawers/` | Deferred potential |
| `src/` | Motor and sensory organs |

## Libraries

| Library | Role |
|---|---|
| **networkx** | Runtime working graph (fast, mutable) |
| **owlready2** | OWL reasoning (consistency checks) |
| **rdflib** | RDF serialization (export/import) |
| **pydantic** | Typed contracts at every boundary |
| **sldb** | Structured Markdown documents |

## Energy

Truth is measured by efficiency. High energy = structural mass without topological truth. Low energy = minimal complexity holding maximal knowledge.

Every edit must be followed by immediate commit to prevent amnesia.

## Routing

The graph is the routing system. Agents navigate by node_id and edge_type, not by guessing file paths.