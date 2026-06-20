# QUALITY CONTROL SYSTEM
**How we catch our own mistakes.** Every significant output must survive this before it's called finished. This is the immune system of the project.

`Part of: PROJECT ASI — Living Instruction System`
`System Version: 1.0 · Status: Living document · Last updated: 2026-06-20`

---

## 1. The mandatory pipeline

No important output skips this:

```
GENERATE → SELF-REVIEW → CRITIQUE → GAP ANALYSIS → MISSING-DOMAIN CHECK
         → CONTRADICTION CHECK → IMPROVE → FINALIZE
```

A first draft is never the final draft. The draft is raw ore; this pipeline is the smelting.

---

## 2. The checklist (run on any significant output)

**Substance**
- [ ] Is every important claim tagged with a confidence level (Established → Unknown)?
- [ ] Does each claim show its **evidence** and what **rung** of the evidence ladder it sits on?
- [ ] Is the **strongest opposing view** present and fairly stated (steel-manned)?
- [ ] Are **fact / interpretation / projection** kept separate?

**Gaps**
- [ ] What is **missing**? What did we conveniently skip?
- [ ] What **assumptions** are hiding here unexamined?
- [ ] Which **domain** would an expert say we ignored? (cross-check [`DOMAIN_DISCOVERY_SYSTEM.md`](DOMAIN_DISCOVERY_SYSTEM.md))
- [ ] What **open questions** does this raise? (send to [`OPEN_QUESTIONS_SYSTEM.md`](OPEN_QUESTIONS_SYSTEM.md))

**Consistency**
- [ ] Does this **contradict** anything elsewhere in the system? If so, resolve it (one must change).
- [ ] Do the cross-links actually point to the right places?

**Clarity (the language rule)**
- [ ] Could a smart 12-year-old follow the *language* (while the *idea* stays deep)?
- [ ] Is every hard word defined on first use? Should any go in [`GLOSSARY.md`](GLOSSARY.md)?

**Honesty**
- [ ] Are we pretending to be more certain than we are?
- [ ] Would this claim survive if it were false? (If yes, it's probably empty — see [`PRINCIPLES.md`](PRINCIPLES.md).)

---

## 3. The special danger: reviewing our own work with the same blind spots

The hardest problem: **the same mind that writes the draft also reviews it** — so it can rubber-stamp its own mistakes. This is a real and serious weakness (especially when an AI assistant both generates *and* checks content).

Defenses:
1. **Switch hats deliberately.** Review in a different *mode* than you wrote: become the harsh critic, the rival expert, the confused beginner — explicitly, one at a time.
2. **Red-team prompt:** "Assume this output is wrong. What's the most likely reason?"
3. **Seek outside contact.** Where stakes are high, check claims against *external* sources and current information rather than trusting internal memory — which can be confidently wrong or out of date.
4. **Make falsifiable predictions.** A prediction that can fail is the one check the author can't fake. Reality is the only reviewer with no blind spots.

---

## 4. Special checks for an AI-assisted project

Because much of this project runs through an AI assistant, add:
- **Hallucination check** — are cited facts, names, numbers, or papers *real*? Verify the load-bearing ones.
- **Staleness check** — is this fast-aging knowledge that may be past the assistant's cutoff? Flag and verify.
- **Sycophancy check** — is the assistant agreeing with the user because it's *true*, or to be agreeable? The house rule is truth over comfort.

---

## 5. Tiers of review (match effort to stakes)

- **Light** (routine notes): run the Clarity + Honesty checks.
- **Standard** (most outputs): run the full checklist once.
- **Deep** (anything load-bearing — a path estimate, a major claim, a roadmap): full checklist + red-team + external verification + a logged prediction.

---

## 6. The audit

Beyond per-output review, the whole system gets a periodic **audit**: a deliberate hunt for blind spots, hidden assumptions, missing domains, and failure modes across *all* documents at once. Audits drive version upgrades (see [`SELF_IMPROVEMENT_SYSTEM.md`](SELF_IMPROVEMENT_SYSTEM.md) and [`VERSION_HISTORY.md`](VERSION_HISTORY.md)). The first audit was run at v1.0 → produced v1.1.
