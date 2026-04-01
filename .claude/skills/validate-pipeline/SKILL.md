---
name: validate-pipeline
description: "End-to-end smoke test of the data pipeline: loads raw data, applies cleaning, feature engineering, and formatting, then validates outputs at each stage. Catches broken imports, schema drift, and integration errors."
argument-hint: "<optional: 'train', 'test', or 'both' (default: both)>"
---

# /validate-pipeline — Pipeline Smoke Test

> **Purpose:** Verify the full pipeline runs without errors and produces expected outputs.
>
> *"A pipeline that worked yesterday can break today — validate before every modeling run."*

## Purpose

This skill runs the complete data pipeline end-to-end as a smoke test. It loads raw data, applies each transformation stage, validates intermediate outputs, and reports any failures. This catches broken imports, missing files, schema changes, dtype mismatches, and row/column count anomalies.

## Output Location

Results are printed directly in the conversation. No file artifacts are created — this is a validation tool, not a data-producing step.

## Workflow

### Step 1: Inventory Pipeline Components

Scan the project for pipeline modules and data files:

1. **Source modules**: Check `src/` for `cleaning.py`, `features.py`, and any other pipeline modules
2. **Raw data**: Verify files exist in `data/raw/`
3. **Existing processed data**: Note what already exists in `data/processed/` (for comparison)

Read each source module to understand the expected function signatures.

If any critical component is missing (no `src/cleaning.py`, no raw data), report immediately and stop.

### Step 2: Build Validation Script

Create a temporary validation script (do NOT overwrite any existing files). The script should:

```python
import sys
import traceback
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent
if (PROJECT_ROOT / "notebooks").is_dir():
    pass
elif (PROJECT_ROOT.parent / "notebooks").is_dir():
    PROJECT_ROOT = PROJECT_ROOT.parent

sys.path.insert(0, str(PROJECT_ROOT))

import pandas as pd

results = []

def check(name, func):
    """Run a validation step and record pass/fail."""
    try:
        result = func()
        results.append({"step": name, "status": "PASS", "detail": result})
        print(f"  ✓ {name}: {result}")
    except Exception as e:
        results.append({"step": name, "status": "FAIL", "detail": str(e)})
        print(f"  ✗ {name}: {e}")
        traceback.print_exc()
```

### Step 3: Validate Each Stage

Run these checks sequentially (each stage depends on the previous):

**Stage 0 — Raw Data Loading**
```python
def load_raw():
    train = pd.read_csv(PROJECT_ROOT / "data/raw/.../train.csv")
    test = pd.read_csv(PROJECT_ROOT / "data/raw/.../test.csv")
    return f"train: {train.shape}, test: {test.shape}"
```
Adapt paths to actual raw data location from `.claude/CLAUDE.md`.

**Stage 1 — Cleaning**
```python
from src.cleaning import clean_dataset  # or actual function name

def validate_cleaning():
    train_raw = pd.read_csv(...)
    test_raw = pd.read_csv(...)
    train_clean = clean_dataset(train_raw)
    test_clean = clean_dataset(test_raw)
    # Checks:
    assert train_clean.shape[0] == train_raw.shape[0], "Row count changed during cleaning"
    assert not train_clean.isnull().all(axis=1).any(), "All-null rows found after cleaning"
    return f"train: {train_clean.shape}, test: {test_clean.shape}, nulls: {train_clean.isnull().sum().sum()}"
```

**Stage 2 — Feature Engineering**
```python
from src.features import build_features  # or actual function name

def validate_features():
    train_clean = ...  # from previous stage
    train_feat = build_features(train_clean)
    # Checks:
    assert train_feat.shape[0] == train_clean.shape[0], "Row count changed during feature engineering"
    assert train_feat.shape[1] >= train_clean.shape[1], "Features were lost, not added"
    new_cols = set(train_feat.columns) - set(train_clean.columns)
    return f"shape: {train_feat.shape}, new features: {len(new_cols)} ({', '.join(sorted(new_cols))})"
```

**Stage 3 — Formatting (if applicable)**
```python
def validate_formatting():
    # Check all columns are numeric (modeling-ready)
    non_numeric = train_fmt.select_dtypes(exclude="number").columns.tolist()
    assert len(non_numeric) == 0, f"Non-numeric columns remain: {non_numeric}"
    # Check no nulls
    null_count = train_fmt.isnull().sum().sum()
    assert null_count == 0, f"{null_count} null values remain"
    return f"shape: {train_fmt.shape}, all numeric: True, nulls: 0"
```

### Step 4: Cross-Stage Validation

After all stages pass individually, run cross-stage checks:

1. **Row preservation**: Same number of rows at every stage (no silent drops)
2. **Column tracking**: Document columns added/removed at each stage
3. **Train/test parity**: Both datasets have the same columns (except target)
4. **Dtype consistency**: Same dtypes for shared columns between train and test
5. **Value ranges**: No infinite values, no extreme outliers introduced by transformations

### Step 5: Report Results

Print a summary table:

```
Pipeline Validation Report
==========================
Stage              Status   Shape (train)   Shape (test)   Notes
─────────────────  ──────   ─────────────   ────────────   ──────────
0. Raw loading     PASS     (891, 12)       (418, 11)
1. Cleaning        PASS     (891, 12)       (418, 11)      3 nulls remaining
2. Features        PASS     (891, 16)       (418, 15)      4 new features
3. Formatting      PASS     (891, 10)       (418, 9)       All numeric, 0 nulls
Cross-stage        PASS     Row counts consistent, dtypes aligned

Overall: PASS (all 5 checks passed)
```

If any stage fails:
- Show the exact error and traceback
- Suggest likely fixes based on the error type
- Stop at the first failure (later stages depend on earlier ones)

### Step 6: Cleanup

Remove any temporary validation script created during the process. Do not modify any existing project files.
