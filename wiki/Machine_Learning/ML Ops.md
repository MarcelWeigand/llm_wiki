
# MLOps

**Summary**: The practices and tooling for making ML systems reliable, reproducible, and maintainable in production — covering the full lifecycle from data management to monitoring.

**Last updated**: 2026-06-27

---

Goal: make ML systems reliable, reproducible, and maintainable in production

---

# ML Ops Lifecycle

![[Pasted image 20260522095857.png]]

---

## 1. Data Management and versioning

- Raw data changes over time. Without versioning, you can't reproduce a past training run or debug why a model suddenly behaves differently.
- The core practices are: version datasets like code, validate schemas before training, and track data lineage

---

## 2. Experiment tracking

- Every training run should be reproducible: the same code + data + hyperparameters must produce the same model
- you can compare 50 runs visually in the MLflow UI (`mlflow ui`) and pick the best one


```python
# --- Experiment tracking with MLflow ---
# pip install mlflow scikit-learn

import mlflow
import mlflow.sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score

X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Every run gets its own entry: params, metrics, artifacts
with mlflow.start_run(run_name="rf_baseline"):
    # Log hyperparameters
    params = {"n_estimators": 100, "max_depth": 5, "random_state": 42}
    mlflow.log_params(params)

    model = RandomForestClassifier(**params)
    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    metrics = {
        "accuracy": accuracy_score(y_test, preds),
        "f1_macro": f1_score(y_test, preds, average="macro"),
    }
    mlflow.log_metrics(metrics)

    # Log the model itself as an artifact
    mlflow.sklearn.log_model(model, artifact_path="model")
    print(f"Run logged — accuracy: {metrics['accuracy']:.3f}")
```

---

## 3. Feature Store

- ensures the features computed during training are identical to those served at inference time

---

## 4. Model registry and versioning

- A model registry is the single source of truth for "what is in production and why". 
- Models move through stages: `Staging → Production → Archived`

```python
# --- Model registry with MLflow ---

import mlflow
from mlflow.tracking import MlflowClient

client = MlflowClient()

# After a successful training run, register the model
run_id = "abc123"  # from mlflow.start_run()
model_uri = f"runs:/{run_id}/model"

registered = mlflow.register_model(model_uri, name="iris_classifier")
print(f"Registered version {registered.version}")

# Promote to Staging after automated tests pass
client.transition_model_version_stage(
    name="iris_classifier",
    version=registered.version,
    stage="Staging",
    archive_existing_versions=False,
)

# Promote to Production after human approval / canary tests
client.transition_model_version_stage(
    name="iris_classifier",
    version=registered.version,
    stage="Production",
    archive_existing_versions=True,   # auto-archives the old prod version
)

# Loading the current production model anywhere:
prod_model = mlflow.sklearn.load_model("models:/iris_classifier/Production")
```

---
## 5. CI/CD

![[Pasted image 20260522165103.png]]
Further triggers for pipeline 1: 

- scheduled retraining 
- drift alert fired
- new labelled data 
- manual trigger

---

## 6. Model Serving

- **how requests reach your model and how predictions come back**

- synchronous REST (real-time predictions)
- asynchronous batch (overnight scoring)
- streaming (Kafka-based pipelines)

![[Pasted image 20260522170348.png]]


|           | What container does?                                                                                                                                                                                                                                                                                             | How it's triggered?           | When to use?                                                                                                                                                                                                                                                                                                                                                                                |
| --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Online    | container runs constantly,<br>caller sends one request to HTTP endpint and waits for response (synchronously), FAST API pattern                                                                                                                                                                                  | other service sending request | fraud check at checkout, recommendation on page load, credit score at loan application,<br>--> anything whre result needs to come back before next step can happen                                                                                                                                                                                                                          |
| Batch     | scheduler fires up container, feeds it million rows and model scores all of them, results gets written back somewhere, container shuts down<br>(async)                                                                                                                                                           | by scheduler                  | score all customers for marketing campaign, run risk scoring on all open loans every morning,<br>--> answer doesn't need to be instant                                                                                                                                                                                                                                                      |
| Streaming | between the two, container runs constantly<br>events arrive continously on a queue, container consumes them one by one (or in micro-batches), scores each event and published to topic<br>within milliseconds, without a caller waiting for response --> just process what is flowing through the pipe<br>(sync) | by queue messages             | - high continous demand:<br>events arrive constantly at scale, not in bursts on demand. Thousands of transactions per second, not a few hundred API calls per minute<br>- you dont need to block the orignal action, the system that sends the event can continue without waiting for the prediction<br>- if the event needs to be consumed not only by ml model but also by other services |
|           |                                                                                                                                                                                                                                                                                                                  |                               |                                                                                                                                                                                                                                                                                                                                                                                             |
When to use what?

![[Pasted image 20260522172330.png]]


Further streaming use cases:
![[Pasted image 20260522172052.png]]



---
## 7. Monitoring & drift detection

- You need to detect two kinds of drift: 
	- data drift (the input distribution shifts) 
	- concept drift (the relationship between inputs and labels changes)

---

## 8. Governance, lineage & fairness

