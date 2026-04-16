---
status: open
priority: p1
depends_on: []
created: 2026-04-16
assigned_to: pirate
---

# Teach Pirate to Use wiki-compiler

Teach the pirate coding agent (running gemma 4b) to use wiki-compiler as its primary knowledge retrieval mechanism.

## Context

Pirate is a small model with fast but limited context. wiki-compiler's topology-based querying is ideal for this — it retrieves precise answers without flooding context.

## Tasks

- [ ] Task 1: Index Navigation — Query Index.md via CLI
- [ ] Task 2: Finding a Concept — Search and query energy concept
- [ ] Task 3: Reading Efficiently — Query before read
- [ ] Task 4: Context Extraction — Use context command
- [ ] Task 5: Self-Assessment — Use status/energy commands
- [ ] Task 6: Iterative Query Practice — Multi-step narrowing
- [ ] Task 7: Synthesize — Answer question using wiki-compiler
- [ ] Task 8: Diagnose a Failure — Use wiki-compiler to debug

## Curriculum

See `wiki/concepts/pirate_curriculum.md` for detailed task descriptions.

## Approach

1. Start interactive session: `pirate --provider google --model gemma-3-4b`
2. Assign tasks one at a time
3. Observe output, debug failures
4. Iterate on Pirate's understanding
5. Document issues in desk/issues/ if systemic failures found

## Notes

- Must use `--provider google --model gemma-3-4b` (or appropriate gemma variant)
- Keep context small — small model can't handle large dumps
- Use desk to track issues discovered during training
