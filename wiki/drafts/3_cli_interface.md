---
identity:
  node_id: "doc:wiki/drafts/3_cli_interface.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/doc-router-design.md", relation_type: "documents"}
---

```

## Details

```
doc-router init                              # Create doc-router.yml + templates/
doc-router scan [--force]                    # Build graph, report stats
doc-router lint                              # Validate tags, check vocabulary
doc-router drift                             # Run drift detection
doc-router verify [--domain X] [--stage Y]   # Mark doc-code links as verified (updates hashes)
doc-router graph [--domain X] [--stage Y]    # Print graph (text) or export JSON
doc-router check                             # Combined lint + drift (single health check)
doc-router new doc|code [--domain] [--stage] # Scaffold from template
doc-router runbook --domain X --stage Y      # Generate runbook
doc-router packet --task "..." --type T      # Compile task packet
  [--domain X] [--stage Y]                   # Optional explicit routing
doc-router serve                             # Start UI server (+ MCP after Phase 6)
```

All commands support `--json` for programmatic use.

---

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/doc-router-design.md`.