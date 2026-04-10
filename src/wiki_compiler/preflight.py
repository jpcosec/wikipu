"""
Preflight validation and minimal-energy action selection for the coordinator.
Enforces House Rules ID-1, ID-2, ID-4, and ID-5 before execution.
"""

from __future__ import annotations

from pathlib import Path
from typing import Literal
from pydantic import BaseModel, Field
from .contracts import KnowledgeNode


class PreflightFinding(BaseModel):
    """A rule violation or recommendation found during preflight."""
    rule_id: str = Field(description="The ID of the rule being evaluated (e.g. 'ID-4').")
    severity: Literal["info", "warning", "error"] = Field(description="Severity of the finding.")
    message: str = Field(description="Human-readable explanation of the finding.")
    action_override: str | None = Field(
        default=None, description="Recommended replacement action (e.g. 'gate', 'abort')."
    )


class PreflightReport(BaseModel):
    """The result of a preflight check for one or more planned actions."""
    is_safe: bool = Field(description="True if no errors were found.")
    findings: list[PreflightFinding] = Field(default_factory=list)


def evaluate_action_safety(
    action_type: str, 
    target_id: str, 
    project_root: Path
) -> PreflightFinding | None:
    """
    Evaluates a single planned action against identity rules.
    Returns a finding if a violation or risk is detected.
    """
    
    # ID-4: Zone Separation
    # Agents should not write to raw/
    if action_type in {"write", "update", "delete"} and target_id.startswith("raw/"):
        return PreflightFinding(
            rule_id="ID-4",
            severity="error",
            message=f"Inviolable zone violation: cannot {action_type} in raw/",
            action_override="abort"
        )
        
    # ID-5: Topology Boundary
    # Any action affecting files outside of src/, wiki/, plan_docs/, or desk/
    # requires a human gate.
    safe_zones = {"src/", "wiki/", "plan_docs/", "desk/", "tests/", "manifests/"}
    is_internal = any(target_id.startswith(zone) for zone in safe_zones)
    
    if not is_internal:
        return PreflightFinding(
            rule_id="ID-5",
            severity="warning",
            message=f"Action targets boundary-crossing path '{target_id}'.",
            action_override="gate"
        )
        
    return None


def select_minimal_energy_action(
    perturbation_type: str,
    target_id: str,
    candidates: list[str]
) -> str:
    """
    ID-2: Minimal Energy. 
    Selects the action that satisfies the requirement with least complexity.
    """
    # Simple heuristic: prioritize extending/updating over creating/splitting
    if "update" in candidates:
        return "update"
    if "rebuild" in candidates:
        return "rebuild"
    return candidates[0] if candidates else "ignore"
