"""Export OWL ontology to Markdown files."""

from pathlib import Path
from typing import Optional

from rdflib import Graph, Literal, Namespace

ONTOLOGY_IRI = "https://wikipu.ai/ontology/"
WIKIPU = Namespace(ONTOLOGY_IRI)


def owl_to_markdown(node_uri, graph: Graph) -> Optional[str]:
    """Export an OWL individual to Markdown format."""
    lines = ["---"]
    lines.append(f"identity:")
    lines.append(f'  node_id: "{node_uri}"')

    for s, p, o in graph.triples((node_uri, WIKIPU.node_type, None)):
        if isinstance(o, Literal):
            lines.append(f'  node_type: "{o}"')
            break

    for s, p, o in graph.triples((node_uri, WIKIPU.status, None)):
        if isinstance(o, Literal):
            lines.append(f"compliance:")
            lines.append(f'  status: "{o}"')
            break

    lines.append("---")
    lines.append("")

    references = []
    for s, p, o in graph.triples((node_uri, WIKIPU.references, None)):
        if isinstance(o, Literal):
            references.append(str(o))

    if references:
        lines.append("## Related Concepts")
        for ref in references:
            lines.append(f"- [[{ref}]]")
        lines.append("")

    return "\n".join(lines)


def export_ontology_to_markdown(
    wiki_root: Path, world: Optional[Graph] = None, force: bool = False
) -> list[Path]:
    """Export entire ontology to Markdown files."""
    if world is None:
        from wiki_compiler.owl_backend.extractor import get_world

        world = get_world()

    exported = []

    for s, p, o in world.triples((None, WIKIPU.node_id, None)):
        md_content = owl_to_markdown(s, world)
        if md_content is None:
            continue

        node_name = str(s).split("/")[-1]
        md_path = wiki_root / f"{node_name}.md"

        if md_path.exists() and not force:
            continue

        md_path.parent.mkdir(parents=True, exist_ok=True)
        md_path.write_text(md_content, encoding="utf-8")
        exported.append(md_path)

    return exported
