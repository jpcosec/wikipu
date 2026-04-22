---
identity:
  node_id: "doc:wiki/reference/cli/context.md"
  node_type: "reference"
edges:
  - {target_id: "file:src/wiki_compiler/main.py", relation_type: "documents"}
  - {target_id: "code:src/wiki_compiler/main.py", relation_type: "documents"}
compliance:
  status: "implemented"
  failing_standards: []
---

Renders focused subgraphs from the compiled knowledge graph for efficient context extraction. This command enables agents to retrieve just enough information for specific tasks without loading the entire graph.

## Signature or Schema

`wiki-compiler context` extracts node neighborhoods and renders them in various formats for consumption by agents and other tools.

## Fields

| Flag | Default | Description |
|---|---|---|
| `--node-id` | none | Root node for context extraction |
| `--depth` | 2 | Traversal depth for neighborhood |
| `--format` | json | Output format: `json`, `markdown`, `summary` |
| `--relation-filter` | none | Restrict to specific relation types |

## Examples

```bash
# Get 2-hop neighborhood around a node
wiki-compiler context --node-id doc:wiki/concepts/energy.md

# Get deeper context for code exploration
wiki-compiler context --node-id file:src/wiki_compiler/energy.py --depth 3

# Summary format for quick overview
wiki-compiler context --node-id doc:wiki/Index.md --format summary
```

## Usage Examples

```bash
# Get 2-hop neighborhood around a node
wiki-compiler context --node-id doc:wiki/concepts/energy.md

# Get deeper context for code exploration
wiki-compiler context --node-id file:src/wiki_compiler/energy.py --depth 3

# Summary format for quick overview
wiki-compiler context --node-id doc:wiki/Index.md --format summary

# Filter by relation type
wiki-compiler context --node-id doc:wiki/Index.md --relation-filter contains
```

## Related Commands

- [[wiki/reference/cli/query.md]] — Full graph queries
- [[wiki/reference/cli/status.md]] — System status