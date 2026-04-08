---
identity:
  node_id: "doc:wiki/reference/builder.md"
  node_type: "doc_standard"
edges:
  - target_id: "file:src/wiki_compiler/builder.py"
    relation_type: documents
  - target_id: "code:src/wiki_compiler/builder.py:BuildResult"
    relation_type: documents
  - target_id: "code:src/wiki_compiler/builder.py:build_wiki"
    relation_type: documents
  - target_id: "code:src/wiki_compiler/builder.py:build_directory_skeleton"
    relation_type: documents
  - target_id: "code:src/wiki_compiler/builder.py:index_markdown_files"
    relation_type: documents
  - target_id: "code:src/wiki_compiler/builder.py:parse_markdown_node"
    relation_type: documents
  - target_id: "code:src/wiki_compiler/builder.py:extract_heading"
    relation_type: documents
  - target_id: "code:src/wiki_compiler/builder.py:extract_transclusions"
    relation_type: documents
  - target_id: "code:src/wiki_compiler/builder.py:calculate_compliance_score"
    relation_type: documents
  - target_id: "code:src/wiki_compiler/builder.py:update_compliance_baseline"
    relation_type: documents
  - target_id: "code:src/wiki_compiler/builder.py:write_baseline"
    relation_type: documents
---

Builds the Knowledge Graph by scanning Markdown wiki nodes and Python source code. It orchestrates the multi-phase compilation: directory skeleton, node ingestion, and facet injection.

## Signature or Schema

```python
def build_wiki(
    source_dir: Path,
    graph_path: Path,
    *,
    project_root: Path | None = None,
    code_roots: list[Path] | None = None,
    baseline_path: Path | None = None,
    update_baseline: bool = False,
) -> BuildResult
```

## Fields

- `BuildResult.graph_path`: Path to the generated `knowledge_graph.json`.
- `BuildResult.compliance_score`: Percentage of compliant nodes.
- `BuildResult.baseline_updated`: Boolean indicating if the baseline was written or updated.

## Usage Examples

```python
from pathlib import Path
from wiki_compiler.builder import build_wiki

result = build_wiki(
    source_dir=Path("wiki"),
    graph_path=Path("knowledge_graph.json"),
    project_root=Path("."),
    update_baseline=True
)
print(f"Compliance Score: {result.compliance_score}%")
```
