"""Adapter for ontology facet services."""

from ontology.facets import (
    ADRInjector,
    FacetRegistry,
    FacetSpec,
    InjectionContext,
    TestMapInjector,
    build_default_registry,
    calculate_compliance_score,
    infer_reference_documents_edges,
    scan_python_file,
    scan_python_sources,
    validate_facet_proposal,
)
from ontology.facets.scanner import infer_io_from_ast

__all__ = [
    "ADRInjector",
    "FacetRegistry",
    "FacetSpec",
    "InjectionContext",
    "TestMapInjector",
    "build_default_registry",
    "calculate_compliance_score",
    "infer_io_from_ast",
    "infer_reference_documents_edges",
    "scan_python_file",
    "scan_python_sources",
    "validate_facet_proposal",
]
