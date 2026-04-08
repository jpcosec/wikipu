---
identity:
  node_id: "doc:wiki/drafts/c1_c_match_view_jobs_match_knowledgegraph_based.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/plan/01_ui/specs/C1_graph_editor_redesign.md", relation_type: "documents"}
---

### Goal

## Details

### Goal

Replace `MatchGraphCanvas` + the three-panel layout with a seeded KnowledgeGraph in LR 2-column layout.

### Existing data shape (current `GraphNode`)

The current `MatchViewData.nodes: GraphNode[]` has `kind: 'requirement' | 'profile'` but no `category` field. To enable category-based grouping, the mock fixture and API type need a `category` field on both requirement and profile nodes:

```ts
// Extend GraphNode in api.types.ts:
interface GraphNode {
  id: string;
  label: string;
  kind: string;
  category?: string;   // NEW — e.g. "technical", "soft_skills", "languages"
  score?: number;
  data?: Record<string, unknown>;
}
```

Update `mock/fixtures/artifacts_match_*.json` to add `category` to nodes. Existing nodes without a category fall into a default `"general"` group.

### KnowledgeGraph data mapping

```
MatchViewData               →  KnowledgeGraph
────────────────────────────────────────────────────────
GraphNode (kind=requirement)  →  GroupNode (section) per category, left col (x=0)
                                 + SimpleNode (entry) inside section
GraphNode (kind=profile)      →  GroupNode (section) per category, right col (x=600)
                                 + SimpleNode (skill) inside section
GraphEdge[]                   →  SimpleEdge with score label
Unmapped profile nodes        →  SimpleNode floating in UnmappedPanel (x=1000)
```

### Adapters

```ts
// apps/review-workbench/src/features/job-pipeline/lib/matchToGraph.ts
export function matchPayloadToGraph(data: MatchViewData): { nodes: SimpleNode[]; edges: SimpleEdge[] }

// MatchEdits — what the gate receives after review
export interface MatchEdits {
  addedEdges:   Array<{ source: string; target: string }>;
  removedEdges: Array<{ id: string }>;
  addedNodes:   Array<{ id: string; label: string; kind: 'profile'; category: string }>;
}
export function graphToMatchEdits(
  original: MatchViewData,
  nodes: SimpleNode[],
  edges: SimpleEdge[]
): MatchEdits
```

### Unmapped panel

A `<UnmappedSkillsPanel>` component (right rail, collapsible):
- Lists `SimpleNode`s of kind=`profile` that have no edges
- Click → selects node and scrolls canvas to it
- Drag from panel to a requirement node → creates edge, moves skill into mapped column

### Gate

Keep `MatchDecisionModal` — triggered by "DECIDE" button added to the KnowledgeGraph sidebar Actions section. Gate payload stays `GateDecisionPayload`.

---

Generated from `raw/docs_postulador_ui/plan/01_ui/specs/C1_graph_editor_redesign.md`.