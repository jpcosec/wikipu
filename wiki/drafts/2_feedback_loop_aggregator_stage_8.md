---
identity:
  node_id: "doc:wiki/drafts/2_feedback_loop_aggregator_stage_8.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/seed/product/07_evidence_tree_feedback_loop.md", relation_type: "documents"}
---

The system collects all ReviewNodes generated in the UI to update context for future executions.

## Details

The system collects all ReviewNodes generated in the UI to update context for future executions.

### Aggregation Mechanism

**Preference Extraction**: Reads ReviewNodes of type STYLE and CORRECTION from past applications.

**Evidence Consolidation**: If you manually added an evidence link in Match (AUGMENTATION), it's permanently saved to the global Evidence Bank for automatic suggestion in similar future applications.

**Prompt Injection**: UI and Backend show which specific corrections are included in the current prompt (provenance transparency).

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/seed/product/07_evidence_tree_feedback_loop.md`.