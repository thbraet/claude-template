---
paths:
  - "**/*.py"
  - "**/*.ipynb"
---
# Reproducibility

- Set random seeds explicitly in every file that uses stochastic operations (random, numpy, sklearn, torch, tensorflow)
- Never use shuffle=True without passing an explicit random_state or seed
- Use sklearn's random_state parameter on every estimator, splitter, and sampler
- Pin the seed value in a single constant (e.g., RANDOM_STATE = 42) rather than scattering magic numbers
- Document the Python version and key package versions at the top of each notebook or in a requirements file
- Every pipeline must be re-runnable from raw data and produce identical results (deterministic output)
- When using train_test_split or cross-validation, always pass random_state for reproducible splits
- GPU-based training may have non-deterministic ops — document when exact reproducibility is not guaranteed and why
