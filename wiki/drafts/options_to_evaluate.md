---
identity:
  node_id: "doc:wiki/drafts/options_to_evaluate.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/plan/future/scrapping_refactor.md", relation_type: "documents"}
---

### trafilatura

## Details

### trafilatura
- Python library, extracts main content from any HTML page (articles, docs, job postings)
- Discards nav/sidebar/footer automatically using heuristic + ML signals
- Drop-in replacement for `extract_text()` in `src/core/scraping/extract/html_to_text.py`
- Minimal integration risk — one function swap, no new architecture
- Lightweight dependency (~5MB)
- Likely what crawl4ai uses internally for content extraction

### crawl4ai
- Full crawling framework designed for LLM pipelines
- Produces clean markdown output ready for LLM consumption
- LLM-powered extraction: pass a prompt to extract structured fields
- CSS/XPath declarative extraction strategies
- Async/batch: 100+ URLs in parallel
- Session persistence (login flows, multi-step navigation)
- Built-in caching
- Heavier integration — would require rethinking `service.py` and fetch layer

Generated from `raw/docs_postulador_langgraph/plan/future/scrapping_refactor.md`.