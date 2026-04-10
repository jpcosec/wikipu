from __future__ import annotations
import pytest
from pathlib import Path
from wiki_compiler.context import load_relevant_checklists

def test_load_relevant_checklists(tmp_path: Path):
    # Setup mock checklists.md
    standards_dir = tmp_path / "wiki/standards"
    standards_dir.mkdir(parents=True)
    checklist_file = standards_dir / "checklists.md"
    checklist_file.write_text("""
### 1. Issue Resolution Checklist (`issue-resolution`)
1. **Tests Pass?** (OP-4.3) — ... `Verification:` `pytest`
2. **Changelog?** (OP-4.4) — ... `Verification:` `ls`
""", encoding="utf-8")
    
    # Match by keyword
    checklists = load_relevant_checklists(tmp_path, "I am working on an issue")
    assert len(checklists) == 1
    assert checklists[0].name == "issue-resolution"
    assert len(checklists[0].items) == 2
    assert checklists[0].items[0].description == "Tests Pass?"
    assert checklists[0].items[0].rule_id == "OP-4.3"
    assert checklists[0].items[0].verification == "pytest"

def test_load_relevant_checklists_no_match(tmp_path: Path):
    checklists = load_relevant_checklists(tmp_path, "nothing relevant")
    assert len(checklists) == 0
