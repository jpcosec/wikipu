---
identity:
  node_id: "doc:wiki/drafts/pipeline_outputs_view.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/docs/ui/ui_view_spec.md", relation_type: "documents"}
---

**Route**: `/jobs/:source/:jobId` + outputs tab

## Details

**Route**: `/jobs/:source/:jobId` + outputs tab
**Current component**: `PipelineOutputsView.tsx`
**Sample reference**: `document_generation.html` (document editing portion)

### What exists today

- File list for selected stage (JSON, Markdown, PNG)
- Read-only preview for non-editable files
- JSON editor (textarea) for extract_understand and match nodes
- Markdown editor for cv.md, motivation_letter.md, application_email.md
- Save to `nodes/<node>/proposed/state.json` or `proposed/*.md`
- PNG viewer for screenshots (scraping diagnostics)

### Gaps vs. sample

| Gap | Description |
|---|---|
| Syntax-highlighted editor | Current uses raw `<textarea>`. Sample implies a rich editor. |
| Side-by-side diff | No diff view between proposed and approved. |
| Approval workflow | Sample has "Approve section" buttons. Current has save-only. |
| Stage timeline | Sample shows pipeline stage timeline in sidebar. Current shows flat file list. |
| Artifact metadata | Sample shows file size, modified date. Current shows only path. |

---

Generated from `raw/docs_postulador_langgraph/docs/ui/ui_view_spec.md`.