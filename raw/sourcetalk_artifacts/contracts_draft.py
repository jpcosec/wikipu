from pydantic import BaseModel, Field
from typing import Literal, Any

# --- 1. La Base Inmutable ---

class Edge(BaseModel):
    """Conexión universal entre nodos."""
    target_id: str
    relation_type: Literal[
        "contains",       # Jerarquía de carpetas
        "depends_on",     # Dependencias de código
        "reads_from",     # I/O Memoria o Disco
        "writes_to",      # I/O Memoria o Disco
        "documents",      # Markdown a Código
        "transcludes"     # Incrustación atómica (DRY Wiki)
    ]
    metadata: dict[str, Any] = Field(default_factory=dict)

class SystemIdentity(BaseModel):
    node_id: str = Field(description="Ej: 'dir:src/scraper' o 'file:src/wiki/concepts/job.md'")
    node_type: Literal["directory", "file", "code_construct", "doc_standard", "concept"]

# --- 2. Dimensiones Configurables (Facets) ---

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

# --- 3. Nodo Unificado ---

class KnowledgeNode(BaseModel):
    identity: SystemIdentity
    edges: list[Edge] = Field(default_factory=list)
    
    semantics: SemanticFacet | None = None
    ast: ASTFacet | None = None
    io_ports: list[IOFacet] = Field(default_factory=list)
    compliance: ComplianceFacet | None = None
    adr: ADRFacet | None = None

# --- 4. Loop Cerrado de Ortogonalidad ---

class TopologyProposal(BaseModel):
    proposed_module_name: str
    intent: str
    glossary_terms_used: list[str]
    proposed_inputs: list[IOFacet]
    proposed_outputs: list[IOFacet]

class CollisionReport(BaseModel):
    is_orthogonal: bool
    colliding_nodes: list[str]
    resolution_suggestion: str | None