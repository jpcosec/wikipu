---
identity:
  node_id: "doc:wiki/drafts/recovery_graph.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/plans/2026-03-04-legacy-functionality-recovery-mapping.md", relation_type: "documents"}
---

```mermaid

## Details

```mermaid
flowchart LR
  subgraph L["Legacy UI Functionalities (claps_codelab)"]
    L1["Catalog: search + categories + add item"]
    L2["Timeline: day tabs + line overrides + remove"]
    L3["Line copy/duplicate + copy full day"]
    L4["Validation + completion flow"]
    L5["Previous quotations modal + DB viewer"]
    L6["Save quotation + Generate PDF"]
  end

  subgraph R["Rebuild Runtime Contracts (already available)"]
    R1["createCatalogActor\n(catalog/category composition)"]
    R2["createBasketDayActor\n(entry-level runtime)"]
    R3["createBasketActor\n(day-wide quotation composition)"]
    R4["Item runtime + shared rule UI sections"]
    R5["Quotation app shells/modals in apps/quotation"]
  end

  subgraph G["Recovery Gaps (Step 05+)"]
    G1["Unify final quotation route shell"]
    G2["Wire catalog click -> basket ship events"]
    G3["Complete duplicate/copy semantics\n(line copy + copy full day)"]
    G4["Bind validation/completion to real basket projections"]
    G5["Load previous quotations adapter"]
    G6["Persistence adapter (save/load)"]
    G7["PDF adapter after save"]
    G8["E2E parity suite vs legacy flows"]
  end

  L1 --> R1
  L1 --> R4
  L2 --> R2
  L2 --> R3
  L3 --> R3
  L4 --> R5
  L5 --> R5
  L6 --> R5

  R1 --> G1
  R3 --> G1
  R4 --> G1

  R1 --> G2
  R3 --> G2

  R3 --> G3

  R5 --> G4
  R3 --> G4

  R5 --> G5
  R5 --> G6
  G6 --> G7

  G2 --> G8
  G3 --> G8
  G4 --> G8
  G5 --> G8
  G6 --> G8
  G7 --> G8
```

Generated from `raw/docs_cotizador/docs/plans/2026-03-04-legacy-functionality-recovery-mapping.md`.