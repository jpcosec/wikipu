"""
Provides logic for validating the orthogonality and uniqueness of proposed Knowledge Graph facets.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

import networkx as nx

from .contracts import FacetOrthogonalityReport, FacetProposal
from .query_executor import execute_query
from .query_language import StructuredQuery
from .registry import FacetRegistry, FacetSpec

DEFAULT_ATTEMPTS = 3
_STOP_WORDS = {
    "what", "how", "is", "are", "this", "the", "a", "an", "does",
    "do", "it", "its", "of", "by", "to", "for", "node", "each",
    "which", "where", "when", "has", "have", "and", "why", "who",
    "with", "from", "into", "onto", "upon", "about", "above", "below",
}


def validate_facet_proposal(
    proposal: FacetProposal,
    registry: FacetRegistry,
    graph: nx.DiGraph,
    state_path: Path,
) -> FacetOrthogonalityReport:
    """
    Evaluates a facet proposal for collisions with existing facets and redundant information.
    """
    colliding_facets = _find_question_collisions(proposal.question, registry)
    field_collisions = _find_field_collisions(proposal.proposed_fields, registry)
    query_already_answered = _check_attempted_query(proposal.attempted_query, graph)

    is_orthogonal = not colliding_facets and not field_collisions and not query_already_answered
    attempts = _update_attempts(state_path, proposal.proposed_facet_name, is_orthogonal)
    suggestion = _build_suggestion(colliding_facets, field_collisions, query_already_answered)

    return FacetOrthogonalityReport(
        is_orthogonal=is_orthogonal,
        colliding_facets=colliding_facets,
        field_collisions=field_collisions,
        query_already_answered=query_already_answered,
        resolution_suggestion=suggestion,
        attempts_remaining=attempts,
    )


def _tokenise(question: str) -> set[str]:
    """
    Converts a question string into a set of meaningful tokens by filtering stop words.
    """
    tokens = re.findall(r"[a-z0-9]+", question.lower())
    return {t for t in tokens if t not in _STOP_WORDS and len(t) >= 2}


def _jaccard(a: set[str], b: set[str]) -> float:
    """
    Calculates the Jaccard similarity index between two sets of tokens.
    """
    if not a and not b:
        return 1.0  # Both questions only have stopwords -> highly similar
    return len(a & b) / len(a | b)


def _find_question_collisions(
    question: str, registry: FacetRegistry, threshold: float = 0.3
) -> list[FacetSpec]:
    """
    Identifies existing facets whose underlying questions are semantically similar to the proposal.
    """
    proposed_tokens = _tokenise(question)
    collisions = []
    for name in registry.facet_names:
        spec = registry.get_spec(name)
        if _jaccard(proposed_tokens, _tokenise(spec.question)) >= threshold:
            collisions.append(spec)
    return collisions


def _find_field_collisions(
    proposed_fields: list[dict[str, str]], registry: FacetRegistry
) -> list[str]:
    """
    Checks if any proposed field names already exist in the global facet registry.
    """
    existing: dict[str, str] = {}
    for name in registry.facet_names:
        for field in registry.get_spec(name).fields:
            existing[field.name] = name
    return [
        f"{f['name']} (already in {existing[f['name']]})"
        for f in proposed_fields
        if f.get("name") in existing
    ]


def _check_attempted_query(attempted_query: dict | None, graph: nx.DiGraph) -> bool:
    """
    Determines if the information targeted by the proposal can already be retrieved via query.
    """
    if not attempted_query:
        return False
    try:
        query = StructuredQuery.model_validate(attempted_query)
        results = execute_query(graph, query)
        return len(results) > 0
    except Exception:
        return False


def _update_attempts(state_path: Path, facet_name: str, is_orthogonal: bool) -> int:
    """
    Tracks and decrements the number of allowed validation attempts for a specific facet.
    """
    state_path.parent.mkdir(parents=True, exist_ok=True)
    state = json.loads(state_path.read_text(encoding="utf-8")) if state_path.exists() else {}
    if is_orthogonal:
        state[facet_name] = DEFAULT_ATTEMPTS
    else:
        state[facet_name] = max(0, int(state.get(facet_name, DEFAULT_ATTEMPTS)) - 1)
    state_path.write_text(json.dumps(state, indent=2), encoding="utf-8")
    return state[facet_name]


def _build_suggestion(
    colliding_facets: list[FacetSpec],
    field_collisions: list[str],
    query_already_answered: bool,
) -> str | None:
    """
    Constructs a human-readable guidance message based on validation failures.
    """
    parts: list[str] = []
    if colliding_facets:
        names = ", ".join(f.facet_name for f in colliding_facets)
        parts.append(f"Question overlaps with existing facets: {names}. Consider adding a field to one of them instead.")
    if field_collisions:
        parts.append(f"Field name collision(s): {', '.join(field_collisions)}. Rename proposed fields.")
    if query_already_answered:
        parts.append(
            "The attempted_query already returns results — this information exists in the graph. "
            "Use a StructuredQuery instead of adding a new facet."
        )
    return " ".join(parts) or None
