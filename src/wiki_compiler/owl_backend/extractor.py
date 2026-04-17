"""Extract Markdown wiki nodes to OWL triples."""

import re
from pathlib import Path
from typing import Optional

import yaml
from owlready2 import Ontology, World

from wiki_compiler.owl_backend import ONTOLOGY_IRI, ONTOLOGY_PATH
from wiki_compiler.owl_backend.frontmatter import extract_frontmatter_triples
from wiki_compiler.owl_backend.wikilinks import extract_wikilinks
from wiki_compiler.owl_backend.annotations import extract_annotations


def get_world() -> World:
    """Get or create the Owlready2 world."""
    world = World()
    if ONTOLOGY_PATH.exists():
        world.get_ontology(f"file://{ONTOLOGY_PATH}")
    return world


def get_ontology(world: World) -> Ontology:
    """Get or create the main wikipu ontology."""
    return world.get_ontology(ONTOLOGY_IRI)


def markdown_to_owl(markdown_path: Path, world: World) -> None:
    """Extract triples from a Markdown file into the quadstore."""
    if not markdown_path.exists() or not markdown_path.suffix == ".md":
        return

    content = markdown_path.read_text(encoding="utf-8")
    frontmatter_match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)

    ontology = get_ontology(world)

    with ontology:
        node_id = markdown_path.stem
        node_class = (
            ontology[node_id] if hasattr(ontology, node_id) else type(node_id, (), {})
        )

        if frontmatter_match:
            frontmatter_text = frontmatter_match.group(1)
            frontmatter_data = yaml.safe_load(frontmatter_text)
            extract_frontmatter_triples(node_class, frontmatter_data, ontology)

        body = content.split("---", 2)[-1] if "---" in content else content
        extract_wikilinks(node_class, body, ontology)
        extract_annotations(node_class, body, ontology)


def extract_all(wiki_root: Path, world: Optional[World] = None) -> World:
    """Extract all wiki nodes to OWL."""
    if world is None:
        world = get_world()

    for md_file in wiki_root.rglob("*.md"):
        markdown_to_owl(md_file, world)

    return world
