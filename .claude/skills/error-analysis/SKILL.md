---
name: error-analysis
description: Generate an error analysis notebook for a trained model. Use during CRISP-DM Modeling to understand where and why the model fails.
argument-hint: "[model path or description]"
user-invocable: true
---

# Error Analysis (CRISP-DM Phase 4)

Generate an error analysis notebook for: $ARGUMENTS

Include sections for:
1. **Overall Performance**: Confusion matrix / residual distribution
2. **Worst Predictions**: Top 20 largest errors with full feature values
3. **Error by Subgroup**: Performance broken down by key categorical features
4. **Error by Feature Range**: Performance across quantiles of numeric features
5. **Temporal Analysis**: Is performance stable over time or degrading?
6. **Confidence Analysis**: Calibration curve, prediction probability distribution
7. **Cluster Analysis**: Cluster the errors -- are there systematic patterns?
8. **Feature Importance for Errors**: What features correlate with large errors?
9. **Recommendations**: Suggested improvements (more data, new features, different model, etc.)
