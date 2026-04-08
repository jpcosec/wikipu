---
identity:
  node_id: "doc:wiki/drafts/1_top_level_picture.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_v2/docs/repo_maps/current_repo_scrape_apply_browseros_ariadne_map.md", relation_type: "documents"}
---

- Scraping/ingestion runtime lives in `src/scraper/` and is still Crawl4AI-based.

## Details

- Scraping/ingestion runtime lives in `src/scraper/` and is still Crawl4AI-based.
- Applying runtime lives in `src/apply/` and now has two backends behind one CLI in `src/apply/main.py`:
  - `crawl4ai` for `xing`, `stepstone`, `linkedin`
  - `browseros` for `linkedin`
- Ariadne exists today as a playbook/data-model concept in the BrowserOS apply path, not as a separate standalone package.
- Control-plane scraping/search entrypoints are also exposed from `src/cli/main.py`.

Generated from `raw/docs_postulador_v2/docs/repo_maps/current_repo_scrape_apply_browseros_ariadne_map.md`.