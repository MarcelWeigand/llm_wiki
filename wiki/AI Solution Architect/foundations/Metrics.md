# AI Metrics — When to Use Which

Organized by **capability** (dimension 1 from [[1 - Overview]]), since the right metric follows directly from what the system does.

---

## 1. Predictive AI — Classification

### Binary Classification

Two classes (defect / ok, fraud / legitimate, churn / no churn).

| Metric                        | What it measures                                                       | Use when                                                                                                                                                                      |
| ----------------------------- | ---------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Accuracy**                  | (TP+TN) / all predictions                                              | Dataset is balanced and all errors cost the same                                                                                                                              |
| **Precision**                 | TP / (TP+FP) — of all predicted positives, how many were correct?      | Min false positives --> False positives are costly (spam filter sending good emails to spam, unnecessary maintenance, too many fraud alerts cause slower customer experience) |
| **Recall** (Sensitivity)      | TP / (TP+FN) — of all actual positives, how many did we catch?         | Min false negatives --> False negatives are costly (missed disease, missed defect, missed fraud)                                                                              |
| **F1 Score**                  | Harmonic mean of precision and recall                                  | Need to balance both — no strong preference for FP vs FN                                                                                                                      |
| **TPR** (True Positive Rate)  | TP / (TP+FN) — identical to Recall                                     | Used as the y-axis of the ROC curve; same concept as Recall, different name                                                                                                   |
| **FPR** (False Positive Rate) | FP / (FP+TN) — of all actual negatives, how many were wrongly flagged? | Used as the x-axis of the ROC curve; controls how many false alarms you generate                                                                                              |
| **ROC-AUC**                   | Area under the TPR vs FPR curve across all thresholds                  | Comparing models, threshold-independent evaluation, balanced datasets                                                                                                         |
| **PR-AUC**                    | Area under the Precision vs Recall curve                               | Imbalanced datasets — ROC-AUC can be misleadingly optimistic when negatives vastly outnumber positives                                                                        |
| **Confusion matrix**          | Full breakdown of TP, TN, FP, FN                                       | Always produce this alongside any metric — it reveals which errors the model makes                                                                                            |
| Brier Score<br>Log-Loss       |                                                                        | Use this when a prediction of **99%** carries a completely different real-world weight or financial consequence than a prediction of **51%**                                  |
|                               |                                                                        |                                                                                                                                                                               |

**FPR vs. 1-Precision — common confusion**: both involve false positives but from different denominators:
- **Precision**: TP / (TP+FP) — denominator is *predicted positives* → "of what I flagged, how many were real?"
- **FPR**: FP / (FP+TN) — denominator is *actual negatives* → "of what was truly negative, how many did I wrongly flag?"

**ROC curve vs. PR curve**:
- **ROC curve** plots TPR (y) vs FPR (x) — use for balanced datasets
- **PR curve** plots Precision (y) vs Recall/TPR (x) — use for imbalanced datasets. When negatives vastly outnumber positives, FPR stays artificially small (large TN denominator), making ROC-AUC look good even when the model produces many false alarms. PR-AUC exposes this.

| Use case                              | Dataset character            | Right metric    | Why                                                                                                                 |
| ------------------------------------- | ---------------------------- | --------------- | ------------------------------------------------------------------------------------------------------------------- |
| Defect detection on production line   | Imbalanced, FN costly        | Recall + PR-AUC | A missed defect ships to the customer — far worse than a false alarm that triggers manual re-inspection             |
| Spam filter                           | FP costly                    | Precision       | A legitimate email in the spam folder damages user trust — false alarms are the primary concern                     |
| Fraud detection                       | Highly imbalanced, FN costly | PR-AUC + Recall | Frauds are rare — ROC-AUC looks deceptively good even when most frauds are missed; PR-AUC exposes the real tradeoff |
| Medical screening / disease diagnosis | FN extremely costly          | Recall          | Missing a disease is dangerous; accept more false positives (extra tests) over missed diagnoses                     |
| Customer churn prediction             | FP and FN both costly        | F1              | Intervention budget is limited — need to balance catching churners vs. wasting budget on false alarms               |

> **Key rule**: Accuracy is almost always the wrong metric for business problems. Ask "what is the cost of a false positive vs. a false negative?" — that determines whether you optimize for precision, recall, or F1.

### Multi-class Classification

N classes, predict exactly one (fault type A/B/C, product category).

- Use the same metrics as binary, but averaged across classes:
  - **Macro average**: average each class equally — highlights poor performance on rare classes
  - **Weighted average**: average weighted by class size — reflects overall accuracy on the full dataset
  - **Micro average**: aggregate all TP/FP/FN globally — dominated by frequent classes
- Use **macro F1** when minority classes matter (e.g., rare fault types must be caught)
- Use **weighted F1** for overall business performance
- Always include a **confusion matrix (NxN)** — shows which classes are confused with each other

### Multi-label Classification

Multiple correct labels per input (a document tagged with multiple topics).

| Metric | What it measures | Use when |
|---|---|---|
| **Subset accuracy** | Fraction of samples where all labels are exactly correct | Strictest — use when exact label sets matter |
| **Hamming loss** | Fraction of individual labels wrongly predicted | Partial credit — a prediction with 4/5 labels right is better than 0/5 |
| **Per-label F1** | F1 computed independently per label | Want to understand per-topic or per-tag performance |

---

## 2. Predictive AI — Regression

Predicting a continuous number (demand, remaining useful life, energy consumption).

| Metric | Formula | Characteristics | Use when |
|---|---|---|---|
| **MAE** (Mean Absolute Error) | avg(\|y - ŷ\|) | Easy to interpret, same unit as target, robust to outliers | All errors matter equally; want a human-readable number |
| **MSE** (Mean Squared Error) | avg((y - ŷ)²) | Penalizes large errors heavily (squares them) | Large mistakes are very bad (e.g., safety-critical predictions) |
| **RMSE** (Root Mean Squared Error) | √MSE | Same unit as target, most commonly reported | Default choice — easy to interpret and sensitive to large errors |
| **MAPE** (Mean Absolute % Error) | avg(\|y - ŷ\| / y) × 100 | Scale-independent, expressed as % | Business communication, comparing accuracy across different SKUs or scales. Fails when actuals are near zero. |
| **R²** (Coefficient of Determination) | 1 - SS_res/SS_tot | % variance explained; 1 = perfect, 0 = predicts the mean, <0 = worse than mean | Comparing models on the same dataset; communicating model fit to stakeholders |

> **Key rule**: RMSE is the default. Use MAE if outliers should not dominate. Use MAPE for business reporting across different scales. Always pair R² with RMSE — R² alone can be misleading.

---

## 3. Generative AI — Text & LLM

Measuring generated text quality is harder than classification — there is rarely one correct answer.

### Automated Metrics (reference-based)

Require a human-written reference answer to compare against.

| Metric | What it measures | Use when |
|---|---|---|
| **BLEU** | N-gram overlap between generated and reference text | Translation, where surface-level wording matters |
| **ROUGE-1/2/L** | Recall-oriented n-gram overlap (ROUGE-L uses longest common subsequence) | Summarization — did the model capture the key content? |
| **BERTScore** | Semantic similarity using embeddings — captures meaning, not just word overlap | When paraphrases should be rewarded; more meaningful than BLEU for most NLP tasks |
| **Perplexity** | How well the model predicts a held-out text — lower = more fluent | Measuring fluency or comparing language models on the same domain; not a measure of correctness |

> **Limitation**: All automated metrics have blind spots. A model can score high BLEU while being factually wrong. Use them for screening, not as the sole quality gate.

### RAG-Specific Metrics

For Retrieval-Augmented Generation systems, two things can fail: the retrieval and the generation.

| Metric | What it measures | Failure mode it catches |
|---|---|---|
| **Context precision** | Are the retrieved chunks actually relevant to the question? | Retriever returning noisy / off-topic chunks |
| **Context recall** | Did retrieval find all the relevant chunks that exist? | Retriever missing key documents |
| **Faithfulness** | Does the generated answer stay within the retrieved context? | LLM hallucinating facts not in the retrieved chunks |
| **Answer relevance** | Is the generated answer relevant to the original question? | LLM going off-topic despite good context |

> Tooling: The **RAGAS** framework implements all four metrics automatically using an LLM-as-judge approach.

### Human Evaluation (gold standard)

Automated metrics are proxies. For production systems, structured human evaluation is required:

| Criterion | What reviewers assess |
|---|---|
| Helpfulness | Does the answer actually solve the user's problem? |
| Factual accuracy | Are the stated facts correct? |
| Coherence | Is the text well-structured and internally consistent? |
| Groundedness | Is the answer supported by the source documents (for RAG)? |

- Run as **A/B win rate**: show two answers side by side, ask which is better — more reliable than absolute ratings
- **LLM-as-judge**: use a capable LLM (e.g., GPT-4) to rate outputs at scale — cost-effective but introduces model bias

---

## 4. Decision Making AI

Decision making AI comes in two distinct forms with different metric sets: classical **RL agents** (trained via reward signals) and **LLM-based agents** (LLMs that plan, call tools, and take multi-step actions at inference time). Evaluate them differently.
see also [[agentic-ai-evaluation]]

### 4a. Reinforcement Learning Agents

RL metrics track the agent's learning progress and final policy quality. Business metrics are always more important than RL-internal metrics.

| Metric | What it measures | Notes |
|---|---|---|
| **Episode return / cumulative reward** | Total reward accumulated per episode | Primary optimization target — is the agent achieving its goal? |
| **Average reward** | Mean reward per time step | For continuous (non-episodic) tasks |
| **Episode length** | Steps taken to reach goal | Shorter is often better (efficiency), but depends on task |
| **Convergence** | Has reward stabilized across training runs? | If reward keeps fluctuating, the policy is unstable |
| **Sample efficiency** | Environment interactions needed to reach target performance | Critical when real-world interaction is expensive or slow |
| **Policy robustness** | Performance under noise, perturbations, or distribution shift | Test with varied environments before deploying |

> **SA rule**: Always define a business metric alongside RL metrics. For energy optimization: cost saved per day. For robotics: pick success rate. RL reward shaping can be gamed — the business metric is the ground truth.

### 4b. LLM-Based Agents

LLM agents plan and execute multi-step tasks using tools (APIs, code execution, search). They are not trained via reward signals — they are evaluated on whether they correctly complete tasks end-to-end. This is harder to measure than classification or RL because tasks are open-ended and the path to success varies.

**End-to-end task metrics** — the most important:

| Metric | What it measures | Use when |
|---|---|---|
| **Task completion rate** | Fraction of assigned tasks the agent completes successfully end-to-end | Primary metric — did the agent actually do what was asked? |
| **Trajectory efficiency** | Number of steps / LLM calls taken vs. optimal path | Agent loops, unnecessary actions, or over-planning are expensive and slow |
| **Human intervention rate** | How often the agent gets stuck and requires human input to continue | Proxy for autonomy level — high rate means the agent cannot be run unsupervised |
| **Error recovery rate** | When a tool call fails or returns unexpected output, does the agent recover and still complete the task? | Robustness — production environments always have noise and partial failures |

**Action-level metrics** — for debugging agent behavior:

| Metric | What it measures | Use when |
|---|---|---|
| **Tool call accuracy** | Did the agent call the right tool with the correct parameters? | Diagnosing whether failures are planning errors or execution errors |
| **Step accuracy** | Were individual reasoning steps or actions correct? | When you have a labeled reference trajectory to compare against |
| **Hallucinated tool calls** | Did the agent invoke tools that don't exist or fabricate tool results? | Critical safety check — a hallucinated API call silently fails or produces wrong output |

**Cost & operational metrics** — always track in production:

| Metric | What it measures | Notes |
|---|---|---|
| **Tokens / cost per task** | Total LLM tokens consumed to complete one task | Agents can be 10–100x more expensive than single-inference models — cost must be scoped upfront |
| **Latency per task** | Wall-clock time from task start to completion | Multi-step agents are slow; set expectations with the business unit early |
| **Success rate under time / budget cap** | Task completion rate when bounded by a token or time limit | Real deployments always have constraints; the unconstrained success rate is misleading |

> **SA rule**: Task completion rate on a representative benchmark is the only metric that matters for go / no-go decisions. Everything else is diagnostic. Define the benchmark tasks *with the business unit* before building — the right tasks are the ones that reflect real workload, not toy examples.

---

## 5. Unsupervised — Clustering

No ground truth labels. Metrics measure internal cluster quality.

| Metric | What it measures | Use when |
|---|---|---|
| **Silhouette score** | How similar a point is to its own cluster vs. the nearest other cluster. Range: -1 to 1, higher = better. | Primary metric for comparing different k values or algorithms without ground truth |
| **Davies-Bouldin Index** | Ratio of within-cluster scatter to between-cluster separation. Lower = better. | Alternative to silhouette when clusters are convex |
| **Inertia (WCSS)** | Sum of squared distances from each point to its cluster centroid | Finding optimal k via the **elbow method** — pick k where inertia stops dropping sharply |
| **Adjusted Rand Index (ARI)** | Agreement between predicted clusters and known ground truth labels. Range: -1 to 1. | When you have some labeled data to validate against |

> **Key rule**: No single metric is definitive for clustering. Use the elbow method (inertia) to narrow down k, then silhouette to pick the best. Always sanity-check cluster contents with domain experts.

---

## 6. Unsupervised — Anomaly Detection

Ground truth is often unavailable (that's why you used unsupervised learning). Evaluation is therefore hard.

| Metric | Use when |
|---|---|
| **Precision@k** | Of the top-k flagged anomalies, how many are real? — most practical: domain expert reviews the top-k alerts | Always start here — it reflects what operations teams actually experience |
| **Recall** | Of all known anomalies, how many did the model flag? | When a labeled set of past incidents exists for validation |
| **ROC-AUC / PR-AUC** | Standard classification metrics applied to anomaly scores | When labeled anomalies are available — PR-AUC preferred due to imbalance |
| **False positive rate** | Fraction of normal events flagged as anomalies | Critical operationally — too many false alarms cause alert fatigue and the system gets ignored |

> **SA rule**: False positive rate is often more business-critical than recall. An anomaly detection system that cries wolf on every shift will be switched off. Define the acceptable false positive rate as a requirement, not an afterthought.

---

## 7. Domain-Specific: Computer Vision

For object detection (YOLO, Faster R-CNN):

| Metric | What it measures |
|---|---|
| **IoU** (Intersection over Union) | Overlap between predicted and ground truth bounding box. Threshold (e.g., 0.5) defines what counts as a correct detection. |
| **mAP** (mean Average Precision) | AP per class at one or more IoU thresholds, averaged across classes. **mAP@0.5** and **mAP@0.5:0.95** are the standard benchmarks. Primary metric for detection models. |
| **Precision / Recall at threshold** | Same as binary classification but per detected object |

For segmentation: **mIoU** (mean Intersection over Union per class) is the standard.

---

## 8. Domain-Specific: NLP Tasks

| Task | Primary metric | Notes |
|---|---|---|
| Text classification | F1 (macro or weighted) | Same as classification section above |
| Named entity recognition | Entity-level Precision, Recall, F1 | Exact span match — a partial entity match counts as wrong |
| Question answering | **Exact Match (EM)** + **Token F1** | EM: is the answer character-for-character correct? Token F1: partial credit for overlapping tokens |
| Translation | BLEU + human eval | BLEU alone is insufficient |
| Summarization | ROUGE-1/2/L + BERTScore | ROUGE measures coverage; BERTScore measures semantic quality |

---

## Use Case Examples

### Predictive AI — Classification

| Use case                                             | Dataset character                  | Right metric                | Why                                                                                                                 |
| ---------------------------------------------------- | ---------------------------------- | --------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| Defect detection on production line                  | Imbalanced, FN costly              | Recall + PR-AUC             | A missed defect ships to the customer — far worse than a false alarm that triggers manual re-inspection             |
| Spam filter                                          | FP costly                          | Precision                   | A legitimate email in the spam folder damages user trust — false alarms are the primary concern                     |
| Fraud detection                                      | Highly imbalanced, FN costly       | PR-AUC + Recall             | Frauds are rare — ROC-AUC looks deceptively good even when most frauds are missed; PR-AUC exposes the real tradeoff |
| Medical screening / disease diagnosis                | FN extremely costly                | Recall                      | Missing a disease is dangerous; accept more false positives (extra tests) over missed diagnoses                     |
| Customer churn prediction                            | FP and FN both costly              | F1                          | Intervention budget is limited — need to balance catching churners vs. wasting budget on false alarms               |
| Fault type classification (type A/B/C/D)             | Multi-class, some rare fault types | Macro F1                    | Treats all classes equally — rare fault types are not drowned out by frequent ones                                  |
| Content moderation (violence + hate speech + nudity) | Multi-label                        | Per-label F1 + Hamming loss | Each label has different business importance and different FP/FN costs — evaluate per label, not in aggregate       |

### Predictive AI — Regression

| Use case | Right metric | Why |
|---|---|---|
| Asset / real estate price prediction | RMSE + R² | RMSE penalizes large errors; R² communicates model fit to non-technical stakeholders |
| Demand forecasting across multiple SKUs | MAPE | Scale-independent — comparing a 10-unit SKU and a 10,000-unit SKU on the same % error metric |
| Remaining useful life (RUL) prediction | MAE + RMSE | MAE gives the average error in hours/days (easy to communicate to maintenance teams); RMSE highlights dangerously large single errors |
| Energy consumption forecast | RMSE | Same unit as the target (kWh) — directly interpretable by the operations team |

### Generative AI

| Use case | Right metric | Why |
|---|---|---|
| Internal Q&A chatbot on company documents (RAG) | RAGAS: faithfulness + context precision/recall + answer relevance | Two independent failure modes: retriever fetches wrong chunks, or LLM hallucinates despite good chunks — both must be evaluated separately |
| Automated meeting / document summarization | ROUGE-L + BERTScore | ROUGE measures content coverage; BERTScore additionally rewards semantically correct paraphrases that ROUGE would penalize |
| Customer service chatbot (no reference answers exist) | LLM-as-judge win rate + human eval | No ground truth to compare against — structured A/B comparison against the previous system is the most reliable signal |
| Code generation | Pass@k | Does the generated code pass the test suite? Correctness is binary — BLEU or ROUGE on code are meaningless |

### Decision Making AI — LLM Agents

| Use case | Right metric | Why |
|---|---|---|
| Process optimization agent (adjusts machine parameters) | Task completion rate + yield improvement | Did the agent find and apply better parameters? The business metric (yield %) is the proof — RL-style metrics don't apply here |
| Document processing agent (extract, classify, route) | Task completion rate + tool call accuracy | Agent must call the right extraction tools in the right order — action-level accuracy pinpoints where the chain breaks down |
| IT helpdesk agent | Task completion rate + human intervention rate + cost per task | Autonomy level and cost per resolved ticket determine whether the agent is economically viable vs. a human |

### Unsupervised

| Use case | Right metric | Why |
|---|---|---|
| Customer segmentation for marketing | Silhouette score + domain expert validation | Silhouette gives a quantitative signal; a marketing expert must confirm the segments are actionable and make business sense |
| Predictive maintenance anomaly detection (no failure labels) | False positive rate + Precision@k | Operators review the top-k alerts per shift — too many false alarms and the system gets ignored regardless of recall |
| Network intrusion detection | PR-AUC + Recall | Attacks are rare (severe imbalance), and a missed intrusion is far costlier than a false alarm |

---

## Quick Reference: Capability → Primary Metric

| Capability | Task | Start with |
|---|---|---|
| Predictive — Classification | Binary, balanced | Accuracy + Confusion matrix |
| Predictive — Classification | Binary, imbalanced | PR-AUC + F1 |
| Predictive — Classification | FN costly (safety, health) | Recall |
| Predictive — Classification | FP costly (alerts, spam) | Precision |
| Predictive — Classification | Multi-class, rare classes matter | Macro F1 |
| Predictive — Regression | Default | RMSE |
| Predictive — Regression | Business reporting | MAPE |
| Generative — LLM | Reference available | BERTScore |
| Generative — RAG | End-to-end quality | RAGAS (faithfulness + relevance) |
| Generative — Production | Gold standard | Human eval / LLM-as-judge win rate |
| Decision making — RL | Learning progress | Episode return + convergence |
| Decision making — RL | Business impact | Domain-specific metric (cost, success rate) |
| Decision making — LLM agent | Go / no-go | Task completion rate on representative benchmark |
| Decision making — LLM agent | Debugging | Tool call accuracy + hallucinated tool calls |
| Decision making — LLM agent | Production operations | Tokens/cost per task + human intervention rate |
| Unsupervised — Clustering | No ground truth | Silhouette score + elbow method |
| Unsupervised — Anomaly detection | Operational | False positive rate + Precision@k |

## Related pages

- [[1 - Overview]]
- [[2 - Framework for new AI use cases - technical and conceptional]]