---
identity:
  node_id: "doc:wiki/drafts/b5_package_deployment.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/runtime/ui/views.md", relation_type: "documents"}
---

**Route:** `/jobs/:source/:jobId/sculpt` (or `/deploy`)

## Details

**Route:** `/jobs/:source/:jobId/sculpt` (or `/deploy`)
**Feature:** `features/job-pipeline/`
**Libraries:** `@tanstack/react-query` · `lucide-react`

### Layout

```
┌──────── Main (max-w-3xl centrado) ─────────────────────────────┐
│  [MISSION_COMPLETE header — glow cyan]                         │
│  ┌── Mission Summary ─────────────────────────────────────┐   │
│  │ Job: Research Assistant – TU Berlin   Score: 0.85      │   │
│  │ Thread: tu_berlin_999001    Completed: 2026-03-10      │   │
│  └────────────────────────────────────────────────────────┘   │
│  ┌── Pipeline Checklist ──────────────────────────────────┐   │
│  │ [✓] SCRAPE         completed                           │   │
│  │ [✓] EXTRACT        completed                           │   │
│  │ ...                                                     │   │
│  └────────────────────────────────────────────────────────┘   │
│  ┌── Package Files ───────────────────────────────────────┐   │
│  │ [FileType] motivation_letter.pdf   84 KB  [download]   │   │
│  │ [DOWNLOAD ALL AS ZIP — COMING_SOON]                   │   │
│  └────────────────────────────────────────────────────────┘   │
│  [MARK AS DEPLOYED →]  (full-width CTA, bg-primary)         │
└───────────────────────────────────────────────────────────────┘
```

### Components
- `<MissionSummaryCard>` — Job metadata and score
- `<PipelineChecklist>` — All stages with ✓/✗ indicators
- `<PackageFileList>` — Files with icons, sizes, download buttons
- `<DeploymentCta>` — Full-width primary button

### API Contract

**Read:**
- `GET /api/v2/query/jobs/:source/:job_id/timeline` → `JobTimeline`
- `GET /api/v2/query/jobs/:source/:job_id/package/files` → `PackageFilesPayload`

**Write:**
- `POST /api/v2/commands/jobs/:source/:job_id/archive` — (future) mark as deployed

---

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/runtime/ui/views.md`.