---
identity:
  node_id: doc:wiki/concepts/the_pca_analogy.md
  node_type: concept
edges:
- target_id: raw:raw/facet_orthogonalization.md
  relation_type: documents
compliance:
  status: implemented
  failing_standards: []
source:
  source_path: raw/facet_orthogonalization.md
  source_hash: 09c124cfbbf2a74ec7fb10ea1638c9348b6707bf3430cdba774567b11f3bac27
  compiled_at: '2026-04-14T16:50:28.659074'
  compiled_from: wiki-compiler
---

In PCA you rotate correlated variables onto orthogonal principal components.

## Definition

In PCA you rotate correlated variables onto orthogonal principal components.

## Examples

- Implementation of this concept within the Wikipu workflow.
- Application of these principles in current documentation.

## Related Concepts

- [[Index]]
- [[core_philosophy]]

## Details

In PCA you rotate correlated variables onto orthogonal principal components.
In the facet system you do the same: find the truly independent questions,
redefine the facets as those questions, rebuild.

The rebuild is free because facets are always derived from source truth (code, docs, git).
The graph is a cached view. Re-orthogonalization = redefine the lenses, re-run the build.

Generated from `raw/facet_orthogonalization.md`.
