# Current Repo Map: Scraping, Crawl4AI, BrowserOS, Applying, Ariadne

Repo root: `/home/jp/postulator/podyulsyot3001`

## 1. Top-level picture

- Scraping/ingestion runtime lives in `src/scraper/` and is still Crawl4AI-based.
- Applying runtime lives in `src/apply/` and now has two backends behind one CLI in `src/apply/main.py`:
  - `crawl4ai` for `xing`, `stepstone`, `linkedin`
  - `browseros` for `linkedin`
- Ariadne exists today as a playbook/data-model concept in the BrowserOS apply path, not as a separate standalone package.
- Control-plane scraping/search entrypoints are also exposed from `src/cli/main.py`.

## 2. Runtime code map

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

## 3. Ariadne-related map

- `src/apply/browseros_models.py`
  - playbook fields include `ariadne_tag`
- `src/apply/playbooks/linkedin_easy_apply_v1.json`
  - concrete Ariadne-style path with `ariadne_tag`, bifurcations, dead ends, dry-run stop
- `plan_docs/issues/apply/applying_feature_design.md`
  - main deferred Ariadne/apply design document
- `data/ariadne/reference_data/applying_traces/linkedin_easy_apply/playbook_linkedin_easy_apply_v1.json`
  - design-time/source trace related to the packaged runtime playbook

Status note:

- Ariadne is partially implemented as typed playbook data plus one packaged LinkedIn path.
- The broader Ariadne knowledge-store vision from the docs (`apply_knowledge/`, path promotion, recorded branch learning) is not implemented yet.

## 4. Documentation map in the current repo

### Scraping docs

- `src/scraper/README.md`
  - module overview, runtime artifacts, extension notes
- `docs/standards/code/crawl4ai_usage.md`
  - repository standard for Crawl4AI usage
- `data/ariadne/assets/crawl4ai_schemas/README.md`
  - schema-cache usage/reference for scraper extraction
- `plan_docs/issues/scraper/crawl4ai_scraper_correction.md`
  - scraper hardening plan tied to apply reliability
- `plan_docs/issues/scraper/scraper_fragility.md`
  - fragility notes affecting application routing and portal stability
- `plan_docs/issues/scraper/application_routing_extraction.md`
  - routing-gap planning related to apply
- `docs/reference/external_libs/crawl4ai_custom_context.md`
  - external Crawl4AI reference asset

### Applying docs

- `src/apply/README.md`
  - documents the original Crawl4AI apply module
  - currently outdated because it does not yet describe `--backend browseros`, LinkedIn, or `--profile-json`
- `plan_docs/issues/apply/stage2_cross_portal_and_autoapply.md`
- `plan_docs/issues/apply/applying_feature_design.md`

### BrowserOS docs

- `docs/reference/external_libs/browseros_interfaces.md`
  - MCP/CDP/interface inventory
- `data/ariadne/reference_data/applying_traces/`
  - portal walkthrough screenshots and the LinkedIn playbook trace

## 5. Test map in the current repo

### Scraping tests

- `tests/unit/scraper/test_smart_adapter.py`

### Applying tests

- `tests/unit/apply/test_models.py`
- `tests/unit/apply/test_smart_adapter.py`

### BrowserOS tests

- `tests/unit/apply/browseros/test_models.py`
- `tests/unit/apply/browseros/test_client.py`
- `tests/unit/apply/browseros/test_executor.py`

## 6. Practical status summary

- Scraping: implemented, Crawl4AI-based, actively used.
- Apply/Crawl4AI: implemented for XING, StepStone, and LinkedIn adapter scaffolding.
- Apply/BrowserOS: implemented foundation plus one packaged LinkedIn path.
- Ariadne: present as a playbook model/path concept and one runtime playbook, but not yet a full path-learning subsystem.
- Docs: planning and reference material is now split across `future_docs/`, `plan_docs/automation/`, `docs/reference/`, and `data/ariadne/reference_data/`.
