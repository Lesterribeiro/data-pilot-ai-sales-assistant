"""
Processamento do dataset de vendas
"""

import pandas as pd


def clean_data(df):

    df = df.copy()

    df.columns = (
        df.columns
        .str.lower()
        .str.strip()
    )

    df = df.drop_duplicates()

    df["status"] = (
        df["status"]
        .astype(str)
        .str.lower()
        .str.strip()
    )

    df["revenue"] = (
        df["quantity"] * df["price"]
    )

    return df
