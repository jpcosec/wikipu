---
identity:
  node_id: "doc:wiki/drafts/ingestion_layer_standards.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_refactor/docs/standards/code/ingestion_layer.md", relation_type: "documents"}
---

Standards for modules that sit at the system boundary — receiving uncontrolled external input and producing a validated internal representation. Extends `basic.md`.

## Details

Standards for modules that sit at the system boundary — receiving uncontrolled external input and producing a validated internal representation. Extends `basic.md`.

Current ingestion components: `src/scraper/` (job portal crawling), `src/review_ui/` (human review input).
Planned: CV ingestion.

Scraper produces non-deterministic output (LLM-assisted extraction, portal variability) and is classified under LLM standards for its output contract. This document covers the **boundary concerns** that apply to all ingestion components regardless of whether the extraction step is deterministic or LLM-based.

---

Generated from `raw/docs_postulador_refactor/docs/standards/code/ingestion_layer.md`.