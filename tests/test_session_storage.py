from __future__ import annotations
from pathlib import Path
import pytest
from wiki_compiler.session_storage import save_session_log, load_session_log, list_sessions, get_latest_session
from wiki_compiler.contracts import SessionLog

def test_session_storage_crud(tmp_path: Path):
    log1 = SessionLog(session_id="s1", start_time="2026-04-10T10:00:00")
    log2 = SessionLog(session_id="s2", start_time="2026-04-10T11:00:00")
    
    # Save
    path1 = save_session_log(tmp_path, log1)
    save_session_log(tmp_path, log2)
    assert path1.exists()
    
    # Load
    loaded = load_session_log(tmp_path, "s1")
    assert loaded.session_id == "s1"
    
    # List
    sessions = list_sessions(tmp_path)
    assert len(sessions) == 2
    assert sessions[0].session_id == "s1"
    assert sessions[1].session_id == "s2"
    
    # Latest
    latest = get_latest_session(tmp_path)
    assert latest.session_id == "s2"

def test_load_missing_session(tmp_path: Path):
    with pytest.raises(FileNotFoundError):
        load_session_log(tmp_path, "missing")
