---
identity:
  node_id: "doc:wiki/drafts/c1_b_cv_editor_cv_knowledgegraph_based.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/plan/01_ui/specs/C1_graph_editor_redesign.md", relation_type: "documents"}
---

### Goal

## Details

### Goal

Replace `BaseCvEditor` + `CvGraphCanvas` with a seeded KnowledgeGraph. The CV is a Document sub-flow; skills are external nodes connected via edges.

### Data mapping

```
CvProfileGraph              →  KnowledgeGraph
──────────────────────────────────────────────────────────
CV root                     →  GroupNode (type=document, label="My CV")
CvEntry.category            →  GroupNode (type=section, parentId=CV doc)
CvEntry[]                   →  SimpleNode (type=entry, parentId=section)
CvSkill[]                   →  SimpleNode (type=skill, positioned right col)
CvDemonstratesEdge[]        →  SimpleEdge (source=entry.id, target=skill.id)
```

### Round-trip: structured fields

`SimpleNodeData.properties: Record<string, string>` holds only flat strings. `CvEntry.fields` is `Record<string, unknown>` and `CvEntry.descriptions` is a structured `CvDescription[]`.

**Pattern: `meta` passthrough blob**. Extend `SimpleNodeData` with:
```ts
meta?: unknown;  // opaque, not shown in UI, preserved in round-trip
```

`cvProfileToGraph`: store `{ fields: entry.fields, descriptions: entry.descriptions, essential: entry.essential }` in `node.data.meta`. `properties` holds only display-ready flat strings (title/date for the node label).

`graphToCvProfile`: restore `CvEntry.fields` and `CvEntry.descriptions` from `node.data.meta`. If meta is missing (newly created node), initialise with empty defaults.

### Adapter location

```ts
// apps/review-workbench/src/features/base-cv/lib/cvToGraph.ts
export function cvProfileToGraph(data: CvProfileGraphPayload): { nodes: SimpleNode[]; edges: SimpleEdge[] }
export function graphToCvProfile(nodes: SimpleNode[], edges: SimpleEdge[]): CvProfileGraphPayload
```

### BaseCvEditor becomes thin

```tsx
export function BaseCvEditor() {
  const query = useCvProfileGraph();
  const save = useSaveCvGraph();
  const { nodes, edges } = useMemo(() => cvProfileToGraph(query.data!), [query.data]);
  return (
    <KnowledgeGraph
      initialNodes={nodes}
      initialEdges={edges}
      onSave={(n, e) => save.mutate(graphToCvProfile(n, e))}
    />
  );
}
```

`KnowledgeGraph` gets an `onSave?: (nodes: SimpleNode[], edges: SimpleEdge[]) => void` prop. When present, a "Save" button appears in the sidebar.

### Layout on load

- Document group: `x=0, y=0`, width=400
- Section groups: stacked vertically inside, `y = 60 + i*200`
- Entry nodes: inside sections, `y = 50 + j*80`
- Skill nodes: `x = 600`, stacked vertically

---

Generated from `raw/docs_postulador_ui/plan/01_ui/specs/C1_graph_editor_redesign.md`.