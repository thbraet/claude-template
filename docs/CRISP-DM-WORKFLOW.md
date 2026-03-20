# CRISP-DM Workflow with Claude Code

How this template maps to the CRISP-DM methodology phases.

## Overview

```
Phase 1: Business Understanding  -->  /project-charter, /success-criteria, /init-ds-project
Phase 2: Data Understanding      -->  /eda-notebook, /data-dictionary, /data-quality
Phase 3: Data Preparation         -->  /feature-doc, /leakage-check, /data-validation
Phase 4: Modeling                  -->  /baseline-model, /experiment-setup, /error-analysis
Phase 5: Evaluation                -->  /model-card, /fairness-audit, /model-comparison
Phase 6: Deployment                -->  /serving-api, /monitoring-config, /runbook
```

## Phase 1: Business Understanding

**Goal**: Define the business problem, success criteria, and project scope.

**Skills**:
- `/init-ds-project [name]` -- Scaffold CRISP-DM project structure
- `/project-charter [problem]` -- Generate project charter document
- `/success-criteria [objective]` -- Map business KPIs to ML metrics

**Agents**: None specific (general-purpose agents apply)

**Key Artifacts**:
- `docs/project_charter.md`
- Success criteria mapping
- Project directory structure

## Phase 2: Data Understanding

**Goal**: Explore the data, assess quality, document schema.

**Skills**:
- `/eda-notebook [dataset]` -- Generate EDA notebook template
- `/data-dictionary [dataset]` -- Document all columns in a dataset
- `/data-quality [dataset]` -- Assess data quality across 6 dimensions

**Agents**:
- `eda-assistant` -- Interactive EDA help
- `data-quality-checker` -- Automated quality profiling

**Key Artifacts**:
- EDA notebooks in `notebooks/02-data-understanding/`
- Data dictionary in `docs/data_dictionary/`
- Data quality report

## Phase 3: Data Preparation

**Goal**: Clean data, engineer features, validate pipeline.

**Skills**:
- `/feature-doc [feature]` -- Document an engineered feature
- `/leakage-check [file]` -- Audit for data leakage
- `/data-validation [dataset]` -- Generate validation suite

**Agents**:
- `ml-reviewer` -- Reviews preprocessing code for correctness

**Key Artifacts**:
- Feature registry in `docs/feature_registry.md`
- Validation suite
- Processed data in `data/processed/`

## Phase 4: Modeling

**Goal**: Build baseline, train models, track experiments.

**Skills**:
- `/baseline-model [type] [target]` -- Generate baseline model
- `/experiment-setup [tracker]` -- Configure experiment tracking
- `/error-analysis [model]` -- Analyze model errors

**Agents**:
- `experiment-tracker` -- Summarize and compare experiments
- `ml-reviewer` -- Review model code

**Key Artifacts**:
- Baseline metrics in `reports/baseline_metrics.json`
- Experiment logs in MLflow/W&B
- Trained models in `models/`

## Phase 5: Evaluation

**Goal**: Assess model performance, fairness, and readiness.

**Skills**:
- `/model-card [model]` -- Generate model card (required for production)
- `/fairness-audit [model] [attributes]` -- Assess bias across protected groups
- `/model-comparison [experiments]` -- Compare experiment results

**Agents**:
- `experiment-tracker` -- Experiment comparison
- `notebook-reviewer` -- Review evaluation notebooks

**Key Artifacts**:
- Model card in `reports/model_cards/`
- Fairness audit results
- Model comparison report

## Phase 6: Deployment

**Goal**: Serve model, set up monitoring, prepare operations.

**Skills**:
- `/serving-api [model]` -- Generate FastAPI serving endpoint
- `/monitoring-config [model]` -- Set up drift detection and alerting
- `/runbook [service]` -- Generate operations runbook

**Agents**:
- `security-reviewer` -- Review serving code for vulnerabilities

**Key Artifacts**:
- Serving API in `src/serving/`
- Monitoring configuration
- Operations runbook

## Cross-Phase Tools

These tools are useful across all phases:

| Tool | Purpose |
|---|---|
| `/code-review` | Review any code changes |
| `/adr [decision]` | Document architectural decisions |
| `/mr-description` | Generate MR descriptions |
| `/incident-report` | Post-incident documentation |
| `/crisp-status` | Check CRISP-DM phase progress |
| `/summarize` | Summarize code or text |
| `/explain-model` | SHAP-based model interpretability |

## Checking Progress

Run `/crisp-status` at any time to see which phases are complete and what artifacts are missing.
