# Colruyt Group -- Claude Code Instructions

You are assisting a data scientist at Colruyt Group, a Belgian retail corporation. All projects follow the **CRISP-DM** methodology (Business Understanding → Data Understanding → Data Preparation → Modeling → Evaluation → Deployment). Always be aware of which CRISP-DM phase the current work belongs to.

@.claude/CLAUDE.md

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

<!-- TEAM: Add team-specific instructions below this line -->

<!-- PROJECT: Fill in project-specific details below this line -->
