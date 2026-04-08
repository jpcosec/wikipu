---
identity:
  node_id: "doc:wiki/drafts/design_decisions_already_made.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/docs/ui/ui_view_spec.md", relation_type: "documents"}
---

1. **Palette + typography**: Fixed by samples. Do not redesign.

## Details

1. **Palette + typography**: Fixed by samples. Do not redesign.
2. **Local-first**: All data lives in `data/jobs/`. No remote sync.
3. **JSON as source of truth**: UI edits map to JSON file writes. No separate DB.
4. **HitL review loop**: Operator must explicitly approve before pipeline continues.
5. **Minimal viable**: No speculative features. Every view must be functional.

---

Generated from `raw/docs_postulador_langgraph/docs/ui/ui_view_spec.md`.