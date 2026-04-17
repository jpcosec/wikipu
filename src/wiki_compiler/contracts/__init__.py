"""
Canonical Pydantic models and contracts for the Knowledge Graph ecosystem.
"""

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
from .node import KnowledgeNode
from .proposals import (
    AuditFinding,
    ArtifactValidationFinding,
    ArtifactValidationReport,
    CleansingProposal,
    CleansingReport,
    CollisionReport,
    FacetOrthogonalityReport,
    FacetProposal,
    TopologyProposal,
)
from .tracking import (
    Checklist,
    ChecklistItem,
    ContextBundle,
    ContextRequest,
    CycleHistory,
    CycleRecord,
    GateRow,
    GateTable,
    RawSourceEntry,
    RawSourceManifest,
    SessionLog,
    TrailArtifact,
    TrailCollection,
)
from .energy import EnergyReport, SystemicEnergy, ZoneContract

__all__ = [
    "Edge",
    "SystemIdentity",
    "IOFacet",
    "ASTFacet",
    "SemanticFacet",
    "ADRFacet",
    "TestMapFacet",
    "ComplianceFacet",
    "SourceFacet",
    "GitFacet",
    "KnowledgeNode",
    "AuditFinding",
    "FacetProposal",
    "FacetOrthogonalityReport",
    "TopologyProposal",
    "CollisionReport",
    "ArtifactValidationFinding",
    "ArtifactValidationReport",
    "RawSourceEntry",
    "RawSourceManifest",
    "GateRow",
    "GateTable",
    "CycleRecord",
    "CycleHistory",
    "TrailArtifact",
    "TrailCollection",
    "SessionLog",
    "ContextRequest",
    "ChecklistItem",
    "Checklist",
    "ContextBundle",
    "CleansingProposal",
    "CleansingReport",
    "SystemicEnergy",
    "EnergyReport",
    "ZoneContract",
]
