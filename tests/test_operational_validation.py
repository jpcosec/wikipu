from __future__ import annotations
from pathlib import Path
import pytest
from wiki_compiler.artifact_validation import validate_wiki_artifact


def write(path: Path, content: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.strip() + "\n", encoding="utf-8")
    return path


def test_validate_task(tmp_path: Path):
    path = write(
        tmp_path / "desk/tasks/test.md",
        """
# Test Task
**Explanation:** Why.
**Reference:** Nodes.
**What to fix:** Result.
**Depends on:** none.
""",
    )
    report = validate_wiki_artifact(path)
    assert report.is_valid is True

    bad_path = write(tmp_path / "desk/tasks/bad.md", "# Missing fields")
    report = validate_wiki_artifact(bad_path)
    assert report.is_valid is False
    assert any(f.rule_id == "task/explanation" for f in report.findings)


def test_validate_gates(tmp_path: Path):
    path = write(
        tmp_path / "desk/Gates.md",
        "| gate_id | proposal | opened | description | status |",
    )
    report = validate_wiki_artifact(path)
    assert report.is_valid is True

    bad_path = write(tmp_path / "desk/Gates.md", "no header")
    report = validate_wiki_artifact(bad_path)
    assert report.is_valid is False
    assert any(f.rule_id == "gates/header" for f in report.findings)


def test_validate_backlog(tmp_path: Path):
    path = write(
        tmp_path / "drawers/idea.md",
        """
# Idea
**Added:** 2026-04-10
**Description:** What.
**Why deferred:** Later.
**Trigger:** Event.
""",
    )
    report = validate_wiki_artifact(path)
    assert report.is_valid is True

    bad_path = write(tmp_path / "drawers/bad.md", "# No metadata")
    report = validate_wiki_artifact(bad_path)
    assert report.is_valid is False
    assert any(f.rule_id == "backlog/trigger" for f in report.findings)


def test_validate_board(tmp_path: Path):
    path = write(
        tmp_path / "desk/Board.md",
        """
# Board
┄┄ Current state
┄┄ Priority roadmap
┄┄ Dependency summary
┄┄ Parallelization map
""",
    )
    report = validate_wiki_artifact(path)
    assert report.is_valid is True

    bad_path = write(tmp_path / "desk/Board.md", "# Just a title")
    report = validate_wiki_artifact(bad_path)
    assert report.is_valid is False
    assert any(f.rule_id == "board/priority_roadmap" for f in report.findings)
