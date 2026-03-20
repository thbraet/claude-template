---
name: eda-notebook
description: Generate a comprehensive EDA notebook template for a dataset. Use during CRISP-DM Data Understanding phase.
argument-hint: "[dataset path or description]"
user-invocable: true
---

# EDA Notebook Generator (CRISP-DM Phase 2)

Create a comprehensive EDA notebook for: $ARGUMENTS

The notebook should include these sections:

1. **Header cell**: Title, author, date, "CRISP-DM Phase: Data Understanding", purpose
2. **Imports**: pandas, numpy, matplotlib, seaborn, plotly (if available)
3. **Data Loading**: Read the dataset, display shape, dtypes, head()
4. **Overview**: df.info(), df.describe(), memory usage
5. **Missing Values**: Heatmap of nulls, percentage per column, MCAR/MAR/MNAR assessment
6. **Univariate Analysis**: Histograms for numerics, value counts for categoricals, box plots
7. **Bivariate Analysis**: Correlation matrix heatmap, scatter plots for top correlations, cross-tabs
8. **Target Variable Analysis** (if applicable): Distribution, class balance, relationship with features
9. **Temporal Patterns** (if date columns exist): Trends, seasonality, stationarity
10. **Outlier Detection**: IQR-based, z-score, visual inspection
11. **Data Quality Summary**: Table of issues found per column
12. **Hypotheses**: List of initial hypotheses for modeling
13. **Conclusions & Next Steps**: Summary of findings, recommended next actions

Name the notebook following convention: `{number}-du-eda-{description}-{initials}.ipynb`
