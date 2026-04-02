---
paths:
  - "data/**"
  - "**/*.py"
  - "**/*.ipynb"
---
# Data Staging

- Never write to, modify, or delete files in data/raw/ — raw data is immutable
- Each pipeline stage writes to data/processed/ with a clear naming convention (e.g., train_clean.csv, train_features.csv)
- Each stage reads from the previous stage's output, not from raw data (except the first stage)
- Never commit CSV, Parquet, or model artifacts >100KB to git — use DVC or Git LFS
- Include row counts and column counts in log output after each pipeline stage for traceability
- All data paths must use PROJECT_ROOT-based resolution, never hardcoded relative paths
- When creating new processed files, document the lineage: which input file and which transformation produced it
