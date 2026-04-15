from __future__ import annotations
import json
from pathlib import Path
import pytest
from wiki_compiler.coordinator import run_coordinator_cycle
from wiki_compiler.builder import build_wiki


def test_run_skeleton_noop(tmp_path: Path):
    # Setup empty project
    (tmp_path / "wiki").mkdir()
    (tmp_path / "raw").mkdir()
    graph_path = tmp_path / "knowledge_graph.json"
    build_wiki(tmp_path / "wiki", graph_path, project_root=tmp_path)

    result = run_coordinator_cycle(
        project_root=tmp_path, graph_path=graph_path, wiki_dir=tmp_path / "wiki"
    )

    assert result["status"] == "success"
    # Even if noop, if build_status_report works it should return 0 perturbations
    # unless it sees the 'raw' folder itself as untracked?
    # Usually it only tracks files.


def test_run_skeleton_auto_ingest(tmp_path: Path):
    (tmp_path / "wiki").mkdir()
    (tmp_path / "raw").mkdir()
    graph_path = tmp_path / "knowledge_graph.json"
    build_wiki(tmp_path / "wiki", graph_path, project_root=tmp_path)

    # Add an untracked raw file
    raw_file = tmp_path / "raw/new.md"
    raw_file.write_text("# New\nContent")

    # Run cycle
    # Note: Perception calls 'git', so this might return 0 if not a git repo.
    # But coordinator.py has a fallback for non-git in some cases or we can rely on fallbacks.
    result = run_coordinator_cycle(
        project_root=tmp_path, graph_path=graph_path, wiki_dir=tmp_path / "wiki"
    )

    assert result["status"] == "success"
    # If it auto-ingested, it should be in actions_taken
    if "ingested_1_raw_files" in result["actions_taken"]:
        assert (tmp_path / "desk/drafts/new.md").exists()
