---
identity:
  node_id: "doc:wiki/drafts/c1_a_fix_graph_terran_theme_sub_flows_document_template.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/plan/01_ui/specs/C1_graph_editor_redesign.md", relation_type: "documents"}
---

### Problem

## Details

### Problem

`KnowledgeGraph.tsx` uses light pastel `CATEGORY_COLORS` (`#e8d5b7`, `#d5e8b7`, …) as inline `backgroundColor` on node cards. Several `.ne-*` CSS classes also hardcode white/light values:

- `.ne-node-child { background: #fff }`
- `.ne-node-free` — no explicit background, inherits ReactFlow's white injection
- `.ne-section { background: rgba(255,255,255,0.72) }`
- `.ne-section-toggle { background: linear-gradient(180deg,#fff,#f6f3ed) }`
- `.ne-template-chip { background: #f8fbff }`
- ReactFlow's own stylesheet injects `.react-flow__node { background: #fff }` wrapping every custom node

### Color fix

Replace `CATEGORY_COLORS` map in `KnowledgeGraph.tsx` with dark border+bg pairs:

```ts
const CATEGORY_COLORS: Record<string, { border: string; bg: string }> = {
  person:      { border: 'rgba(0,242,255,0.5)',   bg: 'rgba(0,242,255,0.07)' },
  skill:       { border: 'rgba(255,170,0,0.5)',   bg: 'rgba(255,170,0,0.07)' },
  project:     { border: 'rgba(0,242,255,0.25)',  bg: 'rgba(0,242,255,0.04)' },
  publication: { border: 'rgba(255,180,171,0.5)', bg: 'rgba(255,180,171,0.07)' },
  concept:     { border: 'rgba(116,117,120,0.5)', bg: 'rgba(116,117,120,0.07)' },
  document:    { border: 'rgba(0,242,255,0.6)',   bg: 'rgba(0,242,255,0.06)' },
  section:     { border: 'rgba(255,170,0,0.4)',   bg: 'rgba(255,170,0,0.05)' },
  entry:       { border: 'rgba(116,117,120,0.4)', bg: 'rgba(30,32,34,0.9)' },
};
```

`SimpleNodeCard` renders with:
```tsx
style={{
  borderLeft: `4px solid ${color.border}`,
  background: color.bg,
  color: 'var(--text-main)',
}}
```

Fix `styles.css` — replace all hardcoded light backgrounds:
```css
/* Remove white backgrounds */
.react-flow__node              { background: transparent !important; }  /* suppress RF injection */
.ne-node-child                 { background: var(--panel); }
.ne-node-free                  { background: transparent; }  /* let category bg show through */
.ne-section                    { background: rgba(0,242,255,0.03); }
.ne-section-toggle             { background: var(--panel); }
.ne-template-chip              { background: var(--panel); }
```

### Sub-flow support — two new node types

**`GroupNode`** (type `group`): a resizable parent container rendered as a titled frame.
- Header bar: category icon + label + child-count badge + collapse toggle
- Body: transparent fill, dashed border using category border color
- Handles on all 4 sides for external connections
- Nodes with category `document` or `section` automatically get `type: 'group'`

**Drag-onto-group (parentId assignment):** ReactFlow does NOT auto-assign `parentId` on drop. The implementer must:
1. On `onNodeDragStop`, hit-test the dragged node's bounding box against all `GroupNode` bounding boxes
2. If the dragged node center falls inside a group, set `parentId = group.id`, `extent = 'parent'`
3. **Recalculate child position to parent-relative coords**: `child.position = { x: child.absX - group.absX, y: child.absY - group.absY }`
4. On "detach" (drag out of group), reverse: convert back to absolute coords and remove `parentId`

**`SubFlowEdge`**: edges whose source or target is a child node inside a group.
- ReactFlow reports child node positions relative to their parent, not the canvas
- When rendering edge paths, resolve absolute position: `absPos = child.position + parent.position`
- Reuse the existing `FloatingEdge` bezier calculation once absolute positions are resolved
- Register as `edgeTypes: { subflow: SubFlowEdge }` and use it for all edges once sub-flows are enabled

### Document node template

Add to `NODE_TEMPLATES`:
```ts
{ name: 'Document', category: 'document', defaults: { title: 'Untitled', type: 'cv' } },
{ name: 'Section',  category: 'section',  defaults: { title: 'New Section' } },
{ name: 'Entry',    category: 'entry',    defaults: { title: '', date: '' } },
```

When `Document` template is dropped onto canvas, create:
1. A `GroupNode` (type=`document`, size 600×400)
2. Two child `GroupNode`s (type=`section`, parentId=doc) labelled "Introduction" + "Body"
3. One placeholder `Entry` leaf inside each section

Entry nodes have a right-side Handle only — for connecting out to skill/requirement external nodes.

---

Generated from `raw/docs_postulador_ui/plan/01_ui/specs/C1_graph_editor_redesign.md`.