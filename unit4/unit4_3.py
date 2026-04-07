import pandas as pd
import numpy as np

def handle_missing_data(filename):
    """Demonstrates how to handle missing data using Pandas."""
    try:
        # Load the data
        df = pd.read_csv(filename)
        
        df.loc[1, 'City'] = np.nan
        df.loc[3, 'Age'] = np.nan
        
        print("--- Original Data (with artificially missing values) ---")
        # df.head(5) just prints the first 5 rows so we don't flood your screen
        print(df[['RollNo', 'Name', 'Age', 'City']].head(5))
        
        print("\n--- 1. Using dropna() ---")
        # dropna() removes ANY row that contains at least one missing value (NaN)
        df_dropped = df.dropna()
        
        print("Notice that the rows with 'NaN' have been completely removed:")
        print(df_dropped[['RollNo', 'Name', 'Age', 'City']].head(5))

       
        print("\n--- 2. Using fillna() ---")
        # fillna() replaces missing values with whatever you tell it to.
        # Here, we tell it to fill missing Cities with 'Unknown' and missing Ages with 0.
        df_filled = df.fillna({'City': 'Unknown', 'Age': 0})
        
        print("Notice that 'NaN' is now replaced with 'Unknown' and '0.0':")
        print(df_filled[['RollNo', 'Name', 'Age', 'City']].head(5))


    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    handle_missing_data("students_data.csv")