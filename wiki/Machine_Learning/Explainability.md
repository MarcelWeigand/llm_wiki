# Model Explainability

**Summary**: Tools and techniques for understanding how and why a model makes decisions — covering global vs local methods, SHAP, LIME, and feature importance.

**Last updated**: 2026-06-27

---

## 1. What is Model Explainability?

A machine learning model is a function: it takes inputs (features) and produces an output (prediction).  
But **why** does it make a specific prediction?

**Model Explainability (XAI — Explainable AI)** is the set of tools and techniques that help humans understand *how* and *why* a model makes decisions.

### Why does it matter?

| Scenario | Why you need explainability |
|---|---|
| Medical diagnosis | Doctors need to understand predictions before acting on them |
| Loan approval | Regulators require reasons for rejected applications |
| Fraud detection | Teams need to verify the model isn't using spurious patterns |
| Debugging | A model with 99% accuracy but wrong reasoning will fail in production |

---

### Two Types of Explainability

```
GLOBAL Explainability              LOCAL Explainability
─────────────────────────          ─────────────────────────
"How does the model work           "Why did the model predict
 overall across all data?"          THIS for THAT specific input?"

Tools: Feature Importance,         Tools: SHAP waterfall,
       Permutation Importance,             SHAP force plot,
       Partial Dependence Plots,           LIME
       SHAP summary plot
```

**Methods overview:**

1. **MDI Feature Importance** — the built-in Random Forest score, fast but biased, how much each feature reduces uncertainty (Gini impurity) across all trees.
2. **Permutation Importance** — shuffles each feature and measures accuracy drop; more reliable
3. **Partial Dependence Plots** — shows the _shape_ of how a feature affects predictions (linear? threshold?)
    ![[Pasted image 20260626173924.png|348]]

4. **SHAP Summary Plot** — global view of all features across all test samples.

    **SHAP (SHapley Additive exPlanations)** is based on a concept from cooperative game theory (Shapley values).
    The idea: treat each feature as a *player* and the prediction as the *payoff*. How much does each player *contribute*?

    **Key concepts**

    | Term | Meaning |
    |---|---|
    | **Base value** | The model's average prediction across all training data (the starting point) |
    | **SHAP value** | How much a feature *pushes* the prediction up or down from the base value |
    | **Final prediction** | Base value + sum of all SHAP values |

    **Why SHAP is better than MDI**

    - Works for **any model** (not just trees)
    - Provides **both global AND local** explanations from the same framework
    - Handles **feature interactions** correctly
    - Has strong theoretical guarantees (consistency, local accuracy, missingness)

local explainability:
5. **SHAP Waterfall Plot** — local: shows exactly how each feature pushed one prediction away from the base value
6. **SHAP Force Plot** — same info in a compact horizontal view
7. **LIME** — model-agnostic local explanation using a local linear approximation
    **Advantage:** Works for any model (truly model-agnostic), including neural networks, XGBoost, etc.  
    **Disadvantage:** Approximation — results can be unstable across runs and depend on the perturbation strategy.  

    **When to use LIME vs SHAP:**
    - Use **SHAP** when you have a tree-based model (faster, exact, theoretically grounded)
    - Use **LIME** for black-box models where you can only call `predict_proba`
		
