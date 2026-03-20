---
name: baseline-model
description: Generate a baseline model for a given problem type. Use at the start of CRISP-DM Modeling phase -- always establish a baseline before complex models.
argument-hint: "[classification|regression|clustering|timeseries] [target column]"
user-invocable: true
---

# Baseline Model Generator (CRISP-DM Phase 4)

Generate a baseline model for: $ARGUMENTS

Based on problem type, create:

**Classification**: DummyClassifier (most_frequent, stratified), LogisticRegression with default params
**Regression**: DummyRegressor (mean, median), LinearRegression with default params
**Clustering**: KMeans with k=2,3,5, simple summary statistics
**Time Series**: Naive (last value), Seasonal naive, Simple moving average

The baseline script must:
1. Load the processed dataset
2. Split train/test (stratified for classification, temporal for time series)
3. Train the simplest possible model
4. Log metrics to MLflow/console
5. Save baseline metrics to reports/baseline_metrics.json
6. Print: "Any model that doesn't beat these numbers is not worth deploying"

This becomes the benchmark all future models must exceed.
