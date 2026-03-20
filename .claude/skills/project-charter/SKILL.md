---
name: project-charter
description: Generate a structured data science project charter. Use at the start of a CRISP-DM project to document business objectives, success criteria, and scope.
argument-hint: "[business problem description]"
user-invocable: true
---

# Project Charter Generator (CRISP-DM Phase 1)

Generate a project charter for: $ARGUMENTS

Template:
# Project Charter: [TITLE]

## Business Objective
[What business problem are we solving? Why now?]

## Stakeholders
| Name | Role | Responsibility |
|---|---|---|
| [name] | Sponsor | Final approval |
| [name] | Domain Expert | Requirements, validation |
| [name] | Data Scientist | Analysis, modeling |

## Success Criteria
| Business KPI | Target | Measurement Method |
|---|---|---|
| [e.g., reduce churn] | [e.g., by 15%] | [e.g., monthly cohort analysis] |

## Data Mining Goals
| Technical Metric | Target | Rationale |
|---|---|---|
| [e.g., AUC-ROC] | [e.g., > 0.85] | [maps to business KPI above] |

## Scope
- In scope: [what we will do]
- Out of scope: [what we will not do]
- Assumptions: [key assumptions]
- Constraints: [timeline, budget, data access, compute]

## Risk Register
| Risk | Impact | Probability | Mitigation |
|---|---|---|---|
| [risk] | High/Med/Low | High/Med/Low | [mitigation] |

## Timeline
| Phase | Duration | Start | End |
|---|---|---|---|
| Business Understanding | [weeks] | | |
| Data Understanding | [weeks] | | |
| Data Preparation | [weeks] | | |
| Modeling | [weeks] | | |
| Evaluation | [weeks] | | |
| Deployment | [weeks] | | |

Save to docs/project_charter.md.
