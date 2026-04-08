---
identity:
  node_id: "doc:wiki/drafts/interaction_modes.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/docs/ui/node_editor_behavior_spec.md", relation_type: "documents"}
---

### Editor State Model

## Details

### Editor State Model

The editor runs with one active state at a time:

- `browse`
- `focus`
- `edit_node`
- `edit_relation`

Transition rules:

- `browse -> focus`: user focuses a node.
- `focus -> edit_node`: user enters node editing for the focused node.
- `focus -> edit_relation`: user selects a relation for editing.
- `edit_node -> focus` or `edit_relation -> focus`: user closes editor after save/discard.
- `focus -> browse`: user unfocuses/reset focus.

Guard rule:

- Leaving `edit_node` or `edit_relation` is blocked until pending changes are resolved by save or discard.

### Selection Model

- Single selection by default (one node or one relation at a time).
- Relation selection clears node selection.
- Node selection clears relation selection.
- Canvas background click clears current selection and returns to `browse` when no focus lock is active.
- Multi-select is out of scope for this draft.

### [A] Browse mode

- User navigates and inspects nodes.
- Hover reveals hover-tier properties.
- Container nodes are initially collapsed to name-first summaries.
- All visible nodes remain draggable if they are free nodes.

### [B] Focus mode

When focusing a node, configurable behavior options include:

- center and zoom to focused node
- dim non-focused nodes
- hide non-focused nodes
- make non-focused nodes unreachable (non-interactive)
- show only selected relation types
- show only relations attached to focused node

Focus behavior must be togglable and composable (multiple options can be active together).
Default focus behavior for this phase:

- center + zoom to focused node
- keep 1-hop neighbors fully visible and interactive
- keep non-neighbors visible but dimmed (target baseline: 20% opacity) and non-interactive
- include a sidebar toggle `Hide non-neighbors` for full isolation when needed

Spatial policy in focus mode:

- focused node at center
- direct neighbors arranged on a deterministic peripheral ring
- transitions must be smoothly animated to preserve user mental map

### [C] Edit mode

- Selecting a node enables property and relation editing for that node.
- For this node-to-node phase, editing opens an overlay modal form.
- Node form supports existing properties and newly added attributes.
- Selecting any relation line opens relation inspection.
- If a relation is editable, relation type and relation attributes can be edited.

Edit entrypoint contract (canonical order):

1. Primary: contextual in-node edit affordance shown on hover/selection
2. Secondary: double-click on node
3. Sidebar edit action is not part of the canonical flow for this phase

Generated from `raw/docs_postulador_langgraph/docs/ui/node_editor_behavior_spec.md`.