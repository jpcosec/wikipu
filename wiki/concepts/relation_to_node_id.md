---
identity:
  node_id: doc:wiki/concepts/relation_to_node_id.md
  node_type: concept
edges:
- target_id: raw:raw/git_tracked_nodes.md
  relation_type: documents
compliance:
  status: implemented
  failing_standards: []
source:
  source_path: raw/git_tracked_nodes.md
  source_hash: 7c36edc7b0a0b842072085f28a670c5aa2609fe5be25d43befc28a8bd7788a7c
  compiled_at: '2026-04-14T16:50:28.660314'
  compiled_from: wiki-compiler
---

The node ID never encodes a git ref. The ID is the stable logical identity. The `GitFacet` is the temporal, mutable layer.

## Definition

The node ID never encodes a git ref.

## Examples

- Implementation of this concept within the Wikipu workflow.
- Application of these principles in current documentation.

## Related Concepts

- [[Index]]
- [[core_philosophy]]

## Details

The node ID never encodes a git ref. The ID is the stable logical identity. The `GitFacet` is the temporal, mutable layer. Separating them preserves edge stability while enabling lifecycle queries.

Generated from `raw/git_tracked_nodes.md`.
