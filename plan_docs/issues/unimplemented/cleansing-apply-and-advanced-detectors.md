# Cleansing Apply and Advanced Detectors

**Explanation:** The cleansing foundation now detects a first wave of structural anomalies and emits `CleansingProposal` objects, but it does not yet apply approved proposals or cover the broader anomaly families from the cleansing protocol.

**Reference:** `src/wiki_compiler/cleanser.py`, `raw/cleansing_protocol.md`, `wiki/reference/cli/cleanse.md`

**What to fix:** Implement proposal application and add the remaining anomaly detectors for code, tests, config, and richer plan/doc heuristics.

**How to do it:**
1. Add `cleanse --apply` with explicit approval handling.
2. Add the remaining detector families from the cleansing protocol.
3. Expand tests to cover each new anomaly class.

**Depends on:** `none`
