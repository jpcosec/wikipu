---
identity:
  node_id: "doc:wiki/drafts/task_6_c1_c_add_category_to_graphnode_and_match_fixtures.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/plan/01_ui/plans/2026-03-23-c1-graph-editor-redesign.md", relation_type: "documents"}
---

The match view requires grouping nodes by category. `GraphNode` currently has no `category` field.

## Details

The match view requires grouping nodes by category. `GraphNode` currently has no `category` field.

**Files:**
- Modify: `apps/review-workbench/src/types/api.types.ts`
- Modify: `apps/review-workbench/src/mock/fixtures/view_match_201397.json`
- Modify: `apps/review-workbench/src/mock/fixtures/view_match_999001.json`

- [ ] **Step 1: Add category field to GraphNode**

In `api.types.ts`, find:
```ts
export interface GraphNode {
  id: string;
  label: string;
  kind: string;
  score?: number;
  priority?: string;
}
```
Add `category?: string;` after `kind`:
```ts
export interface GraphNode {
  id: string;
  label: string;
  kind: string;
  category?: string;
  score?: number;
  priority?: string;
}
```

- [ ] **Step 2: Update view_match_201397.json — add category to requirement nodes**

Open the file. Add `"category"` field to each requirement node. Use these category assignments:

```
degree_psychology_neuroscience      → "qualifications"
exp_programming_experiments         → "technical"
exp_statistical_analysis_R          → "technical"
exp_eeg_data                        → "technical"
ability_independent_scientific_work → "soft_skills"
exp_eye_tracking_data               → "technical"
skills_scientific_writing_presentation → "communication"
knowledge_english                   → "languages"
willingness_teamwork_international  → "soft_skills"
exp_ethics_approval                 → "qualifications"
motivation_empirical_research       → "soft_skills"
ability_teamworking                 → "soft_skills"
readiness_open_science              → "qualifications"
interest_human_machine_interaction  → "technical"
```

For profile nodes:
```
P_EDU_001  → "education"
P_EXP_005  → "experience"
P_EXP_006  → "experience"
P_EXP_007  → "experience"
P_EXP_012  → "experience"
P_SKL_021  → "skills"
P_SKL_022  → "skills"
P_PUB_019  → "publications"
P_PUB_020  → "publications"
P_LNG_026  → "languages"
```

- [ ] **Step 3: Update view_match_999001.json similarly**

Read the file and add matching `"category"` fields to all nodes. Use the same category vocabulary (`"technical"`, `"soft_skills"`, `"qualifications"`, `"languages"`, `"education"`, `"experience"`, `"skills"`, `"publications"`, `"communication"`).

- [ ] **Step 4: Verify build**

```bash
cd apps/review-workbench && npm run build 2>&1 | tail -5
```

- [ ] **Step 5: Commit**

```bash
git add apps/review-workbench/src/types/api.types.ts \
        apps/review-workbench/src/mock/fixtures/view_match_201397.json \
        apps/review-workbench/src/mock/fixtures/view_match_999001.json
git commit -m "feat(ui): add category field to GraphNode and match fixtures (C1-C)"
```

---

Generated from `raw/docs_postulador_ui/plan/01_ui/plans/2026-03-23-c1-graph-editor-redesign.md`.