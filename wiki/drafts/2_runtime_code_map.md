---
identity:
  node_id: "doc:wiki/drafts/2_runtime_code_map.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_v2/docs/repo_maps/current_repo_scrape_apply_browseros_ariadne_map.md", relation_type: "documents"}
---

### Scraping / ingestion

## Details

### Scraping / ingestion

- `src/scraper/main.py`
  - source-specific scrape CLI
  - registers `tuberlin`, `stepstone`, `xing`
- `src/scraper/smart_adapter.py`
  - shared Crawl4AI scraper base
  - imports `AsyncWebCrawler`, `BrowserConfig`, `CrawlerRunConfig`, `JsonCssExtractionStrategy`
  - owns browser config, extraction flow, schema-cache flow, and ingest persistence helpers
- `src/scraper/models.py`
  - `JobPosting` contract
  - includes application-routing scrape-time fields like `application_method` and `application_url`
- `src/scraper/providers/xing/adapter.py`
- `src/scraper/providers/stepstone/adapter.py`
- `src/scraper/providers/tuberlin/adapter.py`
- `src/cli/main.py`
  - adds operator-facing `scrape` and `search` commands that call scraper providers

### Applying / Crawl4AI path

- `src/apply/main.py`
  - common apply CLI
  - backend switch: `--backend crawl4ai|browseros`
  - source switch: `--source xing|stepstone|linkedin`
- `src/apply/models.py`
  - `FormSelectors`, `ApplicationRecord`, `ApplyMeta`
- `src/apply/smart_adapter.py`
  - shared Crawl4AI apply base
  - owns modal open, selector validation, file upload hook, submit flow, artifact writes
- `src/apply/providers/xing/adapter.py`
  - Crawl4AI/C4A-Script portal adapter
- `src/apply/providers/stepstone/adapter.py`
  - Crawl4AI/C4A-Script portal adapter
- `src/apply/providers/linkedin/adapter.py`
  - Crawl4AI/C4A-Script LinkedIn adapter scaffold merged from the worktree

### Applying / BrowserOS path

- `src/apply/browseros_client.py`
  - direct BrowserOS MCP client for `http://127.0.0.1:9200/mcp`
  - handles `initialize`, page lifecycle, snapshots, click/fill/select/upload/screenshot, React setter helper
- `src/apply/browseros_models.py`
  - typed playbook schema for BrowserOS execution
- `src/apply/browseros_executor.py`
  - replays BrowserOS playbooks step-by-step
  - resolves snapshot text to element IDs
  - supports dry-run stop, fallback actions, and human confirmation prompts
- `src/apply/browseros_backend.py`
  - BrowserOS apply provider wrapper used by `src/apply/main.py`
  - currently packages `linkedin` only
- `src/apply/playbooks/linkedin_easy_apply_v1.json`
  - packaged LinkedIn BrowserOS playbook used at runtime

Generated from `raw/docs_postulador_v2/docs/repo_maps/current_repo_scrape_apply_browseros_ariadne_map.md`.