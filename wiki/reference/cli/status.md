---
identity:
  node_id: "doc:wiki/reference/cli/status.md"
  node_type: "reference"
edges:
  - {target_id: "file:src/wiki_compiler/main.py", relation_type: "documents"}
  - {target_id: "file:src/wiki_compiler/perception.py", relation_type: "documents"}
  - {target_id: "code:src/wiki_compiler/perception.py:build_status_report", relation_type: "documents"}
compliance:
  status: "implemented"
  failing_standards: []
---

Reports git-backed drift for graph-tracked files and lists untracked files under `raw/`. This is the first perception-layer runtime surface for detecting when the repository has diverged from the last build.

## Signature or Schema

`wiki-compiler status` reads `knowledge_graph.json`, compares stored `GitFacet.blob_sha` values against the current worktree, and emits JSON describing `modified_nodes` and `untracked_raw_files`.

## Fields

| Flag | Default | Description |
|---|---|---|
| `--graph` | `knowledge_graph.json` | Graph JSON path |
| `--project-root` | `.` | Git repository root to inspect |

## Usage Examples

```bash
wiki-compiler status
```
