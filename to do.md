- integrate workflow for calibration use cases


## 1. Data Split (The 3-Way Split)


Instead of a normal train/test split, you must split your data into three distinct sets:

- **Training Set (60%):** Used to train the core machine learning model.
    
- **Validation/Calibration Set (20%):** Used strictly to tune the calibration layer.
    
- **Test Set (20%):** Kept completely hidden in a vault until the very end to get an honest final score.
    

## 2. Train the Core Model

- Train your chosen algorithm (e.g., Random Forest, XGBoost) using the **Training Set**.
    
- _Note:_ Do not worry about its raw probabilities yet; just focus on getting it to rank and separate the data well.
    

## 3. Apply the Calibration Layer

- Pass the trained core model and the **Validation/Calibration Set** into a calibrator (like Scikit-Learn's `CalibratedClassifierCV`).
    
- The calibrator learns how to map the core model's warped confidence scores to true empirical percentages based on this fresh data.
    

## 4. Final Evaluation (The Brier Score)

- Generate probabilities for your completely unseen **Test Set** using the newly calibrated model.
    
- Calculate the **Brier Score** on these test predictions to mathematically verify that the outputted percentages accurately match real-world frequencies.
    

## 5. Calculate Expected Value / Business Logic

- Feed these calibrated percentages directly into your business formulas (e.g., $\text{Probability of Default} \times \text{Loan Value}$) to make financially sound, risk-adjusted decisions.


Traditional ML workflow

![[Pasted image 20260712231438.png]]


## 1. Data Split (The Standard 2-Way Split)

Because you don’t need a separate step to fix the probabilities, you only need to split your data into two sets:

- **Training Set (80%):** Used to train the model and tune its hyperparameters.
    
- **Test Set (20%):** Kept completely hidden to evaluate the final model.
    

## 2. Train the Core Model

- Train your chosen algorithm (e.g., Random Forest, XGBoost, Logistic Regression) on the **Training Set**.
    
- Optimize the model to maximize sorting and ranking power, using metrics like **ROC-AUC** during cross-validation.
    

## 3. Establish the Decision Threshold (Tuning)

- Instead of calibrating the percentages, look at your validation performance to find the optimal **Threshold** cutoff (the line between 0 and 1).
    
- Slide the threshold up or down to hit your target **Precision** or **Recall** goals based on business costs (e.g., lowering the threshold to catch more fraud).
    

## 4. Final Evaluation (Traditional Metrics)

- Run your model on the unseen **Test Set** using your chosen decision threshold.
    
- Calculate **F1-Score, Precision, Recall, or Accuracy** on the final 0 and 1 predictions to confirm the model makes the right choices on new data.
    

## 5. Deploy the Automated Action

- Deploy the model into production. The system takes the raw model output, applies the hard threshold, and instantly triggers the automated binary action (e.g., `If risk > threshold -> Block Transaction`).