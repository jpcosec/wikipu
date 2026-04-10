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


def _validate_identity_path(
    path: Path, node_id: str
) -> list[ArtifactValidationFinding]:
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


def _validate_adr(path: Path, node: object) -> list[ArtifactValidationFinding]:
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
