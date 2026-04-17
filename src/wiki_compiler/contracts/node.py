"""
The Unified Node for the Knowledge Graph.
"""

from pydantic import BaseModel, Field

from .base import Edge, SystemIdentity
from .facets import (
    ADRFacet,
    ASTFacet,
    ComplianceFacet,
    GitFacet,
    IOFacet,
    SemanticFacet,
    SourceFacet,
    TestMapFacet,
)


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
        description="A list of directed connections to other nodes.",
    )

    semantics: SemanticFacet | None = Field(
        default=None, description="Semantic information like intent and raw docstrings."
    )
    ast: ASTFacet | None = Field(
        default=None,
        description="Abstract Syntax Tree related information about code structure.",
    )
    io_ports: list[IOFacet] = Field(
        default_factory=list,
        description="Details about input/output ports.",
    )
    compliance: ComplianceFacet | None = Field(
        default=None,
        description="Compliance status against defined standards and rules.",
    )
    adr: ADRFacet | None = Field(
        default=None,
        description="Architectural Decision Record related information.",
    )
    test_map: TestMapFacet | None = Field(
        default=None, description="Testing strategy and coverage."
    )
    git: GitFacet | None = Field(
        default=None, description="Git metadata for file-backed or doc-backed nodes."
    )
    source: SourceFacet | None = Field(
        default=None, description="Provenance and source tracking metadata."
    )
