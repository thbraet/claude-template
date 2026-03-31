# Project: Titanic Survival Prediction

## Business Objective
Build a binary classifier that predicts passenger survival (0/1) for 418 Kaggle test-set passengers, maximizing prediction accuracy. See [1.1 Business Objectives](docs/crisp-dm/1-business-understanding/1.1-business-objectives.md).

## CRISP-DM Phase Tracker
| Phase | Status | Key Artifacts |
|---|---|---|
| 1. Business Understanding | Complete | [1.1](docs/crisp-dm/1-business-understanding/1.1-business-objectives.md), [1.2](docs/crisp-dm/1-business-understanding/1.2-situation-assessment.md), [1.3](docs/crisp-dm/1-business-understanding/1.3-data-mining-goals.md), [1.4](docs/crisp-dm/1-business-understanding/1.4-project-plan.md) |
| 2. Data Understanding | Complete | [2.1](docs/crisp-dm/2-data-understanding/2.1-data-collection.md), [2.2](docs/crisp-dm/2-data-understanding/2.2-data-description.md), [2.3](docs/crisp-dm/2-data-understanding/2.3-data-exploration.md), [2.4](docs/crisp-dm/2-data-understanding/2.4-data-quality.md); Notebooks: [2.2](notebooks/2.2-data-description.ipynb), [2.3](notebooks/2.3-data-exploration.ipynb), [2.4](notebooks/2.4-data-quality.ipynb) |
| 3. Data Preparation | Not Started | Feature pipeline, validation suite |
| 4. Modeling | Not Started | Modeling technique selection, test design, model building, assessment |
| 5. Evaluation | Not Started | Result evaluation, process review, next steps |
| 6. Deployment | Not Started | Kaggle submission, final report |

## Data Sources
| Source | Type | Access | Refresh | Description |
|---|---|---|---|---|
| train.csv | File | data/raw/titanic/ | Static | 891 passengers with survival labels |
| test.csv | File | data/raw/titanic/ | Static | 418 passengers to predict |
| gender_submission.csv | File | data/raw/titanic/ | Static | Baseline submission (females survive) |

## Development
- Setup environment: `[conda env create / pip install]`
- Run tests: `[pytest]`
- Run pipeline: `[make data && make train && make evaluate]`
- Run EDA: `[jupyter lab]`

## Key Decisions
[Link to docs/adr/ for Architecture Decision Records]

## Conventions

### Notebook Path Resolution
Never use hardcoded relative paths (`../data/` or `data/`) in Jupyter notebooks. Instead, dynamically resolve the project root so notebooks work regardless of the kernel's working directory (VS Code sets cwd to project root; terminal/nbconvert may use `notebooks/`).

Every notebook's first code cell must include:
```python
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent if "__file__" in dir() else Path.cwd()
if (PROJECT_ROOT / "notebooks").is_dir():
    pass  # cwd is project root
elif (PROJECT_ROOT.parent / "notebooks").is_dir():
    PROJECT_ROOT = PROJECT_ROOT.parent  # cwd is a subdirectory

DATA_DIR = PROJECT_ROOT / "data" / "raw" / "titanic"
```
Use `PROJECT_ROOT`-based paths for all file access in notebooks.

<!-- TEAM: Add team-specific instructions below -->

<!-- PROJECT: Add project-specific context below -->
