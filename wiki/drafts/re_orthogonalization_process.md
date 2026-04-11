---
identity:
  node_id: "doc:wiki/drafts/re_orthogonalization_process.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/facet_orthogonalization.md", relation_type: "documents"}
compliance:
  status: "planned"
  failing_standards: []
source:
  source_path: "raw/facet_orthogonalization.md"
  source_hash: "09c124cfbbf2a74ec7fb10ea1638c9348b6707bf3430cdba774567b11f3bac27"
  compiled_at: "2026-04-10T17:47:33.730653"
  compiled_from: "wiki-compiler"
---

When drift is detected:

## Details

When drift is detected:

1. List all facet questions on the table
2. Find overlapping spaces (co-occurrence, repeated queries, check overlap)
3. Define new axes: independent questions that span the same information space
4. Test each new axis: can it be answered by combining existing ones? If yes, it's a query.
5. Redefine contracts.py, registry specs, and injectors
6. Run wiki-compiler build → graph rebuilds from source

No data migration. The codebase and docs are always the ground truth.

Generated from `raw/facet_orthogonalization.md`.