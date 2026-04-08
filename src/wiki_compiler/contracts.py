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
        "contains",       # Hierarchy (e.g., 'src' -> 'src/ai')
        "depends_on",     # Code dependency (e.g., 'graph.py' -> 'contracts.py')
        "reads_from",     # Data Flow (I/O)
        "writes_to",      # Data Flow (I/O)
        "documents",      # Documentation relation (e.g., 'design_doc.md' -> 'src/module_a')
        "transcludes"     # Atomic embedding (DRY Wiki)
    ] = Field(description="The type of relationship this edge represents.")
    metadata: dict[str, Any] = Field(
        default_factory=dict, 
        description="Additional context for the edge (e.g., line number, conditions, etc.)."
    )

class SystemIdentity(BaseModel):
    """The immutable base identity of any node in your universe."""
    node_id: str = Field(description="A unique absolute identifier for the node (e.g., 'dir:src/data_processor' or 'file:wiki/concepts/core_concept.md').")
    node_type: Literal["directory", "file", "code_construct", "doc_standard", "concept"] = Field(
        description="The type of entity this node represents."
    )

# --- 2. Configurable Dimensions (Facets) ---

class IOFacet(BaseModel):
    """Dimension: Input/Output.

    Question: What data does this node consume or produce?
    """
    medium: Literal["memory", "disk", "network"] = Field(
        description="The medium through which data is transferred (e.g., 'memory', 'disk', 'network')."
    )
    schema_ref: str | None = Field(
        default=None,
        description="The name of the associated Pydantic model, if applicable (e.g., 'JobPosting')."
    )
    path_template: str | None = Field(
        default=None,
        description="The disk path template (e.g., 'output/{source}/data.json') if applicable."
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
        description="List of method or command-line interface (CLI) signatures extracted from the code."
    )
    dependencies: list[str] = Field(
        default_factory=list,
        description="List of internal contract names this node depends on, detected via imports."
    )

class SemanticFacet(BaseModel):
    """Dimension: What each thing does and its Docstrings.

    Question: What does this node do?
    """
    intent: str = Field(description="High-level summary of purpose, extracted from README or module docstring.")
    raw_docstring: str | None = Field(
        default=None,
        description="The raw docstring extracted directly from the code, if available."
    )

class ADRFacet(BaseModel):
    """Dimension: Historical Decision Records.

    Question: What architectural decisions shaped this node?
    """
    decision_id: str = Field(description="Unique identifier for the architectural decision record.")
    status: Literal["proposed", "accepted", "deprecated", "superseded"] = Field(
        description="The current status of the architectural decision."
    )
    context_summary: str = Field(description="Summary of the context and reasons behind the decision, including discarded alternatives.")

class TestMapFacet(BaseModel):
    """Dimension: Testing Strategy and Coverage.

    Question: How is this node tested?
    """
    test_type: Literal["unit", "integration", "e2e", "manual_review"] = Field(
        description="The type of testing applied to this node."
    )
    coverage_percent: float | None = Field(
        default=None,
        description="Percentage of the node covered by automated tests, if measured."
    )

class ComplianceFacet(BaseModel):
    """Dimension: Implementation Status and House Rules Compliance.

    Question: How complete and rule-compliant is this node?
    """
    status: Literal["planned", "scaffolding", "mocked", "implemented", "tested", "exempt"] = Field(
        description="The current stage of implementation or compliance status (e.g., 'planned', 'implemented', 'exempt')."
    )
    failing_standards: list[str] = Field(
        default_factory=list,
        description="List of `wiki/standards` rules that this node currently fails to meet."
    )
    exemption_reason: str | None = Field(
        default=None,
        description="Reason for exemption if the status is 'exempt'."
    )

# --- 3. The Unified Node ---

class KnowledgeNode(BaseModel):
    """
    Any element in the system, from the root folder to a specific function.
    This is the building block of your LLM Wiki.
    """
    identity: SystemIdentity = Field(description="The unique identity and type of this node within the system.")
    edges: list[Edge] = Field(
        default_factory=list,
        description="A list of directed connections to other nodes, indicating relationships like containment, dependencies, or data flow."
    )
    
    # Facets (optional, injected by plugins)
    semantics: SemanticFacet | None = Field(default=None, description="Semantic information like intent and raw docstrings.")
    ast: ASTFacet | None = Field(default=None, description="Abstract Syntax Tree related information about code structure.")
    io_ports: list[IOFacet] = Field(
        default_factory=list,
        description="Details about input/output ports, including medium, schema references, and path templates."
    )
    compliance: ComplianceFacet | None = Field(default=None, description="Compliance status against defined standards and rules.")
    adr: ADRFacet | None = Field(default=None, description="Architectural Decision Record related information, if applicable.")
    test_map: TestMapFacet | None = Field(default=None, description="Testing strategy and coverage for this node.")

# --- 4. Closed Loop Orthogonality and Circuit Breaker ---

class AuditFinding(BaseModel):
    """A finding from an audit check."""
    check_name: str = Field(description="The name of the audit check that produced this finding.")
    node_id: str = Field(description="The ID of the node that failed the check.")
    detail: str = Field(description="A detailed explanation of the failure.")

class FacetProposal(BaseModel):
    """
    A proposal to add a new facet dimension to the registry.
    Must prove the question cannot be answered by existing facets before being accepted.
    """
    proposed_facet_name: str = Field(description="Snake_case name for the new facet.")
    question: str = Field(description="The single question this facet answers. Must be unique across the registry.")
    applies_to: list[str] = Field(description="Node types this facet is relevant for.")
    proposed_fields: list[dict[str, str]] = Field(description="List of {name, type} dicts for the facet's fields.")
    attempted_query: dict | None = Field(
        default=None,
        description="Serialised StructuredQuery. If provided and returns results, proposal is rejected.",
    )

class FacetOrthogonalityReport(BaseModel):
    """Response from validate_facet_proposal."""
    is_orthogonal: bool = Field(description="True if the proposal is orthogonal; False otherwise.")
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
    resolution_suggestion: str | None = Field(default=None, description="A suggestion for resolving the collision.")
    attempts_remaining: int = Field(description="The number of attempts remaining for the agent.")

class TopologyProposal(BaseModel):
    """
    A proposal for a new module design that an Agent must submit for orthogonality validation
    before writing new code. The wiki_compiler evaluates this against the existing graph.
    """
    proposed_module_name: str = Field(description="The proposed name for the new module.")
    intent: str = Field(description="The high-level purpose or intent of the proposed module.")
    glossary_terms_used: list[str] = Field(
        description="List of terms from `wiki/domain_glossary.yaml` that this proposal uses, to check for semantic collisions."
    )
    proposed_inputs: list[IOFacet] = Field(description="A list of proposed input I/O ports for the module.")
    proposed_outputs: list[IOFacet] = Field(description="A list of proposed output I/O ports for the module.")

class CollisionReport(BaseModel):
    """Response from the wiki_compiler to a TopologyProposal."""
    is_orthogonal: bool = Field(description="True if the proposal is orthogonal and does not collide with existing nodes; False otherwise.")
    colliding_node_schemas: list[KnowledgeNode] = Field(
        description="Full schemas of existing nodes that collide with the proposal. Provided to help the agent understand the conflict."
    )
    resolution_suggestion: str | None = Field(
        default=None,
        description="A suggestion for resolving the collision (e.g., 'Reuse node X instead of creating a new one')."
    )
    attempts_remaining: int = Field(description="The number of attempts remaining for the agent to submit an orthogonal proposal before human intervention is required.")