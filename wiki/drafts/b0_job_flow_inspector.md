---
identity:
  node_id: "doc:wiki/drafts/b0_job_flow_inspector.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/runtime/ui/views.md", relation_type: "documents"}
---

**Route:** `/jobs/:source/:jobId`

## Details

**Route:** `/jobs/:source/:jobId`
**Feature:** `features/job-pipeline/`
**Libraries:** `@tanstack/react-query` · `lucide-react`

### Layout

```
┌─────────────── Main (max-w-2xl mx-auto) ───────────────┐
│  [Job header: título + institución + status badge]       │
│  [HitlCtaBanner — solo si pending_hitl]                │
│  [PipelineTimeline vertical]                            │
│  ● SCRAPE ────── completed ── [artifact link]         │
│  ● EXTRACT ───── completed ── [artifact link]         │
│  ◉ MATCH ─────── pending_hitl ── [→ GO TO REVIEW]    │
│  ○ GENERATE ───── pending                              │
│  ○ RENDER ──────── pending                             │
│  ○ PACKAGE ─────── pending                             │
│  [JobMetaPanel: match score, deadline, thread_id]      │
└─────────────────────────────────────────────────────────┘
```

### Stage Dot Colors
```
completed     → ● text-primary
pending_hitl → ◉ text-secondary animate-pulse
running       → ● text-secondary
failed        → ● text-error
pending       → ○ text-on-muted border border-outline
```

### API Contract

**Read:**
- `GET /api/v2/query/jobs/:source/:job_id/timeline` → `JobTimeline`

```ts
{
  source, job_id, thread_id, current_node,
  status: 'running' | 'pending_hitl' | 'completed' | 'failed' | 'archived',
  stages: { name, status, artifact_ref, updated_at }[],
  artifacts: Record<string, string>
}
```

---

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/runtime/ui/views.md`.