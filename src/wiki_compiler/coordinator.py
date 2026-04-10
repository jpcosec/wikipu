"""
The central orchestrator for the autopoietic loop.
"""

from __future__ import annotations

import json
from pathlib import Path
from datetime import datetime
from .perception import build_status_report
from .builder import build_wiki
from .ingest import ingest_raw_sources
from .gates import load_gates, add_gate, update_gate_status, save_gates
from .cleanser import detect_cleansing_candidates, apply_cleansing_proposal


def run_coordinator_cycle(
    project_root: Path,
    graph_path: Path,
    wiki_dir: Path,
    manifest_path: Path | None = None,
) -> dict[str, object]:
    """
    Executes one cycle of the autopoietic loop.
    1. Resume: check for approved gates from previous cycles.
    2. Perception: detect perturbations.
    3. Classification: decide response actions.
    4. Gating: write new gates for actions requiring approval.
    5. Execution: run safe or approved actions.
    6. Rebuild: update the knowledge graph.
    """
    gates_path = project_root / "desk/Gates.md"
    gates_table = load_gates(gates_path)
    
    executed_actions: list[str] = []
    
    # --- 1. Resume Flow ---
    processed_any = False
    gates_to_remove = []
    for gate in list(gates_table.gates):
        if gate.status == "approved":
            # Resume action based on proposal type
            if "cleansing" in gate.proposal.lower() or "test-destroy" in gate.proposal.lower():
                proposal_file = project_root / gate.proposal
                if proposal_file.exists():
                    try:
                        from .contracts import CleansingReport
                        report_data = json.loads(proposal_file.read_text(encoding="utf-8"))
                        report = CleansingReport.model_validate(report_data)
                        for proposal in report.proposals:
                            apply_cleansing_proposal(proposal, project_root)
                        executed_actions.append(f"applied_cleansing_{gate.gate_id}")
                        gates_to_remove.append(gate)
                        processed_any = True
                    except Exception as e:
                        print(f"[ERROR] Failed to apply approved gate {gate.gate_id}: {e}")
    
    if processed_any:
        # Also remove ANY other cleansing gates to prevent redundant cycles
        for other in list(gates_table.gates):
            if other not in gates_to_remove and ("cleansing" in other.proposal.lower() or "test-destroy" in other.proposal.lower()):
                gates_to_remove.append(other)
                
        for g in gates_to_remove:
            if g in gates_table.gates:
                gates_table.gates.remove(g)
                
        save_gates(gates_path, gates_table)
        build_wiki(source_dir=wiki_dir, graph_path=graph_path, project_root=project_root)
        
        return {
            "status": "success",
            "perturbations_detected": 0,
            "actions_taken": executed_actions,
            "open_gates": [g.gate_id for g in gates_table.gates if g.status == "open"]
        }
    
    # --- 2. Perception & Classification ---
    report = build_status_report(graph_path, project_root)
    perturbations = report.get("perturbations", [])
    
    # --- 3. Execution (Safe Actions) ---
    from .preflight import evaluate_action_safety
    
    untracked_raw = [p for p in perturbations if p["type"] == "untracked_raw"]
    for p in untracked_raw:
        if p["action"] == "ingest_raw_source":
            # Preflight check
            finding = evaluate_action_safety("write", f"wiki/drafts/{Path(p['id']).name}", project_root)
            
            if finding and finding.severity == "error":
                print(f"[ERROR] Preflight blocked action: {finding.message}")
                continue
            
            if finding and finding.action_override == "gate":
                # Downgrade to gated action (not implemented in this skeleton yet, 
                # but we could add a gate row here)
                print(f"[INFO] Preflight gated action: {finding.message}")
                continue

            ingest_raw_sources(
                source_dir=project_root / "raw",
                dest_dir=wiki_dir / "drafts",
                project_root=project_root,
                manifest_path=manifest_path
            )
            executed_actions.append(f"ingested_raw_files")
            break # ingest_raw_sources handles all at once

    # --- 4. Gating (Unsafe Actions) ---
    cleansing_report = detect_cleansing_candidates(graph_path)
    if cleansing_report.proposals:
        # Check if we already have an open gate for cleansing
        has_cleansing_gate = any(("cleansing" in g.proposal.lower() or "test-destroy" in g.proposal.lower()) for g in gates_table.gates)
        if not has_cleansing_gate:
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
            prop_path = f"desk/proposals/cleansing-{timestamp}.json"
            (project_root / prop_path).parent.mkdir(parents=True, exist_ok=True)
            (project_root / prop_path).write_text(json.dumps(cleansing_report.model_dump(), indent=2), encoding="utf-8")
            
            new_gate = add_gate(gates_path, prop_path, f"Apply {len(cleansing_report.proposals)} cleansing proposals")
            gates_table = load_gates(gates_path)
            print(f"[INFO] Created {new_gate.gate_id} for cleansing. Cycle pausing for approval.")

    # --- 5. Rebuild ---
    if executed_actions:
        build_wiki(source_dir=wiki_dir, graph_path=graph_path, project_root=project_root)
        executed_actions.append("rebuilt_graph")

    open_gates = [g for g in gates_table.gates if g.status == "open"]
    return {
        "status": "paused" if open_gates else "success",
        "perturbations_detected": len(perturbations),
        "actions_taken": executed_actions,
        "open_gates": [g.gate_id for g in open_gates]
    }
