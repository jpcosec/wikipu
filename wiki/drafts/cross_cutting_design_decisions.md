---
identity:
  node_id: "doc:wiki/drafts/cross_cutting_design_decisions.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_refactor/docs/runtime/pipeline_overview.md", relation_type: "documents"}
---

### Control plane vs. data plane

## Details

### Control plane vs. data plane

All LangGraph state (`MatchSkillState`) carries only routing signals — source, job_id, refs, and decision flags. Heavy payloads (match proposals, generated documents) stay on disk. This keeps checkpointed state small and makes artifacts inspectable without replaying the graph.

### Node execution model

For the schema-v0 top-level pipeline in `src/graph/`, nodes run synchronously by default. The surrounding CLI, scraper, API client, and TUI may still use async where network interaction requires it, but graph-node bodies themselves should stay sync unless a node is genuinely async end-to-end.

### Artifact layout

```text
data/jobs/<source>/<job_id>/
  meta.json
  nodes/<node>/<stage>/<artifact>
```

See `docs/runtime/data_management.md` for the schema-v0 canonical layout.

### Failure model

All nodes fail closed — no silent fallback-to-success. LLM calls use `with_structured_output`. Missing credentials fall back to a demo chain in dev only (explicit guard in `src/core/ai/generate_documents/graph.py`).

### Observability

All log lines use `LogTag` from `src/shared/log_tags.py`. Never write emoji strings by hand. See `docs/standards/docs/documentation_and_planning_guide.md` §3 for the full tag vocabulary.

---

Generated from `raw/docs_postulador_refactor/docs/runtime/pipeline_overview.md`.