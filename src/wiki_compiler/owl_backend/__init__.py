"""OWL Backend module for wikipu - Owlready2 integration."""

from pathlib import Path

ONTOLOGY_IRI = "https://wikipu.ai/ontology/"
ONTOLOGY_PATH = Path(__file__).parent.parent.parent.parent / "wikipu.owl"

from wiki_compiler.owl_backend.extractor import (
    markdown_to_rdf,
    get_world,
    get_ontology,
    extract_all,
)
from wiki_compiler.owl_backend.export import export_to_rdfxml, export_wikipu_ontology
from wiki_compiler.owl_backend.import_export import (
    owl_to_markdown,
    export_ontology_to_markdown,
)

__all__ = [
    "ONTOLOGY_IRI",
    "ONTOLOGY_PATH",
    "markdown_to_rdf",
    "get_world",
    "get_ontology",
    "extract_all",
    "export_to_rdfxml",
    "export_wikipu_ontology",
    "owl_to_markdown",
    "export_ontology_to_markdown",
]
