---
identity:
  node_id: "doc:wiki/drafts/global_components_shared.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/runtime/ui/views.md", relation_type: "documents"}
---

### Layout Shells

## Details

### Layout Shells

| Shell | Used By | Purpose |
|-------|---------|---------|
| `<AppShell>` | A1, A2, A3 | LeftNav + `<Outlet />` |
| `<JobWorkspaceShell>` | B0-B5 | Pipeline TopBar + nested `<Outlet />` |

### Shared Atoms

| Atom | Used In |
|------|---------|
| `<Badge>` | A1, A2, A3, B0, B1, B2, B3 |
| `<Button>` | A1, B0, B1, B2, B3, B4, B5 |
| `<Tag>` | A3, B2 |
| `<Icon>` | All views |
| `<Spinner>` | All views (loading states) |
| `<Kbd>` | A3, B2, B3, B4 |

### Shared Molecules

| Molecule | Used In |
|----------|---------|
| `<SplitPane>` | A2, B2, B3, B4 |

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/runtime/ui/views.md`.