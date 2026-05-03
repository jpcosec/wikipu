from __future__ import annotations
from pydantic import BaseModel, Field
from typing import Literal, Any

# Foundational Contracts from other layers
from kgdb.contracts.node import Edge, KnowledgeNode, SystemIdentity
from ontology.contracts.facets import ComplianceFacet, GitFacet, ASTFacet, SemanticFacet, IOFacet
from ontology.contracts.energy import EnergyReport, SystemicEnergy, ZoneContract

# Locally defined contracts (merged and backward compatible)

class BaseContract(BaseModel):
    pass

class TrailArtifact(BaseModel):
    """A durable fact or signal extracted during closeout."""
    kind: str = Field(default="", description="The category of the extracted signal.")
    content: str = Field(default="", description="The distilled fact or observation.")
    destination: str = Field(default="", description="Target path or node where this fact was encoded.")

class TrailCollection(BaseModel):
    """The aggregate output of a trail collect closeout step."""
    artifacts: list[TrailArtifact] = Field(default_factory=list)
    session_id: str = Field(default="")

class SessionLog(BaseModel):
    """Durable record of a single development session."""
    session_id: str = Field(default="", description="Unique session identifier.")
    start_time: str = Field(default="", description="ISO-8601 start timestamp.")
    end_time: str | None = Field(default=None, description="ISO-8601 end timestamp.")
    branch: str | None = Field(default=None, description="Git branch where work occurred.")
    commit_sha: str | None = Field(default=None, description="Resulting commit SHA.")
    resolved_issues: list[str] = Field(default_factory=list, description="IDs of issues resolved in this session.")
    pending_issues: list[str] = Field(default_factory=list, description="IDs of issues left in progress.")
    trails: TrailCollection | None = Field(default=None, description="Extracted durable signals.")

class RawSourceEntry(BaseModel):
    """Entry in the raw source manifest."""
    path: str = Field(default="", description="The relative path to the file from project root.")
    filename: str = Field(default="", description="The name of the raw source file.")
    content_hash: str = Field(default="", description="SHA-256 hash of the file content.")
    file_kind: str = Field(default="", description="The kind of file (e.g., 'pdf', 'md', 'txt').")
    status: str = Field(default="new", description="The processing status of the source.")
    created: str = Field(default="", description="ISO-8601 timestamp of when the entry was created.")
    notes: str = Field(default="", description="Optional notes about the source.")

class RawSourceManifest(BaseModel):
    """The manifest tracking all raw source files."""
    entries: list[RawSourceEntry] = Field(default_factory=list)

class ContextRequest(BaseModel):
    """A formal request for graph context."""
    node_ids: list[str] = Field(default_factory=list)
    task_hint: str | None = Field(default=None)
    depth: int = Field(default=1)
    include_planned: bool = Field(default=False)

class ChecklistItem(BaseModel):
    """A single item in a verification checklist."""
    description: str = Field(default="", description="What needs to be checked.")
    id: str | None = Field(default=None, description="Backcompat for id")
    text: str | None = Field(default=None, description="Backcompat for text")
    checked: bool = Field(default=False)
    details: str | None = None
    rule_id: str | None = None
    verification: str | None = None

class Checklist(BaseModel):
    """A collection of items for verifying a specific operation."""
    name: str = Field(description="The unique name of the checklist.")
    items: list[ChecklistItem] = Field(default_factory=list)

class ContextBundle(BaseModel):
    """The stable output schema for the context router."""
    nodes: list[KnowledgeNode] = Field(default_factory=list)
    edges: list[Edge] = Field(default_factory=list)
    rationale: dict[str, str] = Field(default_factory=dict)
    scores: dict[str, float] = Field(default_factory=dict)
    active_tasks: list[str] = Field(default_factory=list)
    checklists: list[Checklist] = Field(default_factory=list)
    prose: dict[str, str] = Field(default_factory=dict)

class GateRow(BaseModel):
    """A single row in the desk/Gates.md table."""
    gate_id: str = Field(default="", description="Sequential identifier: gate-<NNN>")
    status: str = Field(default="open", description="The current status of the gate.")
    proposal: Any = Field(default="", description="Relative path to the proposal file or dict.")
    opened: str = Field(default="", description="YYYY-MM-DD when the gate was created.")
    description: str = Field(default="", description="One-line summary of what needs approval.")

class GateTable(BaseModel):
    """The collection of all gates in desk/Gates.md."""
    gates: list[GateRow] = Field(default_factory=list)

class ArtifactValidationFinding(BaseModel):
    """A single validation failure for an authored artifact file."""
    artifact_path: str = Field(default="")
    validator_name: str = Field(default="")
    message: str = Field(default="")
    severity: str = Field(default="error")
    rule_id: str | None = Field(default=None)

class ArtifactValidationReport(BaseModel):
    """Validation result for one authored artifact file."""
    path: str = Field(default="")
    findings: list[ArtifactValidationFinding] = Field(default_factory=list)
    is_valid: bool = Field(default=True)

class CycleRecord(BaseModel):
    """Execution record for one coordinator run."""
    timestamp: str = Field(description="ISO-8601 start time.")
    cycle_id: str = Field(description="Unique ID for the cycle.")
    status: str = Field(default="success", description="Final status: success, paused, or error.")
    perturbations_detected: int = Field(default=0)
    actions_taken: list[str] = Field(default_factory=list)
    open_gates: list[str] = Field(default_factory=list)
    triggered_by: str = Field(default="unknown")
    summary: str = Field(default="")
    energy_before: float = Field(default=0.0)
    energy_after: float = Field(default=0.0)

class CycleHistory(BaseModel):
    """Collection of historical cycle records."""
    cycles: list[CycleRecord] = Field(default_factory=list)

class AuditFinding(BaseModel):
    """A specific finding from an ontology audit."""
    severity: Literal["info", "warning", "error", "critical"] = Field(default="warning")
    category: str = Field(default="")
    node_id: str = Field(default="")
    facet_name: str | None = Field(default=None)
    description: str = Field(default="")
    rationale: str | None = Field(default=None)
    # legacy
    check_name: str | None = Field(default=None)
    detail: str | None = Field(default=None)

class CleansingProposal(BaseModel):
    """A proposed corrective operation."""
    finding_id: str | None = Field(default=None)
    node_id: str = Field(default="")
    suggested_edit: str = Field(default="")
    rationale: str | None = Field(default=None)
    # legacy
    operation: str = Field(default="relocate")
    affected_nodes: list[str] = Field(default_factory=list)
    requires_human_approval: bool = Field(default=True)

class CleansingReport(BaseModel):
    """Machine-readable output of cleansing candidate detection."""
    proposals: list[CleansingProposal] = Field(default_factory=list)

class FacetOrthogonalityReport(BaseModel):
    """Response from validate_facet_proposal."""
    is_orthogonal: bool = Field(description="True if the proposal is orthogonal; False otherwise.")
    confidence: float = Field(default=1.0)
    reasoning: list[str] = Field(default_factory=list)
    colliding_nodes: list[str] = Field(default_factory=list)
    colliding_facets: list[Any] = Field(default_factory=list)
    field_collisions: list[str] = Field(default_factory=list)
    query_already_answered: bool = Field(default=False)
    resolution_suggestion: str | None = Field(default=None)
    attempts_remaining: int = Field(default=3)

class TopologyProposal(BaseModel):
    """Proposal for a new module design."""
    # Old fields
    proposed_module_name: str = Field(default="")
    intent: str = Field(default="")
    glossary_terms_used: list[str] = Field(default_factory=list)
    proposed_inputs: list[Any] = Field(default_factory=list)
    proposed_outputs: list[Any] = Field(default_factory=list)
    # New fields
    proposal_id: str = Field(default="")
    action: str = Field(default="")
    target_id: str = Field(default="")
    payload: dict = Field(default_factory=dict)
    reasoning: str = Field(default="")

class CollisionReport(BaseModel):
    """Response to a TopologyProposal."""
    proposal_id: str = Field(default="")
    is_safe: bool = Field(default=True)
    is_orthogonal: bool = Field(default=True)
    collisions: list[dict] = Field(default_factory=list)
    colliding_node_schemas: list[KnowledgeNode] = Field(default_factory=list)
    resolution_suggestion: str | None = Field(default=None)
    attempts_remaining: int = Field(default=3)

class FacetProposal(BaseModel):
    """Proposal to add a new facet dimension."""
    question: str = Field(default="")
    proposed_facet_name: str = Field(default="")
    applies_to: list[str] = Field(default_factory=list)
    proposed_fields: list = Field(default_factory=list)
    attempted_query: Any = Field(default=None)


__all__ = [
    "AuditFinding",
    "CleansingProposal",
    "CleansingReport",
    "Edge",
    "KnowledgeNode",
    "SystemIdentity",
    "ComplianceFacet",
    "GitFacet",
    "ASTFacet",
    "SemanticFacet",
    "IOFacet",
    "EnergyReport",
    "SystemicEnergy",
    "ZoneContract",
    "ContextRequest",
    "ContextBundle",
    "SessionLog",
    "TrailArtifact",
    "TrailCollection",
    "RawSourceEntry",
    "RawSourceManifest",
    "GateRow",
    "GateTable",
    "ArtifactValidationFinding",
    "Checklist",
    "CycleRecord",
    "CycleHistory",
    "FacetOrthogonalityReport",
    "CollisionReport",
    "TopologyProposal",
    "ArtifactValidationReport",
    "FacetProposal",
]
