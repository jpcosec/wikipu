from __future__ import annotations
import json
from pathlib import Path
import pytest
from wiki_compiler.coordinator import run_coordinator_cycle
from wiki_compiler.builder import build_wiki

def test_run_persists_cycle_record(tmp_path: Path):
    (tmp_path / "wiki").mkdir()
    (tmp_path / "raw").mkdir()
    graph_path = tmp_path / "knowledge_graph.json"
    build_wiki(tmp_path / "wiki", graph_path, project_root=tmp_path)
    
    result = run_coordinator_cycle(tmp_path, graph_path, tmp_path / "wiki")
    
    cycle_id = result["cycle_id"]
    record_path = tmp_path / f"desk/autopoiesis/cycles/{cycle_id}.json"
    
    assert record_path.exists()
    record_data = json.loads(record_path.read_text(encoding="utf-8"))
    assert record_data["cycle_id"] == cycle_id
    assert record_data["status"] == "success"
    assert "timestamp" in record_data
