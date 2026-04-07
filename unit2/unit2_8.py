import csv

def calculate_grade(percentage):
    """Determines the grade based on the percentage."""
    if percentage >= 90:
        return 'A'
    elif percentage >= 80:
        return 'B'
    elif percentage >= 70:
        return 'C'
    elif percentage >= 60:
        return 'D'
    else:
        return 'F'

def process_marks(filename):
    """Reads the file, calculates scores, and displays the details."""
    try:
        # Open the file in read mode
        with open(filename, mode='r') as file:
            reader = csv.reader(file)
            
            # Print the header for our output table
            print("-" * 65)
            print(f"{'RollNo':<8} | {'Student Name':<15} | {'Total':<6} | {'Percentage':<11} | {'Grade'}")
            print("-" * 65)
            
            for row in reader:
                # Ensure the row has the correct number of columns
                if len(row) != 6:
                    continue
                
                # Extract basic info and strip any extra spaces
                roll_no = row[0].strip()
                name = row[1].strip()
                
                # Try to convert marks to floats. 
                # If it fails (like on the header row), we skip to the next line.
                try:
                    mark1 = float(row[2].strip())
                    mark2 = float(row[3].strip())
                    mark3 = float(row[4].strip())
                    mark4 = float(row[5].strip())
                except ValueError:
                    continue
                
                # Calculations (Assuming each subject is out of 100, total = 400)
                total_marks = mark1 + mark2 + mark3 + mark4
                percentage = (total_marks / 400) * 100
                grade = calculate_grade(percentage)
                
                # Display the formatted results
                print(f"{roll_no:<8} | {name:<15} | {total_marks:<6.0f} | {percentage:<10.2f}% | {grade}")
                
            print("-" * 65)

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found. Please ensure it exists.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the function with our sample file
process_marks('student.csv')