---
identity:
  node_id: "doc:wiki/drafts/what_not_to_port.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/plan/01_ui/cv_graph_feature_merge.md", relation_type: "documents"}
---

| Feature | Reason |

## Details

| Feature | Reason |
|---|---|
| `CvGraphEditorPage` breadcrumb nav | ui-redesign has better persistent sidebar nav |
| Inline `getCvProfileGraphPayload()` fetch | ui-redesign uses React Query (better) |
| Raw `fetch()` save | ui-redesign uses `useSaveCvGraph` mutation (better) |
| Sandbox-path component locations | Move everything to `features/base-cv/` |
| `dagre` top-level group layout from dev | ui-redesign dagre layout is simpler and sufficient; keep it, just add group nodes as top-level |

---

Generated from `raw/docs_postulador_langgraph/plan/01_ui/cv_graph_feature_merge.md`.