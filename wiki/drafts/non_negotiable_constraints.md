---
identity:
  node_id: "doc:wiki/drafts/non_negotiable_constraints.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/plan/03_scrapper/playwright_scraping_blueprint.md", relation_type: "documents"}
---

- `src/core/` stays deterministic at node boundaries.

## Details

- `src/core/` stays deterministic at node boundaries.
- Downstream nodes depend on canonical scrape output, not fetch internals.
- Heavy scrape payloads live on disk artifacts.
- Every scrape run persists provenance and replay evidence.
- Auto-postulation remains opt-in and separately audited.

Generated from `raw/docs_postulador_langgraph/plan/03_scrapper/playwright_scraping_blueprint.md`.