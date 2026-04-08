---
identity:
  node_id: "doc:wiki/drafts/condition_examples.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/GUIDES/writing-rules.md", relation_type: "documents"}
---

### Quantity comparisons

## Details

### Quantity comparisons

```json
{ ">": [{ "var": "pax" }, 320] }
```
*Triggers when pax exceeds 320.*

```json
{ "<": [{ "var": "pax" }, 10] }
```
*Triggers when fewer than 10 pax.*

```json
{ "and": [
  { ">=": [{ "var": "pax" }, 50] },
  { "<=": [{ "var": "pax" }, 150] }
] }
```
*Triggers when pax is between 50 and 150 (inclusive).*

---

### Time comparisons

```json
{ ">": [{ "var": "horaMin" }, 1260] }
```
*Triggers when item starts after 21:00 (overtime).*

```json
{ ">": [{ "var": "horaFinMin" }, 1440] }
```
*Triggers when item ends past midnight.*

```json
{ "and": [
  { ">": [{ "var": "horaMin" }, 1260] },
  { "<=": [{ "var": "horaFinMin" }, 1500] }
] }
```
*Triggers when item starts after 21:00 but ends before 01:00.*

> **Why not compare `hora` strings?**
> `'01:00' < '21:00'` is true as a string — wrong for next-day events.
> `horaMin` for 01:00 is 1500, correctly greater than 1260 (21:00).

---

### Duration comparisons

```json
{ ">": [{ "var": "duracionMin" }, 240] }
```
*Triggers when item runs longer than 4 hours.*

---

### Logical operators

```json
{ "or": [
  { "<": [{ "var": "pax" }, 10] },
  { ">": [{ "var": "pax" }, 320] }
] }
```
*Triggers when pax is outside the valid range (10–320).*

```json
{ "!": [{ ">": [{ "var": "pax" }, 0] }] }
```
*Triggers when pax is zero.*

---

### Always / Never

```json
true
```
*Rule always triggers (use for unconditional messages or surcharges).*

```json
false
```
*Rule never triggers (useful for temporarily disabling without deleting).*

---

Generated from `raw/docs_cotizador/docs/GUIDES/writing-rules.md`.