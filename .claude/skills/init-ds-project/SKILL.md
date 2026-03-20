---
name: init-ds-project
description: Scaffold a CRISP-DM aligned data science project structure. Use when starting a new data science project.
argument-hint: "[project name]"
user-invocable: true
---

# Initialize Data Science Project

Create a CRISP-DM aligned project structure for: $ARGUMENTS

Generate the following directory tree:
```
project_name/
├── README.md
├── Makefile                  # make data, make train, make evaluate, make serve
├── pyproject.toml            # or requirements.txt with pinned versions
├── .env.example              # Required environment variables
├── data/
│   ├── raw/                  # Original immutable data
│   ├── interim/              # Intermediate transformed data
│   ├── processed/            # Final datasets for modeling
│   └── external/             # Third-party data sources
├── notebooks/
│   ├── 01-business-understanding/
│   ├── 02-data-understanding/
│   ├── 03-data-preparation/
│   ├── 04-modeling/
│   └── 05-evaluation/
├── src/
│   └── project_name/
│       ├── __init__.py
│       ├── config.py         # Paths, parameters, constants
│       ├── data/             # Data loading and processing
│       ├── features/         # Feature engineering
│       ├── models/           # Model training and prediction
│       └── visualization/    # Plotting utilities
├── models/                   # Serialized models, predictions
├── reports/
│   ├── figures/
│   └── model_cards/
├── docs/
│   ├── adr/                  # Architecture Decision Records
│   ├── data_dictionary/
│   └── project_charter.md
├── tests/
└── .dvc/                     # Data version control (if using DVC)
```

Also create a starter README.md with CRISP-DM phase tracking table and project overview sections.
