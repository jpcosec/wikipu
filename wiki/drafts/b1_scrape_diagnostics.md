---
identity:
  node_id: "doc:wiki/drafts/b1_scrape_diagnostics.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/runtime/ui/views.md", relation_type: "documents"}
---

**Route:** `/jobs/:source/:jobId/scrape`

## Details

**Route:** `/jobs/:source/:jobId/scrape`
**Feature:** `features/job-pipeline/`
**Libraries:** `@tanstack/react-query` · `lucide-react`

### Layout

```
┌──────────────── Main ─────────────────────┬── Control Panel ──┐
│  [SCRAPE_DIAGNOSTICS header]              │ [PHASE: SCRAPE]  │
│  ┌── Fetch Metadata ──────────────────┐  │ URL configurada  │
│  │ URL: https://...                   │  │ Adapter: tu_berlin│
│  │ Retrieved: 2026-03-05T04:50:18Z   │  │ Status: completed │
│  └────────────────────────────────────┘  │ [RE-RUN SCRAPE]  │
│  ┌── Source Text Preview ─────────────┐  │ [ADVANCE →]      │
│  │ [20 líneas collapsable]            │  │                  │
│  └────────────────────────────────────┘  │                  │
│  ┌── Error Screenshot (si existe) ────┐  │                  │
│  │ [img] ERROR_TRACE: ...              │  │                  │
└───────────────────────────────────────────┴───────────────────┘
```

### Components
- `<ScrapeMetaCard>` — URL, timestamp, adapter, HTTP status
- `<SourceTextPreview>` — Collapsible (20 lines → expand)
- `<ErrorScreenshot>` — Conditional image if error
- `<ScrapeControlPanel>` — Re-run + advance actions

### API Contract

**Read:**
- `GET /api/v2/query/jobs/:source/:job_id/artifacts/scrape` → `ArtifactListPayload`

---

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/runtime/ui/views.md`.