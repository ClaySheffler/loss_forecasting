import pandas as pd

def load_input_data(filepath):
    """Load input data from an Excel or CSV file."""
    if filepath.endswith(".csv"):
        return pd.read_csv(filepath)
    elif filepath.endswith(".xlsx"):
        return pd.read_excel(filepath)
    else:
        raise ValueError("Unsupported file format")

def save_output_data(df, filepath):
    """Save DataFrame to CSV or Excel."""
    if filepath.endswith(".csv"):
        df.to_csv(filepath, index=False)
    elif filepath.endswith(".xlsx"):
        df.to_excel(filepath, index=False)
    else:
        raise ValueError("Unsupported file format")