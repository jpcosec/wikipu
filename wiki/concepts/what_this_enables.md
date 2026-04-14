---
identity:
  node_id: doc:wiki/concepts/what_this_enables.md
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
  compiled_at: '2026-04-14T16:50:28.660238'
  compiled_from: wiki-compiler
---

**Drift detection.** If `blob_sha` at build time ≠ current `git hash-object <file>`, the node's facets may be stale. The cleaner can flag it.

## Definition

**Drift detection.

## Examples

- Drift detection.
- Lifecycle queries.
- Edge lifecycle.
- History without reading git log.

## Related Concepts

- [[Index]]
- [[core_philosophy]]

## Details

**Drift detection.** If `blob_sha` at build time ≠ current `git hash-object <file>`, the node's facets may be stale. The cleaner can flag it.

**Lifecycle queries.** "Show me all nodes created after commit X" = filter by `created_at_commit`. "Who owns this module?" = group by `last_modified_author`.

**Edge lifecycle.** If node A depends_on node B, and B's `last_modified_commit` is newer than A's `last_modified_commit`, A may need review. The graph can surface this.

**History without reading git log.** An agent navigating the graph can answer lifecycle questions without shelling out to git — the answers are already in the graph.

---

Generated from `raw/git_tracked_nodes.md`.
