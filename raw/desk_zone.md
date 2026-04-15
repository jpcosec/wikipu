# The Desk Zone

## Core Idea

The repository has four information zones, each with a distinct role and mutability contract:

| Zone | Role | Mutability |
|---|---|---|
| `raw/` | Immutable seed material. The origin. | Read-only |
| `wiki/` | Current truth. Documentation, standards, graph. | Curated, governed |
| `desk/` | Active operational state. Everything currently in motion. | Ephemeral — items deleted when resolved |
| `drawers/` | Deferred ideas not yet in motion. | Low-churn, reviewed periodically |

`desk/` replaces `plan_docs/`. The rename is necessary because `plan_docs/` implies only feature planning. The desk contains all active operational processes: implementation work, proposals, design decisions, self-repair cycles, and the central gate monitor. "What's on the desk?" answers the state of the system in one question.

---

## What Belongs on the Desk

Everything currently in motion that requires a human or agent decision to advance:

| Subdirectory | Contents |
|---|---|
| `desk/Gates.md` | Central gate monitor — all open HITL blocks across all boards |
| `desk/issues/Board.md` | Implementation work board (entry point) |
| `desk/issues/` | Issue files — one per unit of work |
| `desk/proposals/` | Topology and facet proposals awaiting approval |

`Gates.md` lives at the root of `desk/` — it is not a domain board but the monitoring surface across all domains.

---

## The Ephemeral Contract

Everything on the desk is temporary by design. The healthy state is: item resolved → file deleted → changelog updated → only history in git.

An item that survives its own resolution is documentation drift. A desk with no items means the system is in a clean state. The desk is not an archive — it is a live operational surface.

This is the same principle as the former `plan_docs/` ephemerality, extended to all operational domains.

---

## Lifecycle of a Desk Item

```
idea or detected problem
    ↓
raw/ seed (if conceptual) OR direct to desk/ (if actionable)
    ↓
desk/<domain>/Board.md — item added to the appropriate phase
    ↓
desk/<domain>/items/<slug>.md — full item file created
    ↓
if HITL required: desk/Gates.md — gate entry added
    ↓
human resolves gate (approves, decides, answers)
    ↓
agent or human executes resolution
    ↓
desk/<domain>/items/<slug>.md — DELETED
    ↓
desk/<domain>/Board.md — item removed
    ↓
desk/Gates.md — gate line removed (if applicable)
    ↓
changelog.md — one entry recording what was resolved
```

History lives in git log and changelog. The desk is clean.

---

## Renaming from plan_docs/

`plan_docs/` → `desk/`
`plan_docs/issues/Index.md` → `desk/issues/Board.md`
`plan_docs/issues/` → `desk/issues/`

`future_docs/` → `drawers/`

The content does not change in the rename — only the location and the name.

---

## Relation to the Board and Gate Pattern

The desk is the container. Boards and Gates are the structures within it. A Board is a domain view; a Gate is a blocking item; Gates.md is the cross-domain monitor. The desk makes all three accessible from one root directory.

---

## Why "Desk"

The name carries the right semantic naturally:
- "What's on the desk?" = what is currently active
- "Clear the desk" = complete the active work (consistent with the ephemeral contract)
- "Check the desk" = check current operational state before starting new work

It differentiates clearly from `wiki/` (truth, permanent), `raw/` (seed, immutable), and `backlog/` (deferred, not yet active). The desk is where work happens right now.
