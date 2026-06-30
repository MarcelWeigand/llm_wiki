# AI Project Scoping & Effort Estimation

**Summary**: A structured framework for scoping an AI use case once it has been selected — covering phase-based work breakdown, effort multipliers, and what a scoping document must contain.

**Last updated**: 2026-06-25

---

## What is scoping?

Scoping is the step between *deciding to build* and *starting to build*. Its goal is to turn a use case idea into a defined, estimable project — one where everyone agrees on what success looks like, what is and isn't included, and roughly how much effort it will take.

Good scoping prevents the three most common AI project failures:
- **Undefined success** — the model gets built but nobody agrees whether it's good enough
- **Scope creep** — stakeholders add requirements mid-project because nothing was written down as out-of-scope
- **Effort surprise** — the team underestimates data work and integration, then misses deadlines

Scoping is not the same as [[2-feasibility|feasibility assessment]]. Feasibility asks *should we build this?*. Scoping asks *how exactly will we build it, and how long will it take?*

---

## Best practices

**1. Define success before you define the solution**
Agree on a concrete, measurable success metric before any technical discussion. "Improve quality control" is not a success metric. "Reduce false rejection rate from 8% to under 3% on line 4 within 6 months" is. Without this, every stakeholder will evaluate the project against a different mental model.

**2. Scope the data, not just the problem**
Name specific data sources, systems, and owners in the scoping document. "We'll use production data" is not a data scope. Confirm access rights, data volume, update frequency, and who is responsible for data quality issues before the project starts.

**3. Write the out-of-scope list explicitly**
Every scoping document needs a section that says *"this project will not…"*. This is where scope creep originates — not from bad intentions, but from things nobody thought to exclude. Make it a standing agenda item in the scoping conversation.

**4. Separate the PoC from the production commitment**
Scope Phase 1–2 (discovery + PoC) in detail and Phase 3–5 as a range. Don't let stakeholders lock in a production timeline before the PoC has confirmed the model works. Frame it as: "We will know our production timeline after the PoC at week 8."

**5. Put the integration design in the scope**
How the model output reaches the end user is as important as the model itself. Define the integration contract (API, dashboard, alert, file export) in the scope document — it determines which teams need to be involved and often doubles the estimate if forgotten.

**6. Estimate ranges, not point estimates**
For AI projects, single-point estimates create false precision. Always present a range (e.g., "10–16 weeks for production build") and explain what drives the uncertainty. Stakeholders trust ranges more than false precision — and they're more likely to hold you accountable to a range you named than to a number they half-remember.

**7. Name the owner before the project starts**
Every use case needs a named business owner — a person who will act on the model's output and who is accountable for adoption. If nobody can name this person during scoping, the project will stall after deployment. This is a go/no-go signal.

**8. Budget for the annotation project separately**
If labels don't exist, data annotation is its own project with its own timeline, cost, and quality process. It should appear as a distinct workstream in the scope — not as a footnote to Phase 1.

---

## The core challenge: AI ≠ traditional software

Traditional software projects have deterministic outcomes — you specify the feature, you build it, done. AI projects have three additional uncertainty layers:

1. **Model performance is unknown until you try** — you don't know if 90% accuracy is achievable until you've trained on real data
2. **Data quality only becomes clear during development** — the data that "exists" often needs months of cleaning or labeling
3. **"Done" is harder to define** — a model is never perfect; you need to agree upfront on a measurable success threshold

This means AI effort estimates carry higher variance, and the scoping needs to explicitly call that out.

---

## Phase-based work breakdown (WBS for AI)

Break the project into 5 phases, each with distinct deliverables and skill requirements:

| Phase | Duration (typical) | Key activities | Risk of underestimation |
|---|---|---|---|
| **1. Discovery & data assessment** | 2–4 weeks | Confirm problem definition, audit data sources, assess label availability, define success metric | Medium — depends on data access speed |
| **2. Proof of concept (PoC)** | 4–8 weeks | Build baseline model on clean subset, establish feasibility, identify data gaps | High — model may not work; scope creep from stakeholders |
| **3. Production build** | 8–16 weeks | Full data pipeline, model training loop, API/service, retraining infrastructure | High — integration complexity often 2× the model work |
| **4. Deployment & validation** | 4–8 weeks | Shadow mode / A/B test, acceptance testing, performance monitoring setup | Medium |
| **5. Monitoring & maintenance** | Ongoing | Drift detection, retraining cadence, data pipeline maintenance | Often missed entirely in initial scope |

For a typical first AI project at a mid-size enterprise, **total time from kickoff to production: 6–12 months** with a team of 3–5 people.

---

## Effort multipliers (complexity scoring)

Start with a base estimate per phase, then apply multipliers for each risk factor. Multiply only the *affected phases*, not the whole project.

| Factor | Multiplier | When to apply |
|---|---|---|
| Novel problem (no precedent) | ×1.5 | No published benchmark, no existing solution in industry |
| Poor data quality | ×1.5 | Data exists but fragmented, inconsistent, missing values |
| No labels / ground truth | ×2.0 | Requires annotation project before modeling can start |
| Complex system integration | ×1.5 | Output must be embedded in ERP, MES, or core operational system |
| Regulated industry | ×1.5 | GDPR, MDR, FDA — adds validation, documentation, audit trail |
| Low organizational readiness | ×1.3 | No clear process owner, requires significant change management |

---

## The scoping document: what it must contain

A scope document for an AI project should answer these questions explicitly:

1. **Problem definition**: what decision or action does the model enable? (not "predict churn" but "flag customers for retention team 30 days before contract end")
2. **Success metric**: what threshold makes this a success? (e.g., "recall ≥ 85% at ≤ 10% false positive rate")
3. **Data scope**: exactly which data sources are in scope, who owns access, and what preprocessing is assumed
4. **Out of scope**: what the model will *not* do — this is where stakeholders quietly expand scope post-kickoff
5. **Integration contract**: what does the consuming system/user receive? (API response, dashboard, alert, batch file)
6. **Retraining policy**: how often, triggered by what, owned by whom
7. **Exclusions / assumptions**: what data quality or infrastructure is assumed but not guaranteed

---

## Frameworks that exist (and their limits)

- **CRISP-DM** — classic data science process (Business Understanding → Data Understanding → Preparation → Modeling → Evaluation → Deployment). Good for thinking through phases, but too academic for client-facing estimation.
- **ML Canvas** (adapted from Lean Canvas) — good for defining the problem, data, prediction target, and value proposition on one page. Useful early in scoping conversations.
- **TDSP** (Microsoft's Team Data Science Process) — more complete, includes roles and lifecycle, but heavyweight for small projects.
- **MLOps maturity model** — useful for assessing what the client's infrastructure can support; a Level 0 org (manual everything) needs 3× the ops effort of a Level 2 org.

In practice: none of these give you effort numbers. They give you structure. The actual estimate comes from combining the WBS above with the multipliers and anchoring against comparable past projects.

---

## SA rule of thumb

> **The data pipeline and integration almost always take longer than the model.** A rough split for a mature team: 20% modeling, 40% data/feature engineering, 40% integration and deployment. Stakeholders almost always expect 60–80% modeling. Correcting this expectation early is one of the most valuable things an SA can do.

---

## Related pages

- [[0-overview]] — Full lifecycle map
- [[2-feasibility]] — Previous step: selecting the use case
- [[technical-framework]] — Reference for architecture and integration design decisions
- [[Metrics]] — Choosing the right success metric by capability type
- [[2.1 - Regulated industries]]
