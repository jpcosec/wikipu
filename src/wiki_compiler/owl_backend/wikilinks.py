"""Extract wiki-links as :references properties."""

import re
from pathlib import Path
from typing import Optional, Set


WIKILINK_PATTERN = re.compile(r"\[\[([^\]]+)\]\]")


def extract_wikilinks(node_class, body: str, ontology) -> Set[str]:
    """Extract wiki-links and create :references triples."""
    links = set(WIKILINK_PATTERN.findall(body))

    with ontology:
        for link in links:
            link_name = link.strip()
            try:
                ontology.references.append(node_class)
            except AttributeError:
                pass

    if hasattr(node_class, "references"):
        node_class.references = links

    return links


def resolve_wikilink(link: str, wiki_root: Path) -> Optional[Path]:
    """Resolve a wiki-link to an actual file path."""
    candidates = [
        wiki_root / f"{link}.md",
        wiki_root / link,
    ]
    for path in candidates:
        if path.exists():
            return path
    return None
