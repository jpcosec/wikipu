---
identity:
  node_id: "doc:wiki/drafts/project_overview.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_v2/AGENTS.md", relation_type: "documents"}
---

- Python codebase for a modular job-application pipeline.

## Details

- Python codebase for a modular job-application pipeline.
- Main modules live under `src/`:
  - `src/scraper/` - ingest job postings
  - `src/core/tools/translator/` - translate job artifacts
  - `src/core/ai/generate_documents_v2/` - LangGraph document generation
  - `src/core/tools/render/` - deterministic PDF/DOCX rendering
  - `src/review_ui/` - Textual human review UI
- Main operator entrypoint: `python -m src.cli.main`
- LangGraph assistant entrypoint: `langgraph.json` -> `src.core.ai.generate_documents_v2.graph:create_studio_graph`

Generated from `raw/docs_postulador_v2/AGENTS.md`.