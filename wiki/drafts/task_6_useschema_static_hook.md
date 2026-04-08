---
identity:
  node_id: "doc:wiki/drafts/task_6_useschema_static_hook.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/docs/superpowers/plans/2026-03-24-schema-explorer.md", relation_type: "documents"}
---

**Files:**

## Details

**Files:**
- Create: `apps/review-workbench/src/features/schema-explorer/lib/useSchema.ts`

- [ ] **Step 1: Create `useSchema.ts`**

```ts
// apps/review-workbench/src/features/schema-explorer/lib/useSchema.ts
import cvSchema    from '../../../schemas/cv.schema.json';
import jobSchema   from '../../../schemas/job.schema.json';
import matchSchema from '../../../schemas/match.schema.json';
import type { DocumentSchema } from '../../../schemas/types';

export type SchemaDomain = 'cv' | 'job' | 'match';

const SCHEMAS: Record<SchemaDomain, DocumentSchema> = {
  cv:    cvSchema    as unknown as DocumentSchema,
  job:   jobSchema   as unknown as DocumentSchema,
  match: matchSchema as unknown as DocumentSchema,
};

export function useSchema(domain: SchemaDomain): DocumentSchema {
  return SCHEMAS[domain];
}
```

- [ ] **Step 2: Verify TypeScript compiles**

```bash
cd apps/review-workbench && npx tsc --noEmit
# Expected: no errors
```

- [ ] **Step 3: Commit**

```bash
git add apps/review-workbench/src/features/schema-explorer/lib/useSchema.ts
git commit -m "feat(schema-explorer): add useSchema static domain loader"
```

---

Generated from `raw/docs_postulador_ui/docs/superpowers/plans/2026-03-24-schema-explorer.md`.