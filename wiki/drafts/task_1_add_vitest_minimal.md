---
identity:
  node_id: "doc:wiki/drafts/task_1_add_vitest_minimal.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/docs/superpowers/plans/2026-03-24-schema-explorer.md", relation_type: "documents"}
---

**Files:**

## Details

**Files:**
- Modify: `apps/review-workbench/package.json`
- Modify: `apps/review-workbench/vite.config.ts`

- [ ] **Step 1: Install Vitest**

```bash
cd apps/review-workbench
npm install --save-dev vitest
```

- [ ] **Step 2: Add test script to package.json**

In `package.json` scripts, add:
```json
"test": "vitest run",
"test:watch": "vitest"
```

- [ ] **Step 3: Add Vitest config to vite.config.ts**

Read current `vite.config.ts` first, then add `test` block:
```ts
/// <reference types="vitest" />
// existing config +
test: {
  environment: 'node',
  include: ['src/**/*.test.ts'],
}
```

- [ ] **Step 4: Verify Vitest works**

```bash
cd apps/review-workbench
echo 'import { test, expect } from "vitest"; test("smoke", () => expect(1+1).toBe(2));' > src/smoke.test.ts
npm test
# Expected: 1 passed
rm src/smoke.test.ts
```

- [ ] **Step 5: Commit**

```bash
git add apps/review-workbench/package.json apps/review-workbench/vite.config.ts apps/review-workbench/package-lock.json
git commit -m "chore(workbench): add vitest for unit testing"
```

---

Generated from `raw/docs_postulador_ui/docs/superpowers/plans/2026-03-24-schema-explorer.md`.