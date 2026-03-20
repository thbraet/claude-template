---
name: experiment-setup
description: Configure MLflow or Weights & Biases experiment tracking for a project. Use at the start of CRISP-DM Modeling phase.
argument-hint: "[mlflow|wandb]"
user-invocable: true
---

# Experiment Tracking Setup (CRISP-DM Phase 4)

Set up experiment tracking using: $ARGUMENTS (default: mlflow)

Generate:
1. Configuration file (mlflow_config.py or wandb_config.py) with:
   - Project name, experiment name
   - Tracking URI (local or remote)
   - Artifact storage location
2. Training wrapper function that auto-logs:
   - All hyperparameters
   - All metrics (train + validation)
   - Dataset version/hash
   - Code version (git commit SHA)
   - Random seeds
   - Environment info (Python version, key package versions)
   - Model artifacts
   - Feature importance plots
3. requirements.txt additions
4. Example usage in a training script
