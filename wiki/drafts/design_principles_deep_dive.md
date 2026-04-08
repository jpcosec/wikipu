---
identity:
  node_id: "doc:wiki/drafts/design_principles_deep_dive.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/ARCHITECTURE/legacy-ui-recovery.md", relation_type: "documents"}
---

### 1. Behavior parity over markup parity

## Details

### 1. Behavior parity over markup parity

We preserve what the app does, not legacy HTML structure or CSS exactness.

### 2. Single mutation boundary

State changes must go through runtime/component methods and machine events, not ad-hoc template mutation.

### 3. Pure domain core

Pricing, quantity resolution, and rules evaluation stay in pure functions. UI and machine layers do not duplicate this logic.

### 4. Adapter-first integrations

Persistence and service I/O go through explicit ports/adapters (`PersistencePort`, GAS/local adapters). UI remains transport-agnostic.

### 5. Component contracts first

Catalog, basket, validation, and completion interactions must compose from component contracts, not page-specific patches.

### 6. Screen-state-event discipline

Every flow interaction should map cleanly to:

- screen (what user sees),
- state (business stage),
- event/action (transition trigger/effect).

### 7. No backend knowledge in templates

Alpine views should not encode persistence routes, sheet names, or GAS method decisions.

### 8. Parity through architecture, not exceptions

If legacy behavior is missing, extend runtime/adapters/contracts. Do not bypass architecture to get quick parity.

Generated from `raw/docs_cotizador/docs/ARCHITECTURE/legacy-ui-recovery.md`.