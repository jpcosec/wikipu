---
identity:
  node_id: "doc:wiki/drafts/component_variants.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/runtime/ui/design_system.md", relation_type: "documents"}
---

### Status Badge

## Details

### Status Badge

```
[MISSION_CRITICAL]  — bg-secondary/10 text-secondary border border-secondary/30
[VERIFIED]          — bg-primary/10 text-primary border border-primary/30
[PENDING]           — bg-outline/10 text-outline border border-outline/30
[GAP_DETECTED]      — bg-error-container/20 text-error border border-error/30
```

### Pipeline Progress Bar (segmented)

```
[■][■][■][□][□]   — each segment: h-1.5 w-6
Filled: bg-primary shadow-[0_0_4px_rgba(0,242,255,0.4)]
Empty: bg-surface-container border border-outline-variant/30
```

### Evidence Card (draggable)

```
┌─ ID: EV-8892  [drag_indicator] ─┐
│  Título del proyecto             │
│  [TAG_1] [TAG_2]                 │
│ ● terminal port (left edge)       │
└──────────────────────────────────┘
bg-surface-container-high border border-primary/10
hover: border-primary/40
```

---

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/runtime/ui/design_system.md`.