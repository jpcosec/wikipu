---
identity:
  node_id: "doc:wiki/drafts/component_api_public_surface.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/ARCHITECTURE/component-architecture.md", relation_type: "documents"}
---

Every component exposes this interface:

## Details

Every component exposes this interface:

```typescript
interface ComponentAPI {
  // State access
  getState(): Object                    // Current display state
  setState(seed: Object): void          // Load persisted state
  
  // Mode & overrides
  setMode(mode: string): void
  setOverride(field: string, value: any): void
  clearOverride(field: string): void
  clearAllOverrides(): void
  
  // Events
  on(event: string, handler: Function): void
  off(event: string, handler: Function): void
  
  // Introspection
  isUserSet(field: string): boolean
  getErrors(): Array<{message: string}>
  getWarnings(): Array<{message: string}>
}
```

---

Generated from `raw/docs_cotizador/docs/ARCHITECTURE/component-architecture.md`.