"""Validation helpers for authored wiki artifacts."""

from __future__ import annotations

from pathlib import Path

from .builder import parse_markdown_node
from .contracts import ArtifactValidationFinding
from .contracts import ArtifactValidationReport


def validate_wiki_artifact(path: Path) -> ArtifactValidationReport:
    """Validate one wiki markdown artifact against implemented local rules."""
    if not path.exists():
        return ArtifactValidationReport(
            path=path.as_posix(),
            is_valid=False,
            findings=[
                ArtifactValidationFinding(
                    rule_id="artifact/not_found",
                    message=f"File not found: {path.as_posix()}",
                )
            ],
        )

    # Dispatch to operational validators if in specific folders
    parts = path.parts
    if "desk" in parts and "tasks" in parts and path.suffix == ".md":
        if path.name != "Board.md":
            return _validate_task(path)
    if path.name == "Gates.md" and "desk" in parts:
        return _validate_gates(path)
    if "drawers" in parts and path.suffix == ".md":
        return _validate_backlog_item(path)
    if path.name == "Board.md" and "desk" in parts:
        return _validate_board(path)

    findings: list[ArtifactValidationFinding] = []

    try:
        node, _ = parse_markdown_node(path)
    except Exception as exc:
        findings.append(
            ArtifactValidationFinding(
                rule_id="artifact/frontmatter",
                message=f"Invalid frontmatter or schema: {exc}",
            )
        )
        return ArtifactValidationReport(
            path=path.as_posix(),
            is_valid=False,
            findings=findings,
        )

    if node is None:
        findings.append(
            ArtifactValidationFinding(
                rule_id="artifact/frontmatter",
                message="Artifact is missing YAML frontmatter.",
            )
        )
        return ArtifactValidationReport(
            path=path.as_posix(),
            is_valid=False,
            findings=findings,
        )

    for missing in node.compliance.failing_standards if node.compliance else []:
        findings.append(
            ArtifactValidationFinding(
                rule_id=f"artifact/{missing}",
                message=f"Missing required section or abstract: {missing}",
            )
        )

    findings.extend(_validate_identity_path(path, node.identity.node_id))
    if node.identity.node_type == "adr":
        findings.extend(_validate_adr(path, node))

    return ArtifactValidationReport(
        path=path.as_posix(),
        is_valid=not findings,
        findings=findings,
    )


def validate_all_artifacts(project_root: Path) -> list[ArtifactValidationReport]:
    """Traverses the repository and validates all wiki and operational artifacts."""
    reports: list[ArtifactValidationReport] = []

    # 1. All markdown files in wiki/
    wiki_dir = project_root / "wiki"
    if wiki_dir.exists():
        for path in wiki_dir.rglob("*.md"):
            reports.append(validate_wiki_artifact(path))

    # 2. All task files in desk/tasks/
    tasks_dir = project_root / "desk/tasks"
    if tasks_dir.exists():
        for path in tasks_dir.rglob("*.md"):
            if path.name != "Board.md":
                reports.append(validate_wiki_artifact(path))

    # 3. All backlog items in drawers/
    drawers_dir = project_root / "drawers"
    if drawers_dir.exists():
        for path in drawers_dir.rglob("*.md"):
            reports.append(validate_wiki_artifact(path))

    # 4. Operational files in desk/
    desk_dir = project_root / "desk"
    if desk_dir.exists():
        gates_path = desk_dir / "Gates.md"
        if gates_path.exists():
            reports.append(validate_wiki_artifact(gates_path))

        for board_path in desk_dir.rglob("Board.md"):
            reports.append(validate_wiki_artifact(board_path))

    return reports


def _validate_identity_path(
    path: Path, node_id: str
) -> list[ArtifactValidationFinding]:
    """Validate the node_id matches the expected path format."""
    expected = f"doc:{_repo_style_path(path)}"
    if node_id == expected:
        return []
    return [
        ArtifactValidationFinding(
            rule_id="artifact/node_id_path",
            message=f"node_id must match file path: expected {expected}",
        )
    ]


def _repo_style_path(path: Path) -> str:
    """Convert a filesystem path to the repo-style path used by node_id values."""
    parts = path.parts
    if "wiki" in parts:
        return Path(*parts[parts.index("wiki") :]).as_posix()
    if "agents" in parts:
        return Path(*parts[parts.index("agents") :]).as_posix()
    return path.as_posix()


def _validate_task(path: Path) -> ArtifactValidationReport:
    """Validate a task file has required sections."""
    content = path.read_text(encoding="utf-8")
    findings: list[ArtifactValidationFinding] = []

    required_sections = ["Explanation", "Reference", "What to fix", "Depends on"]
    for section in required_sections:
        if f"**{section}:**" not in content:
            findings.append(
                ArtifactValidationFinding(
                    rule_id=f"task/{section.lower().replace(' ', '_')}",
                    message=f"Task missing required field: {section}",
                )
            )

    if not content.startswith("# "):
        findings.append(
            ArtifactValidationFinding(
                rule_id="task/title", message="Task must start with an H1 title."
            )
        )

    return ArtifactValidationReport(
        path=path.as_posix(), is_valid=not findings, findings=findings
    )


def _validate_gates(path: Path) -> ArtifactValidationReport:
    """Validate a gates file has required table structure."""
    content = path.read_text(encoding="utf-8")
    findings: list[ArtifactValidationFinding] = []

    if "| gate_id | proposal | opened | description | status |" not in content:
        findings.append(
            ArtifactValidationFinding(
                rule_id="gates/header",
                message="Gates.md missing required table header.",
            )
        )

    return ArtifactValidationReport(
        path=path.as_posix(), is_valid=not findings, findings=findings
    )


def _validate_backlog_item(path: Path) -> ArtifactValidationReport:
    """Validate a backlog item file has required fields."""
    content = path.read_text(encoding="utf-8")
    findings: list[ArtifactValidationFinding] = []

    required = ["**Added:**", "**Description:**", "**Why deferred:**", "**Trigger:**"]
    for req in required:
        if req not in content:
            findings.append(
                ArtifactValidationFinding(
                    rule_id=f"backlog/{req.strip(':*').lower().replace(' ', '_')}",
                    message=f"Backlog item missing required field: {req}",
                )
            )

    return ArtifactValidationReport(
        path=path.as_posix(), is_valid=not findings, findings=findings
    )


def _validate_board(path: Path) -> ArtifactValidationReport:
    """Validate a board file has required structure."""
    content = path.read_text(encoding="utf-8")
    findings: list[ArtifactValidationFinding] = []

    required_headers = [
        "Current state",
        "Priority roadmap",
        "Dependency summary",
        "Parallelization map",
    ]
    for header in required_headers:
        if f"┄┄ {header}" not in content:
            findings.append(
                ArtifactValidationFinding(
                    rule_id=f"board/{header.lower().replace(' ', '_')}",
                    message=f"Board missing required section: {header}",
                )
            )

    return ArtifactValidationReport(
        path=path.as_posix(), is_valid=not findings, findings=findings
    )


def _validate_adr(path: Path, node: object) -> list[ArtifactValidationFinding]:
    """Validate an ADR file has required structure."""
    findings: list[ArtifactValidationFinding] = []
    adr = getattr(node, "adr", None)
    if adr is None:
        findings.append(
            ArtifactValidationFinding(
                rule_id="artifact/adr_frontmatter",
                message="ADR nodes must declare an `adr` frontmatter block.",
            )
        )
        return findings

    filename_prefix = path.stem.split("_", maxsplit=1)[0]
    if adr.decision_id != filename_prefix:
        findings.append(
            ArtifactValidationFinding(
                rule_id="artifact/adr_decision_id",
                message="ADR decision_id must match the filename prefix.",
            )
        )

    has_documents_edge = any(edge.relation_type == "documents" for edge in node.edges)
    if not has_documents_edge:
        findings.append(
            ArtifactValidationFinding(
                rule_id="artifact/adr_documents_edge",
                message="ADR nodes must include at least one `documents` edge.",
            )
        )
    return findings
