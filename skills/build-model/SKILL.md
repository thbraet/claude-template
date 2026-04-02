---
name: build-model
description: "CRISP-DM 4.3 — Build Model. Guides the construction of baseline and candidate models, including data pipeline setup, training, hyperparameter tuning, and experiment logging. Produces training code artifacts and a structured model building report in docs/crisp-dm/4-modeling/."
argument-hint: "<optional: specific model to build, technique name, or tuning question>"
---

# /build-model — CRISP-DM 4.3: Build Model

> **Phase:** 4. Modeling | **Task:** 4.3 Build Model
>
> *"Run the modeling tool on the prepared dataset to create one or more models. With any modeling tool, there are often a large number of parameters that can be adjusted. List the parameters and their chosen values, along with the rationale for the choice."*

## Purpose

This skill guides the systematic construction of models: starting with the baseline, then building candidate models with default and tuned hyperparameters. Every run is logged to MLflow. It produces both executable code and a structured report documenting what was built and how.

## Output Location

This skill produces two artifacts plus model artifacts:

1. **Jupyter notebook** (primary): `notebooks/4.3-model-building.ipynb` — contains all model training code, hyperparameter tuning, experiment logging, inline outputs, and markdown narrative. This is the working artifact where models are built and evaluated.
2. **Summary document**: `docs/crisp-dm/4-modeling/4.3-model-building.md` — a structured summary of the model building report extracted from the notebook. This is the CRISP-DM documentation artifact.
3. **Model artifacts**: logged to MLflow and/or `models/`

## Workflow

### Step 1: Check for Existing Artifacts

Before starting, check if output artifacts already exist:
- Check for `notebooks/4.3-model-building.ipynb` (the primary notebook)
- Check for `docs/crisp-dm/4-modeling/4.3-model-building.md` (the summary document)
- If either exists, present what's found and ask: *"A model building [notebook/report/both] already exists. Do you want to (1) update it with new experiments, (2) start fresh, or (3) skip this step?"*
- If neither exists, proceed to Step 2.

Also check if prerequisite documents exist:
- Read `docs/crisp-dm/4-modeling/4.1-modeling-techniques.md`
  - If it exists, use it — it defines which techniques to build and their preprocessing requirements.
  - If it does not exist, warn: *"No modeling technique selection found (task 4.1). It's strongly recommended to complete 4.1 first. Proceed anyway?"*
- Read `docs/crisp-dm/4-modeling/4.2-test-design.md`
  - If it exists, use it — it defines the splitting strategy, evaluation metrics, and experiment tracking plan.
  - If it does not exist, warn: *"No test design found (task 4.2). It's strongly recommended to complete 4.2 first. Proceed anyway?"*
- Read `docs/crisp-dm/2-data-understanding/2.3-data-exploration.md`
  - If it exists, reference it — feature hypotheses inform feature selection.
- Check for prepared data artifacts from Phase 3 (data preparation):
  - Look for files in `data/processed/` or `data/interim/`
  - If no prepared data exists, warn: *"No prepared data found. Have you completed Phase 3 (Data Preparation)?"*

### Step 2: Plan the Model Building

Based on the 4.1 and 4.2 documents, create a build plan:

1. **Data pipeline** — how to load prepared data and apply final transforms
2. **Build order** — always baseline first, then candidates in priority order from 4.1
3. **For each technique:**
   - Default configuration (out-of-the-box hyperparameters)
   - Tuning strategy (grid search, Bayesian optimization, manual)
   - Key hyperparameters and search ranges
   - Expected training time
4. **Experiment tracking** — MLflow experiment name, run naming convention from 4.2

Present the plan and ask the user to confirm before proceeding.

### Step 3: Build the Data Pipeline

Generate code to load and prepare data for modeling:

```python
import pandas as pd
import numpy as np
from sklearn.model_selection import TimeSeriesSplit  # or appropriate splitter
import mlflow
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Load prepared data
# [path from Phase 3 output or data/processed/]

# Apply splitting strategy from 4.2
# [temporal split with exact dates from 4.2]

# Fit preprocessing on training data only
# [scaling, encoding — NEVER fit on validation/test]

logger.info(f"Training set: {len(X_train)} records, {X_train.columns.tolist()}")
logger.info(f"Validation set: {len(X_val)} records")
logger.info(f"Test set: {len(X_test)} records (held out)")
```

### Step 4: Build the Baseline Model

Always build the baseline first:

```python
mlflow.set_experiment("[experiment-name]")

with mlflow.start_run(run_name="baseline-[technique]"):
    # Log parameters
    mlflow.log_param("technique", "[baseline technique]")
    mlflow.log_param("data_version", "[DVC hash or date]")
    mlflow.log_param("split_date", "[cutoff date]")

    # Train baseline
    # [baseline implementation]

    # Evaluate on validation set
    # [compute all metrics from 4.2]

    # Log metrics
    mlflow.log_metric("mae", mae_val)
    mlflow.log_metric("rmse", rmse_val)
    # [all metrics from 4.2]

    # Log artifacts
    # [feature importance, residual plots, prediction samples]

    logger.info(f"Baseline MAE: {mae_val:.4f}")
```

Present baseline results before building more complex models. Ask: *"Baseline MAE is [X]. This is our benchmark. Shall we proceed with the candidate models?"*

### Step 5: Build Candidate Models

For each selected technique from 4.1:

**Phase A — Default configuration:**
- Train with out-of-the-box hyperparameters
- Log to MLflow
- Compare against baseline

**Phase B — Hyperparameter tuning:**
- Apply the tuning strategy from the build plan
- Log every tuning run to MLflow
- Use early stopping where applicable
- Report best configuration found

**Phase C — Best configuration:**
- Train with best hyperparameters
- Compute all metrics on validation set
- Log final model artifact

For each model, generate and run code that:
- Sets random seeds for reproducibility
- Fits preprocessing on training data only
- Logs all parameters, metrics, and artifacts to MLflow
- Saves the trained model
- Computes feature importance (where applicable)

### Step 6: Synthesize Results

After all models are built, create a results summary:

| Model | Config | Primary Metric | vs. Baseline | Training Time | Notes |
|-------|--------|---------------|-------------|---------------|-------|
| Baseline | - | [value] | - | [time] | Benchmark |
| [Model A] default | [key params] | [value] | [+/- %] | [time] | [notes] |
| [Model A] tuned | [key params] | [value] | [+/- %] | [time] | [notes] |
| [Model B] default | [key params] | [value] | [+/- %] | [time] | [notes] |
| [Model B] tuned | [key params] | [value] | [+/- %] | [time] | [notes] |

Present results and ask the user:
1. **Do any results look suspicious? (e.g., too good — possible data leakage)**
2. **Should we try additional configurations?**
3. **Ready to proceed to model assessment (4.4)?**

### Step 7: Create the Notebook and Generate the Output Document

The Jupyter notebook at `notebooks/4.3-model-building.ipynb` should have been created during Steps 3-6 as the primary artifact where all model training code is developed and run. If not yet created, create it now using the `NotebookEdit` tool.

**Notebook structure:**
- **Setup & Data Loading** — imports, MLflow configuration, load prepared data
- **Data Pipeline** — preprocessing, splitting per 4.2 test design
- **Baseline Model** — training, evaluation, MLflow logging
- **Candidate Models** — for each technique: default config, tuning, best config
- **Results Summary** — comparison table of all models vs. baseline
- **Data Leakage Checks** — verification that no leakage occurred

Ensure all code cells are executed and outputs are saved.

Then write the summary document.

```bash
mkdir -p docs/crisp-dm/4-modeling
```

Write the file `docs/crisp-dm/4-modeling/4.3-model-building.md` using this template:

```markdown
# 4.3 Model Building Report

> **Project:** [project name]
> **Date:** [current date]
> **CRISP-DM Phase:** 4. Modeling
> **Status:** Draft | Review | Approved

---

## Build Overview

- **Techniques Built:** [list from 4.1]
- **Data Used:** [prepared dataset reference, DVC hash]
- **Splitting Strategy:** [from 4.2]
- **Training Period:** [date range]
- **Validation Period:** [date range]
- **Test Period:** [held out — date range]
- **MLflow Experiment:** [experiment name and link]
- **Total Runs:** [count]

---

## Data Pipeline

- **Input data:** [path and description]
- **Preprocessing steps:** [list — scaling, encoding, etc.]
- **Feature set:** [count] features ([list or reference to feature list])
- **Preprocessing fit:** Training set only (validated: [yes/no])
- **Code location:** [path to pipeline code]

---

## Baseline Model

### Configuration
- **Technique:** [name]
- **Parameters:** [list]
- **MLflow Run ID:** [run ID]

### Results (Validation Set)
| Metric | Value |
|--------|-------|
| [primary metric] | [value] |
| [secondary metrics] | [values] |

### Observations
- [key observations about baseline performance]

---

## Candidate Models

### [Technique Name]

#### Default Configuration
- **Parameters:** [list]
- **MLflow Run ID:** [run ID]
- **Validation [primary metric]:** [value] ([+/- %] vs. baseline)
- **Training time:** [duration]

#### Hyperparameter Tuning
- **Strategy:** [grid search / Bayesian / manual]
- **Search space:**
  | Parameter | Range | Best Value |
  |-----------|-------|------------|
  | [param] | [range] | [best] |
- **Total runs:** [count]
- **Best MLflow Run ID:** [run ID]

#### Best Configuration
- **Parameters:** [list of best hyperparameters]
- **Validation [primary metric]:** [value] ([+/- %] vs. baseline)
- **Training time:** [duration]
- **Feature importance (top 10):**
  | Rank | Feature | Importance |
  |------|---------|-----------|
  | 1 | [feature] | [value] |

[Repeat for each candidate technique]

---

## Results Summary

| Model | Config | [Primary Metric] | vs. Baseline | [Secondary Metric] | Training Time |
|-------|--------|------------------|-------------|-------------------|---------------|
| Baseline | default | [value] | — | [value] | [time] |
| [Model A] | default | [value] | [+/- %] | [value] | [time] |
| [Model A] | tuned | [value] | [+/- %] | [value] | [time] |
| [Model B] | default | [value] | [+/- %] | [value] | [time] |
| [Model B] | tuned | [value] | [+/- %] | [value] | [time] |

---

## Data Leakage Checks

| Check | Status | Evidence |
|-------|--------|---------|
| No future data in features | [Pass/Fail] | [how verified] |
| Preprocessing fit on train only | [Pass/Fail] | [how verified] |
| No target leakage in features | [Pass/Fail] | [how verified] |
| Test set not used during training/tuning | [Pass/Fail] | [how verified] |

---

## Issues Encountered

| # | Issue | Impact | Resolution |
|---|-------|--------|-----------|
| 1 | [issue] | [impact on results] | [how resolved] |

---

## To Be Clarified

[List any items that need further investigation. Remove this section if everything is complete.]

---

## Source Documents

- 4.1 Modeling Techniques: `docs/crisp-dm/4-modeling/4.1-modeling-techniques.md`
- 4.2 Test Design: `docs/crisp-dm/4-modeling/4.2-test-design.md`
- 2.3 Data Exploration: `docs/crisp-dm/2-data-understanding/2.3-data-exploration.md`

---

## Sign-off

| Role | Name | Date | Status |
|------|------|------|--------|
| Lead Data Scientist | | | Pending |
| Reviewer | | | Pending |
```

### Step 8: Summary and Next Steps

After writing both artifacts, present a summary:

> **Model Building complete.** Two artifacts created:
> - **Notebook:** `notebooks/4.3-model-building.ipynb` — full training code with inline outputs
> - **Summary:** `docs/crisp-dm/4-modeling/4.3-model-building.md` — structured report
>
> **Summary:**
> - [N] models built across [N] techniques
> - Baseline [metric]: [value]
> - Best model: [technique + config] with [metric]: [value] ([+/- %] vs. baseline)
> - [N] MLflow runs logged
> - Data leakage checks: [all passed / issues found]
> - [N] items still to be clarified (if any)
>
> **Next step in CRISP-DM:** Run `/assess-model` to perform detailed model assessment including error analysis, subgroup performance, and business impact translation (Task 4.4).

Also update the CRISP-DM phase tracker in `.claude/CLAUDE.md` to add the 4.3 artifact link.

## Quality Checks

Before finalizing, verify:
- [ ] Jupyter notebook exists at `notebooks/4.3-model-building.ipynb` with all training code and inline outputs
- [ ] Notebook cells are executed and outputs are saved (results render when opened)
- [ ] Baseline model was built and evaluated first
- [ ] Every model beats the baseline (or is documented as not doing so)
- [ ] All experiments are logged to MLflow (parameters, metrics, artifacts)
- [ ] Preprocessing was fit on training data only — never on validation or test
- [ ] Random seeds are set for reproducibility
- [ ] Data leakage checks are performed and documented
- [ ] Feature importance is computed for interpretable models
- [ ] The test set was NOT used during training or tuning
- [ ] Training code is saved and reproducible
- [ ] All metrics from the 4.2 test design are computed
- [ ] Results are compared against the success threshold from 1.3
- [ ] No PII or sensitive data in the report or model artifacts
