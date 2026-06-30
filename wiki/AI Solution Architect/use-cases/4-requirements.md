# Requirements Engineering for AI Projects

**Summary**: Translating the scoping document into a detailed engineering specification — covering functional, non-functional, data, and integration requirements for AI systems.

**Last updated**: 2026-06-25

---

## What is requirements engineering?

Requirements engineering (RE) turns the high-level answers from [[3-scoping]] into a specification detailed enough for an engineering team to design, build, and test against. It is the bridge between the project definition and the build phase.

| | Scoping | Requirements Engineering |
|---|---|---|
| **Audience** | Client stakeholders, SA, project lead | Engineering team, data scientists |
| **Question** | What are we building and how long will it take? | Exactly what must the system do, measurably? |
| **Success metric** | "Recall ≥ 85%" | "Recall ≥ 85% on held-out test set of ≥ 500 labeled samples, measured monthly on production data" |
| **Data scope** | "We'll use sensor data from line 4" | "OPC-UA stream at 10 Hz, 6 features, 18 months history, delivered as Parquet to S3 bucket X" |
| **Integration** | "Output goes to the MES" | "REST API, response schema defined, p99 latency < 200 ms, SAP PM ticket format v2.3" |

---

## Why RE is different in AI projects

**Functional requirements are probabilistic.** Classical software either does something or it doesn't. AI systems have a performance distribution. Requirements must specify a target threshold *and* what happens when the system falls below it — not just "the model shall achieve recall ≥ 85%" but "if recall drops below 80% on the monthly evaluation, the system shall raise an alert and fall back to rule-based logic."

**Data is a first-class requirement.** In classical software, data is an input. In AI, data is a dependency that determines what's achievable. Data requirements must be specified with the same rigor as functional ones.

**Requirements must be revisited after the PoC.** The PoC (Phase 2 in [[3-scoping]]) often reveals that the data can't support the originally specified thresholds. RE is not a one-time gate — detailed requirements are drafted before build starts and revised once the PoC results are known.

---

## The four requirement types

### 1. Functional requirements

Define what the system does — input, output, and behavior under edge cases.

- What is the input? (data type, format, source, frequency)
- What is the output? (prediction, score, category, recommendation)
- What is the decision boundary? (threshold for classification, confidence floor)
- What happens when the model is uncertain or input is out-of-distribution?
- What is the fallback behavior? (rule-based logic, human escalation, no-output)

### 2. Non-functional requirements

Define how well the system must perform — often the most under-specified in early projects.

| Dimension | Example specification |
|---|---|
| **Model performance** | Recall ≥ 85%, precision ≥ 70% on held-out test set; re-evaluated monthly |
| **Latency** | p99 inference latency < 200 ms for real-time API; < 4 hours for nightly batch |
| **Availability** | 99.5% uptime during production hours (06:00–22:00) |
| **Explainability** | Every prediction must include top-3 feature contributions (SHAP values) |
| **Fairness** | Performance gap between demographic subgroups < 5 percentage points |
| **Drift tolerance** | Alert if input feature distribution shifts by > 2 standard deviations from training baseline |

### 3. Data requirements

Define what training and inference data the system needs to function correctly.

**Training data spec:**
- Sources, systems, date range
- Minimum volume (rows, images, tokens)
- Label definition: what constitutes a positive / negative example, exactly
- Label quality: inter-annotator agreement threshold, review process
- Class balance requirements and augmentation strategy if imbalanced
- Train / validation / test split strategy

**Inference data contract:**
- Feature names, types, valid ranges
- Missing value handling: which features are nullable, what are defaults
- Update frequency and latency from source system to model input
- Data quality SLA: who owns remediation if upstream data degrades

### 4. Integration requirements

Define how the model connects to the rest of the system.

- **API contract**: endpoint, request/response schema, versioning, authentication
- **Consumer systems**: which systems receive the output and in what format
- **Trigger**: event-driven (per request), scheduled batch, or streaming
- **Latency and throughput**: requests per second, batch size, acceptable queue depth
- **Monitoring hooks**: what metrics does the model expose to the observability layer
- **Rollback interface**: how does the consuming system switch to the fallback if the model is degraded

---

## When to run requirements engineering

For **small projects** (PoC-first approach): combine scoping and high-level RE into one document. Revisit and formalize after the PoC confirms feasibility.

For **larger or regulated projects**: run a dedicated RE phase of 2–4 weeks between scoping sign-off and build kickoff. Involve data engineers, integration architects, and the business owner.

**Key milestone**: RE is complete when the engineering team can answer "how will we know if this is done?" without asking the business again.

---

## Common RE failures in AI projects

**Specifying the metric but not the evaluation protocol**: "recall ≥ 85%" is ambiguous without specifying the test set, the time window, the label source, and the evaluation frequency. Two people can disagree on whether a model passes without either being wrong.

**Leaving the fallback undefined**: Every AI system needs a defined behavior for the cases it can't handle. If the RE document doesn't specify this, the engineering team will implement something arbitrary — and it will surface in production at the worst moment.

**No data quality SLA**: The model can only be as good as the data it receives. If upstream data quality is not specified as a requirement with an owner, the model will silently degrade when data pipelines fail, and nobody will know whose problem it is.

**Treating requirements as fixed**: In AI projects, the PoC changes what's achievable. Build a formal change process into the RE document — a lightweight sign-off when thresholds are revised based on PoC results. Without it, scope changes happen informally and create misalignment.

---

## Related pages

- [[0-overview]] — Full lifecycle map
- [[3-scoping]] — Previous step: project definition and effort estimate
- [[technical-framework]] — Architecture and integration design decisions that feed into integration requirements
- [[2-feasibility]] — Feasibility scorecard provides the first draft of performance thresholds
- [[2.1 - Regulated industries]] — Regulated industries impose additional non-functional requirements (audit trails, validation documentation, explainability)
