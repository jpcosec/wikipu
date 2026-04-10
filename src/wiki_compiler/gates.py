"""
Runtime helpers for managing the desk/Gates.md decision table.
"""

from __future__ import annotations

import re
from pathlib import Path
from datetime import datetime
from .contracts import GateRow, GateTable


def load_gates(gates_path: Path) -> GateTable:
    """Parses desk/Gates.md and returns a GateTable."""
    if not gates_path.exists():
        return GateTable()
    
    content = gates_path.read_text(encoding="utf-8")
    rows: list[GateRow] = []
    
    # Simple markdown table parser
    lines = content.splitlines()
    for line in lines:
        if not line.strip().startswith("|"):
            continue
        if "gate_id" in line.lower() or "---" in line:
            continue
            
        parts = [p.strip() for p in line.split("|") if p.strip()]
        if len(parts) >= 5:
            rows.append(GateRow(
                gate_id=parts[0],
                proposal=parts[1],
                opened=parts[2],
                description=parts[3],
                status=parts[4].lower() # type: ignore
            ))
            
    return GateTable(gates=rows)


def save_gates(gates_path: Path, table: GateTable) -> None:
    """Writes a GateTable to desk/Gates.md in markdown table format."""
    lines = [
        "| gate_id | proposal | opened | description | status |",
        "|---|---|---|---|---|",
    ]
    for gate in table.gates:
        lines.append(f"| {gate.gate_id} | {gate.proposal} | {gate.opened} | {gate.description} | {gate.status} |")
    
    gates_path.parent.mkdir(parents=True, exist_ok=True)
    gates_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def add_gate(
    gates_path: Path, 
    proposal_path: str, 
    description: str,
    gate_id: str | None = None
) -> GateRow:
    """Adds a new open gate to the table."""
    table = load_gates(gates_path)
    
    if gate_id is None:
        # Generate next sequential ID
        existing_ids = []
        for g in table.gates:
            match = re.search(r"gate-(\d+)", g.gate_id)
            if match:
                existing_ids.append(int(match.group(1)))
        
        next_num = max(existing_ids, default=0) + 1
        gate_id = f"gate-{next_num:03d}"
        
    new_gate = GateRow(
        gate_id=gate_id,
        proposal=proposal_path,
        opened=datetime.now().strftime("%Y-%m-%d"),
        description=description,
        status="open"
    )
    
    table.gates.append(new_gate)
    save_gates(gates_path, table)
    return new_gate


def update_gate_status(gates_path: Path, gate_id: str, status: str) -> None:
    """Updates the status of an existing gate."""
    table = load_gates(gates_path)
    for gate in table.gates:
        if gate.gate_id == gate_id:
            gate.status = status # type: ignore
            break
    save_gates(gates_path, table)
