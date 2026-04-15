"""
Canonical Pydantic models and contracts for the Knowledge Graph ecosystem.
Defines the schema for nodes, edges, and facets like ADR, compliance, and I/O.
"""

from pydantic import BaseModel, Field
from typing import Literal, Any

# --- 1. The Immutable Base ---


class Edge(BaseModel):
    """Universal connection between nodes."""

    target_id: str = Field(description="The ID of the target node this edge points to.")
    relation_type: Literal[
        "contains",  # Hierarchy (e.g., 'src' -> 'src/ai')
        "depends_on",  # Code dependency (e.g., 'graph.py' -> 'contracts.py')
        "reads_from",  # Data Flow (I/O)
        "writes_to",  # Data Flow (I/O)
        "documents",  # Documentation relation (e.g., 'design_doc.md' -> 'src/module_a')
        "transcludes",  # Atomic embedding (DRY Wiki)
        "extends",  # Inheritance/Specialization (e.g., 'adr.md' -> 'wiki_node.md')
        "implements",  # Realization of a standard or requirement
    ] = Field(description="The type of relationship this edge represents.")
    metadata: dict[str, Any] = Field(
        default_factory=dict,
        description="Additional context for the edge (e.g., line number, conditions, etc.).",
    )


class SystemIdentity(BaseModel):
    """The immutable base identity of any node in your universe."""

    node_id: str = Field(
        description="A unique absolute identifier for the node (e.g., 'dir:src/data_processor' or 'file:wiki/concepts/core_concept.md')."
    )
    node_type: Literal[
        "directory",
        "file",
        "code_construct",
        "doc_standard",
        "concept",
        "index",
        "how_to",
        "adr",
        "reference",
        "faq",
    ] = Field(description="The type of entity this node represents.")


# --- 2. Configurable Dimensions (Facets) ---


class IOFacet(BaseModel):
    """Dimension: Input/Output.

    Question: What data does this node consume or produce?
    """

    medium: Literal["memory", "disk", "network"] = Field(
        description="The medium through which data is transferred (e.g., 'memory', 'disk', 'network')."
    )
    direction: Literal["input", "output"] = Field(
        default="input",
        description="The direction of data flow (e.g., 'input' for reading, 'output' for writing).",
    )
    schema_ref: str | None = Field(
        default=None,
        description="The name of the associated Pydantic model, if applicable (e.g., 'JobPosting').",
    )
    path_template: str | None = Field(
        default=None,
        description="The disk path template (e.g., 'output/{source}/data.json') if applicable.",
    )


class ASTFacet(BaseModel):
    """Dimension: The Hows (Code Structure).

    Question: How is this node structured?
    """

    construct_type: Literal["function", "class", "script"] = Field(
        description="The type of code construct (e.g., 'function', 'class', 'script')."
    )
    signatures: list[str] = Field(
        default_factory=list,
        description="List of method or command-line interface (CLI) signatures extracted from the code.",
    )
    dependencies: list[str] = Field(
        default_factory=list,
        description="List of internal contract names this node depends on, detected via imports.",
    )


class SemanticFacet(BaseModel):
    """Dimension: What each thing does and its Docstrings.

    Question: What does this node do?
    """

    intent: str = Field(
        description="High-level summary of purpose, extracted from README or module docstring."
    )
    raw_docstring: str | None = Field(
        default=None,
        description="The raw docstring extracted directly from the code, if available.",
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
        description="Summary of the context and reasons behind the decision, including discarded alternatives."
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
        description="Percentage of the node covered by automated tests, if measured.",
    )


class ComplianceFacet(BaseModel):
    """Dimension: Implementation Status and House Rules Compliance.

    Question: How complete and rule-compliant is this node?
    """

    status: Literal[
        "planned", "scaffolding", "mocked", "implemented", "tested", "exempt"
    ] = Field(
        description="The current stage of implementation or compliance status (e.g., 'planned', 'implemented', 'exempt')."
    )
    failing_standards: list[str] = Field(
        default_factory=list,
        description="List of `wiki/standards` rules that this node currently fails to meet.",
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
        description="First commit that introduced the file, if available.",
    )
    last_modified_commit: str | None = Field(
        default=None,
        description="Most recent commit touching the file, if available.",
    )
    last_modified_author: str | None = Field(
        default=None,
        description="Email of the last modifying author, if available.",
    )
    status: Literal["tracked", "untracked", "modified_since_build"] = Field(
        description="Git tracking status known at build or status-check time."
    )


# --- 3. The Unified Node ---


class KnowledgeNode(BaseModel):
    """
    Any element in the system, from the root folder to a specific function.
    This is the building block of your LLM Wiki.
    """

    identity: SystemIdentity = Field(
        description="The unique identity and type of this node within the system."
    )
    edges: list[Edge] = Field(
        default_factory=list,
        description="A list of directed connections to other nodes, indicating relationships like containment, dependencies, or data flow.",
    )

    # Facets (optional, injected by plugins)
    semantics: SemanticFacet | None = Field(
        default=None, description="Semantic information like intent and raw docstrings."
    )
    ast: ASTFacet | None = Field(
        default=None,
        description="Abstract Syntax Tree related information about code structure.",
    )
    io_ports: list[IOFacet] = Field(
        default_factory=list,
        description="Details about input/output ports, including medium, schema references, and path templates.",
    )
    compliance: ComplianceFacet | None = Field(
        default=None,
        description="Compliance status against defined standards and rules.",
    )
    adr: ADRFacet | None = Field(
        default=None,
        description="Architectural Decision Record related information, if applicable.",
    )
    test_map: TestMapFacet | None = Field(
        default=None, description="Testing strategy and coverage for this node."
    )
    git: GitFacet | None = Field(
        default=None, description="Git metadata for file-backed or doc-backed nodes."
    )
    source: SourceFacet | None = Field(
        default=None, description="Provenance and source tracking metadata."
    )


# --- 4. Closed Loop Orthogonality and Circuit Breaker ---


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
    Must prove the question cannot be answered by existing facets before being accepted.
    """

    proposed_facet_name: str = Field(description="Snake_case name for the new facet.")
    question: str = Field(
        description="The single question this facet answers. Must be unique across the registry."
    )
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
        description="'field_name (existing_facet)' strings for each field name collision.",
    )
    query_already_answered: bool = Field(
        default=False,
        description="True if the attempted_query returned results, meaning the information already exists.",
    )
    resolution_suggestion: str | None = Field(
        default=None, description="A suggestion for resolving the collision."
    )
    attempts_remaining: int = Field(
        description="The number of attempts remaining for the agent."
    )


class TopologyProposal(BaseModel):
    """
    A proposal for a new module design that an Agent must submit for orthogonality validation
    before writing new code. The wiki_compiler evaluates this against the existing graph.
    """

    proposed_module_name: str = Field(
        description="The proposed name for the new module."
    )
    intent: str = Field(
        description="The high-level purpose or intent of the proposed module."
    )
    glossary_terms_used: list[str] = Field(
        description="List of terms from `wiki/domain_glossary.yaml` that this proposal uses, to check for semantic collisions."
    )
    proposed_inputs: list[IOFacet] = Field(
        description="A list of proposed input I/O ports for the module."
    )
    proposed_outputs: list[IOFacet] = Field(
        description="A list of proposed output I/O ports for the module."
    )


class CollisionReport(BaseModel):
    """Response from the wiki_compiler to a TopologyProposal."""

    is_orthogonal: bool = Field(
        description="True if the proposal is orthogonal and does not collide with existing nodes; False otherwise."
    )
    colliding_node_schemas: list[KnowledgeNode] = Field(
        description="Full schemas of existing nodes that collide with the proposal. Provided to help the agent understand the conflict."
    )
    resolution_suggestion: str | None = Field(
        default=None,
        description="A suggestion for resolving the collision (e.g., 'Reuse node X instead of creating a new one').",
    )
    attempts_remaining: int = Field(
        description="The number of attempts remaining for the agent to submit an orthogonal proposal before human intervention is required."
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

    cycle_id: str = Field(description="Unique ID for the cycle (e.g. timestamp-based).")
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
        description="Target path or node where this fact was encoded (e.g. 'wiki/concepts/foo.md')."
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

    nodes: list[KnowledgeNode] = Field(
        description="The set of included knowledge nodes."
    )
    edges: list[Edge] = Field(
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
        description="Whether the proposal requires explicit approval before application.",
    )


class CleansingReport(BaseModel):
    """Machine-readable output of cleansing candidate detection."""

    proposals: list[CleansingProposal] = Field(
        default_factory=list,
        description="Detected structural correction proposals.",
    )


class SystemicEnergy(BaseModel):
    """
    ID-2: Minimal Energy.
    The conceptual and structural cost of the current system state.
    """

    energy_score: float = Field(description="The total calculated energy score.")
    node_count: int = Field(description="Total number of nodes in the graph.")
    edge_count: int = Field(description="Total number of edges in the graph.")
    compliance_violations: int = Field(
        description="Total number of failing standards across all nodes."
    )
    perturbations: int = Field(
        description="Number of detected git-backed drifts or untracked files."
    )
    open_gates: int = Field(description="Number of active human-in-the-loop gates.")
    agent_violations: int = Field(
        default=0, description="Number of agent rule violations."
    )

    # Redundancy detection
    redundant_nodes: int = Field(
        default=0,
        description="Number of semantically redundant nodes (Jaccard similarity > threshold).",
    )
    boilerplate_ratio: float = Field(
        default=0.0, description="Ratio of boilerplate to unique content."
    )

    # Descriptive abstraction penalties
    long_files: int = Field(
        default=0, description="Number of files exceeding line threshold."
    )
    complex_functions: int = Field(
        default=0, description="Number of functions exceeding statement threshold."
    )

    # Code-doc drift detection
    drift_flags: int = Field(
        default=0, description="Number of code-doc drift violations detected."
    )

    # Heuristic breakdown
    structural_energy: float = Field(
        description="Energy from redundancy and boilerplate (replaces raw node/edge count)."
    )
    abstraction_energy: float = Field(
        default=0.0, description="Energy from descriptive abstraction penalties."
    )
    violation_energy: float = Field(
        description="Energy contributed by compliance debt."
    )
    perturbation_energy: float = Field(
        description="Energy contributed by systemic uncertainty/drift."
    )
    agent_violation_energy: float = Field(
        default=0.0, description="Energy contributed by agent rule violations."
    )


class EnergyReport(BaseModel):
    """The result of an energy audit."""

    timestamp: str = Field(description="ISO-8601 timestamp of the measurement.")
    current_energy: SystemicEnergy = Field(
        description="The energy state at the time of measurement."
    )
    baseline_energy: SystemicEnergy | None = Field(
        default=None, description="The energy state at the last stable baseline."
    )
    delta: float = Field(
        default=0.0, description="The change in total energy since the baseline."
    )
