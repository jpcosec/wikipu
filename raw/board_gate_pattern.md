# Board and Gate: The HITL Coordination Pattern

## Core Idea

Two distinct constructs govern how the system coordinates with humans:

1. **The Board** — a domain work tree: a structured index of pending items for one concern area, with phases, dependencies, and parallelization. Not a queue (FIFO) and not a flat list. A directed graph of items the system cannot advance without a decision.

2. **The Gate** — a single HITL checkpoint: one item the system cannot proceed past without explicit human input. Gates are embedded in or between Board items.

3. **desk/Gates.md** — the central gate monitor: a flat register of all open gates across all Boards. The single surface a human checks to know what the system is waiting on.

---

## The Board

### Structure

```
<domain>/Board.md
<domain>/items/<item-slug>.md
```

`Board.md` is the index and monitoring surface for one domain. It contains:
- Current state summary (one paragraph)
- Priority roadmap with phases
- Each phase lists items with a one-line description
- Dependency summary (what blocks what)
- Parallelization map

Each item lives in a separate file with: explanation, what to fix, how to do it, depends on.

### Resolution Protocol

When an item is resolved:
1. Verify existing tests are still valid.
2. Add new tests where needed.
3. Run tests.
4. Update changelog.md.
5. Delete the item file AND remove it from Board.md.
6. Commit.

Nothing is "archived" — resolved items live in git history and changelog only.

### Existing Instance

`desk/issues/` is the first Board. It tracks implementation work. The pattern should be replicated for:

| Board | Domain |
|---|---|
| `desk/issues/` | Implementation work (gaps, unimplemented features) |
| `desk/proposals/` | Topology and facet proposals awaiting approval |
| `desk/socratic/` | Open design questions awaiting resolution |
| `desk/autopoiesis/` | Self-repair cycles (cleansing, drift correction, rule patches) |

---

## The Gate

A gate is any item that:
- Cannot be resolved by the system alone
- Blocks the system from proceeding
- Requires explicit human input (approval, decision, or answer)

Gates exist in several forms:
- An issue item waiting to be picked up (implementation decision)
- A CleansingProposal with `requires_human_approval: true`
- A TopologyProposal awaiting approval before scaffolding
- A Socratic question awaiting a design decision
- A trail collect artifact awaiting integration

### Gate Properties

| Property | Description |
|---|---|
| `source_board` | Which Board this gate belongs to |
| `item_id` | The specific item within that Board |
| `gate_type` | `approval`, `decision`, `answer`, `review` |
| `blocking` | What cannot proceed until this gate resolves |
| `opened_at` | When the gate was created |

---

## desk/Gates.md — The Central Monitor

A flat register of all currently open gates across all Boards. One line per gate. The human's daily check.

Format:
```
[gate_type] <source_board>/<item_id> — <one-line description of what is needed> → blocks: <what is blocked>
```

Example:
```
[approval]  proposals/topology_cleanser_module — approve new cleanser.py topology → blocks: implementation start
[decision]  socratic/query_server_design — resolve: CLI-only vs Python API? → blocks: query-server-runtime
[review]    autopoiesis/drift_report_2026_04_09 — 3 stale nodes flagged, approve repairs → blocks: next build
```

When a gate is resolved, its line is removed from Gates.md. The resolution is recorded in changelog.md.

---

## Why Two Constructs

The Board and the Gate solve different problems:

- **Board**: tracks *what work exists* in a domain and *in what order* it should be done. The human reads a Board to understand the state of a domain.
- **Gate**: tracks *what the system is blocked on right now*. The human reads Gates.md to know what needs their attention immediately.

A Board without Gates is a backlog. Gates without a Board have no context. Together: complete visibility into both the strategic state (Board) and the operational state (Gates) of every domain.

---

## Naming Note

The current `plan_docs/issues/Index.md` should be renamed to `desk/issues/Board.md` when the desk zone is implemented. The `issues_guide.md` should be updated to reflect the Board terminology. The Gate pattern is new and has no existing implementation.
