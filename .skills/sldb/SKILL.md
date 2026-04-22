---
name: sldb
description: Use for StructuredNLDoc models that embed a Markdown contract in `__template__`. Extract, render, validate idempotency, and document structured Markdown workflows.
---

# SLDB

Use `sldb` for StructuredNLDoc models and their Markdown documents.

When to use
- Any StructuredNLDoc-backed document that should roundtrip as structured data
- Any structured document change that needs model-level idempotency validation

What it does
- Extracts data from Markdown with a model
- Renders Markdown from data with a model
- Validates model roundtrip behavior
- Keeps field-level descriptions present so the model is self-explanatory to humans and LLMs

Model rule
- Every `StructuredNLDoc` field must use `Field(description="...")` with a non-empty description

## Commands

### Core
| Command | Purpose |
|---|---|
| `sldb extract` | Parse Markdown into model data |
| `sldb render` | Render Markdown from data |
| `sldb validate` | Check roundtrip idempotency |
| `sldb init` | Initialize .sldb/ store |
| `sldb example` | Unpack reference bundle |

### Store (pointer database)
| Command | Purpose |
|---|---|
| `sldb store init` | Initialize .sldb/ in project root |
| `sldb store add` | Link a federated store |
| `sldb store check` | Verify hash cascade integrity |
| `sldb store update` | Full reindex from file states |

### Model (contract registry)
| Command | Purpose |
|---|---|
| `sldb model add` | Register model contract in store |
| `sldb model update` | Re-index model after contract change |

### Doc (document instances)
| Command | Purpose |
|---|---|
| `sldb doc add` | Create + track a document from data |
| `sldb doc track` | Validate + track an existing document |
| `sldb doc update` | Re-render tracked doc with new data |

Python marker modes
- Safe mode is the default; `py` markers stay literal and are not evaluated
- Unsafe mode enables `py` marker evaluation for trusted templates only

Rule
- Every `StructuredNLDoc` field must have a meaningful description.
- For every StructuredNLDoc workflow, run `sldb validate` before finishing.

## Store Architecture

The store is a three-level YAML index cascade (`store_index → models_index → documents_index`) tracking model contracts and their document instances via a Merkle-style hash chain.

Scopes: local (`.sldb/`) takes precedence over global (`~/.sldb/`).

Federation: Link external stores with `sldb store add <path>` to pull models from other repos.

## Cross-Repo Usage

Set `PYTHONPATH` to the root of the repo containing the models:

```bash
PYTHONPATH=/path/to/wikipu sldb validate myapp.docs:RecipeDoc --input recipe.md
```

Or pass `--pythonpath` explicitly:

```bash
sldb validate myapp.docs:RecipeDoc --input recipe.md --pythonpath /path/to/wikipu
```

## Example Bundle

A reference example lives in `sldb_example/`. Use:

```bash
sldb example
```

To unpack the reference bundle locally into a `sldb_example` directory.
