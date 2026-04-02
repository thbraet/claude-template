---
paths:
  - "**/*"
---
# Model Governance

- Every production model must have a model card (use /model-card to generate)
- Model cards must include: intended use, limitations, training data, metrics, fairness assessment
- All experiments must be tracked in MLflow/W&B -- no unlogged training runs
- Model artifacts must be versioned in a model registry (MLflow Model Registry, etc.)
- Fairness metrics must be computed across protected groups before deployment
- A monitoring plan is required before any model goes to production
- Document retraining triggers and cadence
- Maintain a rollback plan for every deployed model
- Model performance must be compared against the current production baseline, not just other experiments
- Data drift and prediction drift must be monitored post-deployment
