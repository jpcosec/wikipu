---
status: open
priority: p2
depends_on: []
created: 2026-04-22
assigned_to: self
---

# Finish SLDB Models for All Node Types

Complete `__template__` for all wiki node types in `wiki_nodes.py`.

## Why

All 7 node types need a StructuredNLDoc model to enforce structure at creation time.

## Node Types Missing Templates

- [ ] HowToDoc — how-to node type
- [ ] DocStandardDoc — rule/schema documents
- [ ] ReferenceDoc — technical reference
- [ ] IndexDoc — navigation index
- [ ] SelfDocDoc — self-documentation
- [ ] BoardDoc — operational board (desk/)
- [ ] GateDoc — gate tracker (desk/)

## Verification

```bash
for model in HowToDoc DocStandardDoc ReferenceDoc IndexDoc SelfDocDoc BoardDoc GateDoc; do
  sldb validate wiki_compiler.contracts.wiki_nodes:$model --pythonpath src
done
```