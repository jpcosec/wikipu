from __future__ import annotations
import subprocess
from pathlib import Path
import pytest
from wiki_compiler.session_storage import save_session_log
from wiki_compiler.contracts import SessionLog, TrailCollection, TrailArtifact

def test_history_command_output(tmp_path: Path):
    # 1. Setup mock history
    log = SessionLog(
        session_id="sess-99",
        start_time="2026-04-10T12:00:00",
        branch="feature/test",
        resolved_issues=["G1"],
        trails=TrailCollection(
            session_id="sess-99",
            artifacts=[TrailArtifact(kind="decision", content="Stabilized API", destination="wiki/")]
        )
    )
    save_session_log(tmp_path, log)
    
    # 2. Run CLI
    import os
    env = os.environ.copy()
    env["PYTHONPATH"] = "src"
    
    result = subprocess.run(
        ["python3", "-m", "wiki_compiler.main", "history", "--project-root", str(tmp_path)],
        capture_output=True,
        text=True,
        env=env
    )
    
    assert result.returncode == 0
    assert "Session: sess-99" in result.stdout
    assert "Branch: feature/test" in result.stdout
    assert "Stabilized API" in result.stdout

def test_history_command_empty(tmp_path: Path):
    import os
    env = os.environ.copy()
    env["PYTHONPATH"] = "src"
    
    result = subprocess.run(
        ["python3", "-m", "wiki_compiler.main", "history", "--project-root", str(tmp_path)],
        capture_output=True,
        text=True,
        env=env
    )
    assert "No session history found" in result.stdout
