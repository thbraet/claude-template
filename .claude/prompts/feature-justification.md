# Feature Justification for Review

Use this prompt when you need to justify engineered features to a reviewer or stakeholder.

## Template

Read `docs/crisp-dm/3-data-preparation/3.3-construct-data.md` and `src/features.py`.

Then produce a feature justification table:

| Feature | What it captures | Source data | Why it helps | Evidence |
|---|---|---|---|---|
| [Name] | [Plain-language description] | [Which raw columns] | [Hypothesis for predictive value] | [Correlation with target, or domain reasoning] |

After the table, address:

1. **Feature count**: How many features total? Is this appropriate for the dataset size? (rule of thumb: at least 10-20 samples per feature)
2. **Leakage check**: Could any feature encode information from the future or the target? Explain why each is safe.
3. **Redundancy check**: Are any features highly correlated with each other? If so, which would you drop and why?
4. **Domain validation**: Do the feature values make domain sense? (e.g., "FamilySize ranges from 1-11, which is plausible for passenger manifests")

Rules:
- Every feature must have a documented reason for existing
- "It improved accuracy" is not sufficient — explain the mechanism
- Flag any feature that could be controversial or hard to explain to stakeholders
