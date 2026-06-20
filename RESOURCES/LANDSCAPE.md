# AGI/ASI LANDSCAPE — who's pursuing it, and how
**A map of the real-world territory:** the labs, startups, and *research bets* currently aiming at AGI/ASI. This complements [`../INSTRUCTIONS/AGI_ASI_INVESTIGATION_SYSTEM.md`](../INSTRUCTIONS/AGI_ASI_INVESTIGATION_SYSTEM.md) (the *abstract* paths) by mapping the *actors* taking them.

`Status: Living map · System Version: 1.5 · Last updated: 2026-06-20`

> ⚠️ **Fast-aging snapshot (as-reported, June 2026).** This is the most perishable file in the project — players, valuations, and model versions change monthly. Figures below are **as reported by web sources and should be re-verified before relying on them**; treat specific numbers/benchmarks as **[Speculative→Likely]**, and the *strategic bets* as the durable, lower-volatility part. (Staleness rule: [`../INSTRUCTIONS/RESOURCE_COLLECTION_SYSTEM.md`](../INSTRUCTIONS/RESOURCE_COLLECTION_SYSTEM.md) §5.)

---

## 1. The main research bets (mapped to our path framework)

Each bet maps to a path in `AGI_ASI_INVESTIGATION_SYSTEM` §2 (P1–P7):

| Bet | Idea in one line | Who's pushing it | Our path |
|---|---|---|---|
| **Scale + reasoning (RL)** | Keep scaling, add RL-trained long "thinking" (reasoning models). | OpenAI, Anthropic, Google DeepMind, xAI, DeepSeek | P1+P2+P6 |
| **Agents / multi-agent** | Intelligence from many tool-using agents collaborating. | OpenAI, Anthropic, Moonshot (agent swarms), most labs | P2+P6 |
| **World models / JEPA** | Predict *abstract states of the world*, not next tokens — learn like an infant. | **Yann LeCun's AMI Labs**, Google (Genie-style), others | P3+P5 |
| **Neurosymbolic / hybrid** | Combine neural pattern-learning with symbolic reasoning. | Various academic + enterprise labs | P5 |
| **Brain-inspired** | Borrow deeper principles from neuroscience. | Academic labs, Numenta-style efforts | P3 |
| **Safety-first superintelligence** | Build ASI with safety as a coupled engineering goal from day one. | **SSI (Sutskever)** | cross-cutting (safety) |

> **The big live debate:** is AGI mostly an *engineering* problem (scale + refine what we have) or a *science* problem (we still lack key ideas)? The data-bottleneck worry (public text running low ~2026) is pushing serious money toward **world models, RL-reasoning, and synthetic data** as scaling's successors. **[Contested]**

---

## 2. The players (frontier labs & startups)

### US frontier labs
| Lab | Who / note | Bet |
|---|---|---|
| **OpenAI** | GPT-series; among highest-valued private AI cos (~$850B reported). | Scale + reasoning + agents |
| **Anthropic** | Claude; safety-focused; reported to top private-AI valuation in 2026. | Scale + reasoning + interpretability/safety |
| **Google DeepMind** | Gemini; deepest research bench (AlphaGo/AlphaFold heritage). | Scale + reasoning + world models + science |
| **xAI** | Grok; very well-capitalized (Nvidia-led rounds). | Scale + compute-heavy |
| **Meta AI (FAIR)** | Llama (open weights); research-heavy. | Open models; (post-LeCun) scaling |
| **Microsoft** | Compute + OpenAI partner; own models (Phi, MAI). | Infra + applied + models |

### New frontier startups (the 2024–26 wave)
| Startup | Founder | Bet |
|---|---|---|
| **SSI (Safe Superintelligence)** | Ilya Sutskever (ex-OpenAI) | "Straight-shot" safe superintelligence; stealth |
| **Thinking Machines Lab** | Mira Murati (ex-OpenAI) | Frontier models + tooling |
| **AMI Labs** (Advanced Machine Intelligence) | Yann LeCun (ex-Meta) | **World models / JEPA** — explicitly *anti-LLM-as-the-path* |
| **Mistral AI** | (France) | Leading European frontier + open models |

### Chinese labs (a major, fast-rising bloc)
**DeepSeek** (efficient frontier, RL-reasoning), **Alibaba (Qwen)** (open, agentic), **Moonshot (Kimi)** (agent swarms), **Zhipu (GLM)**, **MiniMax**, **StepFun**, **ByteDance**, **Baidu**, **Tencent**. Notable theme: strong results at **lower cost**, some training on **domestic (Huawei Ascend) chips** — a geopolitics/compute-governance story.

---

## 3. The enablers & chokepoints (who really controls the path)
AGI bets all run through a few physical bottlenecks (ties to `AGI_ASI_INVESTIGATION_SYSTEM` §4 and the `40-compute-and-physical/` + `50-world-and-society/` domains):
- **Chips:** Nvidia (GPUs) · **TSMC** (fabrication) · **ASML** (lithography) — a *very* thin supply chain.
- **Compute & capital:** the largest VC rounds in history are now AI labs; access to compute ≈ access to the frontier.
- **Energy:** data-center power is bumping into grid limits.
- **Data:** the looming shortage of high-quality public text (→ synthetic data, world models).
- **Geopolitics:** export controls, US–China competition, domestic-chip efforts.

---

## 4. How to keep this current (don't trust this file's specifics for long)
- Frontier-model trackers (e.g., LLM-Stats, cheatsheets), lab blogs (§B of [`PAPERS.md`](PAPERS.md)), and curated roundups (Raschka).
- Re-verify valuations/models before citing; this file is a *map of bets*, not a scoreboard of numbers.

---

## 5. Honest caveats
- **Hype is heavy here.** Valuations and benchmark claims are marketing-adjacent; apply the anti-hype "smell test" ([`../INSTRUCTIONS/PRINCIPLES.md`](../INSTRUCTIONS/PRINCIPLES.md) §2).
- **"Pursuing AGI" ≠ "will reach AGI."** Listing a bet here is *not* an endorsement that it works — that's what the scorecard in `AGI_ASI_INVESTIGATION_SYSTEM` is for.
- Some figures above may be **forward-looking or unverified**; flagged as-reported on purpose.
