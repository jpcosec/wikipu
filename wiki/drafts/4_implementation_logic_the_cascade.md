---
identity:
  node_id: "doc:wiki/drafts/4_implementation_logic_the_cascade.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/plan/03_scrapper/phase1_scraping_and_autoapply.md", relation_type: "documents"}
---

1. **Layer 1 (Fast):** `HttpFetcher` + Strategy Selectors. If data is missing or "Access Denied" detected -> Escalate.

## Details

1. **Layer 1 (Fast):** `HttpFetcher` + Strategy Selectors. If data is missing or "Access Denied" detected -> Escalate.
2. **Layer 2 (Heavy):** `PlaywrightFetcher` (Stealth mode) + Strategy Selectors. If JS fails to render or selectors fail -> Take screenshot & Escalate.
3. **Layer 3 (AI Fallback):** `GenericAdapter` (LLM). Sends rendered HTML to Gemini to "understand" the new layout.

Generated from `raw/docs_postulador_langgraph/plan/03_scrapper/phase1_scraping_and_autoapply.md`.