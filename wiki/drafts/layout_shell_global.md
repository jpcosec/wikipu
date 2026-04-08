---
identity:
  node_id: "doc:wiki/drafts/layout_shell_global.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/plan/01_ui/specs/00_design_system.md", relation_type: "documents"}
---

```

## Details

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

- **LeftNav**: siempre visible, `bg-[#0c0e10]/95`, `border-r border-primary/10`
- **TopBar**: `bg-[#0c0e10]`, `border-b border-primary/10`, logo + pipeline nav + icons
- **RightPanel**: contextual por vista — amber header en HITL, cyan en monitoreo
- **StatusBar**: solo visible en vistas de pipeline job, muestra progreso de etapas

---

Generated from `raw/docs_postulador_ui/plan/01_ui/specs/00_design_system.md`.