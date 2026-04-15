---
id: 14
domain: perception
status: open
priority: p1
depends_on: []
created: 2026-04-15
---

## Explanation

The current `build_status_report` in `perception.py` hardcodes zone scanning (raw/, wiki/src nodes, desk/Gates.md). Adding new zones requires code changes.

Similarly, `energy.py` calculates energy from specific metrics without a pluggable intermediate measure system.

## Reference

- `src/wiki_compiler/perception.py` — `build_status_report()`
- `src/wiki_compiler/energy.py` — `calculate_systemic_energy()`
- `wiki/standards/contracts.md` — existing contract patterns
- `wiki/WhereAmI.md` — six zones definition

## What to Fix

1. Add `ZoneContract` Pydantic model to `contracts.py`
2. Create declarative zone config in wiki topology (e.g., `wiki/standards/zones.md`)
3. Refactor `build_status_report` to read zone contracts and apply them generically
4. Add intermediate energy measures system to `energy.py`
5. Update status report to track desk/ and drawers/ for modified/untracked files

## How to Do It

1. Add to `contracts.py`:
   ```python
   class ZoneContract(BaseModel):
       zone: str
       path: str
       track_modified: bool
       track_untracked: bool
       energy_weight: float
       response_action: str
   ```

2. Create `wiki/standards/zones.md` defining all six zones with contracts

3. Refactor perception to load zone contracts and iterate generically

4. Add `EnergyMeasure` base class with registry pattern

5. Run tests and update changelog

## Validation

- `wiki-compiler status` reports desk/drawers perturbations
- `wiki-compiler energy` includes new zone-based measures
- New zones can be added by editing wiki topology only
