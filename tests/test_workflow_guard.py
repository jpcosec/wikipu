from __future__ import annotations

from wiki_compiler.workflow_guard import FileChange
from wiki_compiler.workflow_guard import guard_workflow


def test_guard_requires_issue_for_code_changes() -> None:
    report = guard_workflow(
        [
            FileChange(status="M ", path="src/wiki_compiler/main.py"),
            FileChange(status="M ", path="changelog.md"),
        ],
        branch_name="issue/workflow-guard",
    )

    assert report.ok is False
    assert any("linked issue" in error for error in report.errors)


def test_guard_accepts_code_changes_with_issue_and_changelog() -> None:
    report = guard_workflow(
        [
            FileChange(status="M ", path="src/wiki_compiler/main.py"),
            FileChange(status="M ", path="tests/test_workflow_guard.py"),
            FileChange(status="M ", path="plan_docs/issues/gaps/workflow.md"),
            FileChange(status="M ", path="changelog.md"),
        ],
        branch_name="issue/workflow-guard",
    )

    assert report.ok is True


def test_guard_requires_issue_index_when_issue_deleted() -> None:
    report = guard_workflow(
        [
            FileChange(status="D ", path="plan_docs/issues/gaps/workflow.md"),
            FileChange(status="M ", path="src/wiki_compiler/main.py"),
            FileChange(status="M ", path="changelog.md"),
        ],
        branch_name="issue/workflow-guard",
    )

    assert report.ok is False
    assert any("Index.md" in error for error in report.errors)


def test_guard_allows_structural_docs_with_override() -> None:
    report = guard_workflow(
        [
            FileChange(status="M ", path="wiki/standards/document_topology.md"),
            FileChange(status="M ", path="AGENTS.md"),
            FileChange(status="M ", path="changelog.md"),
        ],
        branch_name="phase/wiki-topology",
        allow_structural=True,
    )

    assert report.ok is True


def test_guard_requires_issue_or_override_for_docs_changes() -> None:
    report = guard_workflow(
        [
            FileChange(status="M ", path="wiki/standards/document_topology.md"),
            FileChange(status="M ", path="changelog.md"),
        ],
        branch_name="phase/wiki-topology",
    )

    assert report.ok is False
    assert any("docs-only" in error for error in report.errors)


def test_guard_requires_issue_or_phase_branch_for_code_changes() -> None:
    report = guard_workflow(
        [
            FileChange(status="M ", path="src/wiki_compiler/main.py"),
            FileChange(status="M ", path="plan_docs/issues/gaps/workflow.md"),
            FileChange(status="M ", path="changelog.md"),
        ],
        branch_name="main",
    )

    assert report.ok is False
    assert any(
        "issue/<name>` or `phase/<name>` branch" in error for error in report.errors
    )
