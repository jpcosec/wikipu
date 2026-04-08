---
identity:
  node_id: "doc:wiki/drafts/layout_shells.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/runtime/ui/design_system.md", relation_type: "documents"}
---

### Global Shell

## Details

### Global Shell

```
┌─────────────────────────────────────────────────────┐
│  TopBar h-14  [PHD_OS // INTEL_REVIEW]  [nav icons] │
├──────────┬──────────────────────────┬───────────────┤
│ LeftNav  │   Main Canvas            │  RightPanel   │
│  w-64    │   (flex-1)               │  w-80         │
│          │                          │  (contextual) │
│ Portfolio│                          │               │
│ Evidence │                          │               │
│ Sandbox  │                          │               │
│ Settings │                          │               │
└──────────┴──────────────────────────┴───────────────┘
│  StatusBar h-10  (pipeline stage progress)          │
└─────────────────────────────────────────────────────┘
```

- **LeftNav**: `bg-[#0c0e10]/95`, `border-r border-primary/10`
- **TopBar**: `bg-[#0c0e10]`, `border-b border-primary/10`, logo + pipeline nav + icons
- **RightPanel**: contextual per view — amber header in HITL, cyan in monitoring
- **StatusBar**: visible only in job views, shows stage progress

### Pipeline Nav (secondary TopBar in Job views)

```
SCRAPE → EXTRACT → MATCH → REVIEW → GENERATE → PACKAGE
```

- Active stage: `text-primary border-b-2 border-primary shadow-[0_4px_12px_rgba(0,242,255,0.2)]`
- Inactive stages: `text-slate-500 hover:text-primary/70`
- Font: `font-headline uppercase tracking-widest text-xs`

---

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/runtime/ui/design_system.md`.