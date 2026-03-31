"""
Data cleaning module for Titanic survival prediction.

Handles missing value imputation for Age, Embarked, and Fare.
All imputation parameters are fit on training data only.
"""

import re

import numpy as np
import pandas as pd


def extract_title(name: str) -> str:
    """Extract title from passenger name (e.g. 'Braund, Mr. Owen Harris' -> 'Mr')."""
    match = re.search(r",\s*(\w+)\.", name)
    if match:
        return match.group(1)
    return "Unknown"


def map_rare_titles(title: str) -> str:
    """Map rare titles to common groups for imputation."""
    title_map = {
        "Mr": "Mr",
        "Miss": "Miss",
        "Mrs": "Mrs",
        "Master": "Master",
        "Dr": "Mr",
        "Rev": "Mr",
        "Col": "Mr",
        "Major": "Mr",
        "Mlle": "Miss",
        "Ms": "Miss",
        "Mme": "Mrs",
        "Sir": "Mr",
        "Capt": "Mr",
        "Don": "Mr",
        "Dona": "Mrs",
        "Lady": "Mrs",
        "Countess": "Mrs",
        "Jonkheer": "Mr",
    }
    return title_map.get(title, "Mr")


def compute_imputation_params(train_df: pd.DataFrame) -> dict:
    """Compute all imputation parameters from the training set.

    Returns a dict of parameters to be applied to both train and test.
    """
    df = train_df.copy()
    df["_Title"] = df["Name"].apply(extract_title).apply(map_rare_titles)

    # Age: median per title group
    age_medians = df.groupby("_Title")["Age"].median().to_dict()

    # Embarked: mode
    embarked_mode = df["Embarked"].mode()[0]

    # Fare: median per Pclass
    fare_medians = df.groupby("Pclass")["Fare"].median().to_dict()

    return {
        "age_medians_by_title": age_medians,
        "embarked_mode": embarked_mode,
        "fare_medians_by_pclass": fare_medians,
    }


def clean_dataset(df: pd.DataFrame, params: dict) -> pd.DataFrame:
    """Apply cleaning operations to a DataFrame using pre-computed parameters.

    Args:
        df: Raw DataFrame (train or test).
        params: Imputation parameters from compute_imputation_params().

    Returns:
        Cleaned DataFrame with missing values imputed and AgeMissing indicator added.
    """
    out = df.copy()

    # Extract title for Age imputation
    out["_Title"] = out["Name"].apply(extract_title).apply(map_rare_titles)

    # Age: add missingness indicator, then impute by title group
    out["AgeMissing"] = out["Age"].isna().astype(int)
    for title, median_age in params["age_medians_by_title"].items():
        mask = (out["Age"].isna()) & (out["_Title"] == title)
        out.loc[mask, "Age"] = median_age

    # Fill any remaining Age NaN with overall median from params
    overall_age_median = np.median(list(params["age_medians_by_title"].values()))
    out["Age"] = out["Age"].fillna(overall_age_median)

    # Embarked: impute with training mode
    out["Embarked"] = out["Embarked"].fillna(params["embarked_mode"])

    # Fare: impute with Pclass-specific median from training
    if out["Fare"].isna().any():
        for pclass, median_fare in params["fare_medians_by_pclass"].items():
            mask = (out["Fare"].isna()) & (out["Pclass"] == pclass)
            out.loc[mask, "Fare"] = median_fare

    # Drop temporary column
    out = out.drop(columns=["_Title"])

    return out
