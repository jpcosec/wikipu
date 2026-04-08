---
identity:
  node_id: "doc:wiki/drafts/langgraph_and_agent_specific_guidance.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_v2/AGENTS.md", relation_type: "documents"}
---

- Default graph nodes to synchronous `def node(state) -> dict` unless the work is genuinely async end-to-end.

## Details

- Default graph nodes to synchronous `def node(state) -> dict` unless the work is genuinely async end-to-end.
- Keep graph state small; persist heavy payloads to artifacts instead of carrying them through state.
- Use `with_structured_output(...)` for LLM calls rather than parsing free-form strings.
- Expose Studio-friendly graphs through `create_studio_graph()` and keep `langgraph.json` in sync.
- Review flows are payload-driven; resume logic must be deterministic and safe on empty payloads.

Generated from `raw/docs_postulador_v2/AGENTS.md`.