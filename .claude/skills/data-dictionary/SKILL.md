---
name: data-dictionary
description: Generate a data dictionary from a dataset schema. Use during CRISP-DM Data Understanding to document every column.
argument-hint: "[dataset path or DataFrame variable]"
user-invocable: true
---

# Data Dictionary Generator (CRISP-DM Phase 2)

Generate a data dictionary for: $ARGUMENTS

1. Load the dataset and inspect schema (columns, dtypes, sample values)
2. For each column, generate a row in this template:

| Column | Type | Description | Source | Nulls % | Unique | Example Values | Notes |
|---|---|---|---|---|---|---|---|
| [name] | [dtype] | [TO BE FILLED] | [TO BE FILLED] | [computed] | [computed] | [3 examples] | [anomalies found] |

3. Auto-fill what can be detected (type, null%, unique count, examples)
4. Mark Description and Source as "[TO BE FILLED]" for human review
5. Flag columns needing attention (>50% nulls, single value, suspicious patterns)

Save to docs/data_dictionary/[dataset_name].md
