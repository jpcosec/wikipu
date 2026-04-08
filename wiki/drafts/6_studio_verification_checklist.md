---
identity:
  node_id: "doc:wiki/drafts/6_studio_verification_checklist.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_refactor/docs/standards/code/llm_langgraph_methodology.md", relation_type: "documents"}
---

Before considering a LangGraph feature production-ready:

## Details

Before considering a LangGraph feature production-ready:

- [ ] Graph topology visible in Studio (`langgraph.json` correct)
- [ ] Graph pauses at the review breakpoint
- [ ] Thread state is inspectable in the right-hand panel
- [ ] Resume with a valid payload routes correctly
- [ ] Resume with no payload returns safely to pending state
- [ ] Artifacts are written to the expected paths after each phase
- [ ] Demo chain produces valid, identifiable output (no credential required)

Generated from `raw/docs_postulador_refactor/docs/standards/code/llm_langgraph_methodology.md`.