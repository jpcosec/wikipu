---
identity:
  node_id: "doc:wiki/drafts/componentes_at_micos.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/plan/01_ui/specs/00_design_system.md", relation_type: "documents"}
---

### Badge de estado

## Details

### Badge de estado
```
[MISSION_CRITICAL]  — bg-secondary/10 text-secondary border border-secondary/30
[VERIFIED]          — bg-primary/10 text-primary border border-primary/30
[PENDING]           — bg-outline/10 text-outline border border-outline/30
[GAP_DETECTED]      — bg-error-container/20 text-error border border-error/30
```

### Pipeline progress bar (segmentado)
```
[■][■][■][□][□]   — cada segmento es h-1.5 w-6
Lleno: bg-primary shadow-[0_0_4px_rgba(0,242,255,0.4)]
Vacío: bg-surface-container border border-outline-variant/30
```

### Evidence card (draggable)
```
┌─ ID: EV-8892  [drag_indicator] ─┐
│  Título del proyecto             │
│  [TAG_1] [TAG_2]                 │
│ ● terminal port (left edge)      │
└──────────────────────────────────┘
bg-surface-container-high border border-primary/10
hover: border-primary/40
```

### Scrollbar custom
```css
::-webkit-scrollbar { width: 4px; }
::-webkit-scrollbar-thumb { background: rgba(0,242,255,0.2); }
::-webkit-scrollbar-thumb:hover { background: rgba(0,242,255,0.4); }
```

Generated from `raw/docs_postulador_ui/plan/01_ui/specs/00_design_system.md`.