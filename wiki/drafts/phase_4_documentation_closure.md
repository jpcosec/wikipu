---
identity:
  node_id: "doc:wiki/drafts/phase_4_documentation_closure.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/seed/plan/UI_REDESIGN_MERGE_PLAN.md", relation_type: "documents"}
---

### 4.1 Promote Architecture Docs

## Details

### 4.1 Promote Architecture Docs

Move from `plan/` to `docs/runtime/`:

| Source | Destination |
|--------|-------------|
| `plan/01_ui/specs/00_architecture.md` | `docs/runtime/ui_architecture.md` |
| `plan/01_ui/specs/00_design_system.md` | `docs/runtime/ui_design_system.md` |
| `plan/01_ui/specs/00_component_map.md` | `docs/runtime/ui_component_map.md` |
| `plan/01_ui/specs/00_stack.md` | `docs/runtime/ui_stack.md` |

### 4.2 Update Routing Matrix

Add entries to `docs/seed/practices/11_routing_matrix.md`:

```markdown
| ui | all | implementation | `docs/runtime/ui_architecture.md` | `apps/review-workbench/src/` | react, components, features, atoms, molecules | Atomic + Feature-Sliced UI architecture | Legacy sandbox (DELETE) |
| ui | all | development | `docs/runtime/ui_design_system.md` | `apps/review-workbench/src/components/atoms/` | design system, terran command, button, badge | Terran Command design tokens | |
```

### 4.3 Changelog Entry

```markdown

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/seed/plan/UI_REDESIGN_MERGE_PLAN.md`.