---
paths:
  - "src/features.py"
  - "src/feature*.py"
  - "notebooks/3.3*"
  - "notebooks/3.6*"
---
# Feature Documentation

- Every engineered feature must have a docstring or inline comment with: name, formula/logic, source columns, and rationale
- Group related features together in code (e.g., all family-size features, all title-based features)
- Document the expected dtype and value range for each feature
- When deriving features from multiple columns, list all source columns explicitly
- If a feature requires domain knowledge, cite the source or reasoning (e.g., "deck extracted from cabin — proxy for socioeconomic status")
- Never introduce a feature without updating the feature documentation in docs/crisp-dm/3-data-preparation/3.3-construct-data.md
- Features dropped during selection (3.6) must be documented with the reason for removal
