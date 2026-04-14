---
identity:
  node_id: "doc:wiki/standards/trails.md"
  node_type: "doc_standard"
edges:
  - {target_id: "file:src/wiki_compiler/trails.py", relation_type: "documents"}
  - {target_id: "code:src/wiki_compiler/trails.py:collect_cycle_trails", relation_type: "documents"}
  - {target_id: "code:src/wiki_compiler/trails.py:persist_trail", relation_type: "documents"}
compliance:
  status: "implemented"
  failing_standards: []
---

Implements the trail-collect closeout step for distilling durable facts and artifacts from autopoietic cycles. Classifies cycle outcomes into classification categories like `correction` or `new_concept`.

## Rule Schema

```python
def collect_cycle_trails(
    session_id: str, 
    actions_taken: list[str], 
    perturbations: int
) -> TrailCollection

def persist_trail(project_root: Path, collection: TrailCollection) -> Path
```

## Fields

- `session_id`: Unique ID of the cycle being closed out.
- `actions_taken`: List of strings describing the actions performed by the coordinator.
- `perturbations`: Number of system perturbations detected during the cycle.

## Usage Examples

```python
from wiki_compiler.trails import collect_cycle_trails, persist_trail
from pathlib import Path

trail = collect_cycle_trails("cycle-123", ["ingested_raw_files"], 1)
persist_trail(Path("."), trail)
```
