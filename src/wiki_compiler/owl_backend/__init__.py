"""OWL Backend module for wikipu - Owlready2 integration."""

from pathlib import Path

ONTOLOGY_IRI = "https://wikipu.ai/ontology/"
ONTOLOGY_PATH = Path(__file__).parent.parent.parent.parent / "wikipu.owl"

from wiki_compiler.owl_backend.extractor import (
    markdown_to_owl,
    get_world,
    get_ontology,
    extract_all,
)
from wiki_compiler.owl_backend.export import export_to_rdfxml, export_wikipu_ontology

__all__ = [
    "ONTOLOGY_IRI",
    "ONTOLOGY_PATH",
    "markdown_to_owl",
    "get_world",
    "get_ontology",
    "extract_all",
    "export_to_rdfxml",
    "export_wikipu_ontology",
]
