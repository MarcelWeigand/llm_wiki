
AI use case for sales: price optimization

Goal: 
suggesting a price that protects the company's profit margins while maximizing the likelihood of winning the deal

Input data:
buyer-facing transaction features: _Customer Segment, Region, Product Type, Order Volume,_ and the _Final Offered Price_.
other ideas:
- CRM data (customer communication, customer sentiment, transcripts, emails)
- historic sales data
- customer classification, scores
- external finance data (inflation, market indices, currencies)
- raw material prices
- inventory levels




How it works?
- **Step A:** It generates a range of possible prices (e.g., checking every $100 interval between a minimum cost floor and a maximum ceiling).
    
- **Step B:** It passes each of those price options into your trained model one by one to get their respective win probabilities.
    
- **Step C:** It multiplies each price's profit margin by its model-predicted win probability to calculate the **Expected Profit**.
    
- **Step D:** It selects the single price that achieved the highest score.

![[Pasted image 20260706145634.png]]

Risks
- don't include margin into your training data or other internal costs as this is not what the buyer knows and sees, therefore not relevant for the output

- ### 1. Data Leakage via Margin Features

- **Risk:** Including internal costs or profit margins as training inputs to the machine learning model. Because Margin=Price−Cost, feeding this to the classifier introduces a logical redundancy that degrades the model’s ability to predict clean probabilities.
    
- **Mitigation:** Keep the machine learning model strictly "blind" to internal corporate finance metrics during training. Keep cost and margin calculations entirely external in the secondary optimization script.
    

### 2. Blind Spot on Raw Material and Supply Volatility

- **Risk:** The machine learning model might predict a high win probability for a historically popular price point, unaware that the spot price of a raw material (like steel or microchips) has recently spiked, causing an automated price recommendation to inadvertently erode your actual margin.
    
- **Mitigation:** Integrate live enterprise data streams (ERP and supply chain indexes) directly into the _external optimization equation_. If production costs surge, the optimization loop automatically shifts its cost baseline upward, instantly lifting the final recommended price ceiling.
    

### 3. Erosion of Strategic Client Relationships

- **Risk:** Relying purely on an algorithm can cause the system to suggest hyper-aggressive prices to historically loyal accounts, ignoring long-standing strategic partnerships or non-quantifiable human negotiation dynamics.
    
- **Mitigation:** Implement a strict **"Human-in-the-Loop" guardrail**. The AI should never push prices directly to clients; instead, it acts as an advisory co-pilot, presenting optimized targets alongside transparent data explanations to sales leaders who retain final approval authority.


training the model
- first explore which are the signals then use the features for training 
- which features work good?
- verify sales expertise, which hypothesis to verify

