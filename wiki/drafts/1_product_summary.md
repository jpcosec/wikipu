---
identity:
  node_id: "doc:wiki/drafts/1_product_summary.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/docs/ui/review_workbench_product_brief.md", relation_type: "documents"}
---

PhD 2.0 is a local-first review and generation system for PhD job applications.

## Details

PhD 2.0 is a local-first review and generation system for PhD job applications.

Its purpose is to turn a scraped job posting plus candidate profile evidence into reviewed application artifacts:

1. structured extraction of the posting
2. requirement-to-evidence matching
3. generated application documents
4. human review checkpoints before semantic acceptance

The current product direction is **minimal viable architecture**:

- no Neo4j as the working data format
- no heavy enterprise orchestration in the UI
- all operational truth lives in local job folders under `data/jobs/<source>/<job_id>/`
- the UI is a review and correction surface over those real artifacts

This brief is for designing the operator-facing UI/UX of the current product, not the long-term speculative graph platform.

Generated from `raw/docs_postulador_langgraph/docs/ui/review_workbench_product_brief.md`.