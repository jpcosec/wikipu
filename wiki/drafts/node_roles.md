---
identity:
  node_id: "doc:wiki/drafts/node_roles.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/docs/runtime/graph_flow.md", relation_type: "documents"}
---

- `scrape` (`NLLM-ND`): fetches URL and produces canonical scrape artifacts plus compatible ingested payload in state.

## Details

- `scrape` (`NLLM-ND`): fetches URL and produces canonical scrape artifacts plus compatible ingested payload in state.
- `translate_if_needed` (`NLLM-ND`): conditionally normalizes language.
- `extract_understand` (`LLM`): produces structured extraction output.
- `match` (`LLM`): writes match proposal + review artifacts.
- `review_match` (`NLLM-D`): deterministic decision parser and route switch.
- `generate_documents` (`LLM` + deterministic rendering): writes CV/letter/email proposals and assist artifacts.
- `render` (`NLLM-D`): copies generated markdown into `nodes/render/proposed/` and records approved render refs with hashes.
- `package` (`NLLM-D`): validates rendered content hashes, writes `final/*.md` plus `final/manifest.json`, and marks run completed.

Generated from `raw/docs_postulador_langgraph/docs/runtime/graph_flow.md`.