

Idea: have one reusable wiki for AI in manufacturing

1. Show potentials in manufacturing 
2. link to what we have done 
3. generate ideas and structure them (use framework)
4. assess, prioritze ideas

to dos: 
- link to merantix use cases 
- where does CAD optimization fit in?
- rule 1: AI is only as good as feasibility allows depending on whether we have data and, if so, in what condition --> may need to prepare data first
- opportunities and risks of breaking down data silos, and how is that done? build a data lake
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

These are your classic five main areas. They align with the organizational structure of the company (who pays for the project?).

1. **Predictive Maintenance (Maintenance & Asset Management)**
    
2. **Quality Control (Quality Management & Scrap Reduction)**
    
3. **Supply Chain & Logistics (Procurement, Warehousing & Sales Planning)**
    
4. **Knowledge Management (Engineering & HR / Organization)**
    
5. **Sustainability (Energy Management & Resource Efficiency)**


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

| Category                                                | Goal                                                                                                                                                                                                                                                                                                                        | Dimension 2: Function      | Dimension 3: AI Technology                                                                                                                 |
| -------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Early fault detection (anomaly detection)          | The AI raises an alarm as soon as a machine behaves "strangely," before something actually breaks. It's the digital fever check.                                                                                                                                                                                          | descriptive                | _Anomaly detection on time series & sensor data._ Often uses autoencoders (deep learning); unsupervised |
| Remaining useful life prediction (RUL)   | The exact calculation of the remaining time until a component fails (e.g. "This bearing has 42 operating hours left")                                                                                                                                                                                              | predictive                 | supervised, predictive regression models                                                                                                   |
| Fault classification                                    | Not just knowing _that_ something is going to break, but _what_ exactly the problem is.                                                                                                                                                                                                                                           | descriptive & prescriptive | supervised, classification models                                                                                                          |
| *Prescriptive Maintenance* | *The AI not only predicts the fault but directly delivers the solution or intervenes itself*                                                                                                                                                                                                                         | *prescriptive*             |                                                                                                                                            |
| Maintenance assistant                                       | A technician stands in front of a complex packaging machine showing a rare error code. He asks an internal tablet system by voice for the solution. The AI searches through thousands of pages of PDF manuals and old shift logs and answers in natural language with a step-by-step guide | prescriptive & generative  | GenAI/RAG                                                                                                                                  |


### 2. Supply Chain & Logistics

Goal: this area is primarily about optimizing the flow of materials, information, and capital. The organizational goal is to **ensure delivery capability while minimizing inventory and transportation costs**. Here AI mainly helps synchronize external uncertainties (market, weather, suppliers) with internal logistics processes.


| Use case                                                                            | Description                                                                                                                                                                                                                                                                                              |  Dimension 2: Function                       | Dimension 3: AI Technology                                                                                                                                                                                                                                                                                                                         |
| -------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| (Probabilistic) Demand forecasting                                         | AI forecasts future customer demand not as a fixed number, but as a probability distribution, to calculate optimal safety stock levels in the warehouse.                                                                                                                               | predictive               | _Probabilistic time series forecasting._ Algorithms used include Amazon DeepAR, quantile regression, or specialized neural networks (such as Temporal Fusion Transformers) that output distribution parameters ($\mu$, $\sigma$).                                                                     |
| Supplier reliability / Estimated Time of Arrival (ETA) prediction          | AI monitors global supply chains and predicts the exact arrival date of raw materials. It takes into account not only the supplier's schedule but also external data such as port congestion, weather conditions on shipping routes, or border controls                                        | Predictive | predictive, supervised ML models                                                                                                                                                                                                                                                                                                        |
| Automated goods-receipt inspection of delivery notes and freight documents | When trucks deliver materials, hundreds of documents (often international, in various languages and formats) must be matched against actual orders in the ERP system. An AI reads these documents (including scanned or handwritten ones) fully automatically and posts the goods | Descriptive              | _Natural Language Processing (NLP) & Computer Vision._ Specifically, this is **Intelligent Document Processing (IDP)**, combining Optical Character Recognition (OCR) with layout-aware language models (such as LayoutLM) or modern multimodal LLMs to semantically understand tables and text on documents. |

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


| Use case                                                       | Description                                                                                                                                                                                                                                                                 | Dimension 2: Function            | Dimension 3: AI Technology                                                                                                                                                     |
| ------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Automated optical inspection of parts            |                                                                                                                                                                                                                                                                                 | descriptive | computer vision                                                                                                                                                     |
| Predictive quality control / in-process inspection | While a component is being cast, the AI records all process parameters (casting temperature, pressure, humidity, cooling time). Before the part has even cooled, the AI predicts whether invisible inclusions (porosity) have formed inside the metal. | predictive  | _Classification / regression on multivariate time series data._ Algorithms used include Random Forests, Gradient Boosting (XGBoost), or neural networks |

### 4. Knowledge Management

Goal: make isolated knowledge from technical manuals, documentation, and ERP systems automatically retrievable and accessible.
The organizational goal here is not to repair machines or inspect products, but to **secure and structure the company's entire intellectual capital and make it instantly usable for employees**. In times of skilled-labor shortages and demographic change (loss of knowledge as experts retire), this is a major lever in manufacturing.


| Use case                                                                              |     |     |     |
| ------------------------------------------------------------------------------------- | --- | --- | --- |
| Automated patent and technology research for the R&D team                      |     |     |     |
| Automated reading and structuring of shift logs and handover reports |     |     |     |
| AI-supported onboarding and training system for new factory employees              |     |     |     |
| Company-wide "expert finder" (who knows what?)                                       |     |     |     |

### 5. Sustainability

Goal: **minimize CO₂ footprint, energy consumption, and material waste while complying with strict environmental regulations**. Here AI mainly helps uncover hidden waste in complex energy systems.

| Use case                                                                    | Description                                                                                                                                                                                                                                                                                               |  Dimension 2: Function                        | Dimension 3: AI Technology                                                                                                                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Energy consumption forecasting                                                        | AI predicts the factory's electricity or gas consumption for the next hours, days, or weeks. It combines the current production plan (which machines run when?) with external factors such as weather forecasts (cooling/heating needs of the halls) and historical consumption patterns | Predictive                | Time series forecasting. Just like sales or component forecasting, multivariate time series algorithms are used here (e.g. LightGBM, Prophet, or deep learning approaches such as LSTMs), as they excellently capture the temporal trend and external influences. |
| AI-supported "peak shaving" (peak load management)                              |                                                                                                                                                                                                                                                                                                               | Predictive & Prescriptive | _Time series forecasting & mathematical optimization._ Time series forecasting models (e.g. LSTMs or LightGBM) are used                                                                                                                                                                                                                           |
| Intelligent energy-efficiency control of HVAC systems (heating, ventilation, air conditioning) | The AI dynamically regulates ventilation and heating by combining current outdoor weather, the number of employees in the hall, and the waste heat from running machines.                                                                                                                               | Prescriptive              | _Reinforcement learning or model-based predictive control (MPC)._ The AI learns through trial and error in a simulation how the hall behaves thermally, in order to issue optimal control commands.                                                                           |

## MxM Use Cases

Incoming use case ideas, classified according to the framework (Dimension 1–3), before being finally sorted into the respective domain table above.

| Use Case                                                        | Description                                                                                                              | Dimension 1: Domain                     | Dimension 2: Function     | Dimension 3: AI Method                                                            |
| ------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------- | ---------------------------- | ---------------------------------------------------------------------------------------- |
| AI-based CAD optimization                                     | Spatially evaluate 3D geometries, check them against corporate norms & design guidelines, and generate new CAD proposals  | Knowledge Management (Engineering)              | Descriptive & Generative     | Computer vision (3D geometry analysis) + GenAI (CAD generation)                          |
| Early warning system for process anomalies & root cause analysis | Continuous monitoring of process data, alerting on deviations, automated root cause analysis                | Predictive Maintenance                       | Descriptive / Diagnostic     | Anomaly detection on time series (autoencoder, unsupervised)                             |
| Cycle time optimization in production processes                | Analysis of cycle times and bottlenecks, recommendation of optimal process parameters to increase throughput               | Predictive Maintenance (process/equipment)      | Prescriptive                 | Reinforcement learning / operations research (mathematical optimization)                 |
| AI solution for detecting vehicle damage                    | Automated visual detection of body damage (dents, scratches, etc.)                                             | Quality Control                              | Descriptive / Diagnostic     | Computer vision                                                                           |
| AI-based R&D assistant for consumption reports (RAG)        | Assistant searches and synthesizes internal consumption reports for the R&D team in natural language                 | Knowledge Management                            | Generative                   | NLP / GenAI (RAG)                                                                         |
| Digital bill of quantities (offer management, RAG)         | AI structures bills of quantities and automatically supports offer/quote creation                           | Knowledge Management                            | Generative & Prescriptive    | NLP / GenAI (RAG)                                                                         |
| Automatic damage detection (generic)                          | Automated visual damage detection, e.g. on components, packaging, or returns                                  | Quality Control                              | Descriptive / Diagnostic     | Computer vision                                                                           |
| Probabilistic demand forecasting                                | Demand forecast as a probability distribution to optimize safety stock levels                              | Supply Chain & Logistics                     | Predictive                   | Time series forecasting (DeepAR, quantile regression, Temporal Fusion Transformer)        |

**Open points / edge cases:**
- *CAD optimization*: resolves your existing to-do ("where does CAD optimization fit in?") — it lands in Knowledge Management, because it operationalizes engineering knowledge (norms/guidelines) rather than product quality on the workpiece itself.
- *Cycle time optimization*: doesn't fit cleanly into one of the 5 domains, since it relates to the production process as a whole rather than a single asset. Alternative: list it as a subcategory of Predictive Maintenance ("process" instead of "machine"), or add a sixth domain "Production/Process Optimization" if more such cases come up.
- *Vehicle damage detection* vs. *automatic damage detection*: these may be the same use case at different maturity/scope (car-specific vs. generic). Check whether they should be merged.
- *Digital bill of quantities*: also touches Supply Chain & Logistics (offer/contract management with suppliers) — currently placed under Knowledge Management, since the core mechanism is automated document knowledge retrieval.
- *Probabilistic demand forecasting* is essentially identical to the existing "(Probabilistic) Demand forecasting" entry in the Supply Chain table above — should be merged/deduplicated there rather than tracked separately.
