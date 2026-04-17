"""
Session, Trail, and Cycle tracking models.
"""

from pydantic import BaseModel, Field
from typing import Any, Literal


class RawSourceEntry(BaseModel):
    """Entry in the raw source manifest."""

    filename: str = Field(description="The name of the raw source file.")
    path: str = Field(description="The relative path to the file from project root.")
    file_kind: str = Field(description="The kind of file (e.g., 'pdf', 'md', 'txt').")
    content_hash: str = Field(description="SHA-256 hash of the file content.")
    status: Literal["new", "processed", "ignored"] = Field(
        default="new", description="The processing status of the source."
    )
    created: str = Field(
        description="ISO-8601 timestamp of when the entry was created."
    )
    notes: str = Field(default="", description="Optional notes about the source.")


class RawSourceManifest(BaseModel):
    """The manifest tracking all raw source files."""

    entries: list[RawSourceEntry] = Field(default_factory=list)


class GateRow(BaseModel):
    """A single row in the desk/Gates.md table."""

    gate_id: str = Field(description="Sequential identifier: gate-<NNN>")
    proposal: str = Field(description="Relative path to the proposal file.")
    opened: str = Field(description="YYYY-MM-DD when the gate was created.")
    description: str = Field(description="One-line summary of what needs approval.")
    status: Literal["open", "approved", "rejected", "closed"] = Field(
        default="open", description="The current status of the gate."
    )


class GateTable(BaseModel):
    """The collection of all gates in desk/Gates.md."""

    gates: list[GateRow] = Field(default_factory=list)


class CycleRecord(BaseModel):
    """Execution record for one coordinator run."""

    cycle_id: str = Field(description="Unique ID for the cycle.")
    timestamp: str = Field(description="ISO-8601 start time.")
    status: str = Field(description="Final status: success, paused, or error.")
    perturbations_detected: int = Field(default=0)
    actions_taken: list[str] = Field(default_factory=list)
    open_gates: list[str] = Field(default_factory=list)


class CycleHistory(BaseModel):
    """Collection of historical cycle records."""

    cycles: list[CycleRecord] = Field(default_factory=list)


class TrailArtifact(BaseModel):
    """A durable fact or signal extracted during closeout."""

    kind: Literal["decision", "gap", "correction", "new_concept", "rule_patch"] = Field(
        description="The category of the extracted signal."
    )
    content: str = Field(description="The distilled fact or observation.")
    destination: str = Field(
        description="Target path or node where this fact was encoded."
    )


class TrailCollection(BaseModel):
    """The aggregate output of a trail collect closeout step."""

    session_id: str = Field(description="ID of the session or cycle being closed.")
    artifacts: list[TrailArtifact] = Field(default_factory=list)


class SessionLog(BaseModel):
    """Durable record of a single development session."""

    session_id: str = Field(description="Unique session identifier.")
    start_time: str = Field(description="ISO-8601 start timestamp.")
    end_time: str | None = Field(default=None, description="ISO-8601 end timestamp.")
    branch: str | None = Field(
        default=None, description="Git branch where work occurred."
    )
    commit_sha: str | None = Field(default=None, description="Resulting commit SHA.")
    resolved_issues: list[str] = Field(
        default_factory=list, description="IDs of issues resolved in this session."
    )
    pending_issues: list[str] = Field(
        default_factory=list, description="IDs of issues left in progress."
    )
    trails: TrailCollection | None = Field(
        default=None, description="Extracted durable signals (Phase 6)."
    )


class ContextRequest(BaseModel):
    """A formal request for graph context."""

    node_ids: list[str] = Field(default_factory=list)
    task_hint: str | None = Field(default=None)
    depth: int = Field(default=1)
    include_planned: bool = Field(default=False)


class ChecklistItem(BaseModel):
    """A single item in a verification checklist."""

    description: str = Field(description="What needs to be checked.")
    rule_id: str | None = Field(
        default=None, description="The House Rule ID being enforced."
    )
    verification: str | None = Field(
        default=None, description="The command or method to verify the item."
    )


class Checklist(BaseModel):
    """A collection of items for verifying a specific operation."""

    name: str = Field(description="The unique name of the checklist.")
    items: list[ChecklistItem] = Field(default_factory=list)


class ContextBundle(BaseModel):
    """The stable output schema for the context router."""

    nodes: list[Any] = Field(description="The set of included knowledge nodes.")
    edges: list[Any] = Field(
        description="The subset of edges connecting the included nodes."
    )
    rationale: dict[str, str] = Field(
        default_factory=dict, description="Reasoning for each node's inclusion."
    )
    scores: dict[str, float] = Field(
        default_factory=dict, description="Relevance score for each node."
    )
    active_tasks: list[str] = Field(
        default_factory=list, description="Paths to relevant active task files."
    )
    checklists: list[Checklist] = Field(
        default_factory=list, description="Relevant verification checklists."
    )
    prose: dict[str, str] = Field(
        default_factory=dict, description="Markdown prose for doc-backed nodes."
    )
