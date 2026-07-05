# Business Case & ROI for AI Projects

**Summary**: How to quantify the value of an AI use case, structure an executive-ready business case, and avoid the common pitfalls that make AI investments hard to approve or hard to sustain.

**Last updated**: 2026-06-29

---

## Why the Business Case Comes Before the Architecture

The [[technical-framework]] tells you what to build. The business case tells you whether it is worth building. In consulting, the business case must be resolved during [[2-feasibility|feasibility]] — not as an afterthought after scoping has begun.

As an SA rule of thumb: **if you cannot articulate the value in the client's own terms (€, hours, %, risk events), the project will not survive its first executive review**.

---

## The Four Value Levers

Almost every AI business case maps to one or more of these:

### 1. Cost Reduction
Automating or accelerating work that currently consumes human time or generates operational cost.

| Value driver | How to quantify |
|---|---|
| Manual work automated | FTE hours saved per period × fully-loaded hourly rate |
| Error rate reduction | Error cost (rework, penalty, waste) × current error rate × reduction % |
| Process speed-up | Throughput increase → revenue or capacity freed |
| Resource optimisation | Material, energy, or asset cost × waste reduction % |

**Example**: Quality inspection takes 2 inspectors × 8h/day × €50/h = €2,900/week. A CV model reduces inspectors needed to 0.5 FTE. Savings: ~€2,500/week = €130k/year.

### 2. Revenue Uplift
AI increases revenue through better conversion, personalisation, or new service capabilities.

| Value driver | How to quantify |
|---|---|
| Conversion rate improvement | Uplift % × transaction volume × average revenue per conversion |
| Upsell / cross-sell | Recommendation click-through uplift × margin per upsell |
| Faster time-to-market | Days saved in a product cycle × revenue per day of earlier launch |
| New AI-enabled service | Addressable market × expected market share × margin |

**Example**: Recommendation engine improves conversion by 1.5% on 100k monthly visitors with €80 average order value. Revenue uplift: 1,500 × €80 = €120k/month.

### 3. Risk Reduction
AI reduces the probability or cost of negative events — defects, fraud, compliance violations, safety incidents.

| Value driver | How to quantify |
|---|---|
| Fraud / defect prevention | Cost per incident × incident frequency × detection rate improvement |
| Regulatory compliance | Cost of non-compliance (fines, remediation) × probability reduction |
| Safety incidents | Incident cost × frequency × reduction % |
| Unplanned downtime | Cost per hour of downtime × hours avoided per year |

**Example**: Predictive maintenance reduces unplanned downtime from 40h to 10h/year on a line that costs €5,000/h to be down. Value: 30h × €5,000 = €150k/year.

### 4. Productivity Gains
Same team produces more output with AI assistance — not headcount reduction but capacity expansion.

| Value driver | How to quantify |
|---|---|
| Knowledge worker efficiency | Hours per task reduced × FTE count × hourly rate × tasks per year |
| Decision quality | Faster and better decisions → revenue impact or reduced downstream cost |
| Analyst / SA leverage | Senior person handles more engagements per year with AI tooling |

---

## ROI Framework

### Total Investment (one-time + ongoing)

| Cost category | Typical range |
|---|---|
| Data preparation | 30–50% of project build cost |
| Model development | 20–40% of project build cost |
| Integration & deployment | 20–40% of project build cost |
| Infrastructure (cloud/on-prem) | €10k–€200k/year depending on scale |
| Ongoing maintenance & retraining | 20–30% of build cost per year |
| Change management & training | Often underestimated — budget 10–20% of build cost |

### Time to Value

| Phase | Typical duration |
|---|---|
| PoC / pilot (prove it works) | 6–12 weeks |
| Production build | 3–6 months |
| Adoption ramp-up | 3–6 months post-launch |
| **Total: first value realised** | **6–18 months** |

### ROI Calculation

```
Annual value  =  (cost savings + revenue uplift + risk reduction) per year
Annual cost   =  infrastructure + maintenance + licensing
One-time cost =  build cost (data prep + model dev + integration)

ROI (year 1)  =  (Annual value − Annual cost − One-time cost) / One-time cost
ROI (year 3)  =  (3 × Annual value − 3 × Annual cost − One-time cost) / One-time cost
```

Always present three scenarios: **conservative** (only the most certain value levers, lower estimates), **expected** (base case), **optimistic** (full adoption, all value levers materialise). Clients trust a range more than a point estimate.

---

## Structuring an Executive Business Case

### The one-page structure

1. **Problem** — what is the business problem being solved? (one sentence)
2. **Current state cost** — what does the problem cost today? (in €, hours, or risk events)
3. **Proposed solution** — what will be built and how does it solve the problem?
4. **Value** — quantified benefit, broken down by lever (cost, revenue, risk)
5. **Investment** — total cost to build and run (year 1, year 3)
6. **ROI** — payback period and 3-year return
7. **Risks** — top 3 risks and mitigations
8. **Recommendation** — proceed, pilot first, or stop — and why

### Presentation principles

- **Use the client's own numbers**: if the client says downtime costs €8,000/hour, use that number — not an industry benchmark. It becomes their calculation, not yours.
- **Lead with the cost of doing nothing**: "if we don't act, this problem will cost X over 3 years" is often more persuasive than "we can save X."
- **Separate the PoC from the full build**: recommend a time-boxed pilot with a defined go/no-go decision. Executives approve small bets more easily than large commitments.
- **Accuracy ≠ business value**: a model that improves accuracy by 5% is meaningless without translating that into €. Always close the loop from model metric to business metric.

---

## Common Pitfalls

| Pitfall | What goes wrong | Fix |
|---|---|---|
| Overstating the value | Includes every conceivable benefit at optimistic rates | Present conservative / expected / optimistic scenarios |
| Ignoring ongoing cost | Build cost approved but no budget for maintenance | Show 3-year total cost of ownership, not just build |
| Using model metrics as value | "95% accuracy" means nothing to a CFO | Always translate: 95% accuracy = X fewer defects = €Y saved |
| Assuming full adoption | ROI assumes 100% of employees use the tool | Model adoption at 50% and 80% separately |
| No baseline | Cannot show improvement without measuring where you start | Establish the current-state baseline before the project begins |

---

## Related Pages

- [[2-feasibility]] — Business value is the first scoring dimension in the feasibility scorecard
- [[3-scoping]] — ROI inputs inform the go/no-go decision and executive sponsorship
- [[5-production-rollout]] — Ongoing cost and adoption are the production-phase variables that determine whether the ROI is realised
- [[technical-framework]] — Technical feasibility must be established before the ROI calculation is credible
- [[2b-data-readiness]] — Data preparation cost is typically the largest underestimated line item
