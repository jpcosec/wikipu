---
identity:
  node_id: "doc:wiki/reference/cli/scaffold.md"
  node_type: "reference"
edges:
  - {target_id: "file:src/wiki_compiler/main.py", relation_type: "documents"}
  - {target_id: "file:src/wiki_compiler/scaffolder.py", relation_type: "documents"}
  - {target_id: "code:src/wiki_compiler/scaffolder.py:generate_scaffolding", relation_type: "documents"}
compliance:
  status: "implemented"
  failing_standards: []
---

Creates a new module scaffold that matches Wikipu's expected repository shape. Use it after a design has passed the topology proposal flow and you are ready to create files in `src/`.

## Signature or Schema

`wiki-compiler scaffold` creates the boilerplate files and directories for a new module and seeds them with an intent string. It is the command-level entrypoint for beginning implementation after design approval.

## Fields

| Flag | Default | Description |
|---|---|---|
| `--module` | none | Module path to create |
| `--intent` | none | Human-readable module purpose |

## Usage Examples

```bash
wiki-compiler scaffold --module src/example_module --intent "Score and normalize source documents"
```
