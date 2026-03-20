---
paths:
  - "**/*.ipynb"
---
# Notebook Standards

- Every notebook starts with a markdown cell: Title, Author, Date, CRISP-DM Phase, Purpose
- Use the naming convention: {number}-{phase}-{description}-{initials}.ipynb
  - Example: 01-du-eda-initial-exploration-jdoe.ipynb
  - Phase codes: bu (Business Understanding), du (Data Understanding), dp (Data Preparation), mod (Modeling), eval (Evaluation), dep (Deployment)
- Section headers must use markdown cells (##) for logical flow
- Markdown cells explain WHY, code cells show WHAT
- Every notebook ends with a Conclusions cell summarizing findings and next steps
- No magic numbers without explanation -- use named constants
- No hardcoded file paths -- use config files or environment variables
- Notebooks must run top-to-bottom without error (Kernel > Restart & Run All before committing)
- Keep notebooks focused -- one analysis question per notebook
- Import all libraries in the first code cell
- Suppress warnings only with documented justification
