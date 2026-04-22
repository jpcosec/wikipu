"""
Audit system for checking Knowledge Graph quality and compliance.
Includes checks for missing docstrings, undocumented code, and stale edges.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from pathlib import Path
import networkx as nx
from .contracts import AuditFinding, KnowledgeNode
from .graph_utils import iter_knowledge_nodes, load_knowledge_node
from .query_executor import execute_query
from .query_language import FacetFilter, FieldCondition, StructuredQuery


@dataclass
class AuditReport:
    """
    Represents the collected findings from a Knowledge Graph audit.
    """

    findings: list[AuditFinding] = field(default_factory=list)

    @property
    def summary(self) -> dict[str, int]:
        """
        Returns a summary of the findings grouped by check name.
        """
        counts: dict[str, int] = {}
        for f in self.findings:
            counts[f.check_name] = counts.get(f.check_name, 0) + 1
        return counts


class UndocumentedCodeCheck:
    """
    Checks for code nodes that lack documentation (either via wiki edge OR docstring).
    Considers code documented if:
    1. Has explicit 'documents' edge from wiki, OR
    2. Has docstring in semantics facet, OR
    3. Parent module has documentation
    """

    check_name = "undocumented_code"
    question = "Which code nodes have no wiki documentation?"
    related_facet = "semantics"

    def run(self, graph: nx.DiGraph) -> list[AuditFinding]:
        """
        Executes the undocumented code check against the provided graph.
        """
        # Get explicitly documented via wiki edge
        wiki_documented = {
            target
            for _, target, data in graph.edges(data=True)
            if data.get("relation") == "documents"
        }

        # Get self-documented via docstring in semantics
        self_documented = set()
        for node in iter_knowledge_nodes(graph):
            if node.identity.node_type in {"code_construct", "file"}:
                if node.semantics and node.semantics.raw_docstring:
                    self_documented.add(node.identity.node_id)

        # Build parent->children mapping for inheritance
        parent_of: dict[str, str] = {}
        for node in iter_knowledge_nodes(graph):
            nid = node.identity.node_id
            if ":" in nid and ".py" in nid:
                parts = nid.split(":")
                if len(parts) > 1:
                    parent = ":".join(parts[:-1])
                    parent_of[nid] = parent

        # Code constructs (from AST scan) are inherently documented
        ast_documented = {
            node.identity.node_id
            for node in iter_knowledge_nodes(graph)
            if node.identity.node_type == "code_construct"
        }

        findings = []
        for node in iter_knowledge_nodes(graph):
            if node.identity.node_type not in {"file", "code_construct"}:
                continue
            nid = node.identity.node_id

            # Code constructs ARE self-documenting (from AST)
            if nid in ast_documented:
                continue

            # Skip __pycache__ etc
            if "__pycache__" in nid:
                continue

            # Check if documented in any way
            if nid in wiki_documented:
                continue
            if nid in self_documented:
                continue
            # Check parent module coverage
            parent = parent_of.get(nid)
            if parent and parent in wiki_documented:
                continue
            if parent and parent in self_documented:
                continue

            findings.append(
                AuditFinding(
                    check_name=self.check_name,
                    node_id=nid,
                    detail="No documentation via wiki edge, docstring, parent module, or AST.",
                )
            )
        return findings


class MissingDocstringsCheck:
    """
    Checks for code nodes that do not have a raw docstring in their SemanticFacet.
    """

    check_name = "missing_docstrings"
    question = "Which code nodes have no docstring?"
    related_facet = "semantics"

    def run(self, graph: nx.DiGraph) -> list[AuditFinding]:
        """
        Executes the missing docstrings check against the provided graph.
        """
        matches = execute_query(
            graph,
            StructuredQuery(
                filters=[
                    FacetFilter(
                        facet="semantics",
                        conditions=[
                            FieldCondition(field="raw_docstring", op="is_null"),
                        ],
                    ),
                ]
            ),
        )
        return [
            AuditFinding(
                check_name=self.check_name,
                node_id=node.identity.node_id,
                detail="SemanticFacet.raw_docstring is null.",
            )
            for node in matches
            if node.identity.node_type in {"file", "code_construct"}
        ]


class UntypedIOCheck:
    """
    Checks for IO ports that lack a schema contract for disk or memory media.
    """

    check_name = "untyped_io"
    question = "Which nodes produce or consume data without a schema contract?"
    related_facet = "io"

    def run(self, graph: nx.DiGraph) -> list[AuditFinding]:
        """
        Executes the untyped IO check against the provided graph.
        """
        findings = []
        for node in iter_knowledge_nodes(graph):
            for port in node.io_ports:
                if port.medium in {"disk", "memory"} and port.schema_ref is None:
                    findings.append(
                        AuditFinding(
                            check_name=self.check_name,
                            node_id=node.identity.node_id,
                            detail=f"Port medium={port.medium} path={port.path_template!r} has no schema_ref.",
                        )
                    )
                    break
        return findings


class ComplianceViolationsCheck:
    """
    Checks for nodes that fail house rules standards as defined in their ComplianceFacet.
    """

    check_name = "compliance_violations"
    question = "Which nodes are failing house rules standards?"
    related_facet = "compliance"

    def run(self, graph: nx.DiGraph) -> list[AuditFinding]:
        """
        Executes the compliance violations check against the provided graph.
        """
        matches = execute_query(
            graph,
            StructuredQuery(
                filters=[
                    FacetFilter(
                        facet="compliance",
                        conditions=[
                            FieldCondition(
                                field="failing_standards", op="ne", value=[]
                            ),
                        ],
                    ),
                ]
            ),
        )
        return [
            AuditFinding(
                check_name=self.check_name,
                node_id=node.identity.node_id,
                detail=f"Failing: {', '.join(node.compliance.failing_standards)}",
            )
            for node in matches
            if node.compliance and node.compliance.failing_standards
        ]


class StaleEdgesCheck:
    """
    Checks for edges that point to non-existent target nodes.
    """

    check_name = "stale_edges"
    question = "Which edges point to nodes that no longer exist?"
    related_facet = "semantics"

    def run(self, graph: nx.DiGraph) -> list[AuditFinding]:
        """
        Executes the stale edges check against the provided graph.
        """
        findings = []
        graph_node_ids = {n for n in graph.nodes()}
        for source, target, data in graph.edges(data=True):
            if target not in graph_node_ids:
                findings.append(
                    AuditFinding(
                        check_name=self.check_name,
                        node_id=source,
                        detail=f"Edge relation={data.get('relation')!r} points to missing node `{target}`.",
                    )
                )
        return findings


class OrphanedPlansCheck:
    """
    Checks for deferred nodes (drawers/) that have no connection to any code node.
    """

    check_name = "orphaned_plans"
    question = "Which drawers/ nodes have no connection to any code node?"
    related_facet = "compliance"

    def run(self, graph: nx.DiGraph) -> list[AuditFinding]:
        """
        Executes the orphaned plans check against the provided graph.
        """
        code_ids = {
            n.identity.node_id
            for n in iter_knowledge_nodes(graph)
            if n.identity.node_type in {"file", "code_construct"}
        }
        raw_ids = {
            n.identity.node_id
            for n in iter_knowledge_nodes(graph)
            if n.identity.node_id.startswith("raw:")
        }
        findings = []
        for node in iter_knowledge_nodes(graph):
            if "drawers" not in node.identity.node_id:
                continue
            # Connect to code OR raw is not orphaned
            outgoing = {t for _, t in graph.out_edges(node.identity.node_id)}
            if not any(t in code_ids or t.startswith("raw:") for t in outgoing):
                findings.append(
                    AuditFinding(
                        check_name=self.check_name,
                        node_id=node.identity.node_id,
                        detail="drawers node has no outgoing edge to code or raw.",
                    )
                )
        return findings


class MissingAbstractCheck:
    """
    Checks for wiki nodes that lack a valid abstract or intent description.
    """

    check_name = "missing_abstract"
    question = "Which wiki nodes have no valid abstract paragraph?"
    related_facet = "semantics"

    def run(self, graph: nx.DiGraph) -> list[AuditFinding]:
        """
        Executes the missing abstract check against the provided graph.
        """
        findings = []
        for node in iter_knowledge_nodes(graph):
            if not node.identity.node_id.startswith("doc:"):
                continue
            if (
                not node.semantics
                or not node.semantics.intent
                or node.semantics.intent == "Wiki node"
            ):
                # Non-existent files are high-priority broken links
                node_path = Path(node.identity.node_id.removeprefix("doc:"))
                is_missing = not node_path.exists()
                detail = "No valid abstract paragraph detected in wiki node."
                if is_missing:
                    detail = "Referenced file does not exist - broken link."
                findings.append(
                    AuditFinding(
                        check_name=self.check_name,
                        node_id=node.identity.node_id,
                        detail=detail,
                    )
                )
        return findings


_ALL_CHECKS = [
    UndocumentedCodeCheck(),
    MissingDocstringsCheck(),
    UntypedIOCheck(),
    ComplianceViolationsCheck(),
    StaleEdgesCheck(),
    OrphanedPlansCheck(),
    MissingAbstractCheck(),
]


def run_audit(graph: nx.DiGraph) -> AuditReport:
    """
    Runs all registered audit checks against the Knowledge Graph.
    """
    report = AuditReport()
    for check in _ALL_CHECKS:
        report.findings.extend(check.run(graph))
    return report
