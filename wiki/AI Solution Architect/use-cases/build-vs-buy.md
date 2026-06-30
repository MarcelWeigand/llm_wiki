# Build vs. Buy vs. Fine-tune

**Summary**: A decision framework for the most common client question in AI consulting — when to use a vendor API as-is, when to use RAG, when to fine-tune a foundation model, and when to train from scratch.

**Last updated**: 2026-06-29

---

## Why This Decision Matters

Clients almost always ask this question too late — after a team has already committed to an approach. As an SA rule of thumb: **resolve build-vs-buy before architecture design, not during it**. The answer determines team composition, cost structure, vendor dependency, and time to value.

This is a reference tool used across [[2-feasibility|feasibility]], [[3-scoping|scoping]], and [[4-requirements|requirements]]. It also appears as a question in the [[technical-framework]] (Phase 4).

---

## The Four Options

### Option 1: Use Vendor API As-Is
Use a foundation model (GPT-4, Claude, Gemini, Mistral) via API without any modification.

**When to use**:
- Task is general-purpose (summarisation, Q&A, drafting, classification over short texts)
- Speed to market is the priority — days, not months
- No proprietary data advantage that would justify training cost
- Client has no ML team and no desire to build one

**Pros**:
- Fastest path to a working prototype
- No training data, no ML expertise required
- Always access the latest model version
- Predictable per-token pricing

**Cons**:
- Proprietary data sent to a third-party vendor — check data privacy requirements
- Vendor lock-in: prompt changes when the API changes
- No customisation for domain-specific language, format, or style
- Ongoing API cost scales with usage — can become expensive at volume

**Typical use cases**: Internal chatbot, document summarisation, email drafting assistant, general code completion

---

### Option 2: RAG (Retrieval-Augmented Generation)
Use a foundation model via API, but ground it in company-specific documents retrieved from a vector database at inference time.

**When to use**:
- Task requires answers grounded in proprietary, frequently-updated knowledge
- Hallucination is unacceptable — answers must cite a source
- Knowledge base changes frequently (new products, policies, regulations)
- No labeled training data available

**Pros**:
- No model training required — update knowledge by adding documents
- Answers are traceable to source chunks
- Works well with small knowledge bases (hundreds to thousands of documents)
- Modular — retrieval and generation can be improved independently

**Cons**:
- Retrieval quality is a ceiling on answer quality — bad retrieval → bad answers
- Requires building and maintaining a vector database pipeline
- Latency is additive (retrieval + LLM call)
- Does not improve the model's reasoning or language style — only its knowledge

**Typical use cases**: Internal knowledge base Q&A, product documentation assistant, contract review, regulatory Q&A

See [[solution-architecture-patterns]] for the full RAG pipeline architecture.

---

### Option 3: Fine-tune a Foundation Model
Start from a pre-trained foundation model and continue training it on a curated dataset of task-specific examples.

**When to use**:
- Consistent output format or style that cannot be reliably achieved through prompting
- Domain-specific language the general model handles poorly (medical, legal, industrial)
- General model underperforms on the task even with few-shot examples
- Privacy requirement: cannot send data to a vendor API
- High-volume use case where a smaller fine-tuned model is cheaper than API calls at scale

**Pros**:
- Better task-specific performance than prompting alone
- Can be smaller and faster than the general model (reduced inference cost)
- Data stays on-premises if self-hosted
- Can encode proprietary style, terminology, and format

**Cons**:
- Requires labeled training data (hundreds to low thousands of examples minimum)
- Requires ML expertise to run the training pipeline and evaluate results
- Must be periodically retrained as the task or data distribution changes
- Higher upfront cost — model training, evaluation, deployment

**Typical use cases**: Domain-specific NLP classifier, custom code generation, medical report generation, customer-support response model trained on historical tickets

---

### Option 4: Train from Scratch
Build and train a model entirely from your own data, with no foundation model as a starting point.

**When to use**:
- Input is structured / tabular data (tree models or custom neural networks, not LLMs)
- Edge deployment with strict compute constraints (tiny model required)
- Highly specialised domain with no relevant foundation model
- Full control over model architecture is required (e.g., safety-critical systems)
- Massive proprietary dataset where a custom model has a real competitive advantage

**Pros**:
- Full control — architecture, training data, outputs
- No vendor dependency
- Can be extremely efficient for narrow, well-defined tasks
- For tabular data: XGBoost/LightGBM trained from scratch is often the best approach

**Cons**:
- Most expensive: data collection, labeling, model development, infrastructure
- Requires the most ML expertise
- Longest time to production
- Full maintenance burden — no vendor updating the model for you

**Typical use cases**: Predictive maintenance on proprietary sensor data (tree model), quality inspection CNN trained on in-house defect images, custom demand forecasting model

---

## Decision Guide

```
Is the task general-purpose NLP with no proprietary data advantage?
└─► YES → Use vendor API as-is

Is the task grounded Q&A over frequently-updated company documents?
└─► YES → RAG

Is the input structured / tabular data, or does the model need to run on edge?
└─► YES → Train from scratch (tree model or compact NN)

Does the task need consistent domain-specific format, style, or terminology
that prompting alone cannot achieve reliably?
└─► YES → Fine-tune a foundation model
```

---

## Decision Matrix

| Factor | API as-is | RAG | Fine-tune | Train from scratch |
|---|---|---|---|---|
| Time to first prototype | Days | Weeks | Months | Months |
| ML expertise required | None | Low | High | High |
| Training data needed | None | None | Yes (hundreds+) | Yes (thousands+) |
| Proprietary data stays on-prem | ❌ | ❌ (unless self-hosted) | ✅ (if self-hosted) | ✅ |
| Domain language / style control | Low | Low | High | High |
| Knowledge updates | Prompt changes | Add documents | Retrain | Retrain |
| Inference cost at scale | High (API) | High (API + retrieval) | Low (self-hosted) | Low (self-hosted) |
| Vendor dependency | High | Medium | Low | None |

---

## Common Mistakes

- **Defaulting to fine-tuning when RAG would work**: if the problem is "the model doesn't know our company's documents," that's a knowledge problem, not a style problem — RAG is almost always cheaper and faster
- **Defaulting to API when data privacy requires on-prem**: check data governance requirements before committing to a vendor API
- **Training from scratch for NLP tasks**: in 2025, there is almost no NLP use case where training a language model from scratch beats fine-tuning a foundation model
- **Ignoring inference cost at scale**: API cost that seems trivial at prototype scale can become the dominant cost in production at millions of calls per day

---

## Related Pages

- [[technical-framework]] — Phase 4 includes build-vs-buy as an architecture question
- [[solution-architecture-patterns]] — The pattern chosen (RAG, agentic, batch) constrains the build-vs-buy decision
- [[data-readiness]] — Training data availability is the primary gate for fine-tune and train-from-scratch
- [[3-scoping]] — Where the build-vs-buy decision is locked in and costed
- [[5-production-rollout]] — Vendor API dependency affects production maintenance model
