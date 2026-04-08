---
identity:
  node_id: "doc:wiki/drafts/required_architecture_pattern.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_refactor/docs/standards/code/crawl4ai_usage.md", relation_type: "documents"}
---

### 1. Separate discovery/listing from detail extraction

## Details

### 1. Separate discovery/listing from detail extraction

If a source exposes some fields in the listing page and others in the detail page, model them as separate extraction boundaries.

Typical examples:

- listing page: `url`, `job_id`, `posted_date`, teaser salary
- detail page: `responsibilities`, `requirements`, company details

Merge listing + detail payloads before validating against `JobPosting`.

Do not expect one detail-page schema to recover fields that only exist reliably in listing cards.

### 2. Prefer deterministic extraction first

Use:

- `JsonCssExtractionStrategy`
- `JsonXPathExtractionStrategy`
- `RegexExtractionStrategy` when appropriate

The default approach for repetitive pages is LLM-free extraction.

### 3. Use LLM extraction through Crawl4AI only

When deterministic extraction is not enough, use `LLMExtractionStrategy` inside `CrawlerRunConfig`.

Do not:

- call LiteLLM directly from adapter code
- build custom chunking outside Crawl4AI
- manually recreate prompt/extraction plumbing already provided by the library

If we need LLM rescue, it must benefit from Crawl4AI's:

- `input_format`
- chunking
- usage reporting
- strategy integration
- consistent result handling

### 4. Generate schemas from multiple samples when the DOM varies

When generating a schema for a source with layout variation, use multiple representative HTML samples as described in the upstream docs.

Do not rely on a single sample for sites with:

- teaser cards plus detail page content
- repeated sticky headers
- mobile/desktop duplicates
- optional sections that shift element positions

The target is stable selectors, not positional selectors that happen to work once.

### 5. Use interaction tools when the DOM requires preparation

If the page requires expansion, clicking, scrolling, or dynamic hydration before extraction, use Crawl4AI interaction features:

- `js_code`
- `wait_for`
- C4A-Script when the flow is interaction-heavy or easier to express procedurally

Do not try to compensate for an unprepared DOM by making the extractor prompt more vague.

Generated from `raw/docs_postulador_refactor/docs/standards/code/crawl4ai_usage.md`.