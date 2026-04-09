# Git-Tracked Node Identity

## Core Idea

Every node in the knowledge graph that corresponds to a file or code construct in the repository should carry its git lifecycle as a facet. The node's path-based ID (`file:src/wiki_compiler/builder.py`) is the stable identifier — it never changes. But the node's *content* has a git history, and that history should be queryable from the graph.

---

## The Problem with Path-Only Identity

Current node IDs are path-based. This is correct for stability: edges point to node IDs, and renaming a node would break all edges. Path-based IDs must stay.

The problem is that the graph is a snapshot. It answers "what exists now" but not "when did this exist", "who introduced it", or "has this drifted since the last build." Staleness is undetectable without comparing the current file state to the graph state.

---

## The GitFacet

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

## What This Enables

**Drift detection.** If `blob_sha` at build time ≠ current `git hash-object <file>`, the node's facets may be stale. The cleaner can flag it.

**Lifecycle queries.** "Show me all nodes created after commit X" = filter by `created_at_commit`. "Who owns this module?" = group by `last_modified_author`.

**Edge lifecycle.** If node A depends_on node B, and B's `last_modified_commit` is newer than A's `last_modified_commit`, A may need review. The graph can surface this.

**History without reading git log.** An agent navigating the graph can answer lifecycle questions without shelling out to git — the answers are already in the graph.

---

## Implementation Note

`GitFacet` is populated during `build_wiki()` by calling `git log` and `git hash-object` per file. It should be optional (untracked files won't have a `created_at_commit`). The `status` field is the high-value field for the cleaner — it is the primary staleness signal.

---

## Relation to Node ID

The node ID never encodes a git ref. The ID is the stable logical identity. The `GitFacet` is the temporal, mutable layer. Separating them preserves edge stability while enabling lifecycle queries.
