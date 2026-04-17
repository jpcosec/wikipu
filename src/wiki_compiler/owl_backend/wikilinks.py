"""Extract wiki-links as :references properties."""

import re
from typing import Set


WIKILINK_PATTERN = re.compile(r"\[\[([^\]]+)\]\]")


def extract_wikilinks(node_class, body: str, ontology) -> Set[str]:
    """Extract wiki-links and link them as references."""
    links = set(WIKILINK_PATTERN.findall(body))

    if hasattr(node_class, "references"):
        node_class.references = links

    return links
