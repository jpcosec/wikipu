"""
Storage policy and discovery helpers for session logs.
"""

from __future__ import annotations

import json
from pathlib import Path
from .contracts import SessionLog


def get_session_dir(project_root: Path) -> Path:
    """Returns the canonical directory for session logs."""
    return project_root / "desk/autopoiesis/sessions"


def save_session_log(project_root: Path, log: SessionLog) -> Path:
    """Persists a session log to its canonical path."""
    session_dir = get_session_dir(project_root)
    session_dir.mkdir(parents=True, exist_ok=True)
    
    path = session_dir / f"{log.session_id}.json"
    path.write_text(log.model_dump_json(indent=2), encoding="utf-8")
    return path


def load_session_log(project_root: Path, session_id: str) -> SessionLog:
    """Loads a specific session log by ID."""
    path = get_session_dir(project_root) / f"{session_id}.json"
    if not path.exists():
        raise FileNotFoundError(f"Session log not found: {session_id}")
    
    return SessionLog.model_validate_json(path.read_text(encoding="utf-8"))


def list_sessions(project_root: Path) -> list[SessionLog]:
    """Returns all available session logs, sorted by start time."""
    session_dir = get_session_dir(project_root)
    if not session_dir.exists():
        return []
        
    logs: list[SessionLog] = []
    for path in session_dir.glob("*.json"):
        try:
            logs.append(SessionLog.model_validate_json(path.read_text(encoding="utf-8")))
        except Exception:
            continue
            
    return sorted(logs, key=lambda l: l.start_time)


def get_latest_session(project_root: Path) -> SessionLog | None:
    """Returns the most recent session log, or None if none exist."""
    sessions = list_sessions(project_root)
    return sessions[-1] if sessions else None
