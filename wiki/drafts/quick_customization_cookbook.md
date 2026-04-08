---
identity:
  node_id: "doc:wiki/drafts/quick_customization_cookbook.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/docs/ui/node_editor_customization_and_architecture.md", relation_type: "documents"}
---

1. Change available node categories/colors in sandbox

## Details

1. Change available node categories/colors in sandbox
   - Edit `CATEGORY_OPTIONS` and `CATEGORY_COLORS`.
2. Change node templates shown in drag palette
   - Edit `NODE_TEMPLATES`.
3. Change default focus isolation behavior
   - Edit the initial `hideNonNeighbors` state.
4. Change deterministic layout strategy
   - Adjust `layoutAllDeterministic` (Dagre graph params) and/or `layoutFocusNeighborhood`.
5. Change backend skill category normalization
   - Update `_normalize_skill_category` in `src/interfaces/api/read_models.py`.

Generated from `raw/docs_postulador_langgraph/docs/ui/node_editor_customization_and_architecture.md`.