---
identity:
  node_id: "doc:wiki/drafts/cleansing_candidates_by_node_type.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/cleansing_protocol.md", relation_type: "documents"}
compliance:
  status: "planned"
  failing_standards: []
source:
  source_path: "raw/cleansing_protocol.md"
  source_hash: "b5b3922be9089eb922885b17d43a45d212f4078f7ed6c85a899554499a6eead5"
  compiled_at: "2026-04-10T17:47:33.729761"
  compiled_from: "wiki-compiler"
---

### Code nodes (file:src/, code:)

## Details

### Code nodes (file:src/, code:)
- Duplicate: module with IOFacet overlapping another (TopologyProposal gates this
  on entry but does not retroactively audit existing nodes)
- Misplaced: module in wrong architectural layer (e.g. business logic in I/O layer)
- Split candidate: file with too many responsibilities visible in ASTFacet.signatures

### Doc nodes (doc:wiki/)
- Stale: documents edge points to a code node that no longer exists
- Duplicate: two nodes with near-identical abstracts
- Misplaced: wrong node_type for content structure, or wrong folder
- Split: abstract is compound — covers two independently usable concepts

### Plan nodes (doc:plan_docs/)
- Stale: plan with no git activity and no connection to any code node
- Note: plan nodes should self-destruct when the feature lands.
  Their absence after completion is the healthy state.

### Backlog nodes (doc:future_docs/)
- Stale: no activity beyond the 6-month house rule threshold
- Duplicate: two entries describing the same feature from different angles

### Test nodes (file:tests/)
- Orphaned: test file importing a module that no longer exists
- Misplaced: test classified as unit but exercises multiple integrated layers

### Config/data nodes
- Stale: no code node has a reads_from edge pointing to it
- Duplicate: two configs with the same schema_ref

---

Generated from `raw/cleansing_protocol.md`.