---
identity:
  node_id: "doc:wiki/drafts/golden_rule_local_first_superpower.md"
  node_type: "doc_standard"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/seed/product/10_ui_dev_integration_map.md", relation_type: "documents"}
---

Since the interface is a layer over the filesystem, UI has a "superpower" to avoid backend blocks:

## Details

Since the interface is a layer over the filesystem, UI has a "superpower" to avoid backend blocks:

### If backend doesn't stop at a stage (e.g., jumps from generate → render):

1. UI visually stops the user
2. UI retrieves generated files from `proposed/` (created lightning fast in background)
3. User edits calmly in the interface
4. UI uses `PUT /api/v1/jobs/{source}/{job_id}/documents/{doc_key}` to overwrite file
5. UI notifies backend: "Run only the Render node again using the files I just modified"

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/seed/product/10_ui_dev_integration_map.md`.