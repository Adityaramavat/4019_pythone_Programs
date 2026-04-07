import pandas as pd

def display_column_info(filename):
    """Loads a CSV/Excel file and displays its columns and data types."""
    try:
        # 1. Load the data into a Pandas DataFrame
        df = pd.read_csv(filename)
        
        # 2. Display the results
        print(f"--- Column Names and Data Types for '{filename}' ---")
        
        # df.dtypes automatically lists all columns and what type of data they hold
        print(df.dtypes)
        print("-" * 50)
        
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    display_column_info("students_data.csv")