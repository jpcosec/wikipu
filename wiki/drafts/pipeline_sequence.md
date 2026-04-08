---
identity:
  node_id: "doc:wiki/drafts/pipeline_sequence.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_refactor/docs/runtime/pipeline_overview.md", relation_type: "documents"}
---

```

## Details

```
src/scraper/
  ↓  canonical raw job artifacts under `nodes/ingest/proposed/`
src/core/tools/translator/
  ↓  translated fields + content.md
src/core/ai/match_skill/          ← LangGraph, pauses for HITL review
  ↑  review decisions via src/review_ui/ (Textual TUI)
  ↓  approved/state.json
src/core/ai/generate_documents/   ← LangGraph
  ↓  cv.md, cover_letter.md, email_body.txt
src/core/tools/render/
  ↓  PDF / DOCX artifacts
```

Schema-v0 runtime rules for artifact placement, job metadata, and the central data manager are defined in `docs/runtime/data_management.md`.

---

Generated from `raw/docs_postulador_refactor/docs/runtime/pipeline_overview.md`.