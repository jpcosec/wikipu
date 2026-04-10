---
identity:
  node_id: "doc:wiki/reference/coordinator.md"
  node_type: "doc_standard"
edges:
  - {target_id: "file:src/wiki_compiler/coordinator.py", relation_type: "documents"}
  - {target_id: "code:src/wiki_compiler/coordinator.py:run_coordinator_cycle", relation_type: "documents"}
compliance:
  status: "implemented"
  failing_standards: []
---

The central orchestrator for the autopoietic loop. It coordinates the transition between perception, classification, gating, execution, and rebuild phases.

## Rule Schema

```python
def run_coordinator_cycle(
    project_root: Path,
    graph_path: Path,
    wiki_dir: Path,
    manifest_path: Path | None = None,
) -> dict[str, object]
```

## Fields

- `project_root`: The root directory of the Wikipu repository.
- `graph_path`: Path to the `knowledge_graph.json` file.
- `wiki_dir`: Path to the `wiki/` directory.
- `manifest_path`: Optional path to the content manifest for stale detection.

## Usage Examples

```python
from pathlib import Path
from wiki_compiler.coordinator import run_coordinator_cycle

result = run_coordinator_cycle(
    project_root=Path("."),
    graph_path=Path("knowledge_graph.json"),
    wiki_dir=Path("wiki")
)
print(f"Cycle ID: {result['cycle_id']}")
```
