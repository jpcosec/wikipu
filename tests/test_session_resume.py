from __future__ import annotations
import json
from pathlib import Path
import pytest
from wiki_compiler.coordinator import run_coordinator_cycle
from wiki_compiler.builder import build_wiki

def test_session_resume_linkage(tmp_path: Path):
    (tmp_path / "wiki").mkdir()
    (tmp_path / "raw").mkdir()
    graph_path = tmp_path / "knowledge_graph.json"
    build_wiki(tmp_path / "wiki", graph_path, project_root=tmp_path)
    
    # Run first cycle
    res1 = run_coordinator_cycle(tmp_path, graph_path, tmp_path / "wiki")
    id1 = res1["cycle_id"]
    assert res1["resumed_from"] is None
    
    # Run second cycle
    res2 = run_coordinator_cycle(tmp_path, graph_path, tmp_path / "wiki")
    assert res2["resumed_from"] == id1
