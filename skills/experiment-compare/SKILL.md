---
name: experiment-compare
description: "Compare two or more MLflow experiment runs side-by-side: metrics, hyperparameters, feature importance, and training performance. Produces a comparison table and recommendation."
argument-hint: "<run IDs, run names, or 'latest N' to compare recent runs>"
---

# /experiment-compare — MLflow Experiment Comparison

> **Purpose:** Side-by-side comparison of experiment runs to support model selection.
>
> *"Never pick a model based on a single metric — compare systematically."*

## Purpose

This skill loads MLflow experiment runs and produces a structured comparison across metrics, hyperparameters, feature sets, and training characteristics. It helps identify the best-performing model and understand what drove performance differences.

## Output Location

1. **Comparison notebook**: `notebooks/experiment-comparison.ipynb` — full comparison with visualizations
2. **Summary**: printed in conversation

## Workflow

### Step 1: Identify Runs to Compare

Based on the argument:

- **Run IDs provided**: Load those specific runs from MLflow
- **Run names provided**: Search MLflow for matching run names
- **"latest N"**: Load the N most recent runs from the active experiment
- **No argument**: Load all runs from the active experiment, present a numbered list, and ask the user which to compare

```python
import mlflow

# List available experiments
experiments = mlflow.search_experiments()
# List runs in the active experiment
runs = mlflow.search_runs(order_by=["start_time DESC"])
```

If MLflow is not configured or no runs exist, check for:
- Saved model artifacts in `models/` or `reports/`
- Results logged in `docs/crisp-dm/4-modeling/4.3-model-building.md`
- Results in modeling notebooks (`notebooks/4.3-*.ipynb`)

Fall back to manual comparison from these sources if MLflow is unavailable.

### Step 2: Extract Run Data

For each run, extract:

1. **Parameters**: All hyperparameters logged
2. **Metrics**: All evaluation metrics (accuracy, F1, AUC, RMSE, etc.)
3. **Tags**: Model type, CRISP-DM task, data version
4. **Artifacts**: Feature importance files, confusion matrices, model files
5. **Metadata**: Start time, duration, status, user

### Step 3: Build Comparison Tables

**Metrics comparison** (sorted by primary metric):

| Run | Model | Accuracy | F1 | AUC | Precision | Recall | Train Time |
|---|---|---|---|---|---|---|---|
| run_abc | XGBoost | 0.847 | 0.821 | 0.889 | 0.835 | 0.808 | 12.3s |
| run_def | LogReg | 0.812 | 0.789 | 0.861 | 0.801 | 0.778 | 0.4s |

**Hyperparameter comparison** (highlight differences):

| Parameter | run_abc | run_def | Different? |
|---|---|---|---|
| max_depth | 6 | N/A | — |
| learning_rate | 0.1 | N/A | — |
| C | N/A | 1.0 | — |

**Overfit assessment** (train vs validation gap):

| Run | Train Acc | Val Acc | Gap | Risk |
|---|---|---|---|---|
| run_abc | 0.923 | 0.847 | 0.076 | Moderate |
| run_def | 0.819 | 0.812 | 0.007 | Low |

### Step 4: Feature Importance Comparison

If feature importance is logged:
- Compare top-10 features across models
- Highlight features that are important in one model but not another
- Flag features that rank very differently across models (may indicate instability)

### Step 5: Generate Comparison Notebook

Create `notebooks/experiment-comparison.ipynb` with:

1. Setup cell (imports, MLflow connection, PROJECT_ROOT)
2. Run loading and data extraction
3. Metrics comparison table (styled DataFrame)
4. Bar chart: metrics side-by-side
5. Hyperparameter diff table
6. Overfit gap analysis
7. Feature importance comparison (if available)
8. Markdown conclusion cell with recommendation

### Step 6: Recommendation

Based on the comparison, provide a justified recommendation:
- Which model performs best on the primary metric?
- Which model has the best generalization (smallest train/val gap)?
- Which model is simplest (Occam's razor — prefer simpler if performance is close)?
- Are there trade-offs to discuss with stakeholders?

Present as: *"Recommended: [model] because [reason]. However, [trade-off] — discuss with stakeholders if [condition]."*
