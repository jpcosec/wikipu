"""
Configurable Dimensions (Facets) for the Knowledge Graph.
"""

from pydantic import BaseModel, Field
from typing import Literal


class IOFacet(BaseModel):
    """Dimension: Input/Output.

    Question: What data does this node consume or produce?
    """

    medium: Literal["memory", "disk", "network"] = Field(
        description="The medium through which data is transferred."
    )
    direction: Literal["input", "output"] = Field(
        default="input",
        description="The direction of data flow.",
    )
    schema_ref: str | None = Field(
        default=None,
        description="The name of the associated Pydantic model.",
    )
    path_template: str | None = Field(
        default=None,
        description="The disk path template if applicable.",
    )


class ASTFacet(BaseModel):
    """Dimension: The Hows (Code Structure).

    Question: How is this node structured?
    """

    construct_type: Literal["function", "class", "script"] = Field(
        description="The type of code construct."
    )
    signatures: list[str] = Field(
        default_factory=list,
        description="List of method or CLI signatures extracted from the code.",
    )
    dependencies: list[str] = Field(
        default_factory=list,
        description="List of internal contract names this node depends on.",
    )


class SemanticFacet(BaseModel):
    """Dimension: What each thing does and its Docstrings.

    Question: What does this node do?
    """

    intent: str = Field(description="High-level summary of purpose.")
    raw_docstring: str | None = Field(
        default=None,
        description="The raw docstring extracted directly from the code.",
    )


class ADRFacet(BaseModel):
    """Dimension: Historical Decision Records.

    Question: What architectural decisions shaped this node?
    """

    decision_id: str = Field(
        description="Unique identifier for the architectural decision record."
    )
    status: Literal["proposed", "accepted", "deprecated", "superseded"] = Field(
        description="The current status of the architectural decision."
    )
    context_summary: str = Field(
        description="Summary of the context and reasons behind the decision."
    )


class TestMapFacet(BaseModel):
    """Dimension: Testing Strategy and Coverage.

    Question: How is this node tested?
    """

    test_type: Literal["unit", "integration", "e2e", "manual_review"] = Field(
        description="The type of testing applied to this node."
    )
    coverage_percent: float | None = Field(
        default=None,
        description="Percentage of the node covered by automated tests.",
    )


class ComplianceFacet(BaseModel):
    """Dimension: Implementation Status and House Rules Compliance.

    Question: How complete and rule-compliant is this node?
    """

    status: Literal[
        "planned", "scaffolding", "mocked", "implemented", "tested", "exempt"
    ] = Field(description="The current stage of implementation or compliance status.")
    failing_standards: list[str] = Field(
        default_factory=list,
        description="List of rules that this node currently fails to meet.",
    )
    exemption_reason: str | None = Field(
        default=None, description="Reason for exemption if the status is 'exempt'."
    )


class SourceFacet(BaseModel):
    """Dimension: Provenance and Source Tracking.

    Question: Where did this node come from, and is it stale?
    """

    source_path: str = Field(
        description="Relative path to the original raw source file."
    )
    source_hash: str = Field(
        description="Content hash of the raw source at compilation time."
    )
    compiled_at: str = Field(
        description="ISO-8601 timestamp of when the node was compiled."
    )
    compiled_from: str = Field(
        default="wiki-compiler",
        description="The tool or version that performed the compilation.",
    )


class GitFacet(BaseModel):
    """Dimension: Git-tracked state for a file-backed node."""

    blob_sha: str = Field(description="Current blob hash for the file at build time.")
    created_at_commit: str | None = Field(
        default=None,
        description="First commit that introduced the file.",
    )
    last_modified_commit: str | None = Field(
        default=None,
        description="Most recent commit touching the file.",
    )
    last_modified_author: str | None = Field(
        default=None,
        description="Email of the last modifying author.",
    )
    status: Literal["tracked", "untracked", "modified_since_build"] = Field(
        description="Git tracking status known at build or status-check time."
    )
