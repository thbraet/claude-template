# Colruyt Group -- Claude Code Instructions

You are assisting a data scientist at Colruyt Group, a Belgian retail corporation. All projects follow the **CRISP-DM** methodology (Business Understanding → Data Understanding → Data Preparation → Modeling → Evaluation → Deployment). Always be aware of which CRISP-DM phase the current work belongs to.

## Language & Communication

- Use English for all code, comments, documentation, commit messages, and MR descriptions.

## Git Conventions

### Branch Naming
- `feature/JIRA-123-short-description`
- `bugfix/JIRA-456-short-description`

### Commit Messages
Use Conventional Commits with optional CRISP-DM phase scope:
- `feat(modeling): add XGBoost baseline`
- `fix(data-prep): resolve date parsing for transaction data`
- `chore: update dependency versions`
- `docs(evaluation): add model card for churn model`
- `refactor(features): extract RFM calculation into module`
- `test: add integration tests for preprocessing pipeline`

### Merge Requests (GitLab)
- MR title: under 72 characters, imperative mood
- MR description must include: **Summary**, **Changes** (bulleted), **CRISP-DM Phase**, **Test Plan**, **Breaking Changes**
- Use `/mr-description` to generate a standardized MR description from your branch diff.

## What Never Gets Committed
- `.env` files, credentials, API keys, tokens, connection strings
- PII or personal data
- Data files (use DVC or Git LFS) -- never commit CSVs, Parquet, or model artifacts >100MB to git
- Internal URLs in public-facing code

## Tooling
- **Quality gates**: SonarQube
- **Package registry**: Artifactory (artifactory.colruytgroup.com)
- **CI/CD**: GitLab CI/CD
- **Experiment tracking**: MLflow
- **Data versioning**: DVC

## Logging
- Structured JSON logging with severity levels (DEBUG, INFO, WARN, ERROR)
- Include correlation IDs for distributed tracing
- Use OpenTelemetry for observability
- Never log PII

## Security
- No `eval()`, `exec()`, or dynamic code execution
- Validate and sanitize all external inputs
- Use parameterized queries -- never concatenate user input into SQL
- HTTPS only (except localhost)

## Data Science Principles
- Always establish a baseline model before building complex models
- Fit preprocessing on training data only -- never on validation or test sets
- Log every experiment: parameters, metrics, data version, code version
- Raw data is immutable -- never modify original data files in place
- Explore in notebooks, productionize in scripts
- Every engineered feature must be documented (name, formula, source, rationale)
- Check for data leakage at every stage

## Development
- Activate environment: `source .venv/bin/activate`
- Run notebooks: `jupyter lab`
- Run setup: `bash scripts/setup.sh`

## Project Documentation

Project-specific source documents (competition briefs, stakeholder notes, meeting minutes, requirement specs) go in `docs/project/`. CRISP-DM phase artifacts go in `docs/crisp-dm/`. General template documentation goes in `docs/`.

```
docs/
  project/          # Project-specific source documents
  crisp-dm/         # CRISP-DM phase artifacts
  *.md              # General template documentation
```

## Data Staging

Raw data is **immutable** — never modify files in `data/raw/`. Each pipeline stage writes new files to `data/processed/`. Reusable logic lives in `src/` modules; notebooks document decisions and call those modules.

**Rules:**
- Each stage reads from the previous stage's output (or `data/raw/` for the first stage)
- All imputers/encoders/scalers are fit on **train only**, then applied to test
- `src/` functions are pure: DataFrame in → DataFrame out, no side effects
- Notebooks call `src/` functions and write results to `data/processed/`

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
```
Use `PROJECT_ROOT`-based paths for all file access in notebooks.
