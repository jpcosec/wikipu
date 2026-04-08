---
identity:
  node_id: "doc:wiki/drafts/review_checklist_for_crawl4ai_changes.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_refactor/docs/standards/code/crawl4ai_usage.md", relation_type: "documents"}
---

Before merging scraper changes, verify:

## Details

Before merging scraper changes, verify:

- extraction strategies live in `CrawlerRunConfig`
- any LLM usage goes through `LLMExtractionStrategy`
- schema generation uses representative samples for unstable DOMs
- listing-only fields are not being guessed from detail pages
- interaction-heavy pages use Crawl4AI interaction features instead of prompt hacks
- the module README in `src/scraper/README.md` still matches the implementation

Generated from `raw/docs_postulador_refactor/docs/standards/code/crawl4ai_usage.md`.