---
identity:
  node_id: "doc:wiki/drafts/step_01b_node_type_registry_modes.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/plan/future/2026-03-20-ui-plan-review-design.md", relation_type: "documents"}
---

### 1. Architecture Logic

## Details

### 1. Architecture Logic

The registry is populated from the representation schema's `node_types`. The editor ships with base renderers that the schema's `content_type` maps onto. No hardcoded node families.

**Registry shape:** Lookup table keyed by `type_id`. Each entry declares:
- `type_id`, `icon`, `category` — identity and visual grouping
- `payload_schema` — data shape (compiled from schema attributes)
- `renderers` — four modes: minimized, focus, edit_in_context, full_editor
- `supported_anchors` — annotation anchor types
- `default_size`, `allowed_relations` — layout and connection constraints
- `container_config` — if container: child ordering rules, collapse behavior, proxy edge style

**Base renderer set (built-in extensions):**
- entity (generic card with attributes)
- container (collapsible group with children)
- markdown_text (03b)
- code_block (03e)
- json_payload (03c)
- table (03d)
- image (03f)
- html_safe (sanitized embed)

**Two orthogonal axes:**
- **EditorState** (5 states, defined in 01 as part of graph_view, transitions governed by 01c's action taxonomy): `browse | focus | focus_relation | edit_node | edit_relation`
- **Renderer mode** (4 modes, per node type, chosen by dispatcher based on EditorState + node context): `minimized | focus | edit_in_context | full_editor`

The mapping from EditorState to renderer mode is contextual:
- `browse` → all nodes get `minimized`
- `focus` → focused node gets `focus`, others get `minimized`
- `edit_node` → focused node gets `edit_in_context` or `full_editor` (per type config), others get `minimized`
- `focus_relation` / `edit_relation` → focused endpoints get `focus`, others `minimized`

**Dispatcher:** One React Flow `nodeTypes` entry — reads registry by `type_id`, resolves renderer mode from current EditorState + node focus, delegates to correct renderer. Unknown types get fallback (generic card).

### 2. Objectives

1. All nodes render through registry lookup
2. Each registered type supports at least minimized + focus + full_editor
3. Adding a new type = schema entry + optional custom renderer extension. Zero editor shell changes.
4. Container is a first-class type with container_config
5. Fallback renderer handles unknown types gracefully
6. Schema's node_types populate the registry at load time

### 3. Don'ts

- **Don't implement all renderers at once.** Entity + container fully implemented. Others registered with fallback until 03-series.
- **Don't embed rich content rendering here.** Registry declares what a type needs. 03 implements renderers.
- **Don't skip the fallback renderer.** Unknown types must not crash.
- **Don't hardcode mode transitions in the registry.** Registry maps EditorState × node context → renderer mode. EditorState transitions live in 01c.
- **Don't couple payload_schema to a validator.** TypeScript discriminated unions now. Zod later if needed.

### 4. Known Gaps & Open Questions

- **GAP-ARCH-03** (High): Anchor identity model — declared here (`supported_anchors`), implemented in 03a.
- **GAP-DEP-01** (Blocker): This step MUST complete before any 03-series work.

### 5. Library Decision Matrix

No new libraries. React Flow's `nodeTypes` API is the integration surface.

### 6. Test Plan

- **Unit**: Registry lookup returns correct renderers for known types, fallback for unknown. container_config serialization.
- **Component**: Dispatcher renders minimized/focus/edit modes correctly. Unknown type gets fallback.
- **Integration**: Create container node → add child → collapse → proxy edges appear.

### 7. Review Checklist

- [ ] Registry populated from schema
- [ ] All nodes route through dispatcher
- [ ] Fallback renderer works
- [ ] Container type has container_config
- [ ] Adding new entry doesn't touch editor shell
- [ ] Entity + container fully rendered

---

Generated from `raw/docs_postulador_ui/plan/future/2026-03-20-ui-plan-review-design.md`.