---
identity:
  node_id: "doc:wiki/drafts/module_map.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_refactor/docs/runtime/pipeline_overview.md", relation_type: "documents"}
---

| Module | Type | README | Purpose |

## Details

| Module | Type | README | Purpose |
|--------|------|--------|---------|
| `src/scraper/` | Deterministic + LLM fallback | `src/scraper/README.md` | Discover and ingest job postings → `JobPosting` |
| `src/core/tools/translator/` | Deterministic | `src/core/tools/translator/README.md` | Translate scraped JSON fields + Markdown body |
| `src/core/ai/match_skill/` | LangGraph | `src/core/ai/match_skill/README.md` | Requirement-to-evidence matching with HITL review |
| `src/review_ui/` | Textual TUI | `src/review_ui/README.md` | Terminal interface for the match review gate |
| `src/core/ai/generate_documents/` | LangGraph | `src/core/ai/generate_documents/README.md` | CV, letter, and email generation from approved matches |
| `src/core/tools/render/` | Deterministic | `src/core/tools/render/README.md` | Pandoc + Jinja2 → PDF / DOCX |
| `src/shared/` | Library | `src/shared/README.md` | Cross-cutting utilities (log tags) |
| `src/core/ai/match_skill/main.py` | CLI entry point | `src/core/ai/match_skill/README.md` | Run or resume the match skill pipeline |

---

Generated from `raw/docs_postulador_refactor/docs/runtime/pipeline_overview.md`.