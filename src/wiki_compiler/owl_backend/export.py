"""Export quadstore to RDF/XML."""

from pathlib import Path
from typing import Optional

from owlready2 import World

from wiki_compiler.owl_backend import ONTOLOGY_PATH
from wiki_compiler.owl_backend.extractor import get_world


def export_to_rdfxml(
    world: Optional[World] = None, output_path: Optional[Path] = None
) -> Path:
    """Export the quadstore to RDF/XML format."""
    if world is None:
        world = get_world()

    output = output_path or ONTOLOGY_PATH
    world.save(str(output))
    return output


def export_wikipu_ontology(wiki_root: Path, output_path: Optional[Path] = None) -> Path:
    """Build and export the complete wikipu ontology."""
    from wiki_compiler.owl_backend.extractor import extract_all

    world = extract_all(wiki_root)
    return export_to_rdfxml(world, output_path)
