from __future__ import annotations
from pathlib import Path
import pytest
from wiki_compiler.scaffolder import bootstrap_repository, upgrade_repository

def test_bootstrap_repository(tmp_path: Path):
    project_root = tmp_path / "new_project"
    bootstrap_repository(project_root, "Test Project")
    
    expected_dirs = [
        "raw", "wiki/adrs", "wiki/concepts", "wiki/how_to", "wiki/reference",
        "wiki/standards/artifacts", "wiki/standards/languages",
        "manifests", "desk/proposals", "desk/autopoiesis/cycles",
        "plan_docs/issues/gaps", "plan_docs/issues/unimplemented",
        "future_docs", "src", "tests"
    ]
    for d in expected_dirs:
        assert (project_root / d).is_dir()
        assert (project_root / d / ".gitkeep").exists()
        
    assert (project_root / "wiki/Index.md").exists()
    assert (project_root / "desk/Gates.md").exists()
    assert "Test Project" in (project_root / "wiki/Index.md").read_text()

def test_upgrade_repository(tmp_path: Path):
    # Setup a "legacy" project structure (pre-1.1.0)
    project_root = tmp_path / "legacy_project"
    project_root.mkdir()
    (project_root / "wiki").mkdir()
    (project_root / "raw").mkdir()
    
    # Run upgrade
    upgrade_repository(project_root)
    
    # New 1.1.0 components should exist
    assert (project_root / "manifests").is_dir()
    assert (project_root / "desk/proposals").is_dir()
    assert (project_root / "desk/Gates.md").exists()
    assert (project_root / "desk/autopoiesis/cycles").is_dir()
