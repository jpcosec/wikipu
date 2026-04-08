---
identity:
  node_id: "doc:wiki/drafts/8_known_reality_implemented_vs_target_graph.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/docs/operations/agent_entrypoint.md", relation_type: "documents"}
---

Implemented runtime graph is the prep-match flow through delivery: `scrape -> translate_if_needed -> extract_understand -> match -> review_match -> generate_documents -> render -> package`.

## Details

Implemented runtime graph is the prep-match flow through delivery: `scrape -> translate_if_needed -> extract_understand -> match -> review_match -> generate_documents -> render -> package`.

Target architecture docs still describe additional phases (`build_application_context`, motivation letter/CV/email review cycles, etc.). Treat those as target unless explicitly wired in `src/graph.py`.

Generated from `raw/docs_postulador_langgraph/docs/operations/agent_entrypoint.md`.