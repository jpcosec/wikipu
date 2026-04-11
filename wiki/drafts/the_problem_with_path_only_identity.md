---
identity:
  node_id: "doc:wiki/drafts/the_problem_with_path_only_identity.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/git_tracked_nodes.md", relation_type: "documents"}
compliance:
  status: "planned"
  failing_standards: []
source:
  source_path: "raw/git_tracked_nodes.md"
  source_hash: "7c36edc7b0a0b842072085f28a670c5aa2609fe5be25d43befc28a8bd7788a7c"
  compiled_at: "2026-04-10T17:47:33.731120"
  compiled_from: "wiki-compiler"
---

Current node IDs are path-based. This is correct for stability: edges point to node IDs, and renaming a node would break all edges. Path-based IDs must stay.

## Details

Current node IDs are path-based. This is correct for stability: edges point to node IDs, and renaming a node would break all edges. Path-based IDs must stay.

The problem is that the graph is a snapshot. It answers "what exists now" but not "when did this exist", "who introduced it", or "has this drifted since the last build." Staleness is undetectable without comparing the current file state to the graph state.

---

Generated from `raw/git_tracked_nodes.md`.