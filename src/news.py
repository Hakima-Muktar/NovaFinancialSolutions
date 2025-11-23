"""
EDA utilities for FNSPID project.
Contains small, reusable, and testable functions:
- load_news_csv
- headline_length_stats
- articles_per_publisher
"""

import pandas as pd

# -----------------------------
# 1. Load CSV with date parsing
# -----------------------------
def load_news_csv(path, tz_utc_offset=-4):
    """
    Load news CSV and parse the `date` column to UTC.

    Args:
        path (str): Path to CSV file
        tz_utc_offset (int): Dataset timezone offset in hours (default UTC-4)

    Returns:
        pd.DataFrame: DataFrame with parsed `date` column
    """
    df = pd.read_csv(path)
    if 'date' not in df.columns:
        raise ValueError("CSV must contain a 'date' column")
    
    df['date'] = pd.to_datetime(df['date'], errors='coerce')

    # Assign timezone if naive
    def ensure_tz(ts):
        if ts.tzinfo is None:
            return ts.tz_localize(f"Etc/GMT+{abs(tz_utc_offset)}") if not pd.isna(ts) else ts
        return ts

    df['date'] = df['date'].apply(lambda x: ensure_tz(x) if pd.notna(x) else x)

    # Convert to UTC
    try:
        df['date'] = df['date'].dt.tz_convert('UTC')
    except Exception:
        pass

    return df


# -----------------------------
# 2. Headline length statistics
# -----------------------------
def headline_length_stats(df):
    """
    Return descriptive statistics for headline lengths.

    Args:
        df (pd.DataFrame): DataFrame with `headline` column

    Returns:
        pd.Series: Descriptive statistics (count, mean, min, max, etc.)
    """
    return df['headline'].astype(str).str.len().describe()


# -----------------------------
# 3. Articles per publisher
# -----------------------------
def articles_per_publisher(df):
    """
    Count number of articles per publisher, sorted descending.

    Args:
        df (pd.DataFrame): DataFrame with `publisher` column

    Returns:
        pd.Series: Publisher counts sorted descending
    """
    return df['publisher'].fillna('unknown').value_counts()
