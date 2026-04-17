"""
Energy command handler.
"""

from __future__ import annotations
import argparse
from pathlib import Path

from ..energy import run_energy_audit, DRIFT_PENALTY_WEIGHT
from ..graph_utils import load_graph


def handle_energy(args: argparse.Namespace) -> None:
    """Execute the energy command."""
    graph = load_graph(Path(args.graph))
    report = run_energy_audit(graph, Path(args.project_root))

    if getattr(args, "reasoning", False):
        try:
            from wiki_compiler.owl_reasoner import OwlReasoner

            reasoner = OwlReasoner()
            inferred = reasoner.sync_reasoner()
            consistency = reasoner.consistency_check()
            report.inferred_relationships = reasoner.get_inferred_relationships()
            report.reasoning_output = inferred
            report.consistency_status = consistency.get("consistency", ["UNKNOWN"])[0]
        except ImportError:
            pass

    if args.format == "json":
        print(report.model_dump_json(indent=2))
    else:
        ce = report.current_energy
        print(f"## Systemic Energy Report\n")
        print(f"**Total Energy Score: {ce.energy_score:.2f}**\n")
        print(f"### Breakdown")
        print(
            f"- **Structural (Redundancy)**: {ce.structural_energy:.2f} (r={ce.redundant_nodes}, b={ce.boilerplate_ratio:.2f})"
        )
        print(
            f"- **Abstraction (Complexity)**: {ce.abstraction_energy:.2f} (f={ce.long_files}, c={ce.complex_functions})"
        )
        print(
            f"- **Drift (Code-Doc)**: {ce.drift_flags * DRIFT_PENALTY_WEIGHT:.2f} (d={ce.drift_flags})"
        )
        print(
            f"- **Compliance (Debt)**: {ce.violation_energy:.2f} (v={ce.compliance_violations})"
        )
        print(
            f"- **Operational (Drift/Gates)**: {ce.perturbation_energy:.2f} (p={ce.perturbations}, g={ce.open_gates})"
        )
        if ce.agent_violations > 0:
            print(
                f"- **Agent Rule Violations**: {ce.agent_violation_energy:.2f} (v={ce.agent_violations})"
            )

        if getattr(args, "reasoning", False):
            status = getattr(report, "consistency_status", "UNKNOWN")
            print(f"\n### OWL Reasoning")
            print(f"- **Consistency**: {status}")
            inferred = getattr(report, "reasoning_output", {})
            if "reasoning" in inferred:
                print(f"- **Reasoner**: {inferred['reasoning']}")

        if ce.energy_score > 500:
            print(
                f"\n[❌] **CRITICAL ENERGY LEVEL**: System entropy is high. Resolve compliance debt and close open gates immediately."
            )
        elif ce.energy_score > 200:
            print(
                f"\n[⚠️] **HIGH ENERGY**: Consider a cleansing cycle to simplify the graph."
            )
        else:
            print(f"\n[✅] **LOW ENERGY**: System is lean and stable.")
