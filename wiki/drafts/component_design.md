---
identity:
  node_id: "doc:wiki/drafts/component_design.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/plan/01_ui/specs/D1_schema_explorer.md", relation_type: "documents"}
---

### `SchemaExplorer.tsx` (thin page)

## Details

### `SchemaExplorer.tsx` (thin page)

Domain selector pills at top: **CV · Job · Match**. Passes selected schema through `schemaToGraph()`, renders with `KnowledgeGraph` in `readOnly` mode. Job and Match show a placeholder until their schemas are authored.

```tsx
export function SchemaExplorer() {
  const [domain, setDomain] = useState<'cv' | 'job' | 'match'>('cv');
  const schema = useSchema(domain);
  const { nodes, edges } = useMemo(() => schemaToGraph(schema), [schema]);
  return (
    <KnowledgeGraph initialNodes={nodes} initialEdges={edges} readOnly />
  );
}
```

### `schemaToGraph.ts`

```ts
import type { DocumentSchema } from '../../../schemas/types';
import type { SimpleNode, SimpleEdge } from '../../../pages/global/KnowledgeGraph';

export function schemaToGraph(schema: DocumentSchema): {
  nodes: SimpleNode[];
  edges: SimpleEdge[];
}
```

Mapping rules:
- `render_as: "group"` → ReactFlow group node (parentId + extent: 'parent' for children)
  - `group_by` field → creates intermediate group nodes per distinct value
- `render_as: "node"` → regular `SimpleNode`; `abstract: true` nodes rendered with muted style
- `render_as: "attribute"` → **not rendered as a node**; stored in parent's `node.data.meta.attributes`
- Each `edge_type` → `SimpleEdge` with `data.relationType` and stroke color from `visual_encoding`
- `variant_of` types get an `extends` edge to their parent
- `color_token` resolved from `schema.visual_encoding.color_tokens[token]` — no global fallback
- Layout: dagre `rankdir: LR`

### `useSchema.ts`

Location: `features/schema-explorer/lib/useSchema.ts` (static import, no API call).

```ts
import cv    from '../../../schemas/cv.schema.json';
import job   from '../../../schemas/job.schema.json';
import match from '../../../schemas/match.schema.json';
import type { DocumentSchema } from '../../../schemas/types';

const SCHEMAS: Record<string, DocumentSchema> = {
  cv:    cv    as DocumentSchema,
  job:   job   as DocumentSchema,
  match: match as DocumentSchema,
};

export function useSchema(domain: 'cv' | 'job' | 'match'): DocumentSchema {
  return SCHEMAS[domain];
}
```

### `KnowledgeGraph.tsx` additions

- `readOnly?: boolean` prop — suppresses edit panel, save button, drag-to-connect
- `CATEGORY_COLORS` extended with `root`, `abstract`, `edge_node`, `value` tokens

---

Generated from `raw/docs_postulador_ui/plan/01_ui/specs/D1_schema_explorer.md`.