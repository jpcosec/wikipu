---
identity:
  node_id: doc:wiki/concepts/phase_2_inject_facets_semantics.md
  node_type: concept
edges:
- target_id: raw:raw/graph_construction_process.md
  relation_type: documents
compliance:
  status: implemented
  failing_standards: []
source:
  source_path: raw/graph_construction_process.md
  source_hash: 5cce04b66b0ac2624ccae799d5a8d22e00e6b9dd15ccc31cb63eb7dcb12cfaa9
  compiled_at: '2026-04-14T16:50:28.660796'
  compiled_from: wiki-compiler
---

Facets are independent passes over the raw graph. Each pass visits relevant nodes

## Definition

Facets are independent passes over the raw graph.

## Examples

- Key property:

## Related Concepts

- [[Index]]
- [[core_philosophy]]

## Details

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

Generated from `raw/graph_construction_process.md`.
