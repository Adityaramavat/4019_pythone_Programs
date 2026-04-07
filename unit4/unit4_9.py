import pandas as pd
import re

def filter_valid_emails(filename):
    """Reads a CSV and filters for valid emails using a Regular Expression."""
    try:
        # 1. Load the data into Pandas
        df = pd.read_csv(filename)
        
        # 2. Define the Regular Expression pattern for a valid email
        # This string of characters dictates the exact structure an email MUST have
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        
        # 3. Apply the regex to the 'E-Mail' column
        # .str.match() checks every single email against our pattern
        # na=False ensures that if a cell is blank/missing, it is automatically marked as invalid
        valid_students = df[df['E-Mail'].str.match(email_pattern, na=False)]
        
        # 4. Display the results
        print("--- Students with Valid Email Addresses ---")
        if valid_students.empty:
            print("No valid emails found in the dataset.")
        else:
            # Print just the RollNo, Name, and E-Mail columns to keep it neat
            print(valid_students[['RollNo', 'Name', 'E-Mail']])
            print("-" * 43)
            print(f"Total valid emails found: {len(valid_students)}")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# ==========================================
# EXECUTION
# ==========================================
if __name__ == "__main__":
    filter_valid_emails("students_data.csv")