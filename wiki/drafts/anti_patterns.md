---
identity:
  node_id: "doc:wiki/drafts/anti_patterns.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_refactor/docs/standards/code/crawl4ai_usage.md", relation_type: "documents"}
---

The following patterns are not acceptable:

## Details

The following patterns are not acceptable:

- custom post-crawl LiteLLM extraction outside `LLMExtractionStrategy`
- treating schema generation as a substitute for source modeling
- using one detail-page schema to infer listing-only fields
- keeping extraction metadata only in transient logs instead of structured artifacts
- counting a fetch as a successful ingestion when `JobPosting` validation failed

Generated from `raw/docs_postulador_refactor/docs/standards/code/crawl4ai_usage.md`.