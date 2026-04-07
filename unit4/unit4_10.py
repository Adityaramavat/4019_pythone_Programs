import pandas as pd
import re

def filter_country_code_mobile(filename):
    """Filters for mobile numbers formatted as 2-digit country code + 10-digit number."""
    try:
        # 1. Load the data into Pandas
        df = pd.read_csv(filename)
        
        # --- SETUP: Artificially insert test data ---
        # We will add a few specific formats to test our regex!
        df.loc[0, 'Mobile'] = '91-9999933333'  # VALID (2 digits - 10 digits)
        df.loc[2, 'Mobile'] = '44-1234567890'  # VALID (2 digits - 10 digits)
        df.loc[4, 'Mobile'] = '1-8005551234'   # INVALID (1 digit country code)
        df.loc[5, 'Mobile'] = '919876543210'   # INVALID (Missing the hyphen)
        
        # 2. Define the Regular Expression pattern
        # \d{2}   -> Exactly 2 digits
        # -       -> A literal hyphen
        # \d{10}  -> Exactly 10 digits
        mobile_pattern = r'^\d{2}-\d{10}$'
        
        # 3. Apply the regex to the 'Mobile' column
        # We use .astype(str) just in case Pandas accidentally read any plain numbers as integers
        valid_mobiles = df[df['Mobile'].astype(str).str.match(mobile_pattern, na=False)]
        
        # 4. Display the results
        print("--- Students with Valid Country Code Mobile Numbers ---")
        if valid_mobiles.empty:
            print("No valid formatted mobile numbers found in the dataset.")
        else:
            print(valid_mobiles[['RollNo', 'Name', 'Mobile']])

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# ==========================================
# EXECUTION
# ==========================================
if __name__ == "__main__":
    filter_country_code_mobile("students_data.csv")