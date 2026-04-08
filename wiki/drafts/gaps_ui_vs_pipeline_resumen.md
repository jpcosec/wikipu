---
identity:
  node_id: "doc:wiki/drafts/gaps_ui_vs_pipeline_resumen.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/plan/01_ui/specs/00_pipeline_reference.md", relation_type: "documents"}
---

| Etapa Pipeline | Tiene spec UI | Notas |

## Details

| Etapa Pipeline | Tiene spec UI | Notas |
|----------------|---------------|-------|
| scrape | ✅ B1 | |
| translate_if_needed | Parcial | Solo en Job Flow Inspector como etapa — sin vista propia |
| extract_understand | ✅ B2 | |
| match | ✅ B3 | |
| review_match | ✅ B3 (integrado) | El review es parte de la vista match |
| build_application_context | ✅ B3b (especulativo) | Backend no implementado — spec listo |
| review_application_context | ✅ B3b (integrado) | Parte de la vista B3b |
| generate_motivation_letter | ✅ B4 (PREP_MATCH) + B4b (DEFAULT) | B4: 3 tabs simultáneos. B4b: 1 tab activo por gate |
| review_motivation_letter | ✅ B4b Gate C.1 | Tab "COVER_LETTER" |
| tailor_cv | ✅ B4b Gate C.2 | Tab "CV" |
| review_cv | ✅ B4b Gate C.2 | Tab "CV" |
| draft_email | ✅ B4b Gate C.3 | Tab "EMAIL" |
| review_email | ✅ B4b Gate C.3 | Tab "EMAIL" |
| render | En B0/B5 | Solo visible en Job Flow Inspector + Deployment |
| package | ✅ B5 | |

**Cobertura completa.** Todos los nodos del pipeline tienen spec UI. Los marcados como
⚠️ BLOCKED dependen del backend (B3b Fase 10, B4b Fase 8).

Generated from `raw/docs_postulador_ui/plan/01_ui/specs/00_pipeline_reference.md`.