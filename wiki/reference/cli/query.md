---
identity:
  node_id: "doc:wiki/reference/cli/query.md"
  node_type: "reference"
edges:
  - {target_id: "file:src/wiki_compiler/main.py", relation_type: "documents"}
  - {target_id: "file:src/wiki_compiler/query_server.py", relation_type: "documents"}
  - {target_id: "code:src/wiki_compiler/query_server.py:query_main", relation_type: "documents"}
compliance:
  status: "implemented"
  failing_standards: []
---

Queries the compiled knowledge graph for nodes, graph neighborhoods, and I/O matches. This command is the direct runtime surface agents and humans use for graph-first navigation.

## Signature or Schema

`wiki-compiler query` supports direct node lookup, ancestor and descendant traversal, I/O matching, and JSON-file-backed `StructuredQuery` execution. It reads `knowledge_graph.json` and returns JSON describing the matched node schemas.

## Fields

| Flag | Default | Description |
|---|---|---|
| `--graph` | `knowledge_graph.json` | Graph JSON path |
| `--type` | none | Query type: `get_node`, `get_ancestors`, `get_descendants`, `find_by_io` |
| `--node-id` | none | Node identifier for direct or traversal queries |
| `--relation-filter` | none | Restrict traversal to one relation type |
| `--medium` | none | Filter by I/O medium |
| `--schema-ref` | none | Filter by I/O schema reference |
| `--path-template` | none | Filter by I/O path template |
| `--query-file` | none | Path to a `StructuredQuery` JSON payload |

## Usage Examples

```bash
wiki-compiler query --type get_node --node-id file:src/wiki_compiler/main.py
wiki-compiler query --type get_descendants --node-id doc:wiki/Index.md
wiki-compiler query --type find_by_io --path-template knowledge_graph.json
```
