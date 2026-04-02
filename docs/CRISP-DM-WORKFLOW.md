# CRISP-DM Workflow with Claude Code

How this template maps to the CRISP-DM methodology phases.

## Overview

Each CRISP-DM phase has:
- **Skills** (slash commands) — one per task, e.g. `/define-business-objectives` for task 1.1
- **Agents** — one per phase, for broader guidance across multiple tasks
- **Commands** — `/status` to check progress, `/next` to find what to work on

```
Phase 1: Business Understanding  -->  /define-business-objectives, /assess-situation, /determine-data-mining-goals, /produce-project-plan
Phase 2: Data Understanding      -->  /collect-initial-data, /describe-data, /explore-data, /verify-data-quality
Phase 3: Data Preparation         -->  /select-data, /clean-data, /construct-data, /integrate-data, /format-data, /select-features
Phase 4: Modeling                  -->  /select-modeling-techniques, /generate-test-design, /build-model, /assess-model
Phase 5: Evaluation                -->  /evaluate-results, /review-process, /determine-next-steps
Phase 6: Deployment                -->  /plan-deployment, /plan-monitoring, /produce-final-report, /review-project
```

## Phase 1: Business Understanding

**Goal**: Define the business problem, success criteria, and project scope.

**Skills**:
- `/define-business-objectives` — Extract business context from source documents, define objectives and success criteria
- `/assess-situation` — Inventory resources, document requirements, risks, terminology, and costs/benefits
- `/determine-data-mining-goals` — Translate business objectives into technical goals and success criteria
- `/produce-project-plan` — Define stages, durations, resources, dependencies, and decision points

**Agent**: `business-understanding` — Assists with all Phase 1 tasks interactively

**Key Artifacts**:
- `docs/crisp-dm/1-business-understanding/1.1-business-objectives.md`
- `docs/crisp-dm/1-business-understanding/1.2-situation-assessment.md`
- `docs/crisp-dm/1-business-understanding/1.3-data-mining-goals.md`
- `docs/crisp-dm/1-business-understanding/1.4-project-plan.md`

## Phase 2: Data Understanding

**Goal**: Explore the data, assess quality, document schema.

**Skills**:
- `/collect-initial-data` — Document acquisition process, inventory datasets, record storage details
- `/describe-data` — Profile datasets, create data dictionary, document surface statistics
- `/explore-data` — Distributions, correlations, temporal patterns, subgroup analysis
- `/verify-data-quality` — Assess completeness, correctness, consistency, and timeliness

**Agent**: `data-understanding` — Assists with all Phase 2 tasks interactively

**Key Artifacts**:
- `docs/crisp-dm/2-data-understanding/2.1-data-collection.md` through `2.4-data-quality.md`
- Notebooks: `notebooks/2.2-data-description.ipynb`, `notebooks/2.3-data-exploration.ipynb`, `notebooks/2.4-data-quality.ipynb`

## Phase 3: Data Preparation

**Goal**: Clean data, engineer features, validate pipeline.

**Skills**:
- `/select-data` — Decide which datasets, fields, and records to include with documented rationale
- `/clean-data` — Handle missing values, outliers, noise, and encoding errors
- `/construct-data` — Engineer features, derive attributes, generate new records
- `/integrate-data` — Merge datasets from multiple sources into a unified dataset
- `/format-data` — Apply final transformations (type casting, column ordering, splitting)
- `/select-features` — Forward selection, overfit gap analysis, and optimal subset identification

**Agent**: `data-preparation` — Assists with all Phase 3 tasks including feature engineering and selection

**Key Artifacts**:
- `docs/crisp-dm/3-data-preparation/3.1-select-data.md` through `3.5-format-data.md`
- Notebooks: `notebooks/3.1-select-data.ipynb` through `notebooks/3.6-feature-selection.ipynb`
- Processed data in `data/processed/`
- Reusable pipeline code in `src/`

## Phase 4: Modeling

**Goal**: Build baseline, train models, track experiments.

**Skills**:
- `/select-modeling-techniques` — Evaluate candidates against data mining goals and constraints
- `/generate-test-design` — Define train/validation/test splits, metrics, and experiment tracking plan
- `/build-model` — Train baseline and candidate models with experiment logging
- `/assess-model` — Error analysis, subgroup performance, business impact, model selection

**Agent**: `modeling` — Assists with all Phase 4 tasks from technique selection to assessment

**Key Artifacts**:
- `docs/crisp-dm/4-modeling/4.1-modeling-techniques.md` through `4.4-model-assessment.md`
- Notebooks: `notebooks/4.1-modeling-techniques.ipynb` through `notebooks/4.4-model-assessment.ipynb`
- Trained models in `models/`
- Experiment logs in MLflow

## Phase 5: Evaluation

**Goal**: Assess model performance against business objectives, review process, decide next steps.

**Skills**:
- `/evaluate-results` — Assess model against business objectives and success criteria
- `/review-process` — Retrospective of the entire data mining process, lessons learned
- `/determine-next-steps` — Decide to deploy, iterate, or terminate based on evaluation

**Agent**: `evaluation` — Assists with all Phase 5 tasks including go/no-go decisions

**Key Artifacts**:
- `docs/crisp-dm/5-evaluation/5.1-evaluate-results.md` through `5.3-determine-next-steps.md`
- Notebooks: `notebooks/5.1-evaluate-results.ipynb`, `notebooks/5.2-review-process.ipynb`

## Phase 6: Deployment

**Goal**: Plan deployment, set up monitoring, document the project.

**Skills**:
- `/plan-deployment` — Serving architecture, rollout strategy, rollback procedures
- `/plan-monitoring` — Data drift detection, prediction quality tracking, alerting, retraining triggers
- `/produce-final-report` — Executive summary, technical report, model card, and project artifacts index
- `/review-project` — Retrospective, lessons learned, process improvements

**Agent**: `deployment` — Assists with all Phase 6 tasks from deployment planning to project closure

**Key Artifacts**:
- `docs/crisp-dm/6-deployment/6.1-plan-deployment.md` through `6.3-final-report.md`
- Submissions in `submissions/`

## Cross-Phase Tools

| Tool | Purpose |
|---|---|
| `/status` | Full CRISP-DM project dashboard — phases, task completeness, document gaps |
| `/next` | Show the next CRISP-DM task to work on based on current progress |
| `/review-mr` | Review branch or staged changes as a senior developer/data scientist |
| `/sync-to-notion` | Bidirectional sync of CRISP-DM docs with Notion |
| `code-review` agent | Independent code review of a branch or MR before merging |

## Checking Progress

Run `/status` at any time to see which phases are complete and what artifacts are missing. Run `/next` to get a recommendation for what to work on next.
