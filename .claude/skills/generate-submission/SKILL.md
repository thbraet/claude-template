---
name: generate-submission
description: "Generate a Kaggle submission file: loads the best model, predicts on the test set, formats the output CSV, and validates it against the expected submission format."
argument-hint: "<optional: model path, MLflow run ID, or 'best' (default: best)>"
---

# /generate-submission — Kaggle Submission Generator

> **Purpose:** Produce a competition-ready submission file from the best model.
>
> *"The submission file is the deliverable — get the format right."*

## Purpose

This skill loads a trained model, runs predictions on the test set, formats the output as a valid Kaggle submission CSV, and validates it against the expected format (using `gender_submission.csv` as a schema reference). It ensures no missing predictions, correct column names, and valid value ranges.

## Output Location

1. **Submission file**: `submissions/submission_YYYY-MM-DD_HH-MM.csv`
2. **Submission notebook**: `notebooks/generate-submission.ipynb`

## Workflow

### Step 1: Identify Best Model

Based on the argument:

- **Model path provided**: Load from that path directly
- **MLflow run ID provided**: Load model artifact from MLflow
- **"best" or no argument**: Determine the best model by:
  1. Check `docs/crisp-dm/5-evaluation/5.1-evaluate-results.md` for the recommended model
  2. Check `docs/crisp-dm/4-modeling/4.4-model-assessment.md` for the top-ranked model
  3. Search MLflow for the run with the best primary metric
  4. Look for saved models in `models/` directory

If no model can be found, report the issue and ask the user to specify a model path.

### Step 2: Load Model and Test Data

```python
import joblib  # or pickle, or mlflow.sklearn
import pandas as pd

# Load model
model = joblib.load(PROJECT_ROOT / "models" / "best_model.pkl")
# Or: model = mlflow.sklearn.load_model(f"runs:/{run_id}/model")

# Load test data (use the final formatted version)
test = pd.read_csv(PROJECT_ROOT / "data" / "processed" / "test_formatted.csv")

# Load submission template for validation
template = pd.read_csv(PROJECT_ROOT / "data" / "raw" / "..." / "gender_submission.csv")
```

Adapt paths to the actual project structure from `.claude/CLAUDE.md`.

### Step 3: Generate Predictions

```python
# Get feature columns (exclude ID and target columns)
feature_cols = [c for c in test.columns if c not in ["PassengerId", "Survived"]]
X_test = test[feature_cols]

# Predict
predictions = model.predict(X_test)
```

### Step 4: Format Submission

```python
submission = pd.DataFrame({
    "PassengerId": test["PassengerId"].astype(int),
    "Survived": predictions.astype(int)
})
```

### Step 5: Validate Submission

Run these checks before saving:

1. **Row count**: `len(submission)` matches `len(template)` (e.g., 418 for Titanic)
2. **Column names**: Exact match with template columns (case-sensitive)
3. **No missing values**: `submission.isnull().sum().sum() == 0`
4. **Valid values**: All predictions are in the expected set (e.g., {0, 1} for binary classification)
5. **ID completeness**: All expected IDs are present, no duplicates
6. **ID match**: Submission IDs match template IDs exactly

```python
assert len(submission) == len(template), f"Expected {len(template)} rows, got {len(submission)}"
assert list(submission.columns) == list(template.columns), f"Column mismatch"
assert submission.isnull().sum().sum() == 0, "Submission contains null predictions"
assert set(submission["Survived"].unique()).issubset({0, 1}), "Invalid prediction values"
assert submission["PassengerId"].nunique() == len(submission), "Duplicate IDs"
```

If any check fails, report the issue and suggest a fix.

### Step 6: Save Submission

```python
from datetime import datetime

submissions_dir = PROJECT_ROOT / "submissions"
submissions_dir.mkdir(exist_ok=True)

timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
filepath = submissions_dir / f"submission_{timestamp}.csv"
submission.to_csv(filepath, index=False)
```

### Step 7: Generate Notebook

Create `notebooks/generate-submission.ipynb` with:

1. Setup cell (PROJECT_ROOT, imports)
2. Model loading cell
3. Test data loading cell
4. Prediction cell
5. Validation cell (all checks from Step 5)
6. Save cell
7. Markdown summary: model used, prediction distribution, file path

### Step 8: Summary

Report to the user:

```
Submission generated:
  File: submissions/submission_2026-04-01_14-30.csv
  Model: XGBoost (run_abc)
  Rows: 418
  Prediction distribution: 0=262 (62.7%), 1=156 (37.3%)
  Validation: All 6 checks passed ✓
```

Compare prediction distribution with the training set's target distribution as a sanity check. Large deviations may indicate a problem.
