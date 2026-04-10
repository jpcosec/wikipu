from __future__ import annotations
import json
import pytest
from wiki_compiler.contracts import SessionLog, TrailCollection, TrailArtifact

def test_session_log_serialization():
    trail = TrailCollection(
        session_id="sess-1",
        artifacts=[TrailArtifact(kind="decision", content="Use Pydantic", destination="contracts.py")]
    )
    log = SessionLog(
        session_id="sess-1",
        start_time="2026-04-10T10:00:00",
        branch="main",
        resolved_issues=["issue-1"],
        trails=trail
    )
    
    data = log.model_dump()
    assert data["session_id"] == "sess-1"
    assert data["trails"]["artifacts"][0]["kind"] == "decision"
    
    # Round trip
    log2 = SessionLog.model_validate(data)
    assert log2.session_id == "sess-1"
    assert len(log2.trails.artifacts) == 1
