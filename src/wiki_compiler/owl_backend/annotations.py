"""Extract Markdown sections as annotation properties."""

import re
from typing import Optional


def extract_annotations(node_class, body: str, ontology) -> None:
    """Extract sections and content as annotation properties."""
    if hasattr(node_class, "content"):
        clean_body = re.sub(r"^#+\s+", "", body, flags=re.MULTILINE)
        clean_body = re.sub(r"\[\[([^\]]+)\]\]", r"\1", clean_body)
        clean_body = clean_body.strip()
        node_class.content = clean_body

    headers = re.findall(r"^(#{1,6})\s+(.+)$", body, re.MULTILINE)
    if hasattr(node_class, "sections"):
        sections = [{"level": len(h), "title": t.strip()} for h, t in headers]
        node_class.sections = sections
