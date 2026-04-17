"""Export OWL ontology to Markdown files."""

from pathlib import Path
from typing import Optional

from owlready2 import World

from wiki_compiler.owl_backend import get_world, get_ontology, ONTOLOGY_IRI


def owl_to_markdown(individual, wiki_root: Path) -> Optional[str]:
    """Export an OWL individual to Markdown format."""
    lines = ["---"]
    lines.append(f"identity:")
    lines.append(f'  node_id: "{individual.name}"')

    node_type = getattr(individual, "node_type", None)
    if node_type:
        lines.append(f'  node_type: "{node_type}"')

    compliance_status = getattr(individual, "compliance_status", None)
    if compliance_status:
        lines.append(f"compliance:")
        lines.append(f'  status: "{compliance_status}"')

    failing = getattr(individual, "failing_standards", None)
    if failing:
        if not lines[-1].startswith("compliance"):
            lines.append("compliance:")
        lines.append(f"  failing_standards: {list(failing)}")

    lines.append("---")
    lines.append("")

    content = getattr(individual, "content", None)
    if content:
        lines.append(str(content))
        lines.append("")

    sections = getattr(individual, "sections", None)
    if sections:
        for section in sections:
            level = section.get("level", 1)
            title = section.get("title", "")
            lines.append(f"{'#' * level} {title}")
            lines.append("")

    references = getattr(individual, "references", None)
    if references:
        lines.append("## Related Concepts")
        for ref in references:
            lines.append(f"- [[{ref}]]")
        lines.append("")

    return "\n".join(lines)


def export_ontology_to_markdown(
    wiki_root: Path, world: Optional[World] = None, force: bool = False
) -> list[Path]:
    """Export entire ontology to Markdown files."""
    if world is None:
        world = get_world()

    ontology = get_ontology(world)
    exported = []

    for individual in ontology.individuals():
        md_content = owl_to_markdown(individual, wiki_root)
        if md_content is None:
            continue

        node_name = individual.name
        md_path = wiki_root / f"{node_name}.md"

        if md_path.exists() and not force:
            continue

        md_path.parent.mkdir(parents=True, exist_ok=True)
        md_path.write_text(md_content, encoding="utf-8")
        exported.append(md_path)

    return exported
