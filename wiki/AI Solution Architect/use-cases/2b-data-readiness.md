# Data Readiness for AI Projects

**Summary**: A structured framework for assessing whether a client's data can support an AI use case — covering availability, quality, volume, labels, governance, and architecture. Used as a gate before scoping begins.

**Last updated**: 2026-06-29

---

## Why Data Readiness Is a Gate, Not a Detail

Most AI projects that fail technically do so because of data, not models. The model is the easy part. Data readiness must be assessed early — ideally during [[2-feasibility|feasibility]] — because data gaps that surface during build are expensive to fix and often kill the project entirely.

As an SA rule of thumb: **if you cannot answer all six dimensions below with confidence, the project is not ready to scope**.

---

## The Six Dimensions

Assess each on a traffic-light scale: 🟢 ready / 🟡 needs work / 🔴 blocker.

### 1. Availability
Does the data exist and can it be accessed?

| Question                                                             | Red flag                             |
| -------------------------------------------------------------------- | ------------------------------------ |
| Does the data exist at all?                                          | "We probably have it somewhere"      |
| Who owns it and can grant access?                                    | No named data owner                  |
| Is it accessible without a 6-month procurement process?              | IT/legal bottlenecks unresolved      |
| Is it stored in a usable format (not paper, PDFs, handwritten logs)? | Unstructured with no extraction path |

### 2. Volume

Is there enough data for the chosen AI approach?

| Approach                            | Minimum data needed                                    |
| ----------------------------------- | ------------------------------------------------------ |
| Linear model                        | Hundreds of labeled rows                               |
| Tree model (XGBoost/LightGBM)       | Thousands of labeled rows                              |
| Fine-tuned foundation model         | Hundreds to low thousands of examples                  |
| Neural network trained from scratch | Tens of thousands to millions                          |
| RAG / prompt engineering            | No training data needed — quality of documents matters |

Red flag: client says "we have a lot of data" without being able to quantify it or specify what labels are available.

### 3. Quality
Is the data accurate, complete, and consistent?

Key checks:
- **Missing values**: what percentage of records are incomplete? >20% missing on key features is a blocker
- **Consistency**: same entity represented differently across systems (e.g. customer IDs don't match between ERP and CRM)
- **Accuracy**: is the data actually correct? Sensor drift, manual entry errors, outdated records
- **Freshness**: how often is the data updated? A model trained on yearly data cannot make daily predictions

As an SA rule of thumb: **budget 40–60% of project effort for data preparation**, even when the client says "the data is ready."

### 4. Labels / Ground Truth
Can the model be trained and objectively evaluated?

| Situation                                         | Implication                                                                   |
| ------------------------------------------------- | ----------------------------------------------------------------------------- |
| Labels already exist (historical outcomes)        | Supervised learning is feasible                                               |
| Labels can be created (e.g. experts can annotate) | Budget for annotation — typically $0.05–$5 per label depending on complexity  |
| No labels and labeling is infeasible              | Must use unsupervised or self-supervised approach, or use a pre-trained model |
| Outcome is subjective or ambiguous                | Inter-annotator agreement becomes critical — quantify it before committing    |

Label quality matters as much as quantity. A model trained on noisy labels will have a hard ceiling on performance regardless of data volume.

### 5. Governance
What constraints apply to how the data can be used?

| Constraint           | Questions to resolve                                                                               |
| -------------------- | -------------------------------------------------------------------------------------------------- |
| GDPR / privacy       | Can this data be used for ML? Does it contain PII? Must it stay in the EU?                         |
| Industry regulations | See [[2.1 - Regulated industries]] — healthcare, finance, and defence have additional requirements |
| Data residency       | Can data leave the client's premises or country? Affects cloud vs. on-prem decision                |
| Third-party data     | Is any data licensed from a vendor? Does the license permit ML training?                           |
| Retention            | Will the data still exist in 2 years for retraining?                                               |

### 6. Architecture
Where does the data live and how does it flow?

| Pattern                                             | Implication for AI                                                |
| --------------------------------------------------- | ----------------------------------------------------------------- |
| **Data lake** (raw files, S3/ADLS)                  | Good starting point; needs transformation pipeline for ML         |
| **Data warehouse** (structured, BigQuery/Snowflake) | Ready for tabular ML; good data quality guarantees                |
| **Feature store** (precomputed ML features)         | Ideal — reduces training and inference latency                    |
| **Vector database** (embeddings)                    | Required for RAG; needs to be populated and maintained            |
| **Operational databases** (Postgres, Oracle)        | Accessible but not ML-ready; requires ETL                         |
| **Data in silos** (each dept has its own system)    | High integration effort; may require data modelling before any ML |

---

## Data Readiness Assessment Output

Use this as a structured output from the [[2-feasibility|feasibility workshop]] for each use case:

| Dimension    | Status       | Key finding | Action needed |
| ------------ | ------------ | ----------- | ------------- |
| Availability | 🟢 / 🟡 / 🔴 |             |               |
| Volume       | 🟢 / 🟡 / 🔴 |             |               |
| Quality      | 🟢 / 🟡 / 🔴 |             |               |
| Labels       | 🟢 / 🟡 / 🔴 |             |               |
| Governance   | 🟢 / 🟡 / 🔴 |             |               |
| Architecture | 🟢 / 🟡 / 🔴 |             |               |

**All green**: proceed to [[3-scoping|scoping]].
**One or more yellow**: proceed with a data preparation workstream alongside scoping.
**Any red**: pause — resolve the blocker before scoping or accept the project risk explicitly.

---

## Related Pages

- [[Overview]] — The 4 AI dimensions; data volume drives model architecture choice
- [[technical-framework]] — Phase 2 of the technical framework is a data assessment
- [[2-feasibility]] — Where data readiness is scored as part of use case evaluation
- [[3-scoping]] — Data preparation effort must be scoped explicitly
- [[2.1 - Regulated industries]] — Governance constraints by industry
