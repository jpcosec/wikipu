from __future__ import annotations

from pathlib import Path

from wiki_compiler.artifact_validation import validate_wiki_artifact


def write(path: Path, content: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.strip() + "\n", encoding="utf-8")
    return path


def test_validate_wiki_artifact_accepts_valid_concept(tmp_path: Path) -> None:
    path = write(
        tmp_path / "wiki" / "concepts" / "sample.md",
        """
        ---
        identity:
          node_id: "doc:wiki/concepts/sample.md"
          node_type: "concept"
        edges: []
        compliance:
          status: "implemented"
          failing_standards: []
        ---

        This node explains one concept clearly.

        ## Definition

        A definition.

        ## Examples

        One example.

        ## Related Concepts

        Another concept.
        """,
    )

    report = validate_wiki_artifact(path)

    assert report.is_valid is True
    assert report.findings == []


def test_validate_wiki_artifact_reports_missing_abstract(tmp_path: Path) -> None:
    path = write(
        tmp_path / "wiki" / "concepts" / "sample.md",
        """
        ---
        identity:
          node_id: "doc:wiki/concepts/sample.md"
          node_type: "concept"
        edges: []
        compliance:
          status: "implemented"
          failing_standards: []
        ---

        ## Definition

        A definition.
        """,
    )

    report = validate_wiki_artifact(path)

    assert report.is_valid is False
    assert any(f.rule_id == "artifact/abstract" for f in report.findings)


def test_validate_wiki_artifact_reports_adr_filename_mismatch(tmp_path: Path) -> None:
    path = write(
        tmp_path / "wiki" / "adrs" / "002_example.md",
        """
        ---
        identity:
          node_id: "doc:wiki/adrs/002_example.md"
          node_type: "adr"
        adr:
          decision_id: "999"
          status: "accepted"
          context_summary: "Context."
        edges:
          - {target_id: "doc:wiki/standards/house_rules.md", relation_type: "documents"}
        compliance:
          status: "implemented"
          failing_standards: []
        ---

        This ADR records one decision.

        ## Context

        Context.

        ## Decision

        Decision.

        ## Rationale

        Rationale.

        ## Consequences

        Consequences.
        """,
    )

    report = validate_wiki_artifact(path)

    assert report.is_valid is False
    assert any(f.rule_id == "artifact/adr_decision_id" for f in report.findings)


def test_validate_wiki_artifact_reports_missing_frontmatter(tmp_path: Path) -> None:
    path = write(tmp_path / "wiki" / "concepts" / "sample.md", "# No frontmatter")

    report = validate_wiki_artifact(path)

    assert report.is_valid is False
    assert any(f.rule_id == "artifact/frontmatter" for f in report.findings)


def test_validate_wiki_artifact_reports_not_found(tmp_path: Path) -> None:
    report = validate_wiki_artifact(tmp_path / "nonexistent.md")

    assert report.is_valid is False
    assert any(f.rule_id == "artifact/not_found" for f in report.findings)
