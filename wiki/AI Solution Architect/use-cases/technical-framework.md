# Technical Framework for New AI Use Cases

**Summary**: A reference tool used during feasibility and scoping to map any AI use case to its 4 dimensions and design the architecture. Not a sequential phase — a decision guide.

**Last updated**: 2026-06-25

---

## Framework 1 (Technical): Phased Approach

A structured sequence of questions to work through before writing a single line of code.

### Phase 1 — Problem Framing

| Question | What you are looking for |
|---|---|
| What decision does the model support or automate? | Grounds the problem — avoids building a model that outputs a number nobody acts on |
| What is the cost of a wrong prediction? | False positive vs. false negative trade-off drives the evaluation metric (precision vs. recall) |
| What is the baseline today? | Rules, spreadsheets, human judgment — the model must beat this to justify the investment |
| Is AI the right tool? | If the logic can be expressed as rules or a formula, use that. AI adds value when patterns are too complex or too many to hand-code. |

### Phase 2 — Data Assessment

| Question | What you are looking for |
|---|---|
| What data exists and where does it live? | Source systems (ERP, MES, sensors, APIs), format, access rights |
| Is the data labeled? | Determines learning paradigm (see decision guide below) |
| How much data is available? | Rules of thumb: linear models ~hundreds of rows; tree models ~thousands; neural networks ~tens of thousands+ |
| How clean and complete is it? | Missing values, outliers, sensor drift, inconsistent schemas — estimate cleaning effort |
| Are there privacy or compliance constraints? | GDPR, industry regulations — affects where data can be stored and processed |
| Is the data stored across silos? | Data modelling required |

### Phase 3 — AI Dimension Mapping

Use the **Decision Guide** below to determine the 4 dimensions: capability, application domain, learning paradigm, model architecture. This is the core technical scoping step.

### Phase 4 — Architecture & Integration Design

| Question | What you are looking for |
|---|---|
| Where does inference run? | Cloud (high compute, flexible) vs. edge (low latency, no connectivity needed) vs. on-prem (data sovereignty) |
| Batch or real-time? | Batch: run nightly, results in a database. Real-time: model served as API, called per event. |
| What systems does the output connect to? | ERP, MES, SCADA, dashboard — defines integration effort and data flow |
| Latency requirement? | <10ms (edge inference) vs. seconds (API call) vs. hours (batch job) |
| Build or buy? | Fine-tune a foundation model vs. train from scratch vs. use a vendor API vs. buy an off-the-shelf product |

### Phase 5 — Risk & Feasibility

| Question | What you are looking for |
|---|---|
| Is there enough labeled data to train? | If no: can you label it, use unsupervised methods, or use a pre-trained model? |
| Can you evaluate the model objectively? | You need a held-out test set that represents production — if not, the accuracy number is meaningless |
| How will the model fail? | Identify failure modes early: out-of-distribution inputs, adversarial cases, edge cases |
| Who is accountable if the model is wrong? | Defines the level of human oversight required |

### Phase 6 — MLOps & Monitoring

| Question | What you are looking for |
|---|---|
| How is model performance tracked in production? | Business metrics (downtime reduced, defects caught) + ML metrics (accuracy, drift) |
| When and how is the model retrained? | Scheduled retraining vs. triggered by drift detection |
| What is the rollback plan? | If a new model version degrades performance, how quickly can you revert? |
| Who maintains this after go-live? | Data scientist, vendor, or ML platform — ownership must be defined upfront |

---

## Decision Guide: Determining the 4 AI Dimensions

Work through the four steps in order. Each step's answer feeds the next.

### Step 1 — Capability: What does the system do?

```
What should the system output?
│
├─ Creates new content (text, images, audio, video)
│   └─► Generative AI
│
├─ Makes sequential decisions in an environment (optimize, control, schedule)
│   └─► Decision making AI  →  learning paradigm will be Reinforcement Learning
│
└─ Predicts a known outcome from input data
    └─► Predictive AI
         │
         ├─ Output is a CATEGORY
         │   └─► Classification
         │        ├─ 2 possible categories (yes/no, defect/ok)  →  Binary classification
         │        ├─ One category from N options (which product? which fault type?)  →  Multi-class
         │        └─ Multiple categories at once (what topics does this text cover?)  →  Multi-label
         │
         └─ Output is a NUMBER
              └─► Regression
                   ├─ One number (demand next week, remaining useful life)  →  Single output
                   └─ Several numbers at once (x/y/z coordinates, forecast for 10 SKUs)  →  Multiple output
```

### Step 2 — Application Domain: What type of data is the input?

| Input data type | Domain | Typical source |
|---|---|---|
| Images, video, 2D scans | Computer vision | Industrial cameras, quality inspection, satellite |
| Text, documents, logs | NLP | News feeds, ERP notes, contracts, chat |
| Audio, speech | Speech | Microphones, call recordings |
| Sensor streams, financial series, demand history | Time series | IoT sensors, MES, ERP, market data |
| Physical motion, robot joints, spatial data | Robotics | Robot controllers, PLCs |
| Mix of the above | Multi-modal | Combine approaches |

### Step 3 — Learning Paradigm: How does it learn?

```
Do you have labeled training data (input + correct output pairs)?
│
├─ YES — labels available and sufficient
│   └─► Supervised learning
│
├─ NO labels, but you need to find patterns, clusters, or anomalies
│   └─► Unsupervised learning
│
├─ NO labels, but input is text or images and pre-trained models exist
│   └─► Self-supervised (fine-tune a foundation model — BERT, LLM, vision model)
│        Works because the foundation model already learned representations from massive data.
│        You only need a small labeled set for the final fine-tuning step.
│
└─ NO dataset at all — but you can define a reward and interact with an environment
    └─► Reinforcement Learning
         Requires a simulator or real environment to generate experience.
```

### Step 4 — Model Architecture: What is it built with?

```
Is the input tabular / structured data? (rows and columns, from ERP/CRM/sensors as features)
│
├─ YES
│   ├─ Is the relationship roughly linear and interpretability is critical?
│   │   └─► Linear model  (fast, readable coefficients, use as baseline first)
│   │
│   └─ Non-linear patterns, mixed feature types, missing values, need high accuracy?
│       └─► Tree model  (XGBoost / LightGBM — default choice for tabular data)
│
└─ NO — input has spatial or sequential structure
    │
    ├─ Images / video
    │   └─► CNN  (convolutional neural network)
    │
    ├─ Sequential / time series
    │   ├─ Simple series, edge device, limited data or compute
    │   │   └─► RNN / LSTM / GRU
    │   │
    │   └─ Multi-variate, long-range dependencies, large dataset
    │       └─► Transformer  (TFT, PatchTST for time series)
    │
    ├─ Text / NLP
    │   └─► Transformer  (fine-tuned BERT / LLM)
    │
    └─ Mixed modalities (e.g., tabular + text, image + time series)
        └─► Combine architectures  (e.g., XGBoost on tabular + BERT on text → ensemble)
```

---

## Framework 2 (Conceptual): Questions Before Committing

| Area | Questions |
|---|---|
| Business Value | Why use AI? |
| Data | Is data available and high quality? |
| Explainability | Can users understand the output? |
| Auditability | Can we trace decisions later? |
| Human Oversight | Who approves critical decisions? |
| Hallucination Control | How do we ground responses? |
| Privacy | Is sensitive data protected? |
| Security | Can attackers manipulate the system? |
| Monitoring | How do we detect drift? |
| Compliance | Which regulations apply? |

---

## Related pages

- [[0-overview]] — Full lifecycle map
- [[Overview]] — The 4 AI dimensions explained in depth
- [[2-feasibility]] — Where this framework is used to assess technical complexity
- [[3-scoping]] — Where this framework informs architecture and integration design
- [[neural-networks]] — Deep dive on neural network architectures
