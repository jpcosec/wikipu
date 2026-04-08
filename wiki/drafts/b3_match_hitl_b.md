---
identity:
  node_id: "doc:wiki/drafts/b3_match_hitl_b.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/runtime/ui/views.md", relation_type: "documents"}
---

**Route:** `/jobs/:source/:jobId/match`

## Details

**Route:** `/jobs/:source/:jobId/match`
**Feature:** `features/job-pipeline/`
**Libraries:** `@xyflow/react` · `dagre` · `@dnd-kit/core` · `@tanstack/react-query`

### Layout

```
┌── Evidence Bank ──┬──── Match Graph (flex-1) ────┬── Control Panel ──┐
│ [ASSETS_REPO]     │  [dot-grid] [scanline]       │ [PHASE: MATCH]  │
│                   │                               │                  │
│ Evidence cards    │  Requirement nodes (left)     │ Si selección:    │
│ (draggables):     │  Profile nodes (right)       │   JSON readout   │
│ [P_EXP_006]      │  Edges: score badge midpoint  │                  │
│  EEG Detection   │                               │ [COMMIT MATCH]   │
│  [⋮ drag]        │                               │ [REQUEST REGEN]  │
└──────────────────┴──────────────────────────────┴──────────────────┘
```

### Node Types

**RequirementNode:**
```
┌─ [priority badge] ──── [status icon] ─[port]─┐
│  label (requirement text)                     │
│  score: ████░░ (progress bar)                │
│  UNRESOLVED / RESOLVED / GAP                  │
└───────────────────────────────────────────────┘
border-left: score≥0.7→cyan, 0.3-0.6→amber, <0.3→salmon
```

**ProfileNode:**
```
┌─ [ID] ──── [●port] ─┐
│  título corto        │
│  [category badge]    │
└──────────────────────┘
```

### Edge Types
- LLM match: `stroke=#00f2ff` dashed animated, score badge midpoint
- Manual (operator): `stroke=#fecb00` dashed

### API Contract

**Read:**
- `GET /api/v2/query/jobs/:source/:job_id/views/match` → `ViewPayload<'match'>`
- `GET /api/v2/query/jobs/:source/:job_id/evidence-bank` → `EvidenceBankPayload`

**Write:**
- `PUT /api/v2/commands/jobs/:source/:job_id/state/match` — saves graph corrections
- `POST /api/v2/commands/jobs/:source/:job_id/gates/review_match/decide` — approve/regen/reject

---

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/runtime/ui/views.md`.