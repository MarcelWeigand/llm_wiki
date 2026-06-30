# Neural Network Architectures

**Summary**: A reference table for the five main neural network families — how each works, what data it handles best, and when to reach for it.

**Last updated**: 2026-06-25 (updated)

---

## The Foundation: Multi-Layer Perceptron (MLP)

| | |
|---|---|
| **How it works** | Fully connected layers — every neuron connects to every neuron in the next layer. Input flows forward through weighted connections; activation functions (ReLU, sigmoid) introduce non-linearity so the model can learn complex mappings. |
| **Best data types** | Tabular / structured data — fixed-size feature vectors where spatial or sequential structure does not matter. |
| **When to use** | Simple classification or regression on tabular data when tree models underperform. Also used as the prediction "head" bolted on top of other architectures (e.g., after a CNN has extracted image features, an MLP maps them to the final output). Rarely the right primary architecture — [[tree-models]] (XGBoost) beat MLPs on most pure tabular tasks. |

---

## Convolutional Neural Networks (CNN)

| | |
|---|---|
| **How it works** | Small learnable filters (kernels) slide across the input detecting local patterns — edges, textures, shapes — at every spatial position. Pooling layers reduce resolution and increase receptive field. Stacking layers builds a hierarchy from low-level (edges) to high-level (objects) features. Spatially efficient: far fewer parameters than an MLP on the same input. |
| **Best data types** | Images, video, 2D scans, spectrograms (audio treated as a 2D image). Any data with **local spatial structure** where nearby values are correlated. |
| **When to use** | Default architecture for all [[Computer Vision]] tasks — classification, detection, segmentation, anomaly detection. Preferred on edge/embedded devices where Transformers are too heavy. Still competitive when labeled data is limited (pre-trained ImageNet CNNs fine-tune well on small datasets). |

---

## Recurrent Neural Networks (RNN) / LSTM / GRU

| | |
|---|---|
| **How it works** | Processes sequences **one step at a time**, passing a hidden state forward at each step — that state acts as memory of what came before. **LSTM** adds three gates (forget, input, output) to control what the network remembers or discards over long sequences, solving the vanishing gradient problem of plain RNNs. **GRU** is a lighter version of LSTM with two gates — similar performance, faster to train. |
| **Best data types** | Time series, sensor streams, financial sequences, speech audio. Text and NLP (legacy — now dominated by Transformers). Any sequential data where **order and history matter** but compute is constrained. |
| **When to use** | When you need sequence modeling on edge or resource-constrained hardware where Transformers are too expensive. Still practical for short sequences or real-time streaming. For new projects with sufficient compute, prefer Transformers — they outperform RNNs on almost every sequence task and are easier to scale. |

---

## The Modern Standard: Transformers

| | |
|---|---|
| **How it works** | Uses **self-attention**: every position in the sequence attends to every other position simultaneously, learning which parts are most relevant to each other — in parallel, not step-by-step. No recurrence. A separate positional encoding injects order information. Scales extremely well: more data + more compute = reliably better models. Pre-trained on massive unlabeled corpora (self-supervised), then fine-tuned cheaply on task-specific data. |
| **Best data types** | Text and NLP (native domain). Multi-variate time series (TFT, PatchTST). Images when global context matters (Vision Transformer — ViT). Multi-modal inputs (vision + language: CLIP, GPT-4V). Code. |
| **When to use** | When **long-range dependencies** matter — relationships between distant parts of the input. The foundation of all modern LLMs and most state-of-the-art models. Default for NLP. Use ViT for vision when accuracy outweighs inference cost. Requires significantly more data and compute than CNNs or RNNs — not ideal for small datasets without a pre-trained checkpoint to fine-tune from. |

---

## For Relationships: Graph Neural Networks (GNN)

| | |
|---|---|
| **How it works** | Operates directly on **graph-structured data** (nodes + edges). Each node iteratively aggregates feature information from its neighbors — after several rounds of message passing, each node's representation encodes both its own features and its local graph context. Different GNN variants (GCN, GAT, GraphSAGE) differ in how they weight neighbor contributions. |
| **Best data types** | Any data where **relationships between entities are as important as the entities themselves**: supply chain networks, fraud rings, molecular structures, knowledge graphs, social networks, recommendation graphs. |
| **When to use** | When the problem is fundamentally about connectivity — predicting properties of nodes, edges, or entire graphs. Standard architectures (MLP, CNN, Transformer) cannot naturally represent arbitrary graph topology. If your data can be represented as a table or sequence, use a simpler architecture first. Reach for GNNs only when the relational structure is a core part of the signal. |

---

## Quick Comparison

| Architecture | Core mechanism | Natural data | Compute cost |
|---|---|---|---|
| MLP | Fully connected layers | Tabular, feature vectors | Low |
| CNN | Local spatial filters | Images, video, 2D signals | Low–Medium |
| RNN / LSTM / GRU | Step-by-step hidden state | Time series, sequences (legacy) | Low–Medium |
| Transformer | Global self-attention | Text, time series, images, multi-modal | High |
| GNN | Neighbor message passing | Graphs, networks, molecules | Medium–High |

## When to use neural networks on structured/tabular data

The default rule is: **tree models first** (XGBoost, LightGBM) for tabular data. They outperform neural networks in most real-world tabular settings — faster to train, more robust to missing values, less sensitive to hyperparameters.

Override to neural networks when one or more of these conditions holds:

**1. Very large datasets (millions+ rows)**
Tree models plateau in performance as data grows. Neural networks continue to improve with scale. Past ~1–5M rows the performance gap often reverses in the NN's favor.

**2. High-cardinality categorical features**
Features like `product_id`, `user_id`, or `zip_code` with tens of thousands of unique values are poorly handled by tree models (sparse one-hot encoding, limited generalization across unseen values). Neural networks can learn **entity embeddings** — dense vectors that capture semantic similarity between categories.

**3. Multi-modal input (tabular + text or image)**
When structured features need to be combined with unstructured data in a single model, end-to-end neural training is the only option. Common pattern: XGBoost on tabular + BERT on text → ensemble. If tight coupling matters, a unified NN is cleaner.

**4. Sequential / temporal structure across rows**
Standard tabular models assume rows are i.i.d. If rows have ordering that matters (patient visit history, machine operational log), architectures like TabTransformer or FT-Transformer can capture inter-row dependencies that tree models cannot.

**5. Component in a larger differentiable system**
When the tabular model must participate in end-to-end gradient flow — a surrogate model in Bayesian optimization, a state encoder in a reinforcement learning agent, or a differentiable layer in a multi-task network — it must be a neural network. Tree models are not differentiable.

---

**Specialist tabular NN architectures**: TabNet, FT-Transformer, SAINT — designed specifically for tabular data and can narrow or close the gap with tree models on some benchmarks. Still not universally better; benchmark on your data before committing.

---

## Related pages

- [[Overview]]
- [[Computer Vision]]
- [[Algorithms]]