# TestSprite Product Description

## Product Name
PhD 2.0 Deterministic Rebuild

## Product Goal
Rebuild the application pipeline on a clean LangGraph-first architecture, preserving only:
- pydantic contracts,
- graph topology reference,
- deterministic tools.

## Core User Value
- Predictable execution behavior.
- Transparent and inspectable artifacts.
- Step-by-step modular delivery with deterministic test gates.

## Functional Scope
- Deterministic scraping and translation path.
- Contract-driven extraction, matching, review, document generation, render, and package stages (to be rebuilt incrementally).
- HITL redesigned with modern LangGraph/LangChain patterns.

## Non-Goals
- Preserve old runtime implementations.
- Keep legacy prompt execution stack.

## Quality Expectations
- Deterministic tests only at each delivery step.
- Archived successful artifacts under `data/Archived/` as reference benchmarks.

## Delivery Strategy
- One node family at a time.
- Green deterministic tests before moving to the next family.
