---
identity:
  node_id: "doc:wiki/drafts/a3_base_cv_editor.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/runtime/ui/views.md", relation_type: "documents"}
---

**Route:** `/cv`

## Details

**Route:** `/cv`
**Feature:** `features/base-cv/`
**Libraries:** `@xyflow/react` · `dagre` · `@tanstack/react-query`

### Layout

```
┌─ LeftNav ─┬──── ReactFlow Canvas (flex-1) ────────┬── Inspector (w-80) ──┐
│           │  [dot-grid] [scanline]                │ Si nodo seleccionado:│
│           │                                        │   campos editables   │
│           │  [CvEntry nodes] → [CvSkill nodes]   │                      │
│           │  [color por category]                  │ Sin selección:       │
│           │                                        │   ProfileStats       │
└───────────┴────────────────────────────────────────┴──────────────────────┘
```

### Node Types

**CvEntry node:**
```
┌─ [category badge] ─────── [essential ●] ─┐
│  título / institución / fecha             │
│  descripción breve — 1 línea               │
│  ID: P_EXP_005  (mono xs)                │
└───────────────────────────────────────────┘
border color: experience→cyan, education→outline, publication→amber, language→salmon
```

**CvSkill node:**
```
┌─ [label] ── [level badge] ─┐
│  ID: P_SKL_021  [category] │
└────────────────────────────┘
```

### API Contract

**Read:**
- `GET /api/v1/portfolio/cv-profile-graph` → `CvProfileGraphPayload`

**Write:**
- `PUT /api/v1/portfolio/cv-profile-graph` → same payload

---

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/runtime/ui/views.md`.