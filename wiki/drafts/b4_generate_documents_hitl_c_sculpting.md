---
identity:
  node_id: "doc:wiki/drafts/b4_generate_documents_hitl_c_sculpting.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/runtime/ui/views.md", relation_type: "documents"}
---

**Route:** `/jobs/:source/:jobId/sculpt`

## Details

**Route:** `/jobs/:source/:jobId/sculpt`
**Feature:** `features/job-pipeline/`
**Libraries:** `react-resizable-panels` · `@uiw/react-codemirror` · `@tanstack/react-query`

### Layout

```
┌── Tab Bar + Editor (70%) ───────────────────────┬── Context Panel (30%) ──┐
│ [CV] [COVER_LETTER] [EMAIL]    [SAVE] [APPROVE]  │ [PHASE: SCULPTING]     │
│──────────────────────────────────────────────── │                         │
│  CodeMirror (markdown mode, editable)            │ Mini match graph        │
│  [contenido del documento activo]               │ (read-only, estático)   │
│                                                  │ Evidence usada:         │
│                                                  │ [EV-005] EEG Research   │
│                                                  │ [REQUEST REGEN]         │
│                                                  │ [APPROVE ALL]          │
└──────────────────────────────────────────────────┴─────────────────────────┘
```

### Tab Status Indicators
```
Aprobado:          [✓ CV]  → text-primary border-b-2 border-primary
Editado sin guardar: [● CV] → text-secondary (amber dot)
Sin editar:          [CV]   → text-on-muted
```

### API Contract

**Read:**
- `GET /api/v2/query/jobs/:source/:job_id/views/documents` → `ViewPayload<'documents'>`

**Write:**
- `PUT /api/v2/commands/jobs/:source/:job_id/documents/:doc_key` — save document edits
- `POST /api/v2/commands/jobs/:source/:job_id/gates/review_match/decide` — APPROVE_ALL

---

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/runtime/ui/views.md`.