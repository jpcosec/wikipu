---
identity:
  node_id: "doc:wiki/drafts/the_problem.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/facet_orthogonalization.md", relation_type: "documents"}
compliance:
  status: "planned"
  failing_standards: []
source:
  source_path: "raw/facet_orthogonalization.md"
  source_hash: "09c124cfbbf2a74ec7fb10ea1638c9348b6707bf3430cdba774567b11f3bac27"
  compiled_at: "2026-04-10T17:47:33.730501"
  compiled_from: "wiki-compiler"
---

Facets accumulate over time. Without a gate, you end up with:

## Details

Facets accumulate over time. Without a gate, you end up with:
- Redundant facets answering the same question from two angles
- Under-specified facets whose questions overlap partially
- Facets that could be expressed as compound queries over existing ones

This is the same problem as correlated variables in a dataset — the axes aren't independent.

Generated from `raw/facet_orthogonalization.md`.