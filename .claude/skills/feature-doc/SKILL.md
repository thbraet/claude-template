---
name: feature-doc
description: Document a new feature in the feature registry. Use during CRISP-DM Data Preparation to track all engineered features.
argument-hint: "[feature name] [formula/description]"
user-invocable: true
---

# Feature Documentation (CRISP-DM Phase 3)

Document the feature: $ARGUMENTS

Append to docs/feature_registry.md (create if it doesn't exist):

| Feature | Formula/Definition | Source Columns | Rationale | Author | Date | Status |
|---|---|---|---|---|---|---|
| [name] | [how it's computed] | [which raw columns] | [why this feature helps] | [who created it] | [date] | Active/Deprecated |

If this is the first feature, create the file with a header explaining the feature registry purpose.
