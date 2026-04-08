---
identity:
  node_id: "doc:wiki/drafts/5_done_definition.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/plan/03_scrapper/phase1_scraping_and_autoapply.md", relation_type: "documents"}
---

- [ ] `PlaywrightFetcher` implements a `try/except` block that saves `error_screenshot.png` on failure.

## Details

- [ ] `PlaywrightFetcher` implements a `try/except` block that saves `error_screenshot.png` on failure.
- [ ] `ScrapingService` implements the full cascade (Deterministic -> Playwright -> LLM).
- [ ] A dedicated "Bot Profile" directory is configured and isolated from the main browser.
- [ ] Automated crawler detects new jobs by comparing IDs and auto-ingests them into `data/jobs/`.
- [ ] API `portfolio/summary` highlights "URGENT" (deadline < 7 days) and "STALE" (scraped > 14 days ago) jobs.

Generated from `raw/docs_postulador_langgraph/plan/03_scrapper/phase1_scraping_and_autoapply.md`.