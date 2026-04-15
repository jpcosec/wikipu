from __future__ import annotations
import json
from pathlib import Path
import pytest
from wiki_compiler.context import match_active_tasks


def test_match_active_tasks(tmp_path: Path):
    tasks_dir = tmp_path / "desk/tasks"
    tasks_dir.mkdir(parents=True)

    # Task 1: mentions 'auth'
    task1 = tasks_dir / "auth-fix.md"
    task1.write_text("# Auth Fix\nMentions auth_module.", encoding="utf-8")

    # Task 2: mentions 'database'
    task2 = tasks_dir / "db-fix.md"
    task2.write_text("# DB Fix\nMentions database_store.", encoding="utf-8")

    # Test by subgraph node names
    subgraph = {"file:src/auth_module.py"}
    matches = match_active_tasks(tmp_path, subgraph, None)
    print(f"DEBUG: matches for subgraph {subgraph}: {matches}")
    assert any("auth-fix.md" in m for m in matches)
    assert not any("db-fix.md" in m for m in matches)

    # Test by task hint
    matches_hint = match_active_tasks(tmp_path, set(), "need to fix database")
    assert any("db-fix.md" in m for m in matches_hint)
