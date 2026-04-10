from __future__ import annotations
from pathlib import Path
import pytest
from wiki_compiler.gates import load_gates, save_gates, add_gate, update_gate_status
from wiki_compiler.contracts import GateRow, GateTable

def test_load_gates(tmp_path: Path):
    gates_path = tmp_path / "desk/Gates.md"
    gates_path.parent.mkdir()
    gates_path.write_text("""
| gate_id | proposal | opened | description | status |
|---|---|---|---|---|
| gate-001 | desk/proposals/p1.md | 2026-04-10 | test p1 | open |
| gate-002 | desk/proposals/p2.md | 2026-04-10 | test p2 | approved |
""", encoding="utf-8")
    
    table = load_gates(gates_path)
    assert len(table.gates) == 2
    assert table.gates[0].gate_id == "gate-001"
    assert table.gates[1].status == "approved"

def test_add_gate_sequential(tmp_path: Path):
    gates_path = tmp_path / "desk/Gates.md"
    gates_path.parent.mkdir()
    gates_path.write_text("| gate_id | proposal | opened | description | status |\n|---|---|---|---|---|", encoding="utf-8")
    
    add_gate(gates_path, "desk/proposals/p1.md", "desc 1")
    add_gate(gates_path, "desk/proposals/p2.md", "desc 2")
    
    table = load_gates(gates_path)
    assert table.gates[0].gate_id == "gate-001"
    assert table.gates[1].gate_id == "gate-002"

def test_update_gate_status(tmp_path: Path):
    gates_path = tmp_path / "desk/Gates.md"
    gates_path.parent.mkdir()
    add_gate(gates_path, "desk/proposals/p1.md", "desc 1")
    
    update_gate_status(gates_path, "gate-001", "approved")
    
    table = load_gates(gates_path)
    assert table.gates[0].status == "approved"
