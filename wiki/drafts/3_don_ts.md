---
identity:
  node_id: "doc:wiki/drafts/3_don_ts.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/plan/03_scrapper/phase1_scraping_and_autoapply.md", relation_type: "documents"}
---

* **NO LLM Burning:** Do not call the LLM if deterministic selectors successfully extract mandatory fields.

## Details

* **NO LLM Burning:** Do not call the LLM if deterministic selectors successfully extract mandatory fields.
* **NO Profile Sharing:** Never use your primary daily-use Chrome profile; Playwright will crash due to file locks.
* **NO LLM Offsets:** Do not ask the LLM to calculate text offsets; perform deterministic string searching instead.

Generated from `raw/docs_postulador_langgraph/plan/03_scrapper/phase1_scraping_and_autoapply.md`.