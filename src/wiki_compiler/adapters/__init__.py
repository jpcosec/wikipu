"""Adapter layer for split package boundaries."""

from wiki_compiler.adapters.kgdb_query import (
    FacetFilter,
    FieldCondition,
    GraphScope,
    StructuredQuery,
    execute_query,
    match_nodes_from_task,
)
from wiki_compiler.adapters.kgdb_store import (
    add_knowledge_node,
    iter_knowledge_nodes,
    load_graph,
    load_knowledge_node,
    save_graph,
)
from wiki_compiler.adapters.ontology_cleanse import detect_cleansing_candidates
from wiki_compiler.adapters.ontology_energy import run_energy_audit
from wiki_compiler.adapters.ontology_energy import DRIFT_PENALTY_WEIGHT
from wiki_compiler.adapters.ontology_facets import (
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
from wiki_compiler.adapters.ontology_reasoning import (
    ONTOLOGY_IRI,
    OwlConflictCheck,
    OwlReasoner,
    export_wikipu_ontology,
    get_ontology,
    get_world,
)

__all__ = [
    "ADRInjector",
    "DRIFT_PENALTY_WEIGHT",
    "FacetRegistry",
    "FacetFilter",
    "FieldCondition",
    "GraphScope",
    "InjectionContext",
    "ONTOLOGY_IRI",
    "OwlConflictCheck",
    "OwlReasoner",
    "StructuredQuery",
    "TestMapInjector",
    "add_knowledge_node",
    "build_default_registry",
    "calculate_compliance_score",
    "detect_cleansing_candidates",
    "execute_query",
    "export_wikipu_ontology",
    "get_ontology",
    "get_world",
    "infer_reference_documents_edges",
    "iter_knowledge_nodes",
    "load_graph",
    "load_knowledge_node",
    "match_nodes_from_task",
    "run_energy_audit",
    "save_graph",
    "scan_python_file",
    "scan_python_sources",
    "validate_facet_proposal",
]
