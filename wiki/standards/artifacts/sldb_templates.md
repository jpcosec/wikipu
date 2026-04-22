---
identity:
  node_id: "doc:wiki/standards/artifacts/sldb_templates.md"
  node_type: "doc_standard"
edges:
  - {target_id: "doc:.skills/sldb/SKILL.md", relation_type: "documents"}
compliance:
  status: "scaffolding"
  failing_standards: []
---

SLDB templates define the canonical Markdown structure for structured documents in this system. Each template owns a Markdown contract that serves both humans and machines.

## Model Registration

Models live in `src/wiki_compiler/contracts/`:

```python
from sldb import StructuredNLDoc

class WikiNodeDoc(StructuredNLDoc):
    title: str = Field(description="The canonical title of this document.")
    intro: str = Field(description="One-paragraph summary of purpose.")
    compliance_status: str = Field(
        description="One of: planned, scaffold, mocked, implemented, tested, exempt."
    )
    # ... more fields
```

## Template Fields

Every field must have `Field(description="...")` with a meaningful, non-empty description.

## Commands

| Command | Purpose |
|---|---|
| `sldb extract` | Parse Markdown into data |
| `sldb render` | Render Markdown from data |
| `sldb validate` | Check roundtrip idempotency |

## Validation

Run `sldb validate` before committing any SLDB document.

## Cross-Repo

Models are referenced by `<package>.<module>:<ClassName>`. Set `--pythonpath` to the repo root.