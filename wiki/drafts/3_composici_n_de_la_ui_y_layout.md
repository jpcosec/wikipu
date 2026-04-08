---
identity:
  node_id: "doc:wiki/drafts/3_composici_n_de_la_ui_y_layout.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/plan/01_ui/specs/A1_portfolio_dashboard.md", relation_type: "documents"}
---

**Layout:** 12-col grid — `col-span-9` main + `col-span-3` sidebar derecho.

## Details

**Layout:** 12-col grid — `col-span-9` main + `col-span-3` sidebar derecho.

```
┌──────────────── col-9 ─────────────────┬── col-3 ──┐
│  [Search bar + filtros]                │ Deadline  │
│  [Recent Artifacts — 3 cards inline]  │ Sensors   │
│  [Active Application Missions — tabla] │           │
│                                        │ System    │
│                                        │ Status    │
└────────────────────────────────────────┴───────────┘
│  FAB: "Initiate New Application Sequence" (fixed bottom-right) │
```

**Componentes Core:**
- `<PortfolioTable>` — tabla sticky header, filas clickeables, pipeline progress bar segmentado
- `<DeadlineSidebar>` — lista de deadlines con color coding urgency (error/amber/outline)
- `<RecentArtifacts>` — 3 cards de acceso rápido (CV, Cover Letter, JSON)
- `<SystemStatus>` — dot pulsando + uptime (decorativo, bottom del sidebar)

**Columnas de la tabla:**
```
Job_Title | Institution | Source | Pipeline_Stage (progress bar) | Status (badge)
```

**Pipeline_Stage progress bar** — 8 segmentos: scrape, translate, extract, match, review, generate, render, package. Segmentos llenos = completados.

---

Generated from `raw/docs_postulador_ui/plan/01_ui/specs/A1_portfolio_dashboard.md`.