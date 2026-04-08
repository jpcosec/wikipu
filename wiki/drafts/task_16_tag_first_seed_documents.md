---
identity:
  node_id: "doc:wiki/drafts/task_16_tag_first_seed_documents.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/doc-router-phase1-plan.md", relation_type: "documents"}
---

**Files:**

## Details

**Files:**
- Modify: `docs/doc-router-design.md` (add frontmatter)
- Modify: `docs/seed/product/03_methodology.md` (add frontmatter)
- Modify: `docs/seed/product/04_pipeline_stages_phd2.md` (add frontmatter)

- [ ] **Step 1: Tag doc-router-design.md**

Add YAML frontmatter to the top of the file:

```markdown
---
id: practices-doc-router-design
domain: practices
stage: global
nature: design
version: 2026-03-22
---
```

- [ ] **Step 2: Tag methodology doc**

```markdown
---
id: policy-methodology
domain: policy
stage: global
nature: philosophy
version: 2026-03-22
---
```

- [ ] **Step 3: Tag pipeline stages doc**

```markdown
---
id: pipeline-stages-overview
domain: pipeline
stage: global
nature: philosophy
depends_on:
  - policy-methodology
version: 2026-03-22
---
```

- [ ] **Step 4: Verify scan finds them**

Run: `doc-router scan --project .`
Expected: `3 nodes (3 docs, 0 code), 1 edges`

Run: `doc-router graph --project .`
Expected: Lists all 3 nodes and the depends_on edge.

- [ ] **Step 5: Commit**

```bash
git add docs/doc-router-design.md docs/seed/product/03_methodology.md docs/seed/product/04_pipeline_stages_phd2.md
git commit -m "docs: tag first seed documents with doc-router frontmatter"
```

---

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/doc-router-phase1-plan.md`.