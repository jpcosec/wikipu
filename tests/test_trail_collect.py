from __future__ import annotations
import json
from pathlib import Path
import pytest
from wiki_compiler.trails import collect_cycle_trails, persist_trail

def test_collect_cycle_trails_classification():
    session_id = "test-session"
    actions = ["applied_cleansing_gate-001", "ingested_raw_files", "rebuilt_graph"]
    
    collection = collect_cycle_trails(session_id, actions, 2)
    
    kinds = [a.kind for a in collection.artifacts]
    assert "correction" in kinds
    assert "new_concept" in kinds
    assert len(collection.artifacts) == 2

def test_persist_trail(tmp_path: Path):
    from wiki_compiler.contracts import TrailCollection, TrailArtifact
    collection = TrailCollection(
        session_id="session-123",
        artifacts=[TrailArtifact(kind="gap", content="Missing tests", destination="desk/issues/")]
    )
    
    path = persist_trail(tmp_path, collection)
    assert path.exists()
    assert "session-123.json" in path.name
    
    data = json.loads(path.read_text(encoding="utf-8"))
    assert data["session_id"] == "session-123"
    assert data["artifacts"][0]["kind"] == "gap"
