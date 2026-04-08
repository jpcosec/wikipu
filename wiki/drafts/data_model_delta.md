---
identity:
  node_id: "doc:wiki/drafts/data_model_delta.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/plan/01_ui/extract_text_tagger_merge.md", relation_type: "documents"}
---

Add to `RequirementItem` type (already in `api.types`):

## Details

Add to `RequirementItem` type (already in `api.types`):

```ts
interface RequirementItem {
  id: string;
  text: string;
  priority: 'must' | 'nice' | 'nice_to_have';
  spans: unknown[];          // existing
  text_span: RequirementTextSpan | null;  // existing — line range
  // NEW:
  char_start?: number | null;  // character offset in source_markdown
  char_end?: number | null;
  notes?: string;            // operator annotation
}
```

The `char_start` / `char_end` are set when a requirement is created via text selection. LLM-produced requirements may not have them initially — that's fine, line-range highlight still works as fallback.

---

Generated from `raw/docs_postulador_langgraph/plan/01_ui/extract_text_tagger_merge.md`.