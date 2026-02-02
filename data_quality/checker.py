import pandas as pd

def check_not_null(df, columns):
    report = {}
    for col in columns:
        null_count = df[col].isnull().sum()
        report[col] = null_count
    return report