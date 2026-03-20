---
name: model-card
description: Generate a model card following Google's Model Cards framework. Required before any model goes to production. Use during CRISP-DM Evaluation phase.
argument-hint: "[model name or experiment ID]"
user-invocable: true
---

# Model Card Generator (CRISP-DM Phase 5)

Generate a model card for: $ARGUMENTS

Template (based on Google Model Cards for Model Reporting):

# Model Card: [MODEL NAME]

## Model Details
- **Model type**: [algorithm/architecture]
- **Version**: [version number]
- **Date**: [training date]
- **Owner**: [team/person]
- **Contact**: [email]
- **License**: [internal/open-source]

## Intended Use
- **Primary use cases**: [what this model is for]
- **Out-of-scope uses**: [what this model should NOT be used for]
- **Users**: [who will use this model]

## Training Data
- **Source**: [where the data came from]
- **Date range**: [temporal coverage]
- **Size**: [rows, features]
- **Preprocessing**: [key transformations applied]

## Evaluation Data
- **Source**: [same or different from training]
- **Date range**: [temporal coverage]
- **Size**: [rows]

## Performance Metrics
| Metric | Overall | [Subgroup A] | [Subgroup B] | [Subgroup C] |
|---|---|---|---|---|
| [metric 1] | [value] | [value] | [value] | [value] |

## Ethical Considerations
- **Sensitive attributes**: [what protected characteristics are involved]
- **Fairness assessment**: [disparate impact, equalized odds results]
- **Potential harms**: [what could go wrong]
- **Mitigations**: [what was done to address concerns]

## Limitations & Caveats
- [limitation 1]
- [limitation 2]
- [known failure modes]

## Monitoring
- **Metrics tracked**: [what is monitored in production]
- **Drift detection**: [method and thresholds]
- **Retraining trigger**: [when to retrain]
- **Rollback plan**: [how to revert]

Save to reports/model_cards/[model_name].md
