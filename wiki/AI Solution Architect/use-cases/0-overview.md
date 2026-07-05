# AI Use Case Lifecycle — Overview

**Summary**: Navigation page for the full AI use case process — from ideation through feasibility to scoping and build.

**Last updated**: 2026-06-25

---

## The lifecycle

Five sequential phases and one reference tool.

```
IDEATION → FEASIBILITY → SCOPING → REQUIREMENTS → PoC/PILOT → PRODUCTION ROLLOUT
    ↑              ↑          ↑            ↑                          ↑
[catalog      [technical  [technical  [technical               [governance,
 pages]        framework]  framework]  framework]               monitoring,
                                                                 change mgmt]
```

| Step | Page | Question answered | Who |
|---|---|---|---|
| **1. Ideation** | [[1-ideation]] | Which business problems could AI solve? | Business leads, process owners |
| **2. Feasibility** | [[2-feasibility]] · [[2b-data-readiness]] | Which of those are worth building? | Business + data owners + IT |
| **3. Scoping** | [[3-scoping]] | How will we build it, and how long will it take? | SA + data team + IT |
| **4. Requirements** | [[4-requirements]] | Exactly what must the system do, measurably? | SA + engineers + data scientists |
| **5. Production Rollout** | [[5-production-rollout]] | How do we move from pilot to a system actually used in the company? | SA + product owner + change manager |
| **Ref** | [[technical-framework]] | What type of AI problem is this? How do we design it? | SA |
| **Ref** | [[build-vs-buy]] | Use API as-is, RAG, fine-tune, or train from scratch? | SA |
| **Ref** | [[business-case-roi]] | How do we quantify value and build an executive business case? | SA + business owner |

The **reference tools** are not sequential phases — they are used across multiple phases wherever they are relevant.

**PoC vs. production**: Steps 1–4 lead to a time-boxed PoC or pilot that validates the approach. Step 5 is a separate discipline: moving from a working prototype to a system with governance, monitoring, change management, and real users. Most AI projects succeed as PoCs and fail at Step 5.

---

## Key distinctions

**Feasibility vs. scoping**: Feasibility asks *should we build this?* — scored on business value, data availability, technical complexity, and org readiness. Scoping asks *how will we build it?* — phase plan, effort estimate, success metric. Feasibility selects the winner. Scoping defines the project.

**Scoping vs. requirements**: Scoping is executive-level — what, why, how long, how much. Requirements engineering is engineering-level — the detailed specification of functional behavior, model performance thresholds, data contracts, and integration APIs that the team builds and tests against. For small projects these can be combined; for larger or regulated projects they warrant separate phases.

---

## Industry reference catalogs

Used during ideation as concrete examples to show clients what AI looks like in their industry:

- [[catalog-manufacturing]] — Computer vision, time series, and NLP use cases in manufacturing (with deep dives and AI dimensions)
- [[catalog-healthcare]] — Healthcare AI use cases
- [[catalog-merantix]] — Merantix-specific use case examples

---

## Related pages

- [[Overview]] — The 4 AI dimensions (capability, domain, paradigm, architecture)
- [[2.1 - Regulated industries]]
- [[2.2 - EU_AI_Act]]
