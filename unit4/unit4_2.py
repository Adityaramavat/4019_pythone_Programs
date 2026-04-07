import pandas as pd

def analyze_student_data(filename):
    """Loads a CSV file and filters the data based on specific conditions."""
    try:
        # Load the data into our DataFrame
        df = pd.read_csv(filename)
        
        print("\n--- 1. Students from Rajkot City ---")
        rajkot_students = df[df['City'] == 'Rajkot']
        
        if rajkot_students.empty:
            print("No students found from Rajkot (Check your CSV data!).")
        else:
            # We will just print specific columns to keep the output clean
            print(rajkot_students[['RollNo', 'Name', 'City']])

        print("\n--- 2. Male Students ---")
        male_students = df[df['Gender'] == 'Male']
        print(male_students[['RollNo', 'Name', 'Gender']])

        print("\n--- 3. Male Students from Rajkot City ---")
        male_rajkot = df[(df['Gender'] == 'Male') & (df['City'] == 'Rajkot')]
        
        if male_rajkot.empty:
            print("No male students found from Rajkot.")
        else:
            print(male_rajkot[['RollNo', 'Name', 'Gender', 'City']])

        print("\n--- 4. Students Age 20 or Older ---")
        older_students = df[df['Age'] >= 20]
        print(older_students[['RollNo', 'Name', 'Age']])


    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    analyze_student_data("students_data.csv")