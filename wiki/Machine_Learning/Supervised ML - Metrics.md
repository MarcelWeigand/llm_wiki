
# Supervised ML — Metrics

**Summary**: Regression and classification metrics — MAE, MSE, RMSE, R² for regression; precision, recall, and F1 for classification; and metrics specific to unbalanced datasets.

**Last updated**: 2026-06-27

---

## Classification

- binary 
- multi label
- ...
## Regression

Metrics of Regression algorithms

| Mean Absoute Error (MAE)                                                      | Mean Squared Error (MSE)                                                   | Root Mean Squared Error (RMSE)            | R² (Coefficient of Determination)                                                                                       |
| ----------------------------------------------------------------------------- | -------------------------------------------------------------------------- | ----------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| ![[Pasted image 20260515221200.png]]                                          | ![[Pasted image 20260515221227.png]]                                       | ![[Pasted image 20260515221246.png]]      |                                                                                                                         |
| - Average absolute error<br>- Easy to understand                              | - Penalizes large errors heavily                                           | Same unit as target → easier to interpret | Interpretation:<br>- % of variance explained<br><br>Caveat:<br>- Can be misleading<br>- Doesn’t reflect business impact |
| Use when:<br>- All errors matter equally<br>- You want robustness to outliers | Use when:<br>- Large mistakes are very bad (e.g., fraud amount prediction) | Most commonly used in practice,           |                                                                                                                         |

## Unbalanced Datasets - Metrics

![[Pasted image 20260522143420.png]]
