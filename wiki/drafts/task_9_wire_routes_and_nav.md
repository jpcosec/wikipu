---
identity:
  node_id: "doc:wiki/drafts/task_9_wire_routes_and_nav.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/docs/superpowers/plans/2026-03-24-schema-explorer.md", relation_type: "documents"}
---

**Files:**

## Details

**Files:**
- Modify: `apps/review-workbench/src/App.tsx`
- Modify: `apps/review-workbench/src/components/layouts/AppShell.tsx`

- [ ] **Step 1: Add route to `App.tsx`**

Add import:
```ts
import { SchemaExplorer } from './pages/global/SchemaExplorer';
```

Add to the `children` array inside the root route:
```ts
{ path: 'schema', element: <SchemaExplorer /> },
```

- [ ] **Step 2: Add nav item to `AppShell.tsx`**

Add import:
```ts
import { LayoutDashboard, FolderOpen, Network, GitGraph, Layers } from 'lucide-react';
```

Add to `NAV_ITEMS`:
```ts
{ to: '/schema', icon: Layers, label: 'Schema', end: false },
```

- [ ] **Step 3: Open dev server and verify end-to-end**

```bash
cd apps/review-workbench && npm run dev
```

Check:
- `/schema` loads without errors
- CV pill shows the graph with nodes
- Job/Match pills show the stub placeholder
- Node click opens inspector with field list
- No edit panel, no save button visible
- `/cv` still works (not broken by readOnly change)

- [ ] **Step 4: Commit**

```bash
git add apps/review-workbench/src/App.tsx apps/review-workbench/src/components/layouts/AppShell.tsx
git commit -m "feat(schema-explorer): wire /schema route and nav"
```

> **End-to-end checklist (do this after committing):**
> - `/schema` loads — CV graph shows nodes with category colors (not all grey)
> - Job/Match show placeholder text
> - Colour legend visible in header
> - Clicking a node shows its `attributes` in the inspector panel (field name + type + required)
> - No save button, no discard, no undo visible
> - Drag-to-connect disabled (cannot draw edges)
> - `/cv` editor still works normally (not regressed by readOnly change)

Generated from `raw/docs_postulador_ui/docs/superpowers/plans/2026-03-24-schema-explorer.md`.