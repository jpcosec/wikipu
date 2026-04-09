# Gate Table Runtime

**Explanation:** The coordinator needs a concrete gate surface it can pause on, inspect, and resume from. `wiki/standards/artifacts/gate.md` defines the gate artifact, but there is no parser, writer, or state helper for `desk/Gates.md`.

**Reference:** `wiki/standards/artifacts/gate.md`, `wiki/reference/protocols/gate_loop.md`, `src/wiki_compiler/main.py`

**What to fix:** Add typed gate-row models plus read/write helpers for `desk/Gates.md`, including open/approved/rejected state handling.

**How to do it:**
1. Define a gate-row contract and markdown table helpers.
2. Add runtime helpers for list/load/write/update operations.
3. Add focused tests for round-trip parsing and resume-state detection.

**Depends on:** `none`
