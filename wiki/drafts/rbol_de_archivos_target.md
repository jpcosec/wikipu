---
identity:
  node_id: "doc:wiki/drafts/rbol_de_archivos_target.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/plan/01_ui/specs/00_component_map.md", relation_type: "documents"}
---

> Fuente de verdad: `00_architecture.md`. Este árbol replica la estructura canónica.

## Details

> Fuente de verdad: `00_architecture.md`. Este árbol replica la estructura canónica.

```
src/
  components/                  # UI global (Diseño Atómico puro)
    atoms/
      Button.tsx
      Badge.tsx
      Tag.tsx
      Icon.tsx
      Spinner.tsx
      Kbd.tsx
    molecules/
      SplitPane.tsx            # wrapper de react-resizable-panels
      DiagnosticCard.tsx
      ControlPanel.tsx
    organisms/
      IntelligentEditor.tsx    ✅ implementado
      GraphCanvas.tsx          ✅ implementado
      FileTree.tsx            ✅ implementado
    layouts/
      AppShell.tsx             # LeftNav + <Outlet />
      JobWorkspaceShell.tsx    # Pipeline TopBar + <Outlet />
  features/                    # Lógica de negocio (Feature-Sliced)
    portfolio/
      api/usePortfolioSummary.ts
      components/PortfolioTable.tsx, DeadlineSidebar.tsx
    job-pipeline/
      api/useJobTimeline.ts, useViewOne.ts, useViewTwo.ts, useViewThree.ts, ...
      components/RequirementList.tsx, EvidenceBankPanel.tsx, MatchControlPanel.tsx, ...
    base-cv/
      api/useCvProfileGraph.ts
      components/CvGraphEditor.tsx
  pages/
    global/
      PortfolioDashboard.tsx   (A1)
      DataExplorer.tsx         (A2)
      BaseCvEditor.tsx         (A3)
    job/
      JobFlowInspector.tsx     (B0)
      ScrapeDiagnostics.tsx    (B1)
      ExtractUnderstand.tsx    (B2)
      Match.tsx                (B3)
      GenerateDocuments.tsx    (B4)
      PackageDeployment.tsx    (B5)
  types/
    api.types.ts               # PortfolioSummary, ViewOnePayload, GraphNode...
    ui.types.ts                # ReactFlow, DnD, editor state
  utils/
    cn.ts                      # clsx + tailwind-merge
  api/                         # client real (fetch wrapper)
  mock/                        # client mock + fixtures
  sandbox/
    components/IntelligentEditor.tsx   ← prototipo actual
    pages/IntelligentEditorPage.tsx
```

---

Generated from `raw/docs_postulador_ui/plan/01_ui/specs/00_component_map.md`.