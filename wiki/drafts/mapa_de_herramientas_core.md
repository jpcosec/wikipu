---
identity:
  node_id: "doc:wiki/drafts/mapa_de_herramientas_core.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/plan/01_ui/specs/00_pipeline_reference.md", relation_type: "documents"}
---

| Herramienta | Path | Función |

## Details

| Herramienta | Path | Función |
|-------------|------|---------|
| RoundManager | `src/core/round_manager.py` | Gestiona carpetas `rounds/round_NNN/` para iteración de feedback |
| ReviewDecisionService | `src/core/tools/review_decision_service.py` | Parsea checkboxes de decision.md → approve/regen/reject |
| WorkspaceManager | `src/core/io/workspace_manager.py` | Path resolution segura con validación de segmentos |
| ArtifactReader/Writer | `src/core/io/artifact_*.py` | Read/write de artefactos vía WorkspaceManager |
| ProvenanceService | `src/core/io/provenance_service.py` | sha256 hashing de artefactos |
| PromptManager | `src/ai/prompt_manager.py` | Jinja2 rendering de templates + XML tag validation |
| LLMRuntime | `src/ai/llm_runtime.py` | Wrapper Gemini con `generate_structured()` |
| ScrapingService | `src/core/scraping/service.py` | HTTP + Playwright fetching |
| TranslationService | `src/core/tools/translation/service.py` | deep-translator con chunking |

---

Generated from `raw/docs_postulador_ui/plan/01_ui/specs/00_pipeline_reference.md`.