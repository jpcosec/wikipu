---
identity:
  node_id: "doc:wiki/drafts/4_layout_shell.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/plan/01_ui/proposals/component_templates.md", relation_type: "documents"}
---

AppShell, JobWorkspaceShell, SplitPane.

## Details

AppShell, JobWorkspaceShell, SplitPane.

**Reglas:**
- Sin conocimiento de datos de negocio
- Su trabajo: Grid/Flexbox + `<Outlet />` o `children`
- Pueden recibir slots nombrados (`leftPanel`, `rightPanel`) para composición flexible

```tsx
import { cn } from '@/utils/cn';

export interface ShellNameProps {
  children?: React.ReactNode;
  leftPanel?: React.ReactNode;
  className?: string;
}

export function ShellName({ children, leftPanel, className }: ShellNameProps) {
  return (
    <div className={cn('flex h-screen w-full bg-background text-on-surface overflow-hidden', className)}>

      {leftPanel && (
        <aside className="w-64 shrink-0 border-r border-outline/10 bg-surface z-10">
          {leftPanel}
        </aside>
      )}

      <main className="flex-1 relative flex flex-col min-w-0 overflow-y-auto">
        {children}
      </main>

    </div>
  );
}
```

---

Generated from `raw/docs_postulador_ui/plan/01_ui/proposals/component_templates.md`.