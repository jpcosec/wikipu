---
identity:
  node_id: "doc:drawers/OP-RULE-Query-Before-Read.md"
  node_type: "task"
edges:
  - {target_id: "doc:wiki/selfDocs/WhoAmI.md", relation_type: "documents"}
compliance:
  status: "exempt"
---

# Re-evaluate Operational Rule: Query Before Read

> **Status: DEACTIVATED**
> The enforcement of this rule via `.pi/extensions/rule_enforcer.ts` has been manually commented out. It is currently in a state of suspended animation while we re-evaluate its activation and implementation.

**Explanation:** This is a meta-task to re-evaluate the core operational rule, "Query Before Read." While the spirit of the rule is understood and essential for autopoiesis, its rigid application is causing significant friction and high energy penalties. The user has described it as a "pain in the ass."

**Reference:**
- `[[wiki/selfDocs/WhoAmI]]`
- `[[wiki/selfDocs/HowAmI]]`
- `exclusion/agent_violations.log`

**What to fix:** The goal is to find a new equilibrium that preserves the *spirit* of the rule while reducing its operational friction. This involves a formal re-evaluation of its implementation.

**How to do it (suggestions for re-evaluation):**
1.  **Analyze Violation Patterns:** Review the `agent_violations.log`. Are the violations happening in specific contexts? Is there a pattern that suggests a blind spot in the `wiki-compiler`'s capabilities?
2.  **Consider Rule Refinements:** Should there be exceptions? For instance, when initially exploring an unknown file structure or when debugging the compiler itself.
3.  **Evaluate Penalty System:** Is the high energy penalty for this specific violation appropriate? Should it be tiered? A first-time "exploration" read could have a lower penalty than a repeated bypass of a known query path.
4.  **Propose Alternative Mechanisms:** Could an extension or a different workflow guard achieve the same goal with a smarter, more context-aware check?

**Depends on:** none
