# Piece: Missing shadcn/ui Components

**Source:** `node-editor` branch (`src/components/ui/`)

---

## Where it goes

```
apps/review-workbench/src/components/ui/
  accordion.tsx
  alert-dialog.tsx
  command.tsx
  context-menu.tsx
  dialog.tsx
  dropdown-menu.tsx
  input.tsx
  popover.tsx
  scroll-area.tsx
  select.tsx
  sheet.tsx
  skeleton.tsx
  sonner.tsx
  tabs.tsx
  textarea.tsx
```

These are standard shadcn/ui components generated via `npx shadcn@latest add <name>`.

---

## What does it solve

Several pieces in this looting plan require shadcn components that are not currently
installed in `ui-redesign`:

| Component | Required by |
|---|---|
| `context-menu` | `NodeShell` (right-click menu) |
| `sheet` | `NodeInspector`, `EdgeInspector` (slide-over panel) |
| `command` | `CommandMenu` in `GraphEditor` |
| `dialog` | `DeleteConfirm`, `MatchDecisionModal` |
| `dropdown-menu` | `CanvasSidebar` actions |
| `input` | `NodeInspector` form fields |
| `textarea` | `NodeInspector` multi-line fields |
| `tabs` | `CanvasSidebar` sections |
| `select` | `NodeInspector` relation type selector |
| `scroll-area` | `CanvasSidebar`, `NodeInspector` long property lists |
| `popover` | `FiltersSection` in sidebar |
| `accordion` | `FiltersSection`, `CreationSection` |
| `skeleton` | Loading states in inspector panels |
| `sonner` | Toast notifications (delete confirmation, save success) |
| `alert-dialog` | Not currently needed but `DeleteConfirm` uses `dialog` |

---

## How we have it implemented

`src/components/ui/` currently contains only: `button.tsx` (from the node-editor branch).
Custom atoms (`Badge`, `Tag`, `Kbd`, `Spinner`, `Icon`) exist in `components/atoms/`
but are hand-rolled Tailwind components, not shadcn primitives.

---

## What will it affect (collateral modifications)

- `tailwind.config.js` — shadcn requires `darkMode: 'class'` and the `cn` utility.
  Our `tailwind.config.js` already has both.
- `components.json` — shadcn project config must be present. node-editor has it at
  `apps/review-workbench/components.json` — copy and adapt the `aliases` section to
  match our `tsconfig` paths (`@/` → `src/`).
- `lib/utils.ts` — shadcn expects `cn()` exported from `@/lib/utils`. We currently
  export it from `utils/cn.ts`. Either add a re-export or update `components.json`.

---

## Concrete code pieces + source

### Install commands (run from `apps/review-workbench/`)

```bash
npx shadcn@latest add context-menu
npx shadcn@latest add sheet
npx shadcn@latest add command
npx shadcn@latest add dialog
npx shadcn@latest add dropdown-menu
npx shadcn@latest add input textarea select
npx shadcn@latest add tabs scroll-area popover accordion
npx shadcn@latest add skeleton
npx shadcn@latest add sonner
```

### Or copy from node-editor branch directly

```bash
git show node-editor:apps/review-workbench/src/components/ui/sheet.tsx > src/components/ui/sheet.tsx
# repeat for each component
```

Copying is acceptable since these are generated files — they do not evolve unless
shadcn releases a breaking change.

**Full source:** `node-editor:apps/review-workbench/src/components/ui/`
`node-editor:apps/review-workbench/components.json`
