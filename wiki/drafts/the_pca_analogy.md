---
identity:
  node_id: "doc:wiki/drafts/the_pca_analogy.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/facet_orthogonalization.md", relation_type: "documents"}
compliance:
  status: "planned"
  failing_standards: []
source:
  source_path: "raw/facet_orthogonalization.md"
  source_hash: "09c124cfbbf2a74ec7fb10ea1638c9348b6707bf3430cdba774567b11f3bac27"
  compiled_at: "2026-04-10T17:47:33.730539"
  compiled_from: "wiki-compiler"
---

In PCA you rotate correlated variables onto orthogonal principal components.

## Details

In PCA you rotate correlated variables onto orthogonal principal components.
In the facet system you do the same: find the truly independent questions,
redefine the facets as those questions, rebuild.

The rebuild is free because facets are always derived from source truth (code, docs, git).
The graph is a cached view. Re-orthogonalization = redefine the lenses, re-run the build.

Generated from `raw/facet_orthogonalization.md`.