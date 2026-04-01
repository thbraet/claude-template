---
name: init-project
description: "Bootstrap a new data science project from the CRISP-DM template: creates directory structure, copies documentation templates, initializes DVC, and configures .claude/CLAUDE.md with project-specific context."
argument-hint: "<project name and brief description>"
---

# /init-project — Project Bootstrapper

> **Purpose:** Initialize a new data science project from the CRISP-DM template.
>
> *"Every project starts the same way — don't waste time on boilerplate."*

## Purpose

This skill transforms the CRISP-DM template into a project-specific workspace. It gathers key project details, populates the directory structure, resets CRISP-DM documents to blank templates, configures `.claude/CLAUDE.md` with project context, and initializes data versioning.

## Output Location

Modifies the project in-place:
- `.claude/CLAUDE.md` — populated with project-specific details
- `docs/crisp-dm/**/*.md` — reset to blank templates with project name substituted
- `data/raw/<project>/` — directory created for raw data
- `data/processed/` — directory ensured
- `notebooks/` — cleared or kept based on user choice
- `src/` — skeleton modules created

## Workflow

### Step 1: Gather Project Information

Ask the user for the following (skip any provided in the argument):

1. **Project name**: Short identifier (e.g., "churn-prediction", "demand-forecast")
2. **Business objective**: One-sentence description of what the model should do
3. **Data sources**: What data will be used? (files, databases, APIs)
4. **Target variable**: What are we predicting? (name, type: binary/multiclass/regression/ranking)
5. **Primary metric**: How will success be measured? (accuracy, RMSE, F1, AUC, etc.)
6. **Stakeholder**: Who is the business owner of this project?
7. **Timeline**: Any deadlines or milestones?

### Step 2: Reset Project State

Ask the user before proceeding: *"This will reset CRISP-DM documents and update .claude/CLAUDE.md. Existing notebooks and src/ code will NOT be deleted unless you confirm. Proceed?"*

If confirmed:

1. **Clear CRISP-DM docs**: For each `docs/crisp-dm/**/*.md` file, reset to the template structure (headers, empty tables, placeholder text) while preserving the section structure
2. **Update `.claude/CLAUDE.md`**: Replace the project-specific content with new project details
3. **Create data directories**:
   ```
   data/raw/<project-name>/     # For raw data files
   data/processed/               # For pipeline outputs
   ```
4. **Create submission directory** (if competition):
   ```
   submissions/
   ```

### Step 3: Configure `.claude/CLAUDE.md`

Generate the project-specific CLAUDE.md:

```markdown
# Project: <Project Name>

## Business Objective
<Business objective from Step 1>. See [1.1 Business Objectives](docs/crisp-dm/1-business-understanding/1.1-business-objectives.md).

## CRISP-DM Phase Tracker
| Phase | Status | Key Artifacts |
|---|---|---|
| 1. Business Understanding | Not Started | |
| 2. Data Understanding | Not Started | |
| 3. Data Preparation | Not Started | |
| 4. Modeling | Not Started | |
| 5. Evaluation | Not Started | |
| 6. Deployment | Not Started | |

## Data Sources
| Source | Type | Access | Refresh | Description |
|---|---|---|---|---|
| <from Step 1> | | | | |

## Data Staging (Project-Specific)
<Generated based on data sources>

## Key Decisions
(None yet — decisions will be documented as the project progresses)
```

### Step 4: Create Source Module Skeletons

If `src/cleaning.py` and `src/features.py` don't exist or user wants to reset:

```python
# src/cleaning.py
"""Data cleaning pipeline for <project-name>."""

import pandas as pd


def clean_dataset(df: pd.DataFrame) -> pd.DataFrame:
    """Apply all cleaning steps to a dataset.

    Fit parameters on training data only, then apply to both train and test.

    Args:
        df: Raw DataFrame to clean.

    Returns:
        Cleaned DataFrame.
    """
    df = df.copy()
    # TODO: Add cleaning steps
    return df
```

```python
# src/features.py
"""Feature engineering pipeline for <project-name>."""

import pandas as pd


def build_features(df: pd.DataFrame) -> pd.DataFrame:
    """Add engineered features to a dataset.

    Args:
        df: Cleaned DataFrame.

    Returns:
        DataFrame with additional feature columns.
    """
    df = df.copy()
    # TODO: Add feature engineering steps
    return df
```

### Step 5: Initialize DVC (if not already initialized)

```bash
# Check if DVC is initialized
if [ ! -d ".dvc" ]; then
    dvc init
    # Track data directory
    echo "data/raw/" >> .dvc/.gitignore
fi
```

Ask the user if they want to configure a DVC remote.

### Step 6: Update .gitignore

Ensure `.gitignore` includes:

```
# Data files (use DVC)
data/raw/
data/processed/
*.csv
*.parquet
*.pkl
*.joblib

# Models
models/
*.h5
*.onnx

# Environment
.env
.venv/
__pycache__/

# Jupyter
.ipynb_checkpoints/

# MLflow
mlruns/

# OS
.DS_Store
```

### Step 7: Summary

Present the initialized project:

```
Project initialized: <project-name>
═══════════════════════════════════

  .claude/CLAUDE.md          ✓ Configured with project details
  docs/crisp-dm/             ✓ Templates reset (24 documents)
  data/raw/<project-name>/   ✓ Directory created
  data/processed/            ✓ Directory ready
  src/cleaning.py            ✓ Skeleton created
  src/features.py            ✓ Skeleton created
  DVC                        ✓ Initialized

Next step: Run /define-business-objectives to start Phase 1,
           or /next for a guided recommendation.
```
