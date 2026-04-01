---
name: data-lineage
description: "Generate a data lineage report tracing every column from raw data through cleaning, feature engineering, formatting, and into the model. Produces a visual lineage map and a structured markdown report."
argument-hint: "<optional: specific column name or pipeline stage to trace>"
---

# /data-lineage — Data Lineage Tracing

> **Purpose:** Understand where every column came from and how it was transformed.
>
> *"If you can't trace a feature back to raw data, you can't trust it."*

## Purpose

This skill traces the full lineage of data through the project pipeline: raw → cleaned → features → formatted → model input. It produces a structured report showing which raw columns feed into which final features, what transformations were applied, and where columns were added or dropped.

## Output Location

1. **Lineage report**: `docs/crisp-dm/3-data-preparation/data-lineage.md`
2. **Lineage diagram**: printed in conversation as a text-based flow diagram

## Workflow

### Step 1: Inventory Pipeline Stages

Scan the project for pipeline artifacts:

1. **Raw data**: Read column names from `data/raw/` files (CSV headers, Parquet schema)
2. **Cleaned data**: Read column names from `data/processed/*_clean.*`
3. **Feature data**: Read column names from `data/processed/*_features.*`
4. **Formatted data**: Read column names from `data/processed/*_formatted.*`

If any stage is missing, note it and work with what exists.

Also read the pipeline source code:
- `src/cleaning.py` — what columns are modified, added, or dropped
- `src/features.py` — what features are engineered and from which source columns
- Any other `src/*.py` modules that transform data

### Step 2: Build Column Lineage Map

For each column in the final formatted dataset, trace backwards:

1. **Origin**: Which raw column(s) does it derive from? (direct passthrough, transformation, or combination)
2. **Transformations**: What operations were applied at each stage? (imputation, encoding, scaling, binning, etc.)
3. **Stage introduced**: At which pipeline stage was this column first created?
4. **Stage dropped**: If a raw column doesn't appear in the final data, at which stage was it removed and why?

Build a structured table:

| Final Column | Origin Column(s) | Transformations | Introduced At | Notes |
|---|---|---|---|---|
| Age | Age | Title-group median imputation (3.2), StandardScaler (3.5) | raw | Missing values filled by title group |
| FamilySize | SibSp, Parch | SibSp + Parch + 1 (3.3) | 3.3 | Engineered composite feature |
| Cabin_Known | Cabin | isna() → binary flag (3.3), dropped raw Cabin (3.5) | 3.3 | Proxy for ticket class |

### Step 3: Identify Dropped Columns

List all columns that existed in raw data but are absent from the final formatted dataset:

| Dropped Column | Dropped At | Reason |
|---|---|---|
| Name | 3.5 | Free text, replaced by Title feature |
| Ticket | 3.5 | High cardinality, low predictive value |

Cross-reference with `docs/crisp-dm/3-data-preparation/3.1-select-data.md` and `3.3-construct-data.md` for documented rationale.

### Step 4: Generate Lineage Diagram

Produce a text-based flow diagram showing the pipeline stages and column flow:

```
RAW (12 cols)          CLEAN (12 cols)       FEATURES (16 cols)     FORMATTED (10 cols)
├─ PassengerId    ──→  PassengerId      ──→  PassengerId       ──→  (dropped: ID only)
├─ Survived       ──→  Survived         ──→  Survived          ──→  Survived
├─ Pclass         ──→  Pclass           ──→  Pclass            ──→  Pclass
├─ Name           ──→  Name             ──→  Name / Title      ──→  Title_encoded
├─ Age            ──→  Age (imputed)    ──→  Age / AgeBin      ──→  Age_scaled, AgeBin
...
```

Adapt this diagram to the actual project columns.

### Step 5: Flag Lineage Issues

Check for potential problems:
- **Orphan features**: Columns in formatted data with no traceable raw origin
- **Undocumented drops**: Raw columns missing from final data without documented reason
- **Transformation gaps**: Columns that changed between stages without code in `src/`
- **Leakage risks**: Features derived from target-adjacent columns (e.g., using post-event data)

### Step 6: Write Report

Write the lineage report to `docs/crisp-dm/3-data-preparation/data-lineage.md` with sections:

1. **Pipeline Overview** — stages, file locations, row/column counts per stage
2. **Full Column Lineage Table** — the table from Step 2
3. **Dropped Columns** — the table from Step 3
4. **Lineage Diagram** — the visual from Step 4
5. **Issues & Recommendations** — findings from Step 5

### Step 7: Summary

Present a concise summary to the user:
- Total columns traced: N raw → M final
- Columns added (engineered): list
- Columns dropped: list
- Issues found: count and severity
