---
identity:
  node_id: "doc:wiki/drafts/special_effects.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/runtime/ui/design_system.md", relation_type: "documents"}
---

### Scanline Overlay (CRT effect)

## Details

### Scanline Overlay (CRT effect)

```css
.scanline-overlay {
  background:
    linear-gradient(rgba(18,16,16,0) 50%, rgba(0,0,0,0.25) 50%),
    linear-gradient(90deg, rgba(255,0,0,0.03), rgba(0,255,0,0.01), rgba(0,0,255,0.03));
  background-size: 100% 2px, 3px 100%;
  pointer-events: none;
  opacity: 0.2;
}
```

### Tactical Glow (cyan — active elements)

```css
.tactical-glow {
  box-shadow: 0 0 15px rgba(0, 242, 255, 0.15);
}
```

### Alert Glow (amber — deadlines, warnings)

```css
.alert-glow {
  box-shadow: 0 0 15px rgba(255, 170, 0, 0.15);
}
```

### Panel Border

```css
.panel-border {
  border: 1px solid rgba(132, 148, 149, 0.2);
}
```

### Dot-Grid Background (graph canvas)

```css
.node-connector {
  background-image: radial-gradient(circle, rgba(0,242,255,0.08) 1px, transparent 1px);
  background-size: 24px 24px;
}
```

### Edge Pulse (SVG animated)

```css
@keyframes pulse-flow {
  0%   { stroke-dashoffset: 100; opacity: 0.4; }
  50%  { opacity: 1; }
  100% { stroke-dashoffset: 0; opacity: 0.4; }
}
.edge-pulse { animation: pulse-flow 3s linear infinite; }
```

---

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/runtime/ui/design_system.md`.