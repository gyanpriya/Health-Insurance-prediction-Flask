#data_load_eda.py
import pandas as pd

def load_data(file_path):
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
        return None
    except pd.errors.EmptyDataError:
        print("Error: The file is empty.")
        return None
    except pd.errors.ParserError:
        print("Error: There was an issue parsing the file.")
        return None

def basic_eda(df):
    shape = df.shape
    missing_entries = df.isnull().sum().sum()
    duplicate_entries = df.duplicated().sum()
    return shape, missing_entries, duplicate_entries
