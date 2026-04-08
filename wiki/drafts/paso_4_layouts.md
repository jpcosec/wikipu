---
identity:
  node_id: "doc:wiki/drafts/paso_4_layouts.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/plan/01_ui/proposals/phase_0_foundation.md", relation_type: "documents"}
---

### `src/components/layouts/AppShell.tsx`

## Details

### `src/components/layouts/AppShell.tsx`

LeftNav fijo a la izquierda (w-14). Área de contenido scrolleable a la derecha.

```
┌─ LeftNav (w-14, fixed) ──┬─ main (flex-1) ───────────┐
│  [P2]                    │                            │
│  [icon] Portfolio        │   <Outlet />               │
│  [icon] Explorer         │   (PortfolioDashboard,     │
│  [icon] CV               │    DataExplorer, o         │
│                          │    JobWorkspaceShell)       │
│  ── bottom ──            │                            │
│  [icon] Sandbox          │                            │
└──────────────────────────┴────────────────────────────┘
```

```tsx
import { Outlet, NavLink } from 'react-router-dom';
import { LayoutDashboard, FolderOpen, Network, FlaskConical } from 'lucide-react';
import { cn } from '../../utils/cn';

const NAV_ITEMS = [
  { to: '/',        icon: LayoutDashboard, label: 'Portfolio', end: true },
  { to: '/explorer', icon: FolderOpen,     label: 'Explorer',  end: false },
  { to: '/cv',      icon: Network,         label: 'Base CV',   end: false },
];

export function AppShell() {
  return (
    <div className="flex min-h-screen bg-background">
      <nav className="fixed left-0 top-0 h-full w-14 bg-surface flex flex-col items-center py-4 gap-2 border-r border-outline/10 z-50">
        <div className="w-7 h-7 mb-4 border border-primary/40 flex items-center justify-center">
          <span className="text-primary font-mono text-[10px] font-bold">P2</span>
        </div>

        {NAV_ITEMS.map(({ to, icon: Icon, label, end }) => (
          <NavLink
            key={to}
            to={to}
            end={end}
            className={({ isActive }) =>
              cn(
                'w-10 h-10 flex items-center justify-center transition-colors group relative',
                isActive ? 'text-primary tactical-glow' : 'text-on-muted hover:text-on-surface',
              )
            }
          >
            <Icon size={18} />
            <span className="absolute left-full ml-2 px-2 py-1 bg-surface-high text-on-surface text-[10px] font-mono uppercase tracking-widest opacity-0 group-hover:opacity-100 transition-opacity whitespace-nowrap pointer-events-none z-50">
              {label}
            </span>
          </NavLink>
        ))}

        <div className="mt-auto">
          <NavLink
            to="/sandbox/intelligent_editor"
            className="w-10 h-10 flex items-center justify-center text-on-muted hover:text-secondary transition-colors"
          >
            <FlaskConical size={18} />
          </NavLink>
        </div>
      </nav>

      <main className="ml-14 flex-1 min-h-screen">
        <Outlet />
      </main>
    </div>
  );
}
```

---

### `src/components/layouts/JobWorkspaceShell.tsx`

Se renderiza dentro del `<main>` de AppShell. Añade el Pipeline TopBar secundario
con las etapas del job. El `<Outlet>` escupe la vista específica (B0–B4).

```
┌─ Pipeline TopBar ──────────────────────────────────────────────────┐
│  tu_berlin / 201397     FLOW · SCRAPE · [EXTRACT] · MATCH · SCULPT │
├────────────────────────────────────────────────────────────────────┤
│  <Outlet />                                                         │
│  (JobFlowInspector, ScrapeDiagnostics, ExtractUnderstand...)        │
└────────────────────────────────────────────────────────────────────┘
```

```tsx
import { Outlet, useParams, NavLink } from 'react-router-dom';
import { ChevronRight } from 'lucide-react';
import { cn } from '../../utils/cn';

const PIPELINE_STEPS = [
  { label: 'Flow',    path: '' },
  { label: 'Scrape',  path: 'scrape' },
  { label: 'Extract', path: 'extract' },
  { label: 'Match',   path: 'match' },
  { label: 'Sculpt',  path: 'sculpt' },
];

export function JobWorkspaceShell() {
  const { source, jobId } = useParams();
  const base = `/jobs/${source}/${jobId}`;

  return (
    <div className="flex flex-col min-h-full">
      <header className="h-10 flex items-center justify-between px-4 border-b border-outline/10 bg-surface shrink-0">
        {/* Breadcrumb */}
        <div className="flex items-center gap-2 text-[11px] font-mono text-on-muted">
          <NavLink to="/" className="hover:text-primary transition-colors">Portfolio</NavLink>
          <ChevronRight size={12} />
          <span>{source}</span>
          <ChevronRight size={12} />
          <span className="text-primary">{jobId}</span>
        </div>

        {/* Pipeline step nav */}
        <nav className="flex items-center gap-1">
          {PIPELINE_STEPS.map(({ label, path }) => (
            <NavLink
              key={path}
              to={path ? `${base}/${path}` : base}
              end={path === ''}
              className={({ isActive }) =>
                cn(
                  'px-3 py-1 text-[10px] font-mono uppercase tracking-widest transition-colors',
                  isActive
                    ? 'text-primary border-b border-primary'
                    : 'text-on-muted hover:text-on-surface',
                )
              }
            >
              {label}
            </NavLink>
          ))}
        </nav>
      </header>

      <main className="flex-1">
        <Outlet />
      </main>
    </div>
  );
}
```

---

Generated from `raw/docs_postulador_ui/plan/01_ui/proposals/phase_0_foundation.md`.