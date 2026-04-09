# Cross-Session Memory

**Explanation:** Each session starts cold. Decisions made, anomalies found, gates resolved, and design questions answered in session N are not available to session N+1 unless explicitly encoded somewhere during the session. The autopoietic loop requires continuity — the system needs to remember what perturbations it has already responded to, what the outcome was, and what is still pending. Without cross-session memory, the loop is not a loop: it is a series of independent cold starts that re-derive from scratch each time.

**Reference:** `raw/autopoiesis_system.md`, `raw/trail_collect.md`, `desk/Gates.md` (planned)

**What to fix:**
1. Define a `SessionLog` model in `contracts.py`: `session_id`, `opened_at`, `closed_at`, `perturbations_detected: list[str]`, `gates_opened: list[str]`, `gates_resolved: list[str]`, `trail_artifacts: list[TrailArtifact]`, `nodes_created: list[str]`, `nodes_deleted: list[str]`.
2. Define a `TrailArtifact` model: `artifact_type` (`decision` | `gap` | `correction` | `concept` | `rule_patch`), `description`, `routed_to` (file path where it was encoded), `session_id`.
3. Write session logs to `desk/autopoiesis/sessions/<session_id>.json` at session close (via trail collect step).
4. Add a `wiki-compiler history` command that reads session logs and outputs: open gates across all sessions, anomalies that recurred across multiple sessions, decisions that were made and where they were encoded.
5. The autopoiesis loop coordinator reads the most recent session log on startup to restore context before detecting new perturbations.

**How to do it:**
- Session ID = ISO timestamp of session open, e.g. `2026-04-09T02:51`.
- Trail collect (see `raw/trail_collect.md`) is the mechanism that populates `TrailArtifact` entries at session close.
- `history` command is read-only — it surfaces patterns across sessions for human review.
- Session logs are append-only. Never edited after close. The audit trail lives here.

**Depends on:** `unimplemented/autopoiesis-loop-coordinator.md` (the coordinator triggers session open/close and calls trail collect)
