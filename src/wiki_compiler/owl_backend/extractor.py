"""Extract Markdown wiki nodes to OWL triples."""

import re
from pathlib import Path
from typing import Optional

import yaml
from rdflib import Graph, Literal, Namespace, RDF

from wiki_compiler.owl_backend import ONTOLOGY_IRI, ONTOLOGY_PATH


WIKIPU = Namespace(ONTOLOGY_IRI)


def markdown_to_rdf(markdown_path: Path) -> Graph:
    """Extract triples from a Markdown file to an RDF graph."""
    g = Graph()
    g.bind("wikipu", WIKIPU)

    if not markdown_path.exists() or not markdown_path.suffix == ".md":
        return g

    content = markdown_path.read_text(encoding="utf-8")
    frontmatter_match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)

    node_uri = WIKIPU[markdown_path.stem.replace("/", "_").replace(" ", "_")]
    g.add((node_uri, RDF.type, WIKIPU.KnowledgeNode))

    if frontmatter_match:
        frontmatter_text = frontmatter_match.group(1)
        frontmatter_data = yaml.safe_load(frontmatter_text)
        if frontmatter_data:
            identity = frontmatter_data.get("identity", {})
            if identity:
                node_id = identity.get("node_id", "")
                node_type = identity.get("node_type", "")
                if node_id:
                    g.add((node_uri, WIKIPU.node_id, Literal(node_id)))
                if node_type:
                    g.add((node_uri, WIKIPU.node_type, Literal(node_type)))

            compliance = frontmatter_data.get("compliance", {})
            if compliance:
                status = compliance.get("status", "")
                if status:
                    g.add((node_uri, WIKIPU.status, Literal(status)))

    body = content.split("---", 2)[-1] if "---" in content else content
    links = re.findall(r"\[\[([^\]]+)\]\]", body)
    for link in links[:20]:
        g.add((node_uri, WIKIPU.references, Literal(link.strip())))

    return g


def extract_all(wiki_root: Path, world: Optional[Graph] = None) -> Graph:
    """Extract all wiki nodes to OWL Graph."""
    if world is None:
        world = Graph()

    world.bind("wikipu", WIKIPU)

    for md_file in wiki_root.rglob("*.md"):
        g = markdown_to_rdf(md_file)
        for triple in g:
            world.add(triple)

    return world


def get_world() -> Graph:
    """Get the RDF graph (rdflib-based)."""
    g = Graph()
    g.bind("wikipu", WIKIPU)
    if ONTOLOGY_PATH.exists():
        g.parse(str(ONTOLOGY_PATH), format="xml")
    return g


def get_ontology(world: Graph) -> Graph:
    """Get the ontology graph."""
    return world
