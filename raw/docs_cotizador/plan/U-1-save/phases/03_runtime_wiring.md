# Phase 03 - Runtime/UI Wiring Through PersistencePort

## Context

Phase 02 provides the storage boundary.
This phase wires save/load actions to runtime and UI without leaking storage details.

## Objectives

- [ ] Add `confirmSave()` and `loadQuotation(id)` to quotation runtime using `PersistencePort` only.
- [ ] Enable `Confirm & Save` action in validation UI.
- [ ] Show quotation ID after successful save.
- [ ] Keep error handling visible and non-blocking.

## Integration Rules

- No direct model/store calls in UI or runtime.
- Storage choice (local/GAS) is injected at runtime factory boundary.
- Flow semantics remain aligned with legacy save/confirm behavior.

## Outputs

- `apps/quotation/state/createPersistedQuotationRuntime.js`
- `apps/quotation/state/createQuotationInternalRuntime.js`
- `apps/quotation/playground/QuotationFlowInternal.html`
- `bundling/createQuotationFlowComponent.js`

## Implementation Notes

- The quotation flow owner is the persisted quotation runtime state machine.
- `serializeQuotation(...)` is executed inside runtime save orchestration, never from Alpine/UI.
- Save/load are modeled as real runtime stages (`saving`, `loadingQuotation`) before returning to `completed` or the editable flow.
- Storage remains injected through `PersistencePort`, so local and GAS adapters stay behind the same boundary.

## Acceptance

- Save works in sandbox and GAS preview.
- Quotation ID is propagated to completed state.
- Validation transitions through `saving` and returns to `validation` on save failure.
- Load transitions through `loadingQuotation` and rehydrates the editable basket flow.
- Tests remain green.

## Commit

`feat: wire save/load flow through PersistencePort`
