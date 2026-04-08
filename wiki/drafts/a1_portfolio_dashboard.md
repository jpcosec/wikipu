---
identity:
  node_id: "doc:wiki/drafts/a1_portfolio_dashboard.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/runtime/ui/views.md", relation_type: "documents"}
---

**Route:** `/`

## Details

**Route:** `/`
**Feature:** `features/portfolio/`
**Libraries:** `@tanstack/react-query` · `react-router-dom`

### Layout

```
┌──────────────── col-9 ─────────────────┬── col-3 ──┐
│  [Search bar + filtros]                  │ Deadline  │
│  [Recent Artifacts — 3 cards inline]  │ Sensors   │
│  [Active Application Missions — tabla] │           │
│                                        │ System    │
│                                        │ Status    │
└────────────────────────────────────────┴───────────┘
│  FAB: "Initiate New Application Sequence" (fixed bottom-right) │
```

### Components
- `<PortfolioTable>` — Sticky header, clickable rows, segmented pipeline progress bar
- `<DeadlineSidebar>` — Color-coded urgency (error/amber/outline)
- `<RecentArtifacts>` — 3 quick-access cards (CV, Cover Letter, JSON)
- `<SystemStatus>` — Pulsing dot + uptime (decorative)

### API Contract

**Read:**
- `GET /api/v2/query/portfolio/summary` → `PortfolioSummary`

```ts
{
  totals: { jobs, completed, pending_hitl, running, failed, archived },
  jobs: JobListItem[]
}
```

---

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/runtime/ui/views.md`.