---
identity:
  node_id: "doc:wiki/drafts/task_5_schematograph_pure_converter.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/docs/superpowers/plans/2026-03-24-schema-explorer.md", relation_type: "documents"}
---

**Files:**

## Details

**Files:**
- Create: `apps/review-workbench/src/features/schema-explorer/lib/schemaToGraph.ts`
- Modify: `apps/review-workbench/src/features/schema-explorer/lib/schemaToGraph.test.ts`

The converter maps each `render_as: "node"` and `render_as: "group"` type to a `SimpleNode`, and each `edge_type` to a `SimpleEdge`. Types with `render_as: "attribute"` are skipped (they show in the inspector only). Color comes from `visual_encoding.color_tokens[color_token]`.

- [ ] **Step 1: Add converter tests to the existing test file**

Append to `schemaToGraph.test.ts`:

```ts
import { schemaToGraph } from './schemaToGraph';

describe('schemaToGraph', () => {
  const { nodes, edges } = schemaToGraph(schema);

  test('produces one node per non-attribute type', () => {
    const nonAttr = schema.node_types.filter(t => t.render_as !== 'attribute');
    expect(nodes).toHaveLength(nonAttr.length);
  });

  test('attribute types are not in nodes', () => {
    const attrIds = schema.node_types.filter(t => t.render_as === 'attribute').map(t => t.id);
    for (const id of attrIds) {
      expect(nodes.find(n => n.id === id)).toBeUndefined();
    }
  });

  test('each node has a name and category from schema', () => {
    for (const node of nodes) {
      expect(typeof node.data.name).toBe('string');
      expect(typeof node.data.category).toBe('string');
    }
  });

  test('edges are produced for each edge_type', () => {
    expect(edges.length).toBeGreaterThanOrEqual(schema.edge_types.length);
  });

  test('variant_of types get an extends edge to their parent', () => {
    const variantTypes = schema.node_types.filter(t => t.variant_of);
    for (const vt of variantTypes) {
      const extendsEdge = edges.find(
        e => e.source === vt.id && e.target === vt.variant_of
      );
      expect(extendsEdge, `no extends edge for ${vt.id}`).toBeDefined();
    }
  });

  test('color from visual_encoding is stored in node meta', () => {
    const rootNode = nodes.find(n => n.id === schema.document.root_type);
    expect(rootNode?.data.meta).toBeDefined();
  });
});
```

- [ ] **Step 2: Run — expect FAIL (schemaToGraph not found)**

```bash
cd apps/review-workbench && npm test
# Expected: FAIL — cannot find module schemaToGraph
```

- [ ] **Step 3: Implement `schemaToGraph.ts`**

```ts
// apps/review-workbench/src/features/schema-explorer/lib/schemaToGraph.ts
import type { DocumentSchema, SchemaNodeType } from '../../../schemas/types';
import type { SimpleNode, SimpleEdge } from '../../../pages/global/KnowledgeGraph';

function renderToken(type: SchemaNodeType): string {
  // Map schema category to KnowledgeGraph CATEGORY_COLORS key
  const map: Record<string, string> = {
    root:     'root',
    abstract: 'abstract',
    entity:   'entry',
    skill:    'skill',
    edge_node: 'edge_node',
    value:    'value',
  };
  return map[type.color_token] ?? type.color_token;
}

export function schemaToGraph(schema: DocumentSchema): {
  nodes: SimpleNode[];
  edges: SimpleEdge[];
} {
  const nodes: SimpleNode[] = [];
  const edges: SimpleEdge[] = [];

  // Nodes: all non-attribute types
  for (const type of schema.node_types) {
    if (type.render_as === 'attribute') continue;

    const colorToken = schema.visual_encoding.color_tokens[type.color_token];

    nodes.push({
      id: type.id,
      type: type.render_as === 'group' ? 'group' : 'simple',
      position: { x: 0, y: 0 }, // dagre will reposition
      data: {
        name: type.label,
        category: renderToken(type),
        properties: {
          render_as: type.render_as,
          ...(type.abstract ? { abstract: 'true' } : {}),
          ...(type.variant_of ? { variant_of: type.variant_of } : {}),
        },
        meta: {
          schemaType: type,
          colorToken,
        },
      },
    });

    // extends edge for variants
    if (type.variant_of) {
      edges.push({
        id: `extends:${type.id}`,
        source: type.id,
        target: type.variant_of,
        data: {
          relationType: 'extends',
          properties: { label: 'variant of' },
        },
      });
    }
  }

  // Edges from edge_types (skip duplicates already added as extends)
  for (const et of schema.edge_types) {
    // Skip if already covered by variant_of auto-edges
    if (et.id === 'extends') continue;
    const edgeColor = schema.visual_encoding.edge_color_tokens[et.color_token];
    edges.push({
      id: `edge:${et.id}`,
      source: et.from,
      target: et.to,
      data: {
        relationType: et.id,
        properties: {
          label: et.label,
          ...(et.cardinality ? { cardinality: et.cardinality } : {}),
        },
        meta: { edgeColor },
      },
    });
  }

  return { nodes, edges };
}
```

- [ ] **Step 4: Run tests — expect PASS**

```bash
cd apps/review-workbench && npm test
# Expected: all passed
```

> **Note — edge color application is deferred:** `SimpleEdgeData extends Record<string, unknown>` so `meta: { edgeColor }` on edges does not cause a TypeScript error, but edge color is not yet applied to rendered edges (no edge style renderer reads `data.meta.edgeColor`). This is intentional — edge color rendering is a follow-up task once the schema graph is working.

> **Note — CATEGORY_COLORS dependency:** The `renderToken` function maps `root`, `abstract`, `edge_node`, `value` to CATEGORY_COLORS keys that are added in Task 7. Tests pass because they don't exercise CATEGORY_COLORS, but the browser render will show fallback grey for those tokens until Task 7 is done. Complete Task 7 before doing the end-to-end check in Task 9.

- [ ] **Step 5: Commit**

```bash
git add apps/review-workbench/src/features/schema-explorer/lib/schemaToGraph.ts apps/review-workbench/src/features/schema-explorer/lib/schemaToGraph.test.ts
git commit -m "feat(schema-explorer): add schemaToGraph converter with tests"
```

---

Generated from `raw/docs_postulador_ui/docs/superpowers/plans/2026-03-24-schema-explorer.md`.