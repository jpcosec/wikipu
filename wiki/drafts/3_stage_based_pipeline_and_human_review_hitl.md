---
identity:
  node_id: "doc:wiki/drafts/3_stage_based_pipeline_and_human_review_hitl.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/seed/product/03_methodology.md", relation_type: "documents"}
---

The workflow is a LangGraph where success depends on human validation at "semantic gates".

## Details

The workflow is a LangGraph where success depends on human validation at "semantic gates".

### Stage as Minimum Unit

- Each pipeline step is a node with a clear state file.

### UI Review Gates

- "Extraction" and "Matching" stages require an explicit decision (approve/reject) saved to disk before advancing to document generation.

### Comment System

- The interface must allow attaching `feedback.md` at each stage. This file is consumed by the pipeline when requesting "Regeneration".

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/seed/product/03_methodology.md`.