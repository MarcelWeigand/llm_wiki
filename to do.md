- integrate workflow for calibration use cases
- ## 1. Data Split (The 3-Way Split)

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