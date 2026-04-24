"""Adapter for ontology facet services."""

from ontology.facets import (
    ADRInjector,
    FacetRegistry,
    InjectionContext,
    TestMapInjector,
    build_default_registry,
    calculate_compliance_score,
    infer_reference_documents_edges,
    scan_python_file,
    scan_python_sources,
    validate_facet_proposal,
)

__all__ = [
    "ADRInjector",
    "FacetRegistry",
    "InjectionContext",
    "TestMapInjector",
    "build_default_registry",
    "calculate_compliance_score",
    "infer_reference_documents_edges",
    "scan_python_file",
    "scan_python_sources",
    "validate_facet_proposal",
]
