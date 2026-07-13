

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


## 2.2 Probablistic demand forecasting

### The Challenge: The Failure of Deterministic (Single-Point) Forecasting

Traditional AI and legacy engines generate a **deterministic forecast**—a single-point prediction (e.g., _"We will sell exactly 500 units of SKU-A next Tuesday"_).

In reality, a single number is almost always wrong. In manufacturing, treating a forecast as a single absolute metric creates severe vulnerabilities:

1. **Under-forecasting:** Triggers catastrophic stockouts, idle production floors, and lost market share.
    
2. **Over-forecasting:** Bloats warehouse costs, ties up millions in dead working capital, and leads to expired or obsolete stock.
    
3. **Safety Stock Guesswork:** Planners end up applying arbitrary safety buffers (e.g., adding a flat 15% to everything), completely undermining the precision of the AI.


### How it works? 
### Step 1: The AI Model Evaluates Demand Uncertainty

The AI model takes in your raw inputs (historical sales, seasonality, promotions) and outputs a probability distribution. It might tell you:

- There is a 90% chance demand will be at least **400 units**.
    
- There is a 50% chance demand will be **500 units**.
    
- There is only a 10% chance demand will reach **700 units**.

**you do not typically feed cost data directly into the AI forecasting model itself.** The forecasting model's sole job is to understand the physics of demand—analyzing historical sales, weather, and marketing data to predict _what_ people want and _how uncertain_ that prediction is. It does not need to know the price of steel or the cost of warehouse rent to do that.

### Step 2: The Optimization Engine Evaluates the Costs

This is where your financial metrics are introduced. You feed your cost parameters directly into the Optimization Engine (often built into your Advanced Planning & Scheduling (APS) or ERP system).

The engine evaluates two primary financial metrics:

1. **Cost of Understocking (Cu​):** The penalty for not having enough inventory. This includes lost profit margins, expedited shipping fees to rush an order, or contractual penalties for late delivery.
    
2. **Cost of Overstocking (Co​):** The penalty for making too much. This includes warehouse storage costs, capital tied up in inventory, and the risk of the product spoiling or becoming obsolete.

Once the optimization engine has the probability distribution from the AI and the cost metrics from your finance team, it uses a classic operations research formula known as the **Critical Ratio** (or Newsvendor Formula) to find the mathematically optimal service level (SL):

SL=Cu​+Co​Cu​​

This ratio outputs a percentage (e.g., 0.82 or 82%). The system then looks at the AI’s probabilistic distribution and selects the exact production volume that corresponds to the **P82** mark.


### Two Examples of How This Plays Out:

- **Scenario A: High-Margin Medical Equipment**
    
    - **The Costs:** Stocking out costs a massive Cu​=$10,000 (lost high-profit sale + damaged client relationship). Storing an extra unit costs a tiny Co​=$100.
        
    - **The Math:** 10000+10010000​=99%
        
    - **The Decision:** The system targets the **P99** forecast. It overrides the median expectation and orders a massive amount of inventory because the financial penalty of running out far outweighs the cost of storage.
        
- **Scenario B: Perishable/Short Shelf-Life Dairy Products**
    
    - **The Costs:** If you run out, a customer buys another brand (Cu​=$2). If you overproduce, the milk spoils and you throw it away (Co​=$4).
        
    - **The Math:** 2+42​=33%
        
    - **The Decision:** The system targets the **P33** forecast. It intentionally under-produces relative to the average demand because throwing away spoiled inventory is financially worse than missing a few minor sales.