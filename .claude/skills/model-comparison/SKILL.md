---
name: model-comparison
description: Compare multiple experiments from experiment tracking. Use during CRISP-DM Evaluation to select the best model.
argument-hint: "[experiment names or IDs]"
user-invocable: true
---

# Model Comparison (CRISP-DM Phase 5)

Compare experiments: $ARGUMENTS

Generate a comparison report including:
1. **Leaderboard table**: All models ranked by primary metric
2. **Multi-metric comparison**: Radar chart of key metrics per model
3. **Complexity vs Performance**: Plot of model complexity (params, inference time) vs accuracy
4. **Statistical significance**: Paired t-test or Wilcoxon test between top models
5. **Resource comparison**: Training time, memory usage, inference latency
6. **Recommendation**: Which model to deploy and why (considering performance, complexity, interpretability, and business requirements)

If MLflow is configured, query the tracking server. Otherwise, read from reports/ directory.
