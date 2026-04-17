"""Export quadstore to RDF/XML."""

from pathlib import Path
from typing import Optional

from rdflib import Graph

from wiki_compiler.owl_backend import ONTOLOGY_PATH
from wiki_compiler.owl_backend.extractor import get_world


def export_to_rdfxml(
    world: Optional[Graph] = None, output_path: Optional[Path] = None
) -> Path:
    """Export the graph to RDF/XML format."""
    if world is None:
        world = get_world()

    output = output_path or ONTOLOGY_PATH
    world.serialize(str(output), format="xml")
    return output


def export_wikipu_ontology(wiki_root: Path, output_path: Optional[Path] = None) -> Path:
    """Build and export the complete wikipu ontology."""
    from wiki_compiler.owl_backend.extractor import extract_all

    world = extract_all(wiki_root)
    return export_to_rdfxml(world, output_path)
