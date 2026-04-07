from pydantic import BaseModel, Field
from typing import Literal, Any

# --- 1. Immutable Base ---

class Edge(BaseModel):
    target_id: str
    relation_type: Literal[
        "contains", "depends_on", "reads_from", "writes_to", "documents", "transcludes"
    ]
    metadata: dict[str, Any] = Field(default_factory=dict)

class SystemIdentity(BaseModel):
    node_id: str
    node_type: Literal["directory", "file", "code_construct", "doc_standard", "concept"]

# --- 2. Configurable Dimensions (Facets) ---

class IOFacet(BaseModel):
    medium: Literal["memory", "disk", "network"]
    schema_ref: str | None = None
    path_template: str | None = None

class ASTFacet(BaseModel):
    construct_type: Literal["function", "class", "script"]
    signatures: list[str] = Field(default_factory=list)
    dependencies: list[str] = Field(default_factory=list)

class SemanticFacet(BaseModel):
    intent: str
    raw_docstring: str | None = None

class ADRFacet(BaseModel):
    decision_id: str
    status: Literal["proposed", "accepted", "deprecated", "superseded"]
    context_summary: str

class ComplianceFacet(BaseModel):
    status: Literal["planned", "scaffolding", "mocked", "implemented", "tested", "exempt"]
    failing_standards: list[str] = Field(default_factory=list)
    exemption_reason: str | None = None

# --- 3. Unified Node ---

class KnowledgeNode(BaseModel):
    identity: SystemIdentity
    edges: list[Edge] = Field(default_factory=list)
    
    semantics: SemanticFacet | None = None
    ast: ASTFacet | None = None
    io_ports: list[IOFacet] = Field(default_factory=list)
    compliance: ComplianceFacet | None = None
    adr: ADRFacet | None = None

# --- 4. Orthogonality Closed Loop & Circuit Breaker ---

class TopologyProposal(BaseModel):
    proposed_module_name: str
    intent: str
    glossary_terms_used: list[str]
    proposed_inputs: list[IOFacet]
    proposed_outputs: list[IOFacet]

class CollisionReport(BaseModel):
    is_orthogonal: bool
    colliding_node_schemas: list[KnowledgeNode] = Field(description="Full schemas of affected nodes")
    resolution_suggestion: str | None
    attempts_remaining: int
