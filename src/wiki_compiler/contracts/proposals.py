"""
Closed Loop Orthogonality and Circuit Breaker models.
"""

from pydantic import BaseModel, Field
from typing import Literal, Any

from .node import KnowledgeNode


class AuditFinding(BaseModel):
    """A finding from an audit check."""

    check_name: str = Field(
        description="The name of the audit check that produced this finding."
    )
    node_id: str = Field(description="The ID of the node that failed the check.")
    detail: str = Field(description="A detailed explanation of the failure.")


class FacetProposal(BaseModel):
    """
    A proposal to add a new facet dimension to the registry.
    """

    proposed_facet_name: str = Field(description="Snake_case name for the new facet.")
    question: str = Field(description="The single question this facet answers.")
    applies_to: list[str] = Field(description="Node types this facet is relevant for.")
    proposed_fields: list[dict[str, str]] = Field(
        description="List of {name, type} dicts for the facet's fields."
    )
    attempted_query: dict | None = Field(
        default=None,
        description="Serialised StructuredQuery. If provided and returns results, proposal is rejected.",
    )


class FacetOrthogonalityReport(BaseModel):
    """Response from validate_facet_proposal."""

    is_orthogonal: bool = Field(
        description="True if the proposal is orthogonal; False otherwise."
    )
    colliding_facets: list[Any] = Field(
        default_factory=list,
        description="Existing facets whose questions overlap with the proposal.",
    )
    field_collisions: list[str] = Field(
        default_factory=list,
        description="'field_name (existing_facet)' strings for each field collision.",
    )
    query_already_answered: bool = Field(
        default=False,
        description="True if the attempted_query returned results.",
    )
    resolution_suggestion: str | None = Field(
        default=None, description="A suggestion for resolving the collision."
    )
    attempts_remaining: int = Field(
        description="The number of attempts remaining for the agent."
    )


class TopologyProposal(BaseModel):
    """
    A proposal for a new module design.
    """

    proposed_module_name: str = Field(
        description="The proposed name for the new module."
    )
    intent: str = Field(
        description="The high-level purpose or intent of the proposed module."
    )
    glossary_terms_used: list[str] = Field(
        description="List of terms this proposal uses."
    )
    proposed_inputs: list[Any] = Field(
        description="A list of proposed input I/O ports for the module."
    )
    proposed_outputs: list[Any] = Field(
        description="A list of proposed output I/O ports for the module."
    )


class CollisionReport(BaseModel):
    """Response to a TopologyProposal."""

    is_orthogonal: bool = Field(
        description="True if the proposal is orthogonal; False otherwise."
    )
    colliding_node_schemas: list[KnowledgeNode] = Field(
        description="Full schemas of existing nodes that collide with the proposal."
    )
    resolution_suggestion: str | None = Field(
        default=None,
        description="A suggestion for resolving the collision.",
    )
    attempts_remaining: int = Field(
        description="Attempts remaining before human intervention."
    )


class ArtifactValidationFinding(BaseModel):
    """A single validation failure for an authored artifact file."""

    rule_id: str = Field(description="The rule identifier that failed validation.")
    message: str = Field(
        description="Human-readable explanation of the validation failure."
    )


class ArtifactValidationReport(BaseModel):
    """Validation result for one authored artifact file."""

    path: str = Field(
        description="Repository-relative or absolute path to the validated artifact."
    )
    is_valid: bool = Field(
        description="True when the artifact passes all implemented checks."
    )
    findings: list[ArtifactValidationFinding] = Field(
        default_factory=list,
        description="Rule-level validation failures for the artifact.",
    )


class CleansingProposal(BaseModel):
    """A proposed corrective operation for an existing graph node."""

    node_id: str = Field(description="Primary node targeted by the proposal.")
    operation: Literal["destroy", "relocate", "split", "merge"] = Field(
        description="Structural operation proposed for the node."
    )
    rationale: str = Field(description="Why this corrective action is being proposed.")
    affected_nodes: list[str] = Field(
        default_factory=list,
        description="All nodes implicated in the proposed operation.",
    )
    requires_human_approval: bool = Field(
        default=True,
        description="Whether the proposal requires explicit approval.",
    )


class CleansingReport(BaseModel):
    """Machine-readable output of cleansing candidate detection."""

    proposals: list[CleansingProposal] = Field(
        default_factory=list,
        description="Detected structural correction proposals.",
    )
