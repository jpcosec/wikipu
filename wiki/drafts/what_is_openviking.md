---
identity:
  node_id: "doc:wiki/drafts/what_is_openviking.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_refactor/future_docs/new_feature/dev machine/llm_agent_native_context.md", relation_type: "documents"}
---

OpenViking (https://github.com/volcengine/OpenViking) is an open-source context database built around the concept of "Context as a Resource". It provides:

## Details

OpenViking (https://github.com/volcengine/OpenViking) is an open-source context database built around the concept of "Context as a Resource". It provides:

- A layered resource model (raw memory → domain knowledge → logic/tools) for structuring what an agent knows.
- A resource URI scheme (`viking://resources/<name>/`) for addressing context chunks.
- Schema validation for tool inputs/outputs so agents cannot pass malformed data between modules.

The integration idea: map this project's existing artifacts (logs, READMEs, Pydantic contracts, `future_docs/`) onto OpenViking's resource model so an agent working in this codebase can query structured context instead of reading raw files.

---

Generated from `raw/docs_postulador_refactor/future_docs/new_feature/dev machine/llm_agent_native_context.md`.