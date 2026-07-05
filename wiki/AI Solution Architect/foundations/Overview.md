
Goal: Getting an overview of the different dimensions of AI from a solution architect's point of view.
AI has several orthogonal dimensions. Assess them in this order — each answer narrows the next:


1. Capability (what does it do?)
- **Predictive AI**: predicts a known outcome from input data
	- classification (output is a category)
		- binary (2 classes: spam / not spam)
			- **Anomaly detection** is binary classification (anomaly / normal) but typically uses an Unsupervised learning paradigm — the model is trained only on normal data and flags deviations, because anomaly labels are rarely available. The capability is still binary classification; the paradigm dimension is what differs.
		- multi-class (N classes, pick 1: cat / dog / bird)
		- multi-label (N classes, pick many: action + comedy + romance)
	- regression (output is a number)
		- single output (predict one number: house price)
		- multiple output (predict several numbers: lat + lng)
- **Generative AI**: creates new content (text, images, video, speech)
	- plain generation: LLM generates from its trained knowledge alone
	- RAG (Retrieval-Augmented Generation): at inference time, relevant documents are fetched from a vector database and injected into the prompt — the LLM then generates grounded in that retrieved context. Same model, same training, different runtime wiring.
- **Decision making AI**: takes sequences of actions to maximise a goal (agents, RL systems) → always implies Reinforcement Learning as the learning paradigm (see dimension 3)

2. Application domain (where is it used / what type of data?)
- **Tabular / structured data**: rows and columns from databases, ERP, CRM — the most common domain in business ML; no spatial or sequential structure, so tree models dominate here
- **Time series**: ordered sequences over time — sensor streams, demand data, financial prices, logs
- **Computer vision**: images, video, 2D/3D scans — detecting, classifying, segmenting visual content → see [[Computer Vision]] for a breakdown of all sub-tasks
- **NLP**: text and documents — classification, generation, extraction, question answering, translation
- **Speech**: audio — speech recognition (speech→text), synthesis (text→speech), speaker identification
- **Graph**: networks of entities and relationships — supply chain tiers, fraud rings, social networks, knowledge graphs; requires Graph Neural Networks (GNNs)
- **Recommendation**: matching users to items or content — collaborative filtering, content-based, hybrid; combines tabular features with embedding models
- **Multi-modal**: combining two or more domains in one model — e.g. vision + language (GPT-4V, CLIP), audio + text; increasingly common with foundation models
- **Code**: a sub-domain of NLP but distinct in practice — code generation, completion, review, debugging (GitHub Copilot, code LLMs)
- **Robotics**: physical systems, motion planning, manipulation — often combines vision, time series, and RL

3. Learning paradigm (how does it learn?)
- **Supervised**: The model learns from labeled examples — every input has a known correct output. You feed it thousands of (input → output) pairs and it learns the mapping. Requires a labeled dataset. Examples: spam classifier trained on emails tagged spam/not-spam; defect detector trained on images tagged defect/good.
- **Unsupervised**: No labels. The model finds structure in the data on its own — clusters, patterns, anomalies. Used when labeling is too expensive or failures are too rare to collect. Examples: clustering customers by behavior; anomaly detection on sensor data where nobody labeled the failures.
- **Self-supervised**: The model generates its own labels from the raw data. A large model is pre-trained on massive unlabeled corpora by predicting hidden parts of the input (e.g., masked words, next token). The result is a general-purpose representation that can be fine-tuned cheaply on a small labeled dataset. Examples: BERT, GPT, and other foundation models are trained this way.
- **Reinforcement Learning**: No dataset at all. An agent learns by taking actions in an environment, receiving rewards or penalties, and adjusting its policy to maximize cumulative reward over time. Requires a simulator or real environment to interact with. → Always the paradigm when capability is Decision making AI. Examples: RL agent that schedules energy loads to minimize cost; robot that learns to pick parts through trial and error.

---

## Foundations reference pages

These pages extend the 4-dimension framework with the additional knowledge an SA needs for solution design:

- [[2b-data-readiness]] — How to assess whether a client's data can support an AI use case (availability, quality, volume, labels, governance, architecture)
- [[solution-architecture-patterns]] — The six recurring end-to-end patterns for deploying AI systems (batch, real-time API, RAG, agentic, human-in-the-loop, edge)
- [[Metrics]] — Evaluation metrics by capability type (classification, regression, generation)
- [[neural-networks]] — Deep dive on neural network architectures (CNN, RNN/LSTM, Transformer, GNN)
- [[Computer Vision]] — All CV sub-tasks mapped to the 4 dimensions

---

4. Model architecture (what is it built with?)
*Architecture is a consequence of the domain (dimension 2) and capability (dimension 1) — not an independent choice.*

Factors to chose a model from:
- data type 
- data volume
- interpretability: trees are explainable why NNs are not
- training time/compute budget
- deployment contraints: running a tiny tree model on a smart watch vs massive NN in the cloud

- **Linear models** (logistic regression, linear regression, ridge, lasso): Use when the dataset is small, the relationship between features and output is roughly linear, or you need maximum interpretability (coefficients are directly readable). Fast to train, easy to explain to business stakeholders, but cannot capture complex interactions without manual feature engineering. Good baseline to beat before reaching for anything more complex.
- **Tree models** (decision tree, random forest, XGBoost, LightGBM): Use for tabular/structured data — the default choice for most business ML problems. Handle mixed feature types, missing values, and non-linear interactions out of the box. XGBoost/LightGBM are state-of-the-art for tabular data and beat neural networks on most structured datasets. Random forest is more robust and less tuning-intensive but slower. Use when data is tabular and you want high accuracy with reasonable explainability (SHAP values).
- **Neural networks**: Use when the input has spatial, sequential, or hierarchical structure that hand-crafted features cannot capture:
  - **CNN** (convolutional neural network): Images, video, 2D signals — learns local spatial patterns (edges, textures, shapes). Use for computer vision tasks.
  - **RNN / LSTM / GRU**: Sequential data where order matters and the model needs memory of past steps — time series, sensor streams. Being replaced by transformers but still practical on edge devices.
  - **Transformer**: Sequences where long-range dependencies matter — text, multi-variate time series, multi-modal data. Foundation of all modern LLMs and increasingly used for time series (TFT, PatchTST). High data and compute requirements.
