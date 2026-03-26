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

All artifacts are written to: `docs/crisp-dm/2-data-understanding/2.3-data-exploration.md`
Visualizations are saved to: `reports/figures/eda/`

## Workflow

### Step 1: Check for Existing Artifacts

Before starting, check if the output file already exists:
- Read `docs/crisp-dm/2-data-understanding/2.3-data-exploration.md`
- If it exists, present its contents and ask: *"A data exploration report already exists. Do you want to (1) update it, (2) start fresh, or (3) skip this step?"*
- If it does not exist, proceed to Step 2.

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

### Step 4: Generate and Run Analysis Code

For each category, generate Python code that:
- Loads the data using instructions from 2.1
- Performs the analysis
- Saves visualizations to `reports/figures/eda/`
- Prints key statistics

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

os.makedirs("reports/figures/eda", exist_ok=True)

# Load data
df = pd.read_csv("[path]")

# --- Univariate: Target distribution ---
fig, axes = plt.subplots(1, 2, figsize=(14, 5))
df["[target]"].hist(bins=50, ax=axes[0])
axes[0].set_title("[Target] Distribution")
df.boxplot(column="[target]", ax=axes[1])
axes[1].set_title("[Target] Box Plot")
plt.tight_layout()
plt.savefig("reports/figures/eda/target_distribution.png", dpi=150)
plt.close()

# --- Correlations ---
corr = df.select_dtypes(include='number').corr()
plt.figure(figsize=(12, 10))
sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", center=0)
plt.title("Correlation Matrix")
plt.tight_layout()
plt.savefig("reports/figures/eda/correlation_matrix.png", dpi=150)
plt.close()

# --- Temporal patterns ---
# [adapted to the specific temporal structure]

# --- Subgroup analysis ---
# [adapted to the specific segmentation]
```

Present visualizations and key findings to the user as you generate them.

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

### Step 7: Generate the Output Document

After gathering all information, create the output directory and write the document.

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

After writing the document, present a summary:

> **Data Exploration Report created** at `docs/crisp-dm/2-data-understanding/2.3-data-exploration.md`
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

Before finalizing the document, verify:
- [ ] Every analysis connects back to the data mining goals from 1.3
- [ ] The target variable distribution is thoroughly analyzed
- [ ] Temporal patterns are assessed (trend, seasonality, structural breaks) — critical for forecasting projects
- [ ] Correlation analysis covers both target-feature and feature-feature relationships
- [ ] Data leakage risks are explicitly assessed
- [ ] All visualizations have clear titles, axis labels, and are saved to `reports/figures/eda/`
- [ ] Feature hypotheses are actionable and prioritized
- [ ] Modeling implications are specific, not generic
- [ ] Subgroup analysis covers the key segmentation variables (stores, sections)
- [ ] No PII or sensitive data is included in the report or visualizations
- [ ] Code is reproducible (random seeds set, file paths explicit)
- [ ] Document cross-references the 2.1, 2.2, and 1.3 documents where applicable
