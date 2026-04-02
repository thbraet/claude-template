---
name: explore-data
description: "CRISP-DM 2.3 — Explore Data. Performs deeper EDA including distributions, correlations, temporal patterns, subgroup analysis, and hypothesis generation. Produces a structured exploration report with visualizations in docs/crisp-dm/2-data-understanding/."
argument-hint: "<path to data file, dataset name, or specific analysis question>"
---

# /explore-data — CRISP-DM 2.3: Explore Data

> **Phase:** 2. Data Understanding | **Task:** 2.3 Explore Data
>
> *"This task addresses data mining questions using querying, visualization, and reporting techniques. These include distribution of key attributes, relationships between pairs or small numbers of attributes, results of simple aggregations, properties of significant sub-populations, and simple statistical analyses."*

## Purpose

This skill performs deeper exploratory data analysis, going beyond the surface-level description in 2.2 to uncover patterns, relationships, and anomalies that inform feature engineering and modeling decisions. It produces four outputs:

1. **Univariate Analysis** — distributions, outliers, skewness for key variables
2. **Bivariate / Multivariate Analysis** — correlations, target-predictor relationships
3. **Temporal Patterns** — trends, seasonality, calendar effects, structural breaks
4. **Key Findings & Hypotheses** — actionable insights, feature ideas, risk flags

## Output Location

This skill produces two artifacts:

1. **Jupyter notebook** (primary): `notebooks/2.3-data-exploration.ipynb` — contains all analysis code, inline visualizations, and markdown narrative. This is the working artifact where exploration happens.
2. **Summary document**: `docs/crisp-dm/2-data-understanding/2.3-data-exploration.md` — a structured summary of key findings, feature hypotheses, and modeling implications extracted from the notebook. This is the CRISP-DM documentation artifact.

Visualizations are also saved to `reports/figures/eda/` for use in the summary document and downstream reports.

## Workflow

### Step 1: Check for Existing Artifacts

Before starting, check if output artifacts already exist:
- Check for `notebooks/2.3-data-exploration.ipynb` (the primary notebook)
- Check for `docs/crisp-dm/2-data-understanding/2.3-data-exploration.md` (the summary document)
- If either exists, present what's found and ask: *"A data exploration [notebook/report/both] already exists. Do you want to (1) update it, (2) start fresh, or (3) skip this step?"*
- If neither exists, proceed to Step 2.

Also check if prerequisite documents exist:
- Read `docs/crisp-dm/2-data-understanding/2.1-data-collection.md`
  - If it exists, use it — it lists datasets and loading instructions.
- Read `docs/crisp-dm/2-data-understanding/2.2-data-description.md`
  - If it exists, use it — it contains the data dictionary, field types, and red flags to investigate further.
  - If it does not exist, warn the user: *"No data description report found (task 2.2). It's recommended to complete 2.2 first. Proceed anyway?"*
- Read `docs/crisp-dm/1-business-understanding/1.3-data-mining-goals.md`
  - If it exists, use it — it defines the target variable, prediction granularity, and expected features, which should guide the exploration.

### Step 2: Ingest Source Information

Check if the user provided a reference (via `$ARGUMENTS` or in conversation):

- **File path** — Load and analyze the specific file
- **Dataset name** — Look up in 2.1 for location and loading instructions
- **Specific question** (e.g., "Is there seasonality in transport volumes?") — Focus the exploration on that question while still covering the standard analyses
- **No input provided** — If the 2.1/2.2 documents exist, extract the dataset list and ask: *"Which dataset(s) should I explore? Or should I explore all of them with focus on the target variable?"*

### Step 3: Plan the Exploration

Based on the data mining goals (1.3) and the data description (2.2), plan the exploration. The analysis should always include these categories, adapted to the specific data:

**Category 1 — Univariate Analysis:**
- Distribution of the target variable (histogram, box plot)
- Distribution of key numeric features (histograms, QQ plots for normality)
- Frequency distribution of key categorical features (bar charts)
- Outlier detection (IQR method, z-scores)
- Skewness and kurtosis for numeric fields

**Category 2 — Bivariate / Multivariate Analysis:**
- Correlation matrix of numeric features (heatmap)
- Target vs. each key predictor (scatter plots, box plots by category)
- Feature-feature relationships that might indicate multicollinearity
- Cross-tabulations for categorical features
- Interaction effects between key variables

**Category 3 — Temporal Patterns (critical for time series projects):**
- Time series plot of target variable
- Trend decomposition (trend, seasonal, residual)
- Day-of-week effects, month-of-year effects, holiday effects
- Year-over-year comparisons
- Structural breaks or regime changes
- Autocorrelation and partial autocorrelation (ACF/PACF)

**Category 4 — Subgroup Analysis:**
- Target variable by key segments (e.g., by store, by section, by region)
- Variance across subgroups
- Identifying outlier subgroups
- Segment-specific patterns that may require separate models

### Step 4: Create the EDA Notebook

Create a Jupyter notebook at `notebooks/2.3-data-exploration.ipynb` that contains all analysis code with inline visualizations and markdown narrative. The notebook is the primary artifact — all exploration happens here.

**Notebook structure:**

The notebook must be organized into clearly separated sections using markdown cells. Each section should have:
- A markdown cell explaining what the analysis does and why (linking to data mining goals from 1.3)
- Code cells that perform the analysis and display visualizations inline
- A markdown cell summarizing the key findings from that section

**Required notebook sections (as markdown headings):**

1. **Setup & Data Loading** — imports, configuration, load data using instructions from 2.1
2. **Target Variable Analysis** — distribution, class balance, implications
3. **Numeric Feature Distributions** — histograms, box plots, skewness, outlier detection
4. **Categorical Feature Distributions** — bar charts, frequency tables, cardinality
5. **Feature-Target Relationships** — survival rates by feature, cross-tabulations, statistical tests
6. **Correlation Analysis** — correlation matrix heatmap, multicollinearity assessment
7. **Interaction Effects** — key feature interactions (e.g., Sex x Pclass)
8. **Temporal Patterns** — trend, seasonality, structural breaks (or state "N/A" with rationale if not a time series)
9. **Subgroup Analysis** — target variable by key segments, outlier subgroups
10. **Key Findings & Feature Hypotheses** — summary of findings, proposed features, data leakage risks, modeling implications

**Code conventions for the notebook:**
- Set random seeds: `np.random.seed(42)`
- Use `%matplotlib inline` for inline plots
- Save all figures to `reports/figures/eda/` in addition to displaying them inline: `plt.savefig("reports/figures/eda/[name].png", dpi=150, bbox_inches='tight')`
- Use clear plot titles, axis labels, and legends
- Print key statistics as formatted tables or summary text after each analysis
- Include the project's virtual environment kernel

Use the `NotebookEdit` tool to create and populate the notebook cell by cell. Alternate between markdown cells (for narrative) and code cells (for analysis). Run code cells to generate outputs and visualizations inline.

Present key visualizations and findings to the user as you build the notebook.

### Step 5: Synthesize Findings

After running all analyses, synthesize the findings into:

1. **Key Findings** — what the data reveals about the prediction task
2. **Feature Hypotheses** — features suggested by the exploration (e.g., "day-of-week is a strong predictor")
3. **Data Leakage Risks** — any features that might encode the target inappropriately
4. **Modeling Implications** — what the exploration suggests for modeling choices (e.g., "high skew suggests log transform", "seasonality suggests seasonal differencing or Fourier features")
5. **Recommended Next Steps** — what to investigate further, what to address in data preparation

### Step 6: Present Findings and Ask for Input

Present the synthesized findings and ask the user:
1. **Are the findings consistent with domain knowledge?**
2. **Are there any patterns you expected that weren't found?**
3. **Any additional analyses you'd like to see?**

Wait for the user's response before finalizing.

### Step 7: Generate the Summary Document

After the notebook is complete and the user has provided feedback, create the summary document. This document extracts the key findings from the notebook into the structured CRISP-DM format — it does not duplicate the analysis code.

```bash
mkdir -p docs/crisp-dm/2-data-understanding
mkdir -p reports/figures/eda
```

Write the file `docs/crisp-dm/2-data-understanding/2.3-data-exploration.md` using this template:

```markdown
# 2.3 Data Exploration Report

> **Project:** [project name]
> **Date:** [current date]
> **CRISP-DM Phase:** 2. Data Understanding
> **Status:** Draft | Review | Approved

---

## Exploration Overview

- **Datasets Explored:** [list]
- **Target Variable:** [from 1.3]
- **Prediction Granularity:** [from 1.3]
- **Analysis Period:** [date range of data analyzed]
- **Notebook:** `notebooks/2.3-data-exploration.ipynb` (if created)

---

## Univariate Analysis

### Target Variable: [name]
- **Distribution:** [description — normal, skewed, bimodal, etc.]
- **Central Tendency:** mean = [value], median = [value]
- **Spread:** std = [value], IQR = [value]
- **Outliers:** [count] values beyond [method threshold]
- **Skewness:** [value] | **Kurtosis:** [value]
- **Visualization:** ![Target Distribution](../../reports/figures/eda/target_distribution.png)

### Key Numeric Features
| Feature | Mean | Median | Std | Skewness | Outliers | Notes |
|---------|------|--------|-----|----------|----------|-------|
| [feature] | [mean] | [median] | [std] | [skew] | [count] | [notes] |

### Key Categorical Features
| Feature | Top 3 Values (frequency) | Cardinality | Notes |
|---------|-------------------------|-------------|-------|
| [feature] | [val1 (n), val2 (n), val3 (n)] | [unique count] | [notes] |

---

## Bivariate / Multivariate Analysis

### Correlation Matrix
![Correlation Matrix](../../reports/figures/eda/correlation_matrix.png)

**Key Correlations with Target:**
| Feature | Correlation | Strength | Direction |
|---------|-------------|----------|-----------|
| [feature] | [r value] | [Strong/Moderate/Weak] | [Positive/Negative] |

### Feature-Target Relationships
[Description of key relationships found, with visualizations]

### Multicollinearity Concerns
| Feature Pair | Correlation | Risk | Recommendation |
|-------------|-------------|------|----------------|
| [feat A] — [feat B] | [r] | [High/Medium/Low] | [keep both / drop one / combine] |

---

## Temporal Patterns

### Overall Trend
- **Trend Direction:** [increasing / decreasing / flat / nonlinear]
- **Visualization:** ![Time Series](../../reports/figures/eda/time_series_trend.png)

### Seasonality
| Pattern | Period | Strength | Description |
|---------|--------|----------|-------------|
| Day-of-week | 7 days | [Strong/Moderate/Weak] | [description] |
| Monthly | ~30 days | [Strong/Moderate/Weak] | [description] |
| Annual | 365 days | [Strong/Moderate/Weak] | [description] |
| Holiday | Irregular | [Strong/Moderate/Weak] | [description] |

### Structural Breaks
| Date | Description | Possible Cause |
|------|-------------|---------------|
| [date] | [what changed] | [why — e.g., COVID, store renovation, policy change] |

### Autocorrelation
- **Significant lags:** [list of significant ACF/PACF lags]
- **Visualization:** ![ACF/PACF](../../reports/figures/eda/acf_pacf.png)

---

## Subgroup Analysis

### By [segmentation variable, e.g., Store]
| Segment | Count | Target Mean | Target Std | CV% | Notes |
|---------|-------|-------------|------------|-----|-------|
| [segment] | [n] | [mean] | [std] | [cv] | [notes] |

### Outlier Subgroups
- [subgroups with notably different behavior]

### Segment-Specific Patterns
- [patterns that vary by segment — may suggest separate models]

---

## Key Findings

### Confirmed Hypotheses
| # | Hypothesis | Evidence | Implication |
|---|-----------|----------|-------------|
| 1 | [hypothesis] | [what the data shows] | [impact on modeling] |

### Surprising Findings
| # | Finding | Evidence | Implication |
|---|---------|----------|-------------|
| 1 | [finding] | [what was unexpected] | [what to do about it] |

### Data Leakage Risks
| # | Feature(s) | Risk | Recommendation |
|---|-----------|------|----------------|
| 1 | [feature] | [how it could leak target information] | [drop / investigate / safe to use] |

---

## Feature Hypotheses

| # | Proposed Feature | Source Fields | Rationale (from EDA) | Priority |
|---|-----------------|-------------|---------------------|----------|
| 1 | [feature name] | [source columns] | [why EDA suggests this feature] | [High/Medium/Low] |

---

## Modeling Implications

- **Transformations suggested:** [log transform, scaling, encoding, etc.]
- **Feature engineering priorities:** [most promising feature categories]
- **Model family considerations:** [what EDA suggests about model choice]
- **Segmentation needs:** [should separate models be considered?]
- **Data preparation priorities:** [what cleaning/prep is most critical based on EDA]

---

## To Be Clarified

[List any items that need further investigation or domain expert input. Remove this section if everything is complete.]

---

## Source Documents

- [List the sources used]
- 2.1 Data Collection Report: `docs/crisp-dm/2-data-understanding/2.1-data-collection.md`
- 2.2 Data Description Report: `docs/crisp-dm/2-data-understanding/2.2-data-description.md`
- 1.3 Data Mining Goals: `docs/crisp-dm/1-business-understanding/1.3-data-mining-goals.md`

---

## Sign-off

| Role | Name | Date | Status |
|------|------|------|--------|
| Domain Expert | | | Pending |
| Data Scientist | | | Pending |
```

### Step 8: Summary and Next Steps

After writing both artifacts, present a summary:

> **Data Exploration complete.** Two artifacts created:
> - **Notebook:** `notebooks/2.3-data-exploration.ipynb` — full analysis with inline visualizations
> - **Summary:** `docs/crisp-dm/2-data-understanding/2.3-data-exploration.md` — structured findings
> - **Figures:** `reports/figures/eda/` — [N] visualizations saved
>
> **Summary:**
> - [N] key findings documented
> - [N] feature hypotheses generated
> - [N] data leakage risks identified
> - Temporal patterns: [brief summary — e.g., "strong day-of-week and annual seasonality detected"]
> - Top correlated features: [list top 3]
> - [N] items still to be clarified (if any)
>
> **Next step in CRISP-DM:** Run `/verify-data-quality` to perform a systematic data quality assessment — completeness, correctness, consistency, and timeliness (Task 2.4).

Also update the CRISP-DM phase tracker in `.claude/CLAUDE.md` to add the 2.3 artifact link.

## Quality Checks

Before finalizing, verify:
- [ ] Jupyter notebook exists at `notebooks/2.3-data-exploration.ipynb` with all analysis code and inline visualizations
- [ ] Notebook has clear markdown section headings matching the 10 required sections
- [ ] Notebook cells are executed and outputs are saved (visualizations render when opened)
- [ ] Every analysis connects back to the data mining goals from 1.3
- [ ] The target variable distribution is thoroughly analyzed
- [ ] Temporal patterns are assessed (trend, seasonality, structural breaks) — critical for forecasting projects
- [ ] Correlation analysis covers both target-feature and feature-feature relationships
- [ ] Data leakage risks are explicitly assessed
- [ ] All visualizations have clear titles, axis labels, and are saved to `reports/figures/eda/`
- [ ] Feature hypotheses are actionable and prioritized
- [ ] Modeling implications are specific, not generic
- [ ] Subgroup analysis covers the key segmentation variables
- [ ] No PII or sensitive data is included in the report or visualizations
- [ ] Code is reproducible (random seeds set, file paths explicit)
- [ ] Summary document cross-references the notebook and the 2.1, 2.2, and 1.3 documents
