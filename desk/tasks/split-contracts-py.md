# Reduce file complexity in contracts.py

**Explanation:** contracts.py has 628 lines. While it contains many model definitions, it could be organized better.

**Reference:** `src/wiki_compiler/contracts.py`

**What to fix:** Extract related model groups into separate module files (e.g., facets.py, energy_models.py).

**How to do it:**
1. Move facet-related models to facets.py
2. Move energy models to energy_models.py  
3. Import from both in contracts.py

**Depends on:** none
