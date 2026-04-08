---
identity:
  node_id: "doc:wiki/drafts/what_to_keep_ui_redesign_is_canonical.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/plan/01_ui/cv_graph_feature_merge.md", relation_type: "documents"}
---

| What | File | Why keep |

## Details

| What | File | Why keep |
|---|---|---|
| Persistent global nav | shell layout in `ui-redesign` App.tsx | Cleaner UX than sandbox breadcrumbs |
| React Query hooks | `features/base-cv/api/useCvProfileGraph.ts` | Correct cache/mutation pattern |
| `apiClient` CQRS calls | `api/client.ts` query/commands shape | Aligned with API v2 contract |
| `BaseCvEditor` as page root | `pages/global/BaseCvEditor.tsx` | Correct route: `/cv` |
| Design system (`cn`, Tailwind tokens) | throughout | Consistent with ui-redesign theme |

---

Generated from `raw/docs_postulador_langgraph/plan/01_ui/cv_graph_feature_merge.md`.