"""
Feature engineering module for Titanic survival prediction.

Constructs derived attributes from cleaned data (3.2 output).
All transformations are fit on training data only.
"""

import numpy as np
import pandas as pd

from src.cleaning import extract_title, map_rare_titles


def add_title(df: pd.DataFrame) -> pd.DataFrame:
    """Extract title from Name, mapped to 4 groups: Mr, Mrs, Miss, Master."""
    out = df.copy()
    out["Title"] = out["Name"].apply(extract_title).apply(map_rare_titles)
    return out


def add_family_features(df: pd.DataFrame) -> pd.DataFrame:
    """Add FamilySize, FamilySizeBin, and IsAlone."""
    out = df.copy()
    out["FamilySize"] = out["SibSp"] + out["Parch"] + 1
    out["FamilySizeBin"] = pd.cut(
        out["FamilySize"],
        bins=[0, 1, 4, 99],
        labels=["Small", "Medium", "Large"],
    )
    out["IsAlone"] = (out["FamilySize"] == 1).astype(int)
    return out


def add_cabin_features(df: pd.DataFrame) -> pd.DataFrame:
    """Add HasCabin (binary) and Deck (first letter of Cabin)."""
    out = df.copy()
    out["HasCabin"] = out["Cabin"].notna().astype(int)
    out["Deck"] = out["Cabin"].str[0].fillna("Unknown")
    return out


def add_fare_log(df: pd.DataFrame) -> pd.DataFrame:
    """Add log-transformed Fare."""
    out = df.copy()
    out["FareLog"] = np.log1p(out["Fare"])
    return out


def compute_ticket_group_sizes(train_df: pd.DataFrame, test_df: pd.DataFrame) -> dict:
    """Compute ticket group sizes from combined train+test data.

    Ticket groups span both datasets (families may be split across train/test),
    so we compute group sizes on the union to get accurate counts.
    """
    combined_tickets = pd.concat(
        [train_df["Ticket"], test_df["Ticket"]], ignore_index=True
    )
    return combined_tickets.value_counts().to_dict()


def add_ticket_group_size(df: pd.DataFrame, ticket_sizes: dict) -> pd.DataFrame:
    """Add TicketGroupSize using pre-computed ticket counts."""
    out = df.copy()
    out["TicketGroupSize"] = out["Ticket"].map(ticket_sizes)
    return out


def encode_sex(df: pd.DataFrame) -> pd.DataFrame:
    """Binary encode Sex: female=1, male=0."""
    out = df.copy()
    out["Sex"] = out["Sex"].map({"female": 1, "male": 0})
    return out


def encode_embarked(df: pd.DataFrame) -> pd.DataFrame:
    """One-hot encode Embarked with drop_first=True (drops C)."""
    out = df.copy()
    dummies = pd.get_dummies(out["Embarked"], prefix="Embarked", drop_first=True)
    dummies = dummies.astype(int)
    out = pd.concat([out, dummies], axis=1)
    out = out.drop(columns=["Embarked"])
    return out


def encode_family_size_bin(df: pd.DataFrame) -> pd.DataFrame:
    """Ordinal encode FamilySizeBin: Small=0, Medium=1, Large=2."""
    out = df.copy()
    mapping = {"Small": 0, "Medium": 1, "Large": 2}
    out["FamilySizeBin"] = out["FamilySizeBin"].map(mapping)
    return out


def build_features(
    df: pd.DataFrame, ticket_sizes: dict, encode: bool = True
) -> pd.DataFrame:
    """Full feature engineering pipeline.

    Args:
        df: Cleaned DataFrame from clean_dataset().
        ticket_sizes: Pre-computed ticket group sizes from compute_ticket_group_sizes().
        encode: If True, apply encoding (Sex binary, Embarked one-hot, FamilySizeBin ordinal).

    Returns:
        DataFrame with all engineered features added.
    """
    out = df.copy()
    out = add_title(out)
    out = add_family_features(out)
    out = add_cabin_features(out)
    out = add_fare_log(out)
    out = add_ticket_group_size(out, ticket_sizes)

    if encode:
        out = encode_sex(out)
        out = encode_embarked(out)
        out = encode_family_size_bin(out)

    return out
