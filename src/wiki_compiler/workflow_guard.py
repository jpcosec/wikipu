"""Checks issue, changelog, and branch discipline for active work."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import subprocess


CHANGE_PREFIXES = {
    "A ",
    "M ",
    "D ",
    "R ",
    "C ",
    "??",
    "AM",
    "MM",
    "MD",
    "RM",
    "RD",
    "UU",
}
IGNORED_PREFIXES = (
    ".obsidian/",
    ".pytest_cache/",
    ".ruff_cache/",
    "__pycache__/",
)
IGNORED_FILES = {
    ".compliance_baseline.json",
}
CODE_PREFIXES = ("src/", "tests/")
DOC_PREFIXES = ("wiki/", "agents/")
DOC_FILES = {"README.md", "AGENTS.md", "changelog.md"}
ISSUE_PREFIX = "desk/issues/"
ISSUE_INDEX = "desk/issues/Board.md"


@dataclass(frozen=True)
class FileChange:
    """A single git-tracked path change."""

    status: str
    path: str


@dataclass(frozen=True)
class WorkflowGuardReport:
    """Result of checking current work against workflow rules."""

    ok: bool
    checked_files: list[str]
    errors: list[str]


def read_git_changes(project_root: Path) -> list[FileChange]:
    """Return tracked and untracked worktree changes from git status."""
    result = subprocess.run(
        ["git", "status", "--short"],
        cwd=project_root,
        check=True,
        capture_output=True,
        text=True,
    )
    changes: list[FileChange] = []
    for raw_line in result.stdout.splitlines():
        if not raw_line:
            continue
        status = raw_line[:2]
        path = raw_line[3:]
        if " -> " in path:
            path = path.split(" -> ", maxsplit=1)[1]
        changes.append(FileChange(status=status, path=path))
    return changes


def read_current_branch(project_root: Path) -> str:
    """Return the current git branch name, or 'unknown' if not in a git repo."""
    try:
        result = subprocess.run(
            ["git", "branch", "--show-current"],
            cwd=project_root,
            capture_output=True,
            text=True,
            check=True,
        )
        return result.stdout.strip() or "main"
    except (subprocess.CalledProcessError, FileNotFoundError):
        return "unknown"


def guard_workflow(
    changes: list[FileChange],
    *,
    branch_name: str,
    allow_structural: bool = False,
) -> WorkflowGuardReport:
    """Validate active work against issue and commit discipline rules."""
    relevant_changes = [change for change in changes if is_relevant_change(change.path)]
    checked_files = sorted(change.path for change in relevant_changes)
    if not relevant_changes:
        return WorkflowGuardReport(ok=True, checked_files=[], errors=[])

    errors: list[str] = []
    paths = {change.path for change in relevant_changes}
    issue_paths = sorted(path for path in paths if path.startswith(ISSUE_PREFIX))
    has_code_changes = any(path.startswith(CODE_PREFIXES) for path in paths)
    has_doc_changes = any(
        path.startswith(DOC_PREFIXES) or path in DOC_FILES for path in paths
    )
    has_changelog = "changelog.md" in paths
    deleted_issue_paths = sorted(
        change.path
        for change in relevant_changes
        if change.path.startswith(ISSUE_PREFIX) and "D" in change.status
    )

    # If we are making code/doc changes, but there are open issues that AREN'T being deleted in this commit, block.
    if has_code_changes and not issue_paths:
        errors.append(
            "Code or test changes require a linked issue under `plan_docs/issues/`. "
            "Create or update an issue before continuing."
        )

    if has_doc_changes and not issue_paths and not allow_structural:
        errors.append(
            "Documentation or process changes require an issue by default. "
            "Use `--allow-structural` only for intentional structural/docs-only work."
        )

    if (has_code_changes or has_doc_changes) and not has_changelog:
        errors.append("Significant work must update `changelog.md` in the same change.")

    if deleted_issue_paths and ISSUE_INDEX not in paths:
        errors.append(
            "Deleting a resolved issue also requires updating `desk/issues/Board.md`."
        )

    if (
        has_code_changes
        and branch_name
        and not branch_name.startswith(("issue/", "phase/"))
    ):
        errors.append(
            "Code changes should happen on an `issue/<name>` or `phase/<name>` branch."
        )

    return WorkflowGuardReport(
        ok=not errors,
        checked_files=checked_files,
        errors=errors,
    )


def is_relevant_change(path: str) -> bool:
    """Return True when a path should count toward workflow discipline checks."""
    if path in IGNORED_FILES:
        return False
    if any(part == "__pycache__" for part in Path(path).parts):
        return False
    return not path.startswith(IGNORED_PREFIXES)
