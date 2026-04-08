---
identity:
  node_id: "doc:wiki/drafts/rbol_de_carpetas_target.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/plan/01_ui/specs/00_architecture.md", relation_type: "documents"}
---

```

## Details

```
src/
├── api/                        # Capa de red pura (agnóstica a React)
│   ├── client.ts               # Wrapper de fetch (interceptors, auth)
│   └── endpoints.ts            # Definición de URLs (/api/v1/jobs...)
│
├── components/                 # UI global (Diseño Atómico puro, sin lógica de negocio)
│   ├── atoms/                  # Button.tsx, Badge.tsx, Tag.tsx, Spinner.tsx, Kbd.tsx
│   ├── molecules/              # SplitPane.tsx, ControlPanel.tsx, DiagnosticCard.tsx
│   ├── organisms/              # IntelligentEditor.tsx, GraphCanvas.tsx, FileTree.tsx
│   └── layouts/                # AppShell.tsx, JobWorkspaceShell.tsx
│
├── features/                   # Lógica de negocio (el corazón de la app)
│   ├── portfolio/              # A1 — Portfolio Dashboard
│   │   ├── api/                # usePortfolioSummary.ts
│   │   └── components/        # PortfolioTable.tsx, ProgressSegmented.tsx
│   │
│   ├── base-cv/                # A3 — Base CV Editor
│   │   ├── api/                # useCvProfileGraph.ts
│   │   └── components/        # NodeInspectorSidebar.tsx
│   │
│   └── job-pipeline/           # B0–B4 — El flujo del job
│       ├── api/                # useJobTimeline.ts, useExtractState.ts, useMatchState.ts
│       ├── components/         # HitlCtaBanner.tsx, RequirementList.tsx, EvidenceBankSidebar.tsx
│       └── utils/              # helpers de matching, scoring, diff
│
├── pages/                      # Puntos de entrada (rutas) — tontas por diseño
│   ├── global/                 # PortfolioPage.tsx, DataExplorerPage.tsx, CvEditorPage.tsx
│   └── job/                    # JobFlowPage.tsx, ExtractPage.tsx, MatchPage.tsx, DocumentsPage.tsx
│
├── types/                      # Contratos TypeScript (idénticos al backend)
│   ├── api.types.ts            # PortfolioSummary, GraphNode, ViewOnePayload...
│   └── ui.types.ts             # tipos internos de ReactFlow, DnD, editor state
│
├── utils/                      # Helpers globales
│   ├── cn.ts                   # clsx + tailwind-merge
│   └── formatters.ts           # fechas, bytes→MB, duración de stages
│
├── App.tsx                     # Router (createBrowserRouter)
├── main.tsx                    # Entry point — Providers: QueryClient, Theme
└── styles.css                  # Tailwind @theme + utilities
```

---

Generated from `raw/docs_postulador_ui/plan/01_ui/specs/00_architecture.md`.