---
identity:
  node_id: "doc:wiki/drafts/dos_modos_de_ejecuci_n.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/plan/01_ui/specs/00_pipeline_reference.md", relation_type: "documents"}
---

El código define dos configuraciones del grafo:

## Details

El código define dos configuraciones del grafo:

### PREP_MATCH (implementado y runnable hoy)
```
scrape → translate_if_needed → extract_understand → match → review_match
  → generate_documents → render → package
```

### DEFAULT (full pipeline — parcialmente implementado)
```
scrape → translate_if_needed → extract_understand → match → review_match
  → build_application_context → review_application_context
  → generate_motivation_letter → review_motivation_letter
  → tailor_cv → review_cv
  → draft_email → review_email
  → render → package
```

La diferencia clave: en PREP_MATCH, `generate_documents` hace en un solo paso lo que en DEFAULT
se divide en 3 nodos LLM separados (letter, cv, email), cada uno con su propia puerta HITL.

---

Generated from `raw/docs_postulador_ui/plan/01_ui/specs/00_pipeline_reference.md`.