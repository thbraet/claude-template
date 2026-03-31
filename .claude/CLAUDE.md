# Project: Titanic Survival Prediction

## Business Objective
Build a binary classifier that predicts passenger survival (0/1) for 418 Kaggle test-set passengers, maximizing prediction accuracy. See [1.1 Business Objectives](docs/crisp-dm/1-business-understanding/1.1-business-objectives.md).

## CRISP-DM Phase Tracker
| Phase | Status | Key Artifacts |
|---|---|---|
| 1. Business Understanding | Complete | [1.1](docs/crisp-dm/1-business-understanding/1.1-business-objectives.md), [1.2](docs/crisp-dm/1-business-understanding/1.2-situation-assessment.md), [1.3](docs/crisp-dm/1-business-understanding/1.3-data-mining-goals.md), [1.4](docs/crisp-dm/1-business-understanding/1.4-project-plan.md) |
| 2. Data Understanding | Complete | [2.1](docs/crisp-dm/2-data-understanding/2.1-data-collection.md), [2.2](docs/crisp-dm/2-data-understanding/2.2-data-description.md), [2.3](docs/crisp-dm/2-data-understanding/2.3-data-exploration.md), [2.4](docs/crisp-dm/2-data-understanding/2.4-data-quality.md); Notebooks: [2.2](notebooks/2.2-data-description.ipynb), [2.3](notebooks/2.3-data-exploration.ipynb), [2.4](notebooks/2.4-data-quality.ipynb) |
| 3. Data Preparation | Complete | [3.1](docs/crisp-dm/3-data-preparation/3.1-select-data.md), [3.2](docs/crisp-dm/3-data-preparation/3.2-clean-data.md), [3.3](docs/crisp-dm/3-data-preparation/3.3-construct-data.md), [3.4](docs/crisp-dm/3-data-preparation/3.4-integrate-data.md), [3.5](docs/crisp-dm/3-data-preparation/3.5-format-data.md); Notebooks: [3.1](notebooks/3.1-select-data.ipynb), [3.2](notebooks/3.2-clean-data.ipynb), [3.3](notebooks/3.3-construct-data.ipynb), [3.4](notebooks/3.4-integrate-data.ipynb), [3.5](notebooks/3.5-format-data.ipynb) |
| 4. Modeling | In Progress | [4.1](docs/crisp-dm/4-modeling/4.1-modeling-techniques.md), [4.2](docs/crisp-dm/4-modeling/4.2-test-design.md); Notebooks: [4.1](notebooks/4.1-modeling-techniques.ipynb), [4.2](notebooks/4.2-test-design.ipynb) |
| 5. Evaluation | Not Started | Result evaluation, process review, next steps |
| 6. Deployment | Not Started | Kaggle submission, final report |

## Data Sources
| Source | Type | Access | Refresh | Description |
|---|---|---|---|---|
| train.csv | File | data/raw/titanic/ | Static | 891 passengers with survival labels |
| test.csv | File | data/raw/titanic/ | Static | 418 passengers to predict |
| gender_submission.csv | File | data/raw/titanic/ | Static | Baseline submission (females survive) |

## Development
- Activate environment: `source .venv/bin/activate`
- Run notebooks: `jupyter lab`
- Run setup: `bash setup.sh`

## Data Staging

Raw data is **immutable** — never modify files in `data/raw/`. Each pipeline stage writes new files to `data/processed/`. Reusable logic lives in `src/` modules; notebooks document decisions and call those modules.

```
data/
  raw/titanic/                  # IMMUTABLE source files (from Kaggle)
    train.csv
    test.csv
    gender_submission.csv
  processed/                    # Pipeline outputs (one file per stage)
    train_clean.csv             # Task 3.2 output: missing values handled, types fixed
    test_clean.csv
    train_features.csv          # Task 3.3 output: engineered features added
    test_features.csv
    train_formatted.csv         # Task 3.5 output: modeling-ready (all numeric, no raw cols)
    test_formatted.csv

src/                            # Reusable pipeline modules
  __init__.py
  cleaning.py                   # clean_dataset(df) → cleaned DataFrame
  features.py                   # build_features(df) → DataFrame with engineered features
```

**Rules:**
- Each stage reads from the previous stage's output (or `data/raw/` for the first stage)
- All imputers/encoders/scalers are fit on **train only**, then applied to test
- `src/` functions are pure: DataFrame in → DataFrame out, no side effects
- Notebooks call `src/` functions and write results to `data/processed/`

## Key Decisions
- Age imputation uses title-group medians (see `src/cleaning.py`)
- Cleaning parameters are fit on train only, applied to both train and test

## Assumptions & Business Validation Convention

Every CRISP-DM reporting doc (`docs/crisp-dm/**/*.md`) includes an **"Assumptions & Business Validation"** section (placed before "Source Documents") with three subsections:

1. **Assumptions Made** — table with columns: ID, Assumption, Category, Rationale, Status. IDs follow the pattern `A{task}-{n}` (e.g., `A3.2-1`). Status is one of: `Pending verification`, `Verified`, `Reworked (see feedback)`, `Rejected`.
2. **Questions for Business** — table with columns: ID, Question, Related Assumption, Priority, Status. IDs follow `Q{task}-{n}`. Status is one of: `Open`, `Answered`, `Closed`.
3. **Business Feedback Log** — table with columns: Date, Feedback Source, Related Assumption/Question, Feedback, Action Taken, Code/Doc Changes.

**When business feedback is received:**
1. Log the feedback in the relevant doc's Business Feedback Log
2. Update the related Assumption status (to `Verified`, `Reworked`, or `Rejected`)
3. Update the related Question status (to `Answered` or `Closed`)
4. Implement any required code changes
5. Document the code/doc changes in the feedback log row

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

