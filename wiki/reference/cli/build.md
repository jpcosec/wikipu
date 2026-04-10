---
identity:
  node_id: "doc:wiki/reference/cli/build.md"
  node_type: "reference"
edges:
  - {target_id: "file:src/wiki_compiler/main.py", relation_type: "documents"}
  - {target_id: "file:src/wiki_compiler/builder.py", relation_type: "documents"}
  - {target_id: "code:src/wiki_compiler/builder.py:build_wiki", relation_type: "documents"}
compliance:
  status: "implemented"
  failing_standards: []
---

Compiles all wiki Markdown nodes into a NetworkX knowledge graph, runs facet injection passes, calculates a compliance score, and optionally checks or updates a persistent compliance baseline. This is the primary command for regenerating `knowledge_graph.json` after any wiki or source change.

## Signature or Schema

`wiki-compiler build` performs a multi-phase compilation: it scans the wiki directory for Markdown nodes, scans Python source directories for code constructs, injects ADR and test-map facets, then saves the resulting graph to a JSON file. It reports a compliance score and exits non-zero if the score has regressed against the stored baseline.

## Fields

```
wiki-compiler build [OPTIONS]
```

| Flag | Default | Description |
|---|---|---|
| `--source` | `wiki` | Source wiki directory to scan for Markdown nodes |
| `--graph` | `knowledge_graph.json` | Output path for the NetworkX JSON graph |
| `--project-root` | `.` | Project root used for Python source scanning |
| `--code-root` | `src` | Python source root to scan (repeatable) |
| `--baseline` | `.compliance_baseline.json` | Path to the compliance baseline file |
| `--update-baseline` | `false` | When set, overwrites the stored baseline with the current score |

## Usage Examples

```bash
# Basic build from the project root
wiki-compiler build

# Build with a custom wiki directory and output path
wiki-compiler build --source docs/wiki --graph artifacts/graph.json

# Scan multiple code roots
wiki-compiler build --code-root src --code-root lib

# Update the stored compliance baseline after intentional score change
wiki-compiler build --update-baseline
```
