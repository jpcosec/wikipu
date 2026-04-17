---
pill_type: warning
scope: global
language: en
nature: context
bound_to: self
created: 2026-04-17
lifecycle: current
---

# Global Warnings

## Do NOT

1. **Edit with dirty tree** — Commit first, then edit (OP-6)
2. **Skip the desk ritual** — Always run Initialization Ritual first
3. **Batch unrelated changes** — One commit per logical change
4. **Import infrastructure into domain** — DIP violation
5. **Use bare Exception** — Define domain exceptions

## Avoid

- Creating archive folders (history lives in git)
- Using dict instead of Pydantic for data
- Leaving stale gate entries (>1 cycle)
- Keeping drawers items >6 months
- Writing to drawers from desk

## Anti-Patterns

- Jumping straight to read without querying
- Dumping entire files instead of targeted extraction
- Ignoring status/energy output
- Guessing file paths
