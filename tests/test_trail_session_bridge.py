from __future__ import annotations
import json
from pathlib import Path
import pytest
from wiki_compiler.coordinator import run_coordinator_cycle
from wiki_compiler.builder import build_wiki

def test_run_populates_session_log(tmp_path: Path):
    (tmp_path / "wiki").mkdir()
    (tmp_path / "raw").mkdir()
    graph_path = tmp_path / "knowledge_graph.json"
    build_wiki(tmp_path / "wiki", graph_path, project_root=tmp_path)
    
    # Run cycle
    result = run_coordinator_cycle(tmp_path, graph_path, tmp_path / "wiki")
    
    session_id = result["cycle_id"]
    log_path = tmp_path / f"desk/autopoiesis/sessions/{session_id}.json"
    
    assert log_path.exists()
    log_data = json.loads(log_path.read_text(encoding="utf-8"))
    assert log_data["session_id"] == session_id
    assert "start_time" in log_data
    assert "end_time" in log_data
    assert "trails" in log_data
