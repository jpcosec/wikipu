---
identity:
  node_id: "doc:wiki/drafts/implementation_note.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/git_tracked_nodes.md", relation_type: "documents"}
compliance:
  status: "planned"
  failing_standards: []
source:
  source_path: "raw/git_tracked_nodes.md"
  source_hash: "7c36edc7b0a0b842072085f28a670c5aa2609fe5be25d43befc28a8bd7788a7c"
  compiled_at: "2026-04-10T17:47:33.731228"
  compiled_from: "wiki-compiler"
---

`GitFacet` is populated during `build_wiki()` by calling `git log` and `git hash-object` per file. It should be optional (untracked files won't have a `created_at_commit`). The `status` field is the high-value field for the cleaner — it is the primary staleness signal.

## Details

`GitFacet` is populated during `build_wiki()` by calling `git log` and `git hash-object` per file. It should be optional (untracked files won't have a `created_at_commit`). The `status` field is the high-value field for the cleaner — it is the primary staleness signal.

---

Generated from `raw/git_tracked_nodes.md`.