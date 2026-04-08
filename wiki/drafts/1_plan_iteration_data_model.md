---
identity:
  node_id: "doc:wiki/drafts/1_plan_iteration_data_model.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/superpowers/specs/2026-03-23-doc-router-phase2-design.md", relation_type: "documents"}
---

Plans live on disk as markdown files with YAML frontmatter, following a naming convention:

## Details

Plans live on disk as markdown files with YAML frontmatter, following a naming convention:

```
docs/plans/
  {group}/                          # plan group (e.g. "cv-graph-editor")
    plan_{group}_0.md               # AI-generated plan v0
    review_{group}_0.md             # User's reviewed/edited version
    plan_{group}_1.md               # AI-generated plan v1 (incorporates review)
    review_{group}_1.md             # ...
```

### Frontmatter Schema

```yaml
---
id: plan-{group}-{version}
domain: pipeline                    # which domain this plan targets
stage: extract                      # which stage (or "global")
nature: development
type: plan                          # "plan" or "review"
group: {group}                      # links the iteration chain
version: 0                          # iteration number
parent: null                        # review_{group}_0 has parent: plan_{group}_0
status: draft                       # draft | active | approved | superseded
touches:                            # files this plan creates or modifies
  - path: src/nodes/extract/logic.py
    symbol: run_logic               # optional: specific function/class within file
  - path: src/nodes/extract/contract.py
  - path: docs/runtime/node_io_matrix.md
---
```

### Plan Path Configuration

The plans directory is configurable in `doc-router.yml`:

```yaml
plan_paths:
  plans: docs/plans/           # default location for plan files
```

If not specified, defaults to `docs/plans/` relative to project root.

### Iteration Rules

- `plan_{group}_N` is the AI's artifact. `review_{group}_N` is the user's.
- When a review is saved, the source plan gets `status: superseded`.
- The `parent` field links a review to its source plan.
- The `touches` field powers file tree highlighting and graph filtering.

### Status Lifecycle

```
draft → active → superseded
                → approved
```

- **draft**: Initial state when a plan/review file is first created.
- **active**: The current working version (only one plan and one review per group can be active).
- **approved**: User has approved this plan — ready for implementation.
- **superseded**: A newer version exists; this version is archived.

Saving a review sets the source plan to `superseded` and the review to `active`.

### Symbol Resolution

When `touches` includes a `symbol`, the backend uses the existing Python AST scanner (`scanner/python.py`) to resolve the symbol to a line range. If the symbol is not found (renamed, deleted), the touch entry is still valid but the line range is `null` — the frontend shows the file without scrolling to a specific location. Resolution is done on-demand per request (no caching in Phase 2).

---

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/superpowers/specs/2026-03-23-doc-router-phase2-design.md`.