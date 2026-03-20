---
name: fairness-audit
description: Generate a fairness/bias audit for a model across protected attributes. Use during CRISP-DM Evaluation before deployment decisions.
argument-hint: "[model] [protected attributes]"
user-invocable: true
---

# Fairness Audit (CRISP-DM Phase 5)

Audit model fairness for: $ARGUMENTS

Generate Python code that:
1. Load model predictions and test data with protected attributes
2. Compute metrics per subgroup:
   - Demographic Parity (prediction rates across groups)
   - Equalized Odds (TPR and FPR across groups)
   - Calibration (predicted probability accuracy across groups)
   - Disparate Impact Ratio (should be > 0.8 per four-fifths rule)
3. Visualize: bar charts of metrics across groups, ROC curves per group
4. Flag violations with severity ratings
5. Suggest mitigations (threshold adjustment, resampling, fairness constraints)
6. Generate a summary suitable for the model card

Use Fairlearn if available, otherwise implement metrics directly with sklearn.
