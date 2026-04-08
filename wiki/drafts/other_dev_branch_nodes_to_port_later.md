---
identity:
  node_id: "doc:wiki/drafts/other_dev_branch_nodes_to_port_later.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_refactor/future_docs/new_feature/extract_understand_node.md", relation_type: "documents"}
---

These exist on dev but are not yet in the refactored branch:

## Details

These exist on dev but are not yet in the refactored branch:

- **render node**: Copies markdown from generate_documents to render directory, computes SHA256 manifest. Currently the refactored branch has `src/core/tools/render/` which is more advanced (Pandoc + Jinja2 + multi-engine).
- **package node**: Copies rendered docs to `final/`, verifies hash integrity, creates `PackageManifest`.
- **build_application_context, tailor_cv, draft_email, review_* nodes**: Referenced in dev graph edges but NOT implemented. These are future scope.

Generated from `raw/docs_postulador_refactor/future_docs/new_feature/extract_understand_node.md`.