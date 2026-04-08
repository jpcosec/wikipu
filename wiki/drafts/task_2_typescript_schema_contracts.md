---
identity:
  node_id: "doc:wiki/drafts/task_2_typescript_schema_contracts.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/docs/superpowers/plans/2026-03-24-schema-explorer.md", relation_type: "documents"}
---

**Files:**

## Details

**Files:**
- Create: `apps/review-workbench/src/schemas/types.ts`

- [ ] **Step 1: Create `types.ts`**

```ts
// apps/review-workbench/src/schemas/types.ts

export type RenderAs = 'group' | 'node' | 'attribute';
export type RelationType = 'contains' | 'extends' | 'semantic_edge' | 'references';

export interface SchemaAttribute {
  name: string;
  type: string;
  required: boolean;
  values?: string[];
  note?: string;
}

export interface SchemaChild {
  type: string;
  via: string;
  group_by?: string;
}

export interface SchemaNodeType {
  id: string;
  label: string;
  render_as: RenderAs;
  color_token: string;
  abstract?: boolean;
  variant_of?: string;
  attributes: SchemaAttribute[];
  children?: SchemaChild[];
}

export interface SchemaEdgeType {
  id: string;
  label: string;
  from: string;
  to: string;
  color_token: string;
  animated?: boolean;
  cardinality?: string;
  note?: string;
}

export interface ColorToken {
  border: string;
  bg: string;
}

export interface EdgeColorToken {
  stroke: string;
}

export interface VisualEncoding {
  color_tokens: Record<string, ColorToken>;
  edge_color_tokens: Record<string, EdgeColorToken>;
}

export interface DocumentSchema {
  document: {
    id: string;
    label: string;
    version: string;
    description: string;
    root_type: string;
  };
  node_types: SchemaNodeType[];
  edge_types: SchemaEdgeType[];
  visual_encoding: VisualEncoding;
}
```

- [ ] **Step 2: Verify TypeScript compiles**

```bash
cd apps/review-workbench && npx tsc --noEmit
# Expected: no errors
```

- [ ] **Step 3: Commit**

```bash
git add apps/review-workbench/src/schemas/types.ts
git commit -m "feat(schema): add DocumentSchema TypeScript contracts"
```

---

Generated from `raw/docs_postulador_ui/docs/superpowers/plans/2026-03-24-schema-explorer.md`.