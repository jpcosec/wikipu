---
identity:
  node_id: doc:wiki/concepts/the_gitfacet.md
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
  compiled_at: '2026-04-14T16:50:28.660198'
  compiled_from: wiki-compiler
---

Add a `GitFacet` to nodes that correspond to tracked repository objects. Fields:

## Definition

Add a `GitFacet` to nodes that correspond to tracked repository objects.

## Examples

- Implementation of this concept within the Wikipu workflow.
- Application of these principles in current documentation.

## Related Concepts

- [[Index]]
- [[core_philosophy]]

## Details

Add a `GitFacet` to nodes that correspond to tracked repository objects. Fields:

| Field | Description |
|---|---|
| `blob_sha` | Git blob SHA of the file at build time. Changes when content changes. |
| `created_at_commit` | Commit hash that first introduced this file/construct. |
| `last_modified_commit` | Most recent commit that touched this file/construct. |
| `last_modified_author` | Author of that commit. |
| `status` | `tracked`, `untracked`, `modified_since_build` |

`modified_since_build` is set when `blob_sha` at build time differs from `blob_sha` in the current working tree. This makes staleness machine-detectable.

---

Generated from `raw/git_tracked_nodes.md`.
