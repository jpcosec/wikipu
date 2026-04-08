---
identity:
  node_id: "doc:wiki/drafts/paso_3_router_con_createbrowserrouter.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/plan/01_ui/proposals/phase_0_foundation.md", relation_type: "documents"}
---

### `src/App.tsx`

## Details

### `src/App.tsx`

`JobWorkspaceShell` se anida dentro de `AppShell` — el LeftNav siempre renderiza,
nunca se duplica, nunca parpadea al navegar entre vistas.

```tsx
import { createBrowserRouter, RouterProvider } from 'react-router-dom';
import { AppShell } from './components/layouts/AppShell';
import { JobWorkspaceShell } from './components/layouts/JobWorkspaceShell';
import { PortfolioDashboard } from './pages/global/PortfolioDashboard';
import { DataExplorer } from './pages/global/DataExplorer';
import { BaseCvEditor } from './pages/global/BaseCvEditor';
import { JobFlowInspector } from './pages/job/JobFlowInspector';
import { ScrapeDiagnostics } from './pages/job/ScrapeDiagnostics';
import { ExtractUnderstand } from './pages/job/ExtractUnderstand';
import { Match } from './pages/job/Match';
import { GenerateDocuments } from './pages/job/GenerateDocuments';
import { PackageDeployment } from './pages/job/PackageDeployment';
import { IntelligentEditorPage } from './sandbox/pages/IntelligentEditorPage';

const router = createBrowserRouter([
  {
    path: '/',
    element: <AppShell />,          // LeftNav siempre visible
    children: [
      // Vistas globales
      { index: true,       element: <PortfolioDashboard /> },
      { path: 'explorer',  element: <DataExplorer /> },
      { path: 'cv',        element: <BaseCvEditor /> },

      // Job workspace — anidado, hereda el LeftNav de AppShell
      {
        path: 'jobs/:source/:jobId',
        element: <JobWorkspaceShell />,   // inyecta el Pipeline TopBar
        children: [
          { index: true,      element: <JobFlowInspector /> },  // B0
          { path: 'scrape',   element: <ScrapeDiagnostics /> }, // B1
          { path: 'extract',  element: <ExtractUnderstand /> }, // B2
          { path: 'match',    element: <Match /> },             // B3
          { path: 'sculpt',      element: <GenerateDocuments /> }, // B4
          { path: 'deployment', element: <PackageDeployment /> }, // B5
        ],
      },
    ],
  },
  // Sandbox — fuera del AppShell, sin LeftNav
  { path: '/sandbox/intelligent_editor', element: <IntelligentEditorPage /> },
]);

export default function App() {
  return <RouterProvider router={router} />;
}
```

**Árbol de rutas:**
```
/                        → PortfolioDashboard  (A1)
/explorer                → DataExplorer         (A2)
/cv                      → BaseCvEditor         (A3)
/jobs/:source/:jobId     → JobFlowInspector     (B0)
/jobs/:source/:jobId/scrape   → ScrapeDiagnostics   (B1)
/jobs/:source/:jobId/extract  → ExtractUnderstand   (B2)
/jobs/:source/:jobId/match    → Match               (B3)
/jobs/:source/:jobId/sculpt      → GenerateDocuments   (B4)
/jobs/:source/:jobId/deployment → PackageDeployment    (B5)
/sandbox/intelligent_editor      → IntelligentEditorPage (sin shell)
```

---

Generated from `raw/docs_postulador_ui/plan/01_ui/proposals/phase_0_foundation.md`.