---
identity:
  node_id: "doc:wiki/drafts/current_smell.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_refactor/future_docs/issues/profile_input_loading_node.md", relation_type: "documents"}
---

The current implementation suggests leftover legacy compatibility:

## Details

The current implementation suggests leftover legacy compatibility:

- list-shaped payloads are accepted
- dict payloads with `evidence` are also accepted
- normalization is not guaranteed to happen uniformly on every input path

This dual behavior is a signal that the profile contract is not fully consolidated yet.

Generated from `raw/docs_postulador_refactor/future_docs/issues/profile_input_loading_node.md`.