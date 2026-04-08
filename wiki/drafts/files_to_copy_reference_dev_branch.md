---
identity:
  node_id: "doc:wiki/drafts/files_to_copy_reference_dev_branch.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/plan/01_ui/extract_text_tagger_merge.md", relation_type: "documents"}
---

| Dev source | Target (ui-redesign) | Notes |

## Details

| Dev source | Target (ui-redesign) | Notes |
|---|---|---|
| `RichTextPane.tsx` — `toOffset()` helper | `utils/text-offsets.ts` | Copy verbatim |
| `RichTextPane.tsx` — `buildSegments()` | `features/job-pipeline/components/SourceTextPane.tsx` | Adapt to `RequirementItem[]` instead of `HighlightNote[]` |
| `RichTextPane.tsx` — `captureSelection()` | `SourceTextPane.tsx` | Adapt: emit `{start, end, text}` via prop callback |
| `RichTextPane.tsx` — keyboard handler | `ExtractUnderstand.tsx` | Simplified to 2 keys only (1=must, 2=nice) |
| `RichTextPane.tsx` — `EditableField` | Inline in `RequirementItem.tsx` | Already partially exists (double-click edit) |

---

Generated from `raw/docs_postulador_langgraph/plan/01_ui/extract_text_tagger_merge.md`.