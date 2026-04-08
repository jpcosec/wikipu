---
identity:
  node_id: "doc:wiki/drafts/2_objective.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/plan/03_scrapper/phase1_scraping_and_autoapply.md", relation_type: "documents"}
---

Build a 3-layer scraping system (Fallback Cascade) that is:

## Details

Build a 3-layer scraping system (Fallback Cascade) that is:
1. **Deterministic-First:** Extract data using known CSS/XPath selectors to minimize LLM usage.
2. **Auditable:** Generate visual evidence (screenshots) automatically upon failure for easy debugging of JS-intensive sites.
3. **Persistent:** Utilize a dedicated, isolated Chrome profile to maintain sessions for auto-applying with your real account.
4. **Intelligent:** Track deadlines and "stale" status using metadata from JSON artifacts to prioritize applications.

Generated from `raw/docs_postulador_langgraph/plan/03_scrapper/phase1_scraping_and_autoapply.md`.