# Worktree Map: Scraping, Crawl4AI, BrowserOS, Applying, Ariadne

Worktree root: `/home/jp/postulator/.worktrees/feat-apply-module`

## 1. Top-level picture

- Scraping/ingestion runtime lives in `src/scraper/` and is Crawl4AI-based, same general structure as the main repo.
- Applying runtime in this worktree is Crawl4AI-only.
- This worktree adds LinkedIn to the apply module, but it does not contain the BrowserOS runtime implementation.
- Ariadne is absent from runtime code here and appears only implicitly in planning gaps, not as code or packaged playbooks.

## 2. Runtime code map

### Scraping / ingestion

- `src/scraper/main.py`
  - source-specific scrape CLI
- `src/scraper/smart_adapter.py`
  - shared Crawl4AI scraper base
- `src/scraper/models.py`
  - `JobPosting` contract including apply-routing fields
- `src/scraper/providers/xing/adapter.py`
- `src/scraper/providers/stepstone/adapter.py`
- `src/scraper/providers/tuberlin/adapter.py`
- `src/cli/main.py`
  - operator-facing scrape/search flow

### Applying / Crawl4AI path

- `src/apply/main.py`
  - single apply CLI without backend switching
  - supports `--source xing|stepstone|linkedin`
- `src/apply/models.py`
  - `FormSelectors`, `ApplicationRecord`, `ApplyMeta`
- `src/apply/smart_adapter.py`
  - shared Crawl4AI apply base
- `src/apply/providers/xing/adapter.py`
- `src/apply/providers/stepstone/adapter.py`
- `src/apply/providers/linkedin/adapter.py`

### BrowserOS path

- No BrowserOS runtime code found in this worktree.
- Specifically absent versus the main repo:
  - no `src/apply/browseros_client.py`
  - no `src/apply/browseros_models.py`
  - no `src/apply/browseros_executor.py`
  - no `src/apply/browseros_backend.py`
  - no `src/apply/playbooks/`
  - no `--backend browseros` support in `src/apply/main.py`

## 3. Ariadne-related map

- No Ariadne-tagged runtime code or playbook JSON found in this worktree.
- No `browseros_*` docs or trace directories found here.
- Ariadne is therefore effectively absent from the worktree implementation snapshot.

## 4. Documentation map in the worktree

### Scraping docs

- `src/scraper/README.md`
- `docs/standards/code/crawl4ai_usage.md`
- `data/ariadne/assets/crawl4ai_schemas/README.md` in main repo now replaces the old root schema-cache location
- `plan_docs/issues/scraper/crawl4ai_scraper_correction.md` in main repo now replaces the older plan location
- `plan_docs/issues/scraper/scraper_fragility.md`
- `future_docs/crawl4ai_custom_context (1).md`

### Applying docs

- `src/apply/README.md`
  - documents the Crawl4AI apply module
- older per-step apply plan docs that have since been removed from main

### BrowserOS docs

- No BrowserOS documentation files found in this worktree snapshot.

## 5. Test map in the worktree

### Scraping tests

- `tests/unit/scraper/test_smart_adapter.py` in main repo now replaces the older flat test path

### Applying tests

- `tests/unit/apply/test_models.py` in main repo now replaces the older flat test path
- `tests/unit/apply/test_smart_adapter.py` in main repo now replaces the older flat test path

### BrowserOS tests

- None found.

## 6. Practical status summary

- Scraping: implemented, Crawl4AI-based.
- Apply/Crawl4AI: implemented for XING, StepStone, plus LinkedIn extension.
- Apply/BrowserOS: not implemented in this worktree.
- Ariadne: not implemented in runtime code in this worktree.
- Docs: older doc layout was split across `plan_docs/apply/` and `future_docs/`; main has since moved away from both that layout and the later `plan_docs/applying/` bucket.
