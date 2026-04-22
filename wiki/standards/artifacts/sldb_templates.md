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

## Store Architecture

The store is a three-level YAML index cascade tracking model contracts and their document instances via a Merkle-style hash chain. Initialize with `sldb store init` in the project root.

## Commands

### Core
| Command | Purpose |
|---|---|
| `sldb extract` | Parse Markdown into data |
| `sldb render` | Render Markdown from data |
| `sldb validate` | Check roundtrip idempotency |

### Store
| Command | Purpose |
|---|---|
| `sldb store init` | Initialize .sldb/ store |
| `sldb store add` | Link federated store |
| `sldb store check` | Verify hash integrity |
| `sldb store update` | Full reindex |

### Model
| Command | Purpose |
|---|---|
| `sldb model add` | Register model contract |
| `sldb model update` | Re-index after contract change |

### Doc
| Command | Purpose |
|---|---|
| `sldb doc add` | Create + track document |
| `sldb doc track` | Track existing document |
| `sldb doc update` | Re-render with new data |

## Validation

Run `sldb validate` before committing any SLDB document.

## Cross-Repo

Models are referenced by `<package>.<module>:<ClassName>`. Set `--pythonpath` to the repo root. Federate stores with `sldb store add <path>` to pull models from other repos.