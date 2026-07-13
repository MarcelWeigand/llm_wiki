

Idea: have one reusable wiki for AI in manufacturing

1. Show potentials in manufacturing 
2. link to what we have done 
3. generate ideas and structure them (use framework)
4. assess, prioritze ideas

to dos: 

- rule 1: AI is only as good as feasibility allows depending on whether we have data and, if so, in what condition --> may need to prepare data first
- have the AI summarize MxM use cases according to a defined structure --> langdoc agent
	- Business problem 
	- Solution: high-level technical description of the technologies. Input and output of the model in the solution
	- Risks and how they were mitigated
	- Learnings


### Areas in manufacturing where AI can be applied to

![[Pasted image 20260705104017.png]]

### Framework to structure AI initiatives in manufacturing

![[Pasted image 20260705112711.png|635]]

### Dimension 1: The Domain (Where does it happen?)

These are your six main areas. The first five align with the organizational structure of the company (who pays for the project?); the sixth, Production/Process Optimization, was added to capture use cases that operate on the production process itself — cycle times, throughput, machine settings — rather than on a single asset (Predictive Maintenance), the finished product (Quality Control), or the flow of goods (Supply Chain).

1. **Predictive Maintenance (Maintenance & Asset Management)**
    
2. **Quality Control (Quality Management & Scrap Reduction)**
    
3. **Supply Chain & Logistics (Procurement, Warehousing & Sales Planning)**
    
4. **Knowledge Management (Engineering & HR / Organization)**
    
5. **Sustainability (Energy Management & Resource Efficiency)**
    
6. **Production/Process Optimization (Process Engineering & Operations)**


### Dimension 2: The Function / Time Horizon (What does the AI do?)

This is where we solve the problem of overlaps. No matter which domain you're in, at its core the AI always does one of four things. This helps you cluster the subcategories cleanly:

- **Descriptive / Diagnostic (Detect & Understand):** What is happening right now and why? _(e.g. visual defect detection in quality control OR anomaly detection on a machine)._
    
- **Predictive (Forecast):** What will happen in the future? _(e.g. demand forecasting in the supply chain OR remaining useful life in maintenance)._
    
- **Prescriptive (Optimize / Recommend):** What is the best course of action? _(e.g. optimal changeover schedule in production OR automatic furnace temperature adjustment for sustainability)._
    
- **Generative (Create):** Generate new knowledge or documents. _(e.g. AI assistant searching maintenance manuals in knowledge management)._


### Dimension 3: The AI Method (Which tool is used?)

These are the mathematical "hats" the AI wears. **Important:** a method can be used in _any_ domain. That's why pure method lists are so confusing.

- **Time Series Forecasting:** DeepAR, ARIMA, LSTMs.
    
- **Computer Vision:** CNNs, object detection.
    
- **Natural Language Processing (NLP) / GenAI:** Large Language Models (LLMs), RAG systems.
    
- **Reinforcement Learning / Operations Research:** Mathematical optimization algorithms


### 1. Predictive Maintenance (Machine Condition)

Goal: reduce downtime through optimized maintenance. Avoidance of **machine downtime**.
**Predictive Maintenance** looks at the **machine** (the operating asset). The goal is to keep the equipment running (availability).

Typical data: continuous sensor data (vibration, current, temperature of the machine).

| Category                                  | Goal                                                                                                                                                                                                                                                                                       | Dimension 2: Function      | Dimension 3: AI Technology                                                                              |
| ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------- | ------------------------------------------------------------------------------------------------------- |
| Early fault detection (anomaly detection) | The AI raises an alarm as soon as a machine behaves "strangely," before something actually breaks. It's the digital fever check.                                                                                                                                                           | descriptive                | _Anomaly detection on time series & sensor data._ Often uses autoencoders (deep learning); unsupervised |
| Remaining useful life prediction (RUL)    | The exact calculation of the remaining time until a component fails (e.g. "This bearing has 42 operating hours left")                                                                                                                                                                      | predictive                 | supervised, predictive regression models                                                                |
| Fault classification                      | Not just knowing _that_ something is going to break, but _what_ exactly the problem is.                                                                                                                                                                                                    | descriptive & prescriptive | supervised, classification models                                                                       |
| *Prescriptive Maintenance*                | *The AI not only predicts the fault but directly delivers the solution or intervenes itself*                                                                                                                                                                                               | *prescriptive*             |                                                                                                         |
| Maintenance assistant                     | A technician stands in front of a complex packaging machine showing a rare error code. He asks an internal tablet system by voice for the solution. The AI searches through thousands of pages of PDF manuals and old shift logs and answers in natural language with a step-by-step guide | prescriptive & generative  | GenAI/RAG                                                                                               |
| Visual equipment monitoring               | Cameras continuously watch equipment for visible signs of wear or damage — leaks, corrosion, belt tears, broken components — catching issues before they cause a stoppage.                                                                                                                 | descriptive                | Computer vision (object detection, visual anomaly detection) combined with time-series sensor data      |
| Digital twin visual feedback              | Camera feeds are fused with sensor data to keep a digital twin of the shop floor in sync with real production status, surfacing discrepancies as they happen.                                                                                                                              | descriptive                | Computer vision (multi-camera tracking, sensor fusion)                                                  |

*Source: [[catalog-manufacturing]] — see "Predictive Maintenance Through Visual Monitoring" and "Digital Twin Visual Feedback" in the Computer Vision table, and the "Predictive Maintenance" deep dive for the full anomaly-detection → RUL architecture.*


### 2. Supply Chain & Logistics

Goal: this area is primarily about optimizing the flow of materials, information, and capital. The organizational goal is to **ensure delivery capability while minimizing inventory and transportation costs**. Here AI mainly helps synchronize external uncertainties (market, weather, suppliers) with internal logistics processes.

Typical data: transactional ERP/MES records (customer orders, historical sales, inventory levels, supplier delivery history), logistics and freight documents (delivery notes, invoices — often scanned or multilingual), plus external signals (weather, port congestion, news feeds).


| Use case                                                                   | Description                                                                                                                                                                                                                                                                                                                                 | Dimension 2: Function      | Dimension 3: AI Technology                                                                                                                                                                                                                                                                                                                                         |
| -------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| (Probabilistic) Demand forecasting                                         | AI forecasts future customer demand not as a fixed number, but as a probability distribution, to calculate optimal safety stock levels in the warehouse. The same forecast feeds production planning: SKU-level forecasts are reconciled bottom-up/top-down to product-family and plant level to drive scheduling and material procurement. | predictive                 | _Probabilistic time series forecasting._ Algorithms used include Amazon DeepAR, quantile regression, or specialized neural networks (such as Temporal Fusion Transformers) that output distribution parameters ($\mu$, $\sigma$). For simpler tabular demand data, gradient boosted trees (XGBoost, LightGBM) with lag/calendar features are a common alternative. |
| Supplier reliability / Estimated Time of Arrival (ETA) prediction          | AI monitors global supply chains and predicts the exact arrival date of raw materials. It takes into account not only the supplier's schedule but also external data such as port congestion, weather conditions on shipping routes, or border controls                                                                                     | Predictive                 | predictive, supervised ML models                                                                                                                                                                                                                                                                                                                                   |
| Automated goods-receipt inspection of delivery notes and freight documents | When trucks deliver materials, hundreds of documents (often international, in various languages and formats) must be matched against actual orders in the ERP system. An AI reads these documents (including scanned or handwritten ones) fully automatically and posts the goods                                                           | Descriptive                | _Natural Language Processing (NLP) & Computer Vision._ Specifically, this is **Intelligent Document Processing (IDP)**, combining Optical Character Recognition (OCR) with layout-aware language models (such as LayoutLM) or modern multimodal LLMs to semantically understand tables and text on documents.                                                      |
| Inventory and warehouse monitoring                                         | Cameras track inventory levels, pallets, containers, and material movement — e.g. automatically counting finished goods as they leave a production line.                                                                                                                                                                                    | Descriptive                | Computer vision (object tracking, object counting, OCR)                                                                                                                                                                                                                                                                                                            |
| OCR for labels, serials & barcodes                                         | Reads labels, serial numbers, barcodes, QR codes, and batch/lot numbers directly off products and packaging for traceability and compliance (e.g. verifying every package has the correct lot number and expiry date).                                                                                                                      | Descriptive                | Computer vision (OCR, image classification, text recognition)                                                                                                                                                                                                                                                                                                      |
| Robotic guidance & pick-and-place                                          | Helps robots locate randomly oriented parts in a bin and pick the correct one — used for kitting, order picking, and warehouse automation.                                                                                                                                                                                                  | Descriptive & Prescriptive | Computer vision (3D vision, stereo cameras, object detection, pose estimation)                                                                                                                                                                                                                                                                                     |
| Supply chain risk prediction                                               | Predicts supplier delays, shortages, or logistics disruptions by combining structured ERP data (financials, delivery history, single-source flags) with NLP signal extraction from news feeds.                                                                                                                                              | Predictive                 | Gradient boosting classifiers + graph-based analytics (supplier network) + NLP (BERT/LLM) on news                                                                                                                                                                                                                                                                  |

*Source: [[catalog-manufacturing]] — see "Inventory and Warehouse Monitoring," "OCR for Manufacturing Documents," "Robotic Guidance and Pick-and-Place," and "Supply Chain Risk Prediction" in the Computer Vision / Time Series tables, plus the "Demand Forecasting & Production Planning" and "Supply Chain Risk Detection" deep dives.*

#### 2.1 Demand forecasting

Areas of application:
- across the entire value chain

1.) Product development & market launch
- **Initial demand / market acceptance:** How quickly is the new product adopted by customers?
    
- **Ramp-up curve:** How fast does demand rise in the first weeks after launch?
    
- **Supplier material availability:** How reliable are the delivery times of new suppliers for critical components?

2.) Maturity phase & series production

- **Primary demand (customer orders):** The exact weekly or monthly sales volume of the end product.
    
- **Secondary demand (component & raw material consumption):** How many screws, cables, or tons of steel are consumed (derived from the sales forecast)?
    
- **Capacity and machine utilization:** How many hours will the equipment be occupied?
    
- **Scrap rates (yield):** What percentage of parts will be defective in production (important for calculating the material buffer)?

3.) Product phase-out

- **Residual demand (last time buy):** How many end products do retailers or customers still want to order one last time before production stops?
    
- **Inventory drawdown rate:** How quickly are existing stocks consumed, to minimize the risk of costly write-offs (scrapping)?

4.) After-sales & maintenance

- **Spare parts demand (MRO):** When and where will components fail due to wear?
    
- **Return and complaint rates:** How many defective parts come back to the factory for repair?


### 3. Quality Control

Goal: increase **product** quality. Avoidance of **scrap & complaints**.
**Quality Control** looks at the **product** (the workpiece). The goal is to deliver a defect-free product (quality).

Typical data: camera images, 3D scans, dimensions, surface characteristics of the product.


| Use case                                           | Description                                                                                                                                                                                                                                            | Dimension 2: Function | Dimension 3: AI Technology                                                                                                                                                                    |
| -------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Automated optical inspection of parts              | Cameras inspect products for defects — scratches, cracks, dents, missing components, incorrect assembly, paint defects, surface contamination — as they move along the line.                                                                           | descriptive           | Computer vision (object detection, image classification, semantic segmentation, anomaly detection — e.g. fine-tuned YOLO/Mask R-CNN, or PatchCore/Autoencoder for a good-parts-only baseline) |
| Predictive quality control / in-process inspection | While a component is being cast, the AI records all process parameters (casting temperature, pressure, humidity, cooling time). Before the part has even cooled, the AI predicts whether invisible inclusions (porosity) have formed inside the metal. | predictive            | _Classification / regression on multivariate time series data._ Algorithms used include Random Forests, Gradient Boosting (XGBoost), or neural networks                                       |
| Assembly verification                              | Vision system checks that a product is assembled correctly — right part, right orientation, no missing screws, wiring connected properly — before it moves to the next station.                                                                        | descriptive           | Computer vision (object detection, image comparison, instance segmentation)                                                                                                                   |
| In-line process monitoring                         | Cameras observe a process in real time (e.g. metal casting, injection molding, food production) and flag abnormalities as they occur, rather than only inspecting the finished part.                                                                   | descriptive           | Computer vision (video analytics, real-time anomaly detection)                                                                                                                                |
| Yield prediction                                   | Predicts whether a production batch will meet quality specifications before the process finishes, so out-of-spec batches can be caught or corrected early (e.g. wafer yield in semiconductor fabs).                                                    | predictive            | Gradient boosting (XGBoost, LightGBM), Random Forest, neural networks                                                                                                                         |

*Source: [[catalog-manufacturing]] — see "Automated Quality Inspection," "Assembly Verification," and "Process Monitoring" in the Computer Vision table, "Yield Prediction" in the Time Series table, and the "Visual Quality Inspection / Defect Detection" deep dive for the full architecture (edge inference, active learning loop, dataset imbalance challenges).*

### 4. Knowledge Management

Goal: make isolated knowledge from technical manuals, documentation, and ERP systems automatically retrievable and accessible.
The organizational goal here is not to repair machines or inspect products, but to **secure and structure the company's entire intellectual capital and make it instantly usable for employees**. In times of skilled-labor shortages and demographic change (loss of knowledge as experts retire), this is a major lever in manufacturing.

Typical data: unstructured text and documents (technical manuals, PDFs, shift logs and handover reports, patents, engineering guidelines/norms), plus structured records from ERP/PLM systems and CAD/engineering files.


| Use case                                                              | Description                                                                                                                                                                                                                                       | Dimension 2: Function    | Dimension 3: AI Technology                                                          |
| --------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------ | ----------------------------------------------------------------------------------- |
| Automated patent and technology research for the R&D team             | An assistant scans patent databases and technical literature, summarizes relevant prior art, and flags competing or conflicting patents so engineers can assess freedom-to-operate without manually reading hundreds of filings.                  | Descriptive & Generative | NLP / GenAI (semantic search + RAG over patent corpora, summarization)              |
| Automated reading and structuring of shift logs and handover reports  | The AI reads free-text shift logs and handover notes, extracts structured events (incidents, machine states, actions taken), and makes them searchable so the next shift and management retain what happened without re-reading raw notes.        | Descriptive & Generative | NLP / GenAI (information extraction, entity recognition, summarization)             |
| AI-supported onboarding and training system for new factory employees | A conversational assistant answers new-hire questions from work instructions, SOPs, and safety documents, and generates role-specific training material and quizzes — shortening ramp-up time and easing the loss of retiring experts' knowledge. | Generative               | NLP / GenAI (RAG over internal documentation, content generation)                   |
| Company-wide "expert finder" (who knows what?)                        | The AI indexes documents, tickets, and project records to map which employees have worked on which topics, so anyone can quickly find the right internal expert for a specific problem or machine.                                                | Descriptive              | NLP / GenAI (semantic search, entity linking, knowledge graph over people ↔ topics) |
| Improve CAD creation from norms and guidelines                        | The AI checks 3D geometries against corporate norms and design guidelines and generates new or corrected CAD proposals, operationalizing engineering rules that would otherwise live only in experts' heads.                                      | Generative               | Computer vision (3D geometry analysis) + GenAI (CAD/image generation)               |
| Generating BOMs out of RfQs                                           | The AI reads incoming requests for quotation (RfQs) — often unstructured documents — and drafts a structured bill of materials (BOM) to accelerate and standardize offer/quote creation.                                                          | Descriptive & Generative | NLP / GenAI (document understanding + RAG, structured extraction)                   |

*Note: [[catalog-manufacturing]] currently only covers Computer Vision and Time Series & Structured Data use cases — it has no NLP/GenAI section yet, so nothing from the catalog maps here. The R&D assistant and digital bill-of-quantities ideas in the MxM Use Cases table below are the main candidates to backfill this domain.*

### 5. Sustainability

Goal: **minimize CO₂ footprint, energy consumption, and material waste while complying with strict environmental regulations**. Here AI mainly helps uncover hidden waste in complex energy systems.

Typical data: energy meter readings (electricity, gas) and load profiles, machine setpoints and production schedules, building/HVAC sensor data (temperature, occupancy), plus external weather forecasts and energy price signals.

| Use case                                                                                       | Description                                                                                                                                                                                                                                                                              | Dimension 2: Function     | Dimension 3: AI Technology                                                                                                                                                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Energy consumption forecasting                                                                 | AI predicts the factory's electricity or gas consumption for the next hours, days, or weeks. It combines the current production plan (which machines run when?) with external factors such as weather forecasts (cooling/heating needs of the halls) and historical consumption patterns | Predictive                | Time series forecasting. Just like sales or component forecasting, multivariate time series algorithms are used here (e.g. LightGBM, Prophet, or deep learning approaches such as LSTMs), as they excellently capture the temporal trend and external influences.                                                                                                           |
| AI-supported "peak shaving" (peak load management)                                             | Shifts flexible loads (heating, compressors, batch processes) away from expensive peak-price windows without impacting production throughput.                                                                                                                                            | Predictive & Prescriptive | _Time series forecasting & mathematical optimization._ A demand forecast (LSTM/LightGBM) feeds either a reinforcement learning agent or a classical mixed-integer linear program (MILP) that schedules flexible loads against price forecasts and production constraints — MILP is more interpretable and constraint-safe, RL handles more complex stochastic environments. |
| Intelligent energy-efficiency control of HVAC systems (heating, ventilation, air conditioning) | The AI dynamically regulates ventilation and heating by combining current outdoor weather, the number of employees in the hall, and the waste heat from running machines.                                                                                                                | Prescriptive              | _Reinforcement learning or model-based predictive control (MPC)._ The AI learns through trial and error in a simulation how the hall behaves thermally, in order to issue optimal control commands.                                                                                                                                                                         |

*Source: [[catalog-manufacturing]] — see "Energy Consumption Optimization" in the Time Series table and the "Energy Consumption Optimization" deep dive (MILP vs. RL scheduling, safety-constraint handling).*

### 6. Production/Process Optimization

Goal: run the production process itself at its economic optimum. Avoidance of **lost throughput and process waste** (idle time, suboptimal cycle times, off-spec settings).
**Production/Process Optimization** looks at the **process** (the parameter set / recipe that runs across one or more machines to produce output) — distinct from Predictive Maintenance (the machine's health), Quality Control (the finished product), and Supply Chain (the flow of goods).

Typical data: MES process logs, machine setpoints (temperature, pressure, speed, feed rate), cycle-time and throughput counters, quality/yield outcomes per run.

| Use case                                                | Description                                                                                                                                                                            | Dimension 2: Function     | Dimension 3: AI Technology                                                                                                                                                                                                                  |
| ------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Cycle time optimization                                 | Analysis of cycle times and bottlenecks, recommendation of optimal process parameters to increase throughput                                                                           | Prescriptive              | Reinforcement learning / operations research (mathematical optimization)                                                                                                                                                                    |
| Process parameter optimization / throughput forecasting | Recommends optimal machine settings (temperature, pressure, speed, feed rate) to maximize throughput and minimize defects, and forecasts how many units a line will produce in a shift | Predictive & Prescriptive | A surrogate model (gradient boosted trees or a feedforward neural network) learns parameters → quality/yield/throughput, then Bayesian optimization (BoTorch/Optuna) or a reinforcement learning agent searches it for the optimal settings |

*Source: [[catalog-manufacturing]] — see "Process Optimization" and "Production Throughput Forecasting" in the Time Series table, and the "Process Parameter Optimization (Digital Twin)" deep dive for the surrogate-model architecture and multi-objective trade-off challenges.*

## MxM Use Cases

Incoming use case ideas, classified according to the framework (Dimension 1–3), before being finally sorted into the respective domain table above.

| Use Case                                                        | Description                                                                                                              | Dimension 1: Domain                     | Dimension 2: Function     | Dimension 3: AI Method                                                            |
| ------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------- | ---------------------------- | ---------------------------------------------------------------------------------------- |
| AI-based CAD optimization                                     | Spatially evaluate 3D geometries, check them against corporate norms & design guidelines, and generate new CAD proposals  | Knowledge Management (Engineering)              | Descriptive & Generative     | Computer vision (3D geometry analysis) + GenAI (CAD generation)                          |
| Early warning system for process anomalies & root cause analysis | Continuous monitoring of process data, alerting on deviations, automated root cause analysis                | Predictive Maintenance                       | Descriptive / Diagnostic     | Anomaly detection on time series (autoencoder, unsupervised)                             |
| AI solution for detecting vehicle damage                    | Automated visual detection of body damage (dents, scratches, etc.)                                             | Quality Control                              | Descriptive / Diagnostic     | Computer vision                                                                           |
| AI-based R&D assistant for consumption reports (RAG)        | Assistant searches and synthesizes internal consumption reports for the R&D team in natural language                 | Knowledge Management                            | Generative                   | NLP / GenAI (RAG)                                                                         |
| Digital bill of quantities (offer management, RAG)         | AI structures bills of quantities and automatically supports offer/quote creation                           | Knowledge Management                            | Generative & Prescriptive    | NLP / GenAI (RAG)                                                                         |
| Automatic damage detection (generic)                          | Automated visual damage detection, e.g. on components, packaging, or returns                                  | Quality Control                              | Descriptive / Diagnostic     | Computer vision                                                                           |
| Probabilistic demand forecasting                                | Demand forecast as a probability distribution to optimize safety stock levels                              | Supply Chain & Logistics                     | Predictive                   | Time series forecasting (DeepAR, quantile regression, Temporal Fusion Transformer)        |
| Worker safety monitoring                                | Detects unsafe situations on the shop floor — missing PPE (helmets, glasses), workers entering hazardous zones, unsafe behavior around machinery | *No domain fit — see open point below* | Descriptive / Diagnostic | Computer vision (person detection, PPE detection, pose estimation) |

**Open points / edge cases:**
- *CAD optimization*: resolves your existing to-do ("where does CAD optimization fit in?") — it lands in Knowledge Management, because it operationalizes engineering knowledge (norms/guidelines) rather than product quality on the workpiece itself.
- *Cycle time optimization* and *process parameter optimization / throughput forecasting* have moved out of this table into the new **Production/Process Optimization** domain (§6) above, since two independent catalog use cases pointed at the same gap.
- *Worker safety monitoring* (from [[catalog-manufacturing]]): still doesn't fit any of the 6 domains — it's an EHS/compliance concern, not maintenance, quality, supply chain, knowledge, sustainability, or process optimization. Candidate for a future "Health & Safety" domain if more safety-related use cases come up; parked here until then.
- *Vehicle damage detection* vs. *automatic damage detection*: these may be the same use case at different maturity/scope (car-specific vs. generic). Check whether they should be merged.
- *Digital bill of quantities*: also touches Supply Chain & Logistics (offer/contract management with suppliers) — currently placed under Knowledge Management, since the core mechanism is automated document knowledge retrieval.
- *Probabilistic demand forecasting* is essentially identical to the existing "(Probabilistic) Demand forecasting" entry in the Supply Chain table above — should be merged/deduplicated there rather than tracked separately.

---
### Data Types

#### OT Data (Operational Technology)

This is the raw, real-time data generated on the actual factory floor. It is inherently physical and fast-moving

- **Examples:** Machine telemetry, vibration data, temperature readings from sensors, pressure metrics, PLCs (Programmable Logic Controllers), SCADA systems, and industrial camera feeds used for visual quality checks.
- **AI Value:** This data tells the AI the current _physical state_ of your machines (e.g., _"Bearing temperature on Line 3 just spiked by 15 degrees"_)

#### IT Data (Information Technology)

This is the transactional and administrative data that manages the business side of the manufacturing company.

- **Examples:** Enterprise Resource Planning (ERP) data (like SAP or Oracle), Manufacturing Execution Systems (MES), supply chain logs, customer orders, shift schedules, and maintenance histories
- **AI Value:** This data provides the _business context_. It tells the AI things like, _"Line 3 is currently running a rush order for our most important client, and the operator on duty is a trainee"_

#### ET Data (Engineering Technology)

This is the design, structural, and simulation data created during the product development and factory planning phases.

- **Examples:** Computer-Aided Design (CAD) files, Product Lifecycle Management (PLM) schemas, material specifications, and 3D simulation/digital twin data.
- **AI Value:** This data provides the _ideal baseline specifications_. It tells the AI, _"According to the original engineering blueprint, this specific alloy should never exceed 180°C during stamping"

---

## Pain Points in manufacturing 

- Combining enterprise data (SAP) with manufacturing data from different systems using different data models/schemas/formats