---
identity:
  node_id: "doc:wiki/drafts/public_facade.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/plan/03_scrapper/playwright_scraping_blueprint.md", relation_type: "documents"}
---

`src/core/scraping/service.py` exposes only:

## Details

`src/core/scraping/service.py` exposes only:

```python
def scrape_detail(request: ScrapeDetailRequest) -> ScrapeDetailResult
def crawl_listing(request: CrawlListingRequest) -> CrawlListingResult
```

Generated from `raw/docs_postulador_langgraph/plan/03_scrapper/playwright_scraping_blueprint.md`.