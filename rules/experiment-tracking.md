---
paths:
  - "notebooks/4.*.ipynb"
  - "notebooks/4*.ipynb"
  - "src/model*.py"
  - "src/train*.py"
---
# Experiment Tracking

- Every modeling notebook must log to MLflow (or the configured tracker) — no unlogged training runs
- Each experiment run must include: run name, model type, all hyperparameters, and at least one evaluation metric
- Use descriptive run names that encode the experiment intent (e.g., "xgb-tuned-depth6-lr01", not "run_42")
- Log the data version (DVC hash or file checksum) alongside every run
- Log feature lists so you can trace which features each model used
- Tag runs with the CRISP-DM task (e.g., "4.3-baseline", "4.3-candidate-tuned")
- Never overwrite or delete prior experiment runs — append new runs for comparison
- Log training duration and resource usage (memory, CPU/GPU) for cost estimation
- Save model artifacts (pickled models, ONNX exports) as MLflow artifacts, not loose files
