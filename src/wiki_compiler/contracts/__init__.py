"""Canonical Pydantic models and contracts for the Knowledge Graph ecosystem."""

from importlib import import_module

from wiki_compiler.contracts.tracking import (
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


_EXPORTS = {
    "ADRDoc": "ontology.contracts.wiki_nodes",
    "ADRFacet": "ontology.contracts.facets",
    "ASTFacet": "ontology.contracts.facets",
    "ArtifactValidationFinding": "ontology.contracts.proposals",
    "ArtifactValidationReport": "ontology.contracts.proposals",
    "AuditFinding": "ontology.contracts.proposals",
    "CleansingProposal": "ontology.contracts.proposals",
    "CleansingReport": "ontology.contracts.proposals",
    "CollisionReport": "ontology.contracts.proposals",
    "ComplianceFacet": "ontology.contracts.facets",
    "ConceptDoc": "ontology.contracts.wiki_nodes",
    "DocStandardDoc": "ontology.contracts.wiki_nodes",
    "Edge": "kgdb.contracts",
    "EnergyReport": "wiki_compiler.contracts.energy",
    "FacetOrthogonalityReport": "ontology.contracts.proposals",
    "FacetProposal": "ontology.contracts.proposals",
    "GitFacet": "ontology.contracts.facets",
    "HowToDoc": "ontology.contracts.wiki_nodes",
    "IOFacet": "ontology.contracts.facets",
    "IndexDoc": "ontology.contracts.wiki_nodes",
    "KnowledgeNode": "kgdb.contracts",
    "ReferenceDoc": "ontology.contracts.wiki_nodes",
    "SelfDocDoc": "ontology.contracts.wiki_nodes",
    "SemanticFacet": "ontology.contracts.facets",
    "SourceFacet": "ontology.contracts.facets",
    "SystemIdentity": "kgdb.contracts",
    "SystemicEnergy": "wiki_compiler.contracts.energy",
    "TestMapFacet": "ontology.contracts.facets",
    "TopologyProposal": "ontology.contracts.proposals",
    "ZoneContract": "wiki_compiler.contracts.energy",
}

__all__ = sorted(_EXPORTS) + [
    "Checklist",
    "ChecklistItem",
    "ContextBundle",
    "ContextRequest",
    "CycleHistory",
    "CycleRecord",
    "GateRow",
    "GateTable",
    "RawSourceEntry",
    "RawSourceManifest",
    "SessionLog",
    "TrailArtifact",
    "TrailCollection",
]


def __getattr__(name: str):
    module_name = _EXPORTS.get(name)
    if module_name is None:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
    module = import_module(module_name)
    value = getattr(module, name)
    globals()[name] = value
    return value
