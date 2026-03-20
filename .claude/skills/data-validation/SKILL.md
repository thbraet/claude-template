---
name: data-validation
description: Generate a data validation suite using pandera or Great Expectations. Use during CRISP-DM Data Preparation.
argument-hint: "[dataset path]"
user-invocable: true
---

# Data Validation Suite Generator (CRISP-DM Phase 3)

Generate validation code for: $ARGUMENTS

1. Inspect the dataset schema and statistics
2. Generate a pandera DataFrameSchema (preferred) or Great Expectations suite that validates:
   - Column presence and types
   - Null constraints (based on observed patterns)
   - Value ranges (min/max for numerics)
   - Allowed values (for low-cardinality categoricals)
   - String patterns (for emails, IDs, dates)
   - Row-level checks (cross-column constraints)
   - Statistical checks (mean within range, std dev bounds)
3. Include both "hard" checks (must pass) and "soft" checks (warnings)
4. Generate a test file that runs the validation on sample data
