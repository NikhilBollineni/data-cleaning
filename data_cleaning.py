import pandas as pd
from sklearn.preprocessing import StandardScaler


def clean_data(df):
    # Make a copy of the DataFrame to avoid modifying the original data
    df_clean = df.copy()

    # Convert all column names to lowercase and replace spaces with underscores
    df_clean.columns = df_clean.columns.str.lower().str.replace(' ', '_')

    # Replace missing numeric values with the column mean
    for col in df_clean.select_dtypes(include=['float64', 'int64']):
        df_clean[col] = df_clean[col].fillna(df_clean[col].mean())

    # Replace missing categorical values with the most common category
    for col in df_clean.select_dtypes(include=['object']):
        df_clean[col] = df_clean[col].fillna(df_clean[col].mode()[0])

    # Scale numeric columns to have mean 0 and variance 1
    scaler = StandardScaler()
    for col in df_clean.select_dtypes(include=['float64', 'int64']):
        df_clean[col] = scaler.fit_transform(df_clean[[col]])

    return df_clean
