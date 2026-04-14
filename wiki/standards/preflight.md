---
identity:
  node_id: "doc:wiki/standards/preflight.md"
  node_type: "doc_standard"
edges:
  - {target_id: "file:src/wiki_compiler/preflight.py", relation_type: "documents"}
  - {target_id: "code:src/wiki_compiler/preflight.py:evaluate_action_safety", relation_type: "documents"}
  - {target_id: "code:src/wiki_compiler/preflight.py:select_minimal_energy_action", relation_type: "documents"}
  - {target_id: "code:src/wiki_compiler/preflight.py:PreflightFinding", relation_type: "documents"}
  - {target_id: "code:src/wiki_compiler/preflight.py:PreflightReport", relation_type: "documents"}
compliance:
  status: "implemented"
  failing_standards: []
---

Preflight validation and minimal-energy action selection for the coordinator. It enforces House Rules ID-1, ID-2, ID-4, and ID-5 before execution, ensuring actions are safe and require the least amount of system perturbation.

## Rule Schema

```python
def evaluate_action_safety(
    action_type: str, 
    target_id: str, 
    project_root: Path
) -> PreflightFinding | None

def select_minimal_energy_action(
    perturbation_type: str,
    target_id: str,
    candidates: list[str]
) -> str
```

## Fields

- `action_type`: The type of action being evaluated (e.g., 'write', 'delete').
- `target_id`: The node ID or path being targeted.
- `candidates`: A list of possible action strings to resolve a perturbation.

## Usage Examples

```python
from wiki_compiler.preflight import evaluate_action_safety
from pathlib import Path

finding = evaluate_action_safety("write", "raw/data.txt", Path("."))
if finding:
    print(f"Blocked by {finding.rule_id}: {finding.message}")
```
