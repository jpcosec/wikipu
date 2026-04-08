---
identity:
  node_id: "doc:wiki/drafts/b2_extract_understand_hitl_a.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/runtime/ui/views.md", relation_type: "documents"}
---

**Route:** `/jobs/:source/:jobId/extract`

## Details

**Route:** `/jobs/:source/:jobId/extract`
**Feature:** `features/job-pipeline/`
**Libraries:** `react-resizable-panels` · `@uiw/react-codemirror` · `@tanstack/react-query`

### Layout

```
┌── Source Text (50%) ─────────┬── Requirements (50%) ──────┬── Control Panel ──┐
│ [SOURCE_TEXT header]          │ [EXTRACTED_REQS header]    │ [PHASE: EXTRACT]  │
│                              │                            │                   │
│ Markdown con spans           │ RequirementItem:           │ [Technical tab]   │
│ resaltados al hover          │ [ID] [priority badge]      │ Selected req JSON │
│                              │ texto editable             │                   │
│                              │                            │ [Stage Actions]   │
│                              │ [+ Add Requirement]        │                   │
└──────────────────────────────┴────────────────────────────┴───────────────────┘
```

### Span Interaction
- Hover on `RequirementItem` → highlights spans in source: `bg-primary/20 border-x border-primary`
- Click highlighted span → selects corresponding requirement

### Priority Badge
```
must → bg-secondary/10 text-secondary [MUST]
nice → bg-outline/10 text-on-muted [NICE]
```

### API Contract

**Read:**
- `GET /api/v2/query/jobs/:source/:job_id/views/extract` → `ViewPayload<'extract'>`

**Write:**
- `PUT /api/v2/commands/jobs/:source/:job_id/state/extract_understand`

---

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/runtime/ui/views.md`.