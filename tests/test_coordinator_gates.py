from __future__ import annotations
import json
import networkx as nx
from pathlib import Path
import pytest
from wiki_compiler.coordinator import run_coordinator_cycle
from wiki_compiler.builder import build_wiki
from wiki_compiler.contracts import KnowledgeNode, SystemIdentity, SemanticFacet
from wiki_compiler.graph_utils import add_knowledge_node, save_graph
from wiki_compiler.gates import update_gate_status

def test_coordinator_gate_pause_and_resume(tmp_path: Path):
    # 1. Setup project with a cleansing candidate (compound abstract)
    wiki_dir = tmp_path / "wiki"
    wiki_dir.mkdir()
    (tmp_path / "raw").mkdir()
    (tmp_path / "desk/proposals").mkdir(parents=True)
    
    # Create a compound node
    doc_file = wiki_dir / "compound.md"
    doc_file.write_text("""---
identity:
  node_id: "doc:wiki/compound.md"
  node_type: "concept"
---
This node does A. It also does B.
""", encoding="utf-8")
    
    graph_path = tmp_path / "knowledge_graph.json"
    build_wiki(wiki_dir, graph_path, project_root=tmp_path)
    
    # 2. Run coordinator - should PAUSE and create a gate
    result_1 = run_coordinator_cycle(tmp_path, graph_path, wiki_dir)
    assert result_1["status"] == "paused"
    assert len(result_1["open_gates"]) == 1
    gate_id = result_1["open_gates"][0]
    
    gates_path = tmp_path / "desk/Gates.md"
    assert gates_path.exists()
    assert gate_id in gates_path.read_text()
    
    # 3. Approve the gate manually
    update_gate_status(gates_path, gate_id, "approved")
    
    # 4. Run coordinator again - should RESUME and apply
    # Let's mock a 'destroy' proposal to verify full apply loop
    from wiki_compiler.contracts import CleansingReport, CleansingProposal
    proposal_path = tmp_path / "desk/proposals/test-destroy.json"
    report = CleansingReport(proposals=[
        CleansingProposal(node_id="doc:wiki/compound.md", operation="destroy", rationale="test", affected_nodes=["doc:wiki/compound.md"])
    ])
    proposal_path.write_text(json.dumps(report.model_dump(), indent=2))
    
    # Update gate to point to our test destroy proposal
    from wiki_compiler.gates import load_gates, save_gates
    table = load_gates(gates_path)
    table.gates[0].proposal = "desk/proposals/test-destroy.json"
    table.gates[0].status = "approved"
    save_gates(gates_path, table)
    
    result_2 = run_coordinator_cycle(tmp_path, graph_path, wiki_dir)
    assert result_2["status"] == "success"
    assert any("applied_cleansing" in a for a in result_2["actions_taken"])
    
    # Verify file is gone
    assert not doc_file.exists()
