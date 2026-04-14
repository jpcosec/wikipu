---
identity:
  node_id: doc:wiki/concepts/detection_signals.md
  node_type: concept
edges:
- target_id: raw:raw/cleansing_protocol.md
  relation_type: documents
compliance:
  status: implemented
  failing_standards: []
source:
  source_path: raw/cleansing_protocol.md
  source_hash: b5b3922be9089eb922885b17d43a45d212f4078f7ed6c85a899554499a6eead5
  compiled_at: '2026-04-14T16:50:28.657985'
  compiled_from: wiki-compiler
---

Each operation maps to a detectable graph condition:

## Definition

Each operation maps to a detectable graph condition:.

## Examples

- Implementation of this concept within the Wikipu workflow.
- Application of these principles in current documentation.

## Related Concepts

- [[Index]]
- [[core_philosophy]]

## Details

Each operation maps to a detectable graph condition:

Destroy:
  - Node has no incoming edges AND compliance status is planned AND no git activity
  - Node's documents target no longer exists in the graph (stale_edges check)
  - Plan node with no connected code node after 30+ days

Relocate:
  - node_id prefix does not match node_type convention
  - Node has no contains parent (orphan in the hierarchy)
  - Node's folder does not match its declared node_type

Split:
  - Abstract is longer than 3 sentences
  - Node body has two or more ## sections each with independent abstracts
  - SemanticFacet.intent contains conjunctions suggesting dual purpose ("and", "also")

Merge:
  - Jaccard similarity between two nodes' abstracts exceeds threshold (0.5)
  - Two nodes share the same IOFacet path_template
  - Two nodes have identical ASTFacet.signatures lists

---

Generated from `raw/cleansing_protocol.md`.
