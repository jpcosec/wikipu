---
identity:
  node_id: "doc:wiki/drafts/task_4_job_and_match_schema_stubs.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/docs/superpowers/plans/2026-03-24-schema-explorer.md", relation_type: "documents"}
---

**Files:**

## Details

**Files:**
- Create: `apps/review-workbench/src/schemas/job.schema.json`
- Create: `apps/review-workbench/src/schemas/match.schema.json`

- [ ] **Step 1: Create `job.schema.json`**

```json
{
  "document": {
    "id": "job_posting",
    "label": "Job Posting",
    "version": "0.1",
    "description": "Structured job posting with requirements extracted by extract_understand node.",
    "root_type": "__stub__"
  },
  "node_types": [],
  "edge_types": [],
  "visual_encoding": {
    "color_tokens": {},
    "edge_color_tokens": {}
  }
}
```

- [ ] **Step 2: Create `match.schema.json`**

```json
{
  "document": {
    "id": "match_result",
    "label": "Match Result",
    "version": "0.1",
    "description": "Match envelope linking CV evidence to job requirements via skill nodes.",
    "root_type": "__stub__"
  },
  "node_types": [],
  "edge_types": [],
  "visual_encoding": {
    "color_tokens": {},
    "edge_color_tokens": {}
  }
}
```

- [ ] **Step 3: Commit**

```bash
git add apps/review-workbench/src/schemas/job.schema.json apps/review-workbench/src/schemas/match.schema.json
git commit -m "feat(schema): add job and match schema stubs"
```

---

Generated from `raw/docs_postulador_ui/docs/superpowers/plans/2026-03-24-schema-explorer.md`.