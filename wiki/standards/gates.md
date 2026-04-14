---
identity:
  node_id: "doc:wiki/standards/gates.md"
  node_type: "doc_standard"
edges:
  - {target_id: "file:src/wiki_compiler/gates.py", relation_type: "documents"}
  - {target_id: "code:src/wiki_compiler/gates.py:load_gates", relation_type: "documents"}
  - {target_id: "code:src/wiki_compiler/gates.py:save_gates", relation_type: "documents"}
  - {target_id: "code:src/wiki_compiler/gates.py:add_gate", relation_type: "documents"}
  - {target_id: "code:src/wiki_compiler/gates.py:update_gate_status", relation_type: "documents"}
compliance:
  status: "implemented"
  failing_standards: []
---

Runtime helpers for managing the `desk/Gates.md` decision table. Handles parsing the markdown table into `GateTable` objects, adding new gates, and saving updates back to the file.

## Rule Schema

```python
def load_gates(gates_path: Path) -> GateTable
def save_gates(gates_path: Path, table: GateTable) -> None
def add_gate(
    gates_path: Path, 
    proposal_path: str, 
    description: str,
    gate_id: str | None = None
) -> GateRow
def update_gate_status(gates_path: Path, gate_id: str, status: str) -> None
```

## Fields

- `gates_path`: Path to the `desk/Gates.md` file.
- `table`: A `GateTable` Pydantic model instance.
- `gate_id`: Unique identifier for the gate (e.g., `gate-001`).
- `status`: The new status string (e.g., 'approved', 'rejected').

## Usage Examples

```python
from wiki_compiler.gates import load_gates, update_gate_status
from pathlib import Path

gates_file = Path("desk/Gates.md")
table = load_gates(gates_file)
for gate in table.gates:
    if gate.status == "open":
        print(f"Pending: {gate.proposal}")
```
