---
identity:
  node_id: "doc:wiki/reference/drafts.md"
  node_type: "doc_standard"
edges:
  - {target_id: "file:src/wiki_compiler/drafts.py", relation_type: "documents"}
  - {target_id: "code:src/wiki_compiler/drafts.py:detect_stale_nodes", relation_type: "documents"}
  - {target_id: "code:src/wiki_compiler/drafts.py:write_stale_drafts", relation_type: "documents"}
  - {target_id: "code:src/wiki_compiler/drafts.py:promote_draft_node", relation_type: "documents"}
compliance:
  status: "implemented"
  failing_standards: []
---

Manages the delta-compile and draft-write workflow for stale wiki nodes. Detects when raw sources have changed compared to their graph representations and handles regenerating draft stubs and promoting them.

## Rule Schema

```python
def detect_stale_nodes(graph_path: Path, manifest_path: Path) -> list[str]
def write_stale_drafts(
    graph_path: Path, 
    manifest_path: Path, 
    drafts_dir: Path,
    project_root: Path = Path(".")
) -> list[Path]
def promote_draft_node(
    node_id: str, 
    drafts_dir: Path, 
    project_root: Path = Path(".")
) -> Path
```

## Fields

- `graph_path`: Path to the `knowledge_graph.json` file.
- `manifest_path`: Path to the raw source CSV manifest.
- `drafts_dir`: Path to the `wiki/drafts/` directory.

## Usage Examples

```python
from wiki_compiler.drafts import detect_stale_nodes
from pathlib import Path

stale = detect_stale_nodes(Path("knowledge_graph.json"), Path("manifest.csv"))
print(f"Found {len(stale)} stale nodes.")
```
