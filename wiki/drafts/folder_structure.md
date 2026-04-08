---
identity:
  node_id: "doc:wiki/drafts/folder_structure.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/runtime/ui/architecture.md", relation_type: "documents"}
---

```

## Details

```
src/
├── api/                          # Network layer (pure fetch, React-agnostic)
│   ├── client.ts                 # Fetch wrapper (interceptors, auth)
│   └── endpoints.ts              # URL definitions (/api/v1/jobs...)
│
├── components/                   # Global UI (Atomic Design, zero business logic)
│   ├── atoms/                    # Button.tsx, Badge.tsx, Tag.tsx, Spinner.tsx, Kbd.tsx, Icon.tsx
│   ├── molecules/                # SplitPane.tsx, ControlPanel.tsx, DiagnosticCard.tsx
│   ├── organisms/                # IntelligentEditor.tsx, GraphCanvas.tsx, FileTree.tsx
│   └── layouts/                  # AppShell.tsx, JobWorkspaceShell.tsx
│
├── features/                     # Business logic (Feature-Sliced)
│   ├── portfolio/                # A1 — Portfolio Dashboard
│   │   ├── api/                 # usePortfolioSummary.ts
│   │   └── components/          # PortfolioTable.tsx, DeadlineSidebar.tsx
│   │
│   ├── explorer/                 # A2 — Data Explorer
│   │   ├── api/                 # useExplorerBrowse.ts
│   │   └── components/          # ExplorerTree.tsx, FilePreview.tsx
│   │
│   ├── base-cv/                 # A3 — Base CV Editor
│   │   ├── api/                 # useCvProfileGraph.ts
│   │   └── components/         # CvGraphCanvas.tsx, NodeInspector.tsx
│   │
│   └── job-pipeline/             # B0–B5 — Job workflow views
│       ├── api/                 # useJobTimeline.ts, useViewExtract.ts, useViewMatch.ts
│       └── components/         # MatchGraphCanvas.tsx, RequirementList.tsx, EvidenceBankPanel.tsx
│
├── pages/                        # Route entry points (dumb by design)
│   ├── global/                  # PortfolioDashboard.tsx, DataExplorer.tsx, BaseCvEditor.tsx
│   └── job/                    # JobFlowInspector.tsx, ScrapeDiagnostics.tsx, ExtractUnderstand.tsx, Match.tsx, GenerateDocuments.tsx, PackageDeployment.tsx
│
├── types/                        # TypeScript contracts (aligned with backend)
│   ├── api.types.ts             # PortfolioSummary, GraphNode, ViewPayload...
│   └── ui.types.ts              # ReactFlow, DnD, editor state
│
├── utils/                        # Global helpers
│   ├── cn.ts                    # clsx + tailwind-merge
│   └── formatters.ts           # dates, bytes→MB, stage duration
│
├── mock/                         # Mock API layer (VITE_MOCK toggle)
│   ├── client.ts                # Mock fetch implementation
│   └── fixtures/                # Mock data fixtures
│
├── App.tsx                      # Router (createBrowserRouter)
├── main.tsx                     # Entry point (QueryClient, Theme providers)
└── styles.css                   # Tailwind @theme + utilities
```

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/runtime/ui/architecture.md`.