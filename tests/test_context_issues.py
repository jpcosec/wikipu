from __future__ import annotations
import json
from pathlib import Path
import pytest
from wiki_compiler.context import match_active_issues

def test_match_active_issues(tmp_path: Path):
    issues_dir = tmp_path / "plan_docs/issues/unimplemented"
    issues_dir.mkdir(parents=True)
    
    # Issue 1: mentions 'auth'
    issue1 = issues_dir / "auth-fix.md"
    issue1.write_text("# Auth Fix\nMentions auth_module.", encoding="utf-8")
    
    # Issue 2: mentions 'database'
    issue2 = issues_dir / "db-fix.md"
    issue2.write_text("# DB Fix\nMentions database_store.", encoding="utf-8")
    
    # Test by subgraph node names
    subgraph = {"file:src/auth_module.py"}
    matches = match_active_issues(tmp_path, subgraph, None)
    print(f"DEBUG: matches for subgraph {subgraph}: {matches}")
    assert any("auth-fix.md" in m for m in matches)
    assert not any("db-fix.md" in m for m in matches)
    
    # Test by task hint
    matches_hint = match_active_issues(tmp_path, set(), "need to fix database")
    assert any("db-fix.md" in m for m in matches_hint)
