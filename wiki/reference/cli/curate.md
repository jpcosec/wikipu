---
identity:
  node_id: "doc:wiki/reference/cli/curate.md"
  node_type: "reference"
edges:
  - {target_id: "file:src/wiki_compiler/main.py", relation_type: "documents"}
  - {target_id: "file:src/wiki_compiler/curate.py", relation_type: "documents"}
  - {target_id: "code:src/wiki_compiler/curate.py:score_drafts", relation_type: "documents"}
  - {target_id: "code:src/wiki_compiler/curate.py:promote_draft", relation_type: "documents"}
compliance:
  status: "implemented"
  failing_standards: []
---

Scores draft wiki nodes for promotion readiness and promotes selected drafts into the canonical wiki. This command is the middle step between `wiki-compiler ingest` and durable `wiki/` content.

## Signature or Schema

`wiki-compiler curate` has two modes. `--score` ranks draft nodes by quality signals such as abstract quality, non-fallback node type, and draft file existence. `--promote NODE_ID DEST` moves one draft file into `wiki/<DEST>` and rewrites its `node_id` to match the promoted path.

## Fields

| Flag | Default | Description |
|---|---|---|
| `--score` | none | Score all drafts under `--drafts-dir` |
| `--promote NODE_ID DEST` | none | Promote one draft node to `wiki/<DEST>` |
| `--graph` | `knowledge_graph.json` | Graph JSON used for draft scoring |
| `--drafts-dir` | `wiki/drafts` | Draft wiki directory |
| `--wiki-dir` | `wiki` | Canonical wiki root for promotion |

## Usage Examples

```bash
wiki-compiler curate --score
wiki-compiler curate --promote doc:wiki/drafts/source_a/example.md concepts/example.md
```
