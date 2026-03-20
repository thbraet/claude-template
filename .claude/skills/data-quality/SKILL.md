---
name: data-quality
description: Generate a data quality assessment report for a dataset. Use during CRISP-DM Data Understanding phase.
argument-hint: "[dataset path]"
user-invocable: true
---

# Data Quality Assessment (CRISP-DM Phase 2)

Assess data quality for: $ARGUMENTS

Generate Python code that evaluates these quality dimensions:

1. **Completeness**: Null/missing values per column, overall completeness score
2. **Uniqueness**: Duplicate rows, near-duplicates, primary key violations
3. **Validity**: Values outside expected ranges, invalid formats, type mismatches
4. **Consistency**: Cross-field validation (e.g., end_date > start_date), referential integrity
5. **Timeliness**: Data freshness, gaps in time series, expected vs actual row counts
6. **Accuracy**: Statistical outliers (IQR, z-score), impossible values

Output a structured report:
## Data Quality Report: [DATASET]
- **Overall Score**: [0-100]
- **Dimensions**: [table of scores per dimension]
- **Critical Issues**: [blocking issues that must be resolved]
- **Warnings**: [issues that should be investigated]
- **Recommendations**: [suggested data cleaning steps for Phase 3]
