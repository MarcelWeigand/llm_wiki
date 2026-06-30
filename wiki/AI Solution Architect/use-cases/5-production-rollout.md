# Step 5: PoC to Production Rollout

**Summary**: The transition from a successful AI pilot to a production-ready system used in the company — covering the business, management, and technical dimensions that determine whether an AI project actually delivers value.

**Last updated**: 2026-06-29

---

## Why This Phase Is Different

A PoC proves the idea works. Production requires the idea to work **reliably, at scale, with real users** — these are different bars. Most AI projects that fail technically succeed as PoCs: the model was accurate enough, the idea was sound. They fail at adoption, integration, governance, or maintenance.

The PoC-to-production transition is where AI projects are won or lost.

---

## Business Perspective

**Define exit criteria before the PoC starts, not after.** Agree upfront: "we proceed to production if X, we stop if Y." Post-hoc criteria get adjusted to fit results.

**Separate PoC success from production readiness.** A PoC proves feasibility; production requires reliability at scale with real users and real consequences.

**Quantify the full cost of production**, not just build cost. Ongoing monitoring, retraining, support, and change management are typically 40–60% of total cost over two years. Stakeholders who approved the PoC budget often underestimate this.

**Identify the internal champion** who will own adoption — someone with both the authority to enforce the change and the motivation to drive it. Without this person, AI systems get built and ignored.

**Plan the rollout scope explicitly**: full deployment vs. limited rollout vs. embedded in existing workflow. Each has a different change management cost and a different risk profile.

---

## Management Perspective

**Assign a product owner, not a project owner.** A project ends at launch; a product needs ongoing iteration. AI systems degrade — they need an owner who treats them as living software, not a delivered artefact.

**Build the cross-functional team early**: business owner, data scientist, ML engineer, IT/DevOps, and a change manager. Missing any of these creates a gap that surfaces at go-live.

**Establish a governance model before launch**: who approves model updates, who reviews performance regressions, who handles edge-case escalations, and who can pull the emergency brake. Undecided governance is a production incident waiting to happen.

**Get regulatory and compliance sign-off before production**, not in parallel with build. In regulated industries (healthcare, finance) this is a hard gate — see [[2.1 - Regulated industries]] and [[2.2 - EU_AI_Act]].

**Commit to a post-launch support period** (minimum 3–6 months). This is when real user behavior surfaces problems the PoC never caught. Plan for it in the budget and in the team's capacity.

**Communication plan**: every user of the AI system needs to know what it does, what it cannot do, and how to escalate problems. Unexplained AI behavior destroys trust quickly and is hard to rebuild.

---

## Technical Perspective

### Reproducibility
Can you reproduce the PoC result from scratch? Version-control data, code, and model weights before calling it a success. If the PoC cannot be reproduced, production will be built on an unknown foundation.

### Scalability
PoC data is always cleaner and smaller than production data. Load test against production volumes before committing to an architecture. Latency and throughput assumptions from the PoC are almost always wrong.

### Monitoring and Drift Detection
Set up monitoring **before launch, not after the first incident**. Define what "healthy" looks like before you can detect "unhealthy." The minimum required:
- Performance dashboards (model quality over time)
- Data drift alerts (input distribution shifting from training distribution)
- Latency and error rate monitoring
- Business metric tracking (not just model metrics)

See [[ML Ops]] for the full MLOps lifecycle including drift detection patterns.

### Retraining Pipeline
Model performance degrades as the world changes (data drift, concept drift). Plan when and how the model gets updated before launch — automated retraining pipelines are ideal; at minimum, the process must be documented and tested.

### Shadow Mode / Canary Deployment
Run the AI in parallel with the existing process before full cutover. Compare outputs, catch failures, and build user trust before flipping the switch. This is the lowest-risk path to production for most AI systems.

### Fallback Behavior
Define what the system does when the model fails, is unavailable, or returns low-confidence output. Options: fall back to the manual process, return a "not sure" response, escalate to a human. The answer should never be "crashes" or "silently wrong."

### Integration
Connecting to existing systems (ERP, CRM, data pipelines) typically takes as long as building the AI itself. Scope the integration explicitly in [[3-scoping]] and [[4-requirements]] — don't leave it to the end.

### Security
For LLM-based systems: validate all inputs, sanitize all outputs before passing to downstream systems, apply least-agency to tool permissions. See [[llm-security]] for the full OWASP Top 10 for LLM Applications.

---

## Common PoC-to-Production Failure Modes

| Failure | Root cause | Prevention |
|---|---|---|
| "It worked in the PoC" | PoC used curated data; production data is messy and drifts | Load test + data quality audit before launch |
| No one uses it | No change management, no champion, no workflow integration | Assign champion + change manager in scoping phase |
| Silent degradation | No monitoring — model degrades for months before anyone notices | Monitoring live on day one, before launch |
| Integration surprise | Last-mile connection to existing systems scoped too late | Scope integration explicitly in [[3-scoping]] |
| Metric mismatch | PoC optimized for accuracy; business cares about throughput or cost | Align metrics in [[4-requirements]] |
| Governance gap | No one knows who approves a model update or handles an incident | Governance model agreed before launch |

---

## Go / No-Go Decision Framework

Before moving from PoC to production, assess all of:

- [ ] Exit criteria met (defined before PoC started)
- [ ] Business champion identified and committed
- [ ] Full production cost quantified and approved
- [ ] Cross-functional production team assembled
- [ ] Governance model defined (owners, approvals, escalation path)
- [ ] Regulatory / compliance sign-off obtained
- [ ] Monitoring and alerting infrastructure ready
- [ ] Retraining plan documented
- [ ] Fallback behavior implemented and tested
- [ ] Integration load tested at production volumes
- [ ] User communication plan ready
- [ ] Post-launch support period budgeted

---

## Related Pages

- [[0-overview]] — Full lifecycle context
- [[3-scoping]] — Where integration scope and effort should be locked in
- [[4-requirements]] — Where success metrics and performance thresholds are defined
- [[ML Ops]] — MLOps lifecycle: retraining, drift detection, model registry, CI/CD
- [[2.1 - Regulated industries]] — Compliance gates that block production rollout
- [[2.2 - EU_AI_Act]] — EU regulatory requirements for production AI systems
- [[llm-security]] — Security checklist for LLM-based production systems
