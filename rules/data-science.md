---
paths:
  - "**/*.py"
  - "**/*.ipynb"
  - "**/*.sql"
---
# Data Science Best Practices

- Always establish a baseline model before building complex models
- Fit all preprocessing (scalers, encoders, imputers) on training data only -- never on validation or test
- Set random seeds for all stochastic processes and document them (numpy, random, torch, sklearn)
- Every experiment must be logged: parameters, metrics, data version, code version, environment
- Raw data is immutable -- never modify original data files in place
- Explore in notebooks, productionize in scripts -- refactor reused notebook code into src/ modules
- Check for data leakage at every stage (target leakage, temporal leakage, preprocessing leakage)
- Pin all dependency versions (requirements.txt with ==, poetry.lock, conda-lock)
- Every result must be reproducible from raw data with a single command (make, dvc repro, etc.)
- Prefer pandas/polars for tabular data, not manual loops
- Use DVC or similar for data versioning -- never commit large data files to git
- Feature engineering code must be identical between training and serving
