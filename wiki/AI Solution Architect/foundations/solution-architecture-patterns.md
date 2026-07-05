# AI Solution Architecture Patterns

**Summary**: The six recurring end-to-end patterns for deploying AI systems in production — above the model selection level, covering how components connect, where inference runs, and how humans stay in the loop.

**Last updated**: 2026-06-29

---

## Why Architecture Patterns Matter

Choosing the right model (covered in [[technical-framework]] and [[Overview]]) is only half the design problem. The other half is how the model fits into the broader system: where inference runs, how data flows in, what happens with the output, and who reviews decisions. These architecture patterns recur across industries and use cases — recognising them early in [[3-scoping|scoping]] prevents costly redesigns later.

---
## Solving data silos

Problem:
- The "Single Source of Truth" Does Not Exist
- Incomplete Insights for Machine Learning: If you want to predict customer churn, you need CRM data (Sales), support tickets (Customer Success), and product usage logs (Engineering). If those are siloed, your model can only see one piece of the puzzle, leading to highly inaccurate predictions
- Wasted Storage and Engineering Resources: Silos breed duplication. Different teams unknowingly store the same massive datasets in different cloud buckets or on-premise servers.
- Severe Security and Compliance Risks: It is incredibly difficult to enforce data privacy laws (like GDPR or CCPA) if you don't actually know where all your data live
- Lacking standardization: different DQ standards acoss organization
- Slow Operational Speed: When data isn't unified, getting answers to simple cross-departmental questions requires manual effort

Solution:
1) The Centralized Approach: Data Lakehouse
A Centralized Data Lakehouse unifies the cheap, unstructured storage of a traditional Data Lake (like AWS S3 or Azure Blob) with the structure, ACID transactions, and governance features of a Data Warehouse.
All raw data from across the enterprise is ingested into a single, central platform. A centralized data engineering team is then responsible for cleaning, transforming, and optimizing it into refined tables (often using formats like Delta Lake or Apache Iceberg) for data scientists to use

| Pros (+)                                                                                                                                                                                                 | Cons (-)                                                                                                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Simplified Governance:** Security policies, access controls (RBAC), and compliance rules are enforced in one single place                                                                              | **The Central Bottleneck:** The central data engineering team becomes a massive bottleneck. They often don't understand the business context of the data they are transforming, leading to delays |
| **Single Source of Truth:** High consistency. It is easier to ensure that there is only one definitive "Customer Table" used across the entire company                                                   | **The "Data Swamp" Risk:** If ingestion is not strictly managed, the lake quickly degrades into an unorganized, unsearchable mess of stale files                                                  |
| **Easier Global ML Training:** Data scientists have a single endpoint to connect to. Running large-scale, cross-domain ML models is straightforward because all data resides in the same storage cluster | **High Initial Architecture Costs:** Migrating diverse, massive legacy pipelines into one central infrastructure requires significant upfront investment and time                                 |

2) The Decentralized Approach: Data Mesh
A Data Mesh rejects the idea of a central data repository and a central team. Instead, it treats **Data as a Product** and shifts ownership back to the business domains that actually generate the data (e.g., the Sales team owns the Sales data product; the Logistics team owns the Logistics data product).

Each domain is responsible for building, cleaning, and exposing their data via standardized, discoverable interfaces (like APIs or curated cloud tables). A central "Data Platform" team simply provides the self-service infrastructure and global governance standards (e.g., a shared data catalog), but they do not touch or manage the data itself

| Pros (+)                                                                                                                                                                                              | Cons (-)                                                                                                                                                                                                                              |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Scales Unboundedly:** Because domain teams manage their own data pipelines, the architecture scales naturally as the company grows. No central bottleneck.                                          | **Organizational Complexity:** Requires a massive cultural shift. Domain teams must hire or upskill their own data engineers, which many departments resist.                                                                          |
| **Higher Data Quality:** The people who create the data are the ones managing it. The Sales team knows exactly what an "active lead" status means, resulting in cleaner, more accurate data products. | **Fragile Consistency:** Ensuring that different domains use the exact same definitions (e.g., how "revenue" is calculated) across independent pipelines is incredibly difficult --> **create a platform**                            |
| **Agile and Fast:** Business units can iterate, add new data sources, and deploy localized ML models quickly without waiting for a central IT queue.                                                  | **Harder Cross-Domain ML:** If a data scientist needs to train a model that relies on data from five different domains, they must stitch together five separate data products, which can introduce latency and integration headaches. |

## The Architect's Verdict: Which should you choose?

- **Choose a Centralized Data Lakehouse if:** Your company is mid-sized to large but has a centralized IT structure, your data domains are highly interdependent, and your primary goal is to establish strict, uniform governance for heavy, cross-departmental AI model training.
    
- **Choose a Decentralized Data Mesh if:** Your organization is a massive enterprise with highly autonomous business units, the central IT team is drowning in data requests, and you have the budget and maturity to treat data teams as product teams within individual business departments.

## Key Risks & How to Mitigate Them

Unifying data across an enterprise is as much a political and security challenge as it is a technical one.


| Risk                             | Impact on ML Project                                                                                                               | Mitigation Strategy                                                                                                                                                                                                                             |
| -------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| The "Data Swamp" Effect          | Ingesting low-quality, unmapped data makes the unified layer unusable for data scientists                                          | **Implement Data Quality Gates:** Use tools like _Great Expectations_ to validate data quality (checking for missing values, schema drifts, or anomalies) _before_ it enters the analytics layer.                                               |
| Security & Compliance Violations | Centralizing data can easily expose PII (Personally Identifiable Information) or breach regulations like GDPR/CCPA.                | **RBAC & Attribute-Based Access Control:** Implement dynamic masking and anonymization at the ingestion layer. Ensure data scientists train models on anonymized data and use tools like _Apache Ranger_ or cloud-native IAM to restrict access |
| Organizational Resistance        | System owners (e.g., the ERP team) are often protective of their data and slow to grant access                                     | **Executive Sponsorship & Value-First Approach:** Frame data sharing not as a chore, but as a value driver. Build a quick, high-ROI MVP using just two silos to prove the business value before asking for enterprise-wide access.              |
| Feature Creep / Scope Bloat      | Trying to unify _all_ enterprise data at once results in a multi-year project that delivers zero business value in the short term. | **Use-Case Driven Ingestion:** Do not try to boil the ocean. Look at the specific ML model you want to build (e.g., Churn Prediction) and _only_ unify the data sources required for that specific model first.                                 |


---

## Pattern 1: Batch Inference Pipeline

**What it is**: The model runs on a schedule (nightly, weekly) over a large dataset. Results are stored and consumed downstream.

```
Data source → ETL/transform → Model → Output table → BI / dashboard / ERP
```

**When to use**:
- No real-time latency requirement (hours/days are acceptable)
- Large volume to score at once (millions of records)
- Outputs feed reports, dashboards, or planning tools

**Examples**: Demand forecasting, churn scoring, credit risk batch scoring, predictive maintenance alerts generated overnight

**Trade-offs**:
- ✅ Simple, cheap to operate, easy to audit
- ✅ Model can be large and slow — latency doesn't matter
- ❌ Staleness: predictions are only as fresh as the last batch run
- ❌ Cannot react to real-time events

---

## Pattern 2: Real-Time Inference (Model as API)

**What it is**: The model is deployed as a REST API endpoint. Each incoming event triggers a synchronous model call.

```
User / system event → API call → Model server → Prediction → Consuming system
```

**When to use**:
- Per-event decisions with strict latency requirements (<1s)
- Model must respond to the current state, not a batch snapshot
- Output drives an immediate action (show a recommendation, trigger an alert)

**Examples**: Fraud detection at payment time, product recommendations on page load, quality inspection at production line speed

**Trade-offs**:
- ✅ Fresh predictions, event-driven
- ✅ Integrates with any system that can call an API
- ❌ Requires model serving infrastructure (scaling, redundancy, monitoring)
- ❌ Model must be fast enough to meet latency SLA

---

## Pattern 3: RAG Pipeline (Retrieval-Augmented Generation)

**What it is**: An LLM is grounded in company-specific documents retrieved at inference time from a vector database. The model generates answers based on retrieved context, not just its training data.

```
Query → Embedding → Vector DB search → Retrieved chunks + Query → LLM → Answer
```

**When to use**:
- LLM needs to answer questions about proprietary, frequently-updated knowledge
- Hallucination risk is unacceptable — answers must be grounded in verifiable sources
- No training data available or practical to collect

**Examples**: Internal knowledge base Q&A, contract review, technical documentation assistant, customer support over product manuals

**Trade-offs**:
- ✅ No model training required; knowledge base updated by adding documents
- ✅ Traceable — can cite the source chunk for any answer
- ❌ Retrieval quality is a bottleneck — bad retrieval → bad answers
- ❌ Vector DB must be populated, maintained, and kept in sync with source documents
- ❌ Latency is additive: retrieval + LLM call

See [[build-vs-buy]] for when RAG is preferred over fine-tuning.

---

## Pattern 4: Agentic / LLM + Tool Use Pipeline

**What it is**: An LLM that autonomously decides which tools to call (APIs, databases, code execution) in order to complete a multi-step task. See [[agentic-ai-definition]] for the full definition.

```
Goal → LLM reasoning → Tool call → Result → LLM reasoning → ... → Final output
```

**When to use**:
- Task requires multiple steps with intermediate decisions
- No fixed execution path — the model must adapt based on results
- Tools are diverse (search, calculate, write, call API)

**Examples**: Automated report generation, data analysis agent, IT support agent, sales research assistant

**Trade-offs**:
- ✅ Handles complex, variable tasks that no fixed pipeline could cover
- ✅ Tool set can be extended without retraining the model
- ❌ Non-deterministic — same input may produce different tool call sequences
- ❌ Requires robust observability and guardrails — see [[agentic-ai-observability]] and [[llm-security]]
- ❌ Cost scales with number of LLM calls per task

---

## Pattern 5: Human-in-the-Loop

**What it is**: The model makes a recommendation or draft; a human reviews and approves before the decision takes effect. The human decision and any corrections are fed back to improve the model.

```
Input → Model → Recommendation → Human review queue → Approved / Corrected → Action
                                                             ↓
                                                      Feedback loop → retraining
```

**When to use**:
- High-stakes or regulated decisions where errors are costly (healthcare, finance, legal)
- Model confidence is variable — route low-confidence cases to humans
- Early deployment where trust in the model is not yet established
- Regulatory requirement for human oversight

**Examples**: Medical image triage (radiologist reviews flagged scans), loan approval (ML scores, human decides on borderline cases), content moderation

**Trade-offs**:
- ✅ Safe for high-stakes use cases; builds trust incrementally
- ✅ Human corrections become training data — model improves over time
- ❌ Human bottleneck limits throughput — must design the review queue carefully
- ❌ Requires change management: humans must trust and act on model recommendations

---

## Pattern 6: Embedded / Edge Model

**What it is**: The model runs on the device — a machine, camera, robot, or IoT sensor — rather than calling a central API.

```
Local sensor → On-device model → Local decision / alert
```

**When to use**:
- No reliable network connectivity
- Latency requirement below what a cloud API can deliver (<10ms)
- Data sovereignty: raw data must not leave the device or facility
- Large data volume where sending everything to the cloud is impractical

**Examples**: Quality inspection camera at production line, predictive maintenance on factory floor without cloud connectivity, autonomous robot navigation

**Trade-offs**:
- ✅ Low latency, works offline, data stays local
- ✅ Reduces cloud compute and bandwidth cost at scale
- ❌ Model must be small and efficient (quantization, pruning, distillation)
- ❌ Updating the model across many devices requires a deployment pipeline (OTA updates)
- ❌ Limited compute — cannot run large foundation models

---

## Pattern Comparison

| Pattern | Latency | Data freshness | ML complexity | Human involvement | Typical cost |
|---|---|---|---|---|---|
| Batch pipeline | Hours/days | Low | Low | None (output reviewed later) | Low |
| Real-time API | <1s | High | Medium | None at inference | Medium |
| RAG pipeline | 1–5s | High (docs updated independently) | Low–medium | None at inference | Medium |
| Agentic | Seconds–minutes | High | High | Optional oversight | High (multi-LLM calls) |
| Human-in-the-loop | Minutes–hours | Medium | Any | Core to the system | Medium + staff |
| Edge/embedded | <10ms | High | Low–medium | None | Low (hardware cost) |

---

## Choosing a Pattern

Start with these questions during [[3-scoping|scoping]]:

1. **What is the latency requirement?** → eliminates batch; may require edge
2. **Does the output drive an immediate action or a future one?** → real-time vs. batch
3. **Is the input a document/knowledge question or structured data?** → RAG vs. predictive
4. **Does the task require multiple adaptive steps?** → agentic
5. **Are the stakes high enough to require human review?** → human-in-the-loop
6. **Is connectivity unreliable or is data sovereignty required?** → edge

Patterns can be combined: a human-in-the-loop system can sit on top of a real-time API; a RAG pipeline can be part of an agentic system.

---

## Related Pages

- [[Overview]] — Model architecture selection (the layer below these patterns)
- [[technical-framework]] — Phase 4 covers architecture and integration design
- [[build-vs-buy]] — Determines which model/foundation sits inside the pattern
- [[3-scoping]] — Where the architecture pattern is decided and scoped
- [[agentic-ai-definition]] — Deep dive on the agentic pattern
- [[agentic-ai-observability]] — Observability requirements specific to agentic pattern
- [[llm-security]] — Security considerations for patterns using LLMs
