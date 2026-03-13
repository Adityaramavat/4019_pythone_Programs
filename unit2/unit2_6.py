''' 6. Write a program to read a file which contains only numbers. Display total
of all numbers with maximum and minimum number.'''

def analyze_numbers_file(filename):
    try:
        numbers = []
        
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if line:  # Skip empty lines
                    # Split line by whitespace and convert to numbers
                    for num_str in line.split():
                        numbers.append(float(num_str))
        
        if not numbers:
            print("No numbers found in the file.")
            return
        
        total = sum(numbers)
        maximum = max(numbers)
        minimum = min(numbers)
        
        print(f"Total of all numbers: {total}")
        print(f"Maximum number: {maximum}")
        print(f"Minimum number: {minimum}")
        print(f"Total numbers processed: {len(numbers)}")
        
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except ValueError:
        print("Error: File contains non-numeric data.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Usage
filename = "numeric.txt"  # Replace with your file name
analyze_numbers_file(filename)
