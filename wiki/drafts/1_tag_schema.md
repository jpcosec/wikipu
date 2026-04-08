---
identity:
  node_id: "doc:wiki/drafts/1_tag_schema.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/doc-router-design.md", relation_type: "documents"}
---

The foundation. Developers annotate code and docs so the framework can build the graph.

## Details

The foundation. Developers annotate code and docs so the framework can build the graph.

### 1.1 In Docs (YAML Frontmatter)

```markdown
---
id: pipeline-match-design
domain: pipeline
stage: match
nature: philosophy
implements:
  - src/nodes/match/logic.py
  - src/nodes/match/contract.py
depends_on:
  - pipeline-extract-design
version: 2026-03-22
---
```

### 1.2 In Code

**Python** — structured docstrings:

```python
class MatchLogic:
    """Aligns candidate evidence to job requirements.

    :doc-id: pipeline-match-impl
    :domain: pipeline
    :stage: match
    :nature: implementation
    :doc-ref: pipeline-match-design
    :contract: src/nodes/match/contract.py::MatchInput
    :hitl-gate: review_match
    """
```

**TypeScript** — JSDoc:

```typescript
/**
 * @doc-id ui-match-view
 * @domain ui
 * @stage match
 * @nature implementation
 * @doc-ref pipeline-match-design
 */
```

### 1.3 Tag Rules

| Field | Required | Description |
|-------|----------|-------------|
| `id` | Yes | Globally unique, human-readable identifier |
| `domain` | Yes | Which part of the system (from project vocabulary) |
| `stage` | No | Which pipeline step (from project vocabulary). Defaults to `global` if omitted |
| `nature` | Yes | Document type (from project vocabulary, e.g. `philosophy`, `implementation`, `development`, `testing`) |
| `implements` | No | Doc → code links (list of file paths or `path::Symbol`) |
| `doc-ref` | No | Code → doc links (doc `id` references) |
| `depends_on` | No | Doc → doc dependency edges |
| `contract` | No | Links to schema/contract definitions |
| `hitl-gate` | No | Names the HITL review point, if any |
| `version` | Yes (docs) | Last-verified date. See drift detection rules below |

### 1.4 Project Config

```yaml
# doc-router.yml (project root)
project: my-project
domains: [ui, api, pipeline, core, cli, data, policy]
stages: [scrape, translate, extract, match, strategy, drafting, render, package]
natures: [philosophy, implementation, development, testing]
doc_paths:
  central: docs/
  plans: plan/
templates:
  docs: templates/docs/
  code: templates/code/
```

The vocabulary is per-project. Doc-Router validates tags against this config — unknown domains or stages are lint errors.

---

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/doc-router-design.md`.