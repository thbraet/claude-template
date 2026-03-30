# Project: Store Capacity Forecast

## Business Objective
Predict incoming transport units (carts, pallets, boxes) per CLP store, per day, per section, 3-6 weeks ahead for workforce planning. See [1.1 Business Objectives](docs/crisp-dm/1-business-understanding/1.1-business-objectives.md).

## CRISP-DM Phase Tracker
| Phase | Status | Key Artifacts |
|---|---|---|
| 1. Business Understanding | In Progress | [1.1-business-objectives.md](docs/crisp-dm/1-business-understanding/1.1-business-objectives.md) |
| 2. Data Understanding | Not Started | EDA notebooks, data dictionary |
| 3. Data Preparation | Not Started | Feature pipeline, validation suite |
| 4. Modeling | Not Started | [4.1-modeling-techniques.md](docs/crisp-dm/4-modeling/4.1-modeling-techniques.md), [4.2-test-design.md](docs/crisp-dm/4-modeling/4.2-test-design.md), [4.3-model-building.md](docs/crisp-dm/4-modeling/4.3-model-building.md), [4.4-model-assessment.md](docs/crisp-dm/4-modeling/4.4-model-assessment.md) |
| 5. Evaluation | Not Started | Model card, fairness audit |
| 6. Deployment | Not Started | Serving API, monitoring, runbook |

## Data Sources
| Source | Type | Access | Refresh | Description |
|---|---|---|---|---|
| Guido Kuylit CSV | File | CSV extract | One-time (6 years) | Transport units per store per day |
| ODCF | DB | TBD | Daily | DC outflow forecast |
| ASB | DB | TBD | Daily | Ideal store delivery forecast |
| Plato | DB | TBD | Weekly | Workforce planning drivers & prognoses |
| Sales Forecast | DB | TBD | Weekly | 13-week sales forecast per store |

## Development
- Setup environment: `[conda env create / pip install]`
- Run tests: `[pytest]`
- Run pipeline: `[make data && make train && make evaluate]`
- Run EDA: `[jupyter lab]`

## Key Decisions
[Link to docs/adr/ for Architecture Decision Records]

## Conventions
[Project-specific conventions beyond org standards in root CLAUDE.md]

<!-- TEAM: Add team-specific instructions below -->

<!-- PROJECT: Add project-specific context below -->
