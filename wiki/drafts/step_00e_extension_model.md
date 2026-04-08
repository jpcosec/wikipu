---
identity:
  node_id: "doc:wiki/drafts/step_00e_extension_model.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/plan/future/2026-03-20-ui-plan-review-design.md", relation_type: "documents"}
---

### 1. Architecture Logic

## Details

### 1. Architecture Logic

The editor is a host runtime that discovers and mounts extensions at load time. Every feature that varies by domain is an extension. Built-in features use the same API as project extensions. No privileged internal paths.

**One pattern:** Every extension follows: declare → register → mount → communicate via dispatch.

**10 extension types:**

| Type | What it does | Built-in examples |
|---|---|---|
| `node_renderer` | Renders a node type in one or more display modes | entity, container, markdown_text, code_block |
| `sidebar_panel` | Dockable panel (left/right/float via FlexLayout) | Explorer, Outline, Filters, Node Palette |
| `inspector_section` | Tab inside the node inspector | Metadata, Relationships, History |
| `toolbar_action` | Button on the floating bottom toolbar | Zoom, Pan, Relayout, Filter |
| `context_action` | Right-click menu item on node/edge | Layout Focus, Expand Context, Delete |
| `canvas_overlay` | Floating overlay on canvas | Focus Mode status bar, zoom controls |
| `layout_algorithm` | New layout preset type | dag_default, focus_centered, tree_top_down |
| `source_adapter` | New data source type | neo4j, json_file, api |
| `edge_renderer` | Custom edge rendering | solid, dashed, proxy |
| `keyboard_shortcut` | Keyboard binding | Ctrl+Z undo, Delete remove |

**Activation rules:** Extensions declare when they're active. Inactive extensions don't mount.

```
activateWhen:
  schema: "cv_profile"       # only in this schema
  nodeType: "entry"           # only when this type focused
  editorState: "focus"        # EditorState value (browse/focus/focus_relation/edit_node/edit_relation)
  rendererMode: "edit_in_context"  # renderer mode (minimized/focus/edit_in_context/full_editor)
  all: [rule, rule]           # AND
  any: [rule, rule]           # OR
```

Extensions can activate on either EditorState (the 5-state machine from graph_view) or rendererMode (the 4-mode renderer axis from 01b), or both. See 01b for the mapping between these two axes.

**Performance model:**
- **Schema load**: registry compiles all extensions into O(1) lookup tables. Happens once.
- **Mode/view change**: table lookup. Happens rarely.
- **Node focus change**: table lookup + prop update on cached component.
- **Pan/zoom/drag**: zero registry involvement.
- **Prerender cache**: extensions declare cacheable modes. Cached until payload changes.
- **Background precomputation**: idle-time prerender of neighbors' focus mode.

**Panel docking:** FlexLayout-react handles all docking. Panels are sidebar_panel extensions. User drags to reposition. Layout serialized as part of view presets.

**Schema-driven inspector:** RJSF renders forms from representation schema's attributes compiled to JSON Schema. Custom renderers (relation pills, mastery scale, tags) are registered as RJSF custom widgets AND as inspector_section extensions.

**HTML snippets:** `html_safe` content type renders sanitized HTML via DOMPurify (see html_safe section after 03f for sanitization rules).

### 2. Objectives

1. All built-in features are registered through `registry.register()` — same API as project extensions
2. Adding a new extension type requires: one interface definition + one mount slot in the host
3. Activation rules evaluated at compile time (schema load), not per-frame
4. FlexLayout integration: panels dock left/right/float, layout serialized
5. RJSF integration: inspector forms render from schema attributes
6. Prerender cache works for declared cacheable modes
7. Extension developer guide exists with "I want to... → Create this → Register it" table

### 3. Don'ts

- **Don't create privileged internal paths.** Built-in extensions register the same way as external ones.
- **Don't evaluate activation rules on every state change.** Compile lookup tables at schema load. Re-evaluate only on discrete transitions (schema change, mode change, view change).
- **Don't mount invisible extensions.** Inactive or hidden panels don't render React components. Mount on first show, keep mounted (hidden) for reuse.
- **Don't allow extensions to mutate state directly.** All mutations through `dispatch(action)`. Extensions read via selectors.

### 4. Known Gaps & Open Questions

- **GAP-EXT-01** (Medium): Extension packaging — how are third-party extensions distributed? NPM packages? Local files? Deferred until the first external consumer exists.
- **GAP-EXT-02** (Low): Extension conflict resolution — what if two extensions register for the same slot with equal priority? Suggested: last-registered wins, with console warning.

### 5. Library Decision Matrix

- **Dockable panels**: FlexLayout-react — committed. See LIB-DOCK-01.
- **Schema-driven forms**: RJSF — committed. See LIB-FORMS-01.
- **Extension registry**: Custom (~300 lines).

### 6. Test Plan

- **Unit**: registry.register() stores extension. registry.compile() builds correct lookup tables. Activation rules evaluate correctly for all operators (schema, nodeType, mode, all, any).
- **Component**: sidebar_panel extension mounts in FlexLayout. inspector_section extension renders as RJSF custom widget. context_action appears in right-click menu for matching node type.
- **Integration**: Register custom node_renderer → create node of that type → correct renderer mounts in all modes.

### 7. Review Checklist

- [ ] All built-in features registered via registry.register()
- [ ] Lookup tables are O(1)
- [ ] Activation rules compile at schema load
- [ ] FlexLayout panels dock/float/serialize
- [ ] RJSF forms render from schema attributes
- [ ] Prerender cache works for declared modes
- [ ] Developer guide table exists

---

Generated from `raw/docs_postulador_ui/plan/future/2026-03-20-ui-plan-review-design.md`.