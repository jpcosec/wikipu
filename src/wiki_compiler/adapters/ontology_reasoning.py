"""Adapter for ontology reasoning services."""

from ontology.reasoning import OwlConflictCheck, OwlReasoner
from ontology.reasoning.owl_backend import (
    ONTOLOGY_IRI,
    export_wikipu_ontology,
    get_ontology,
    get_world,
)

__all__ = [
    "ONTOLOGY_IRI",
    "OwlConflictCheck",
    "OwlReasoner",
    "export_wikipu_ontology",
    "get_ontology",
    "get_world",
]
