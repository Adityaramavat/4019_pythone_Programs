import csv
import random

def generate_excel_file():
    """Generates a CSV file with 20 student records that can be opened in Excel."""
    
    # Sample data to pick from
    first_names_m = ["Aaron", "Bob", "Charlie", "David", "Ethan", "Frank", "George", "Henry", "Ian", "Jack"]
    first_names_f = ["Alice", "Bella", "Chloe", "Diana", "Emma", "Fiona", "Grace", "Hannah", "Isla", "Julia"]
    last_names = ["Smith", "Johnson", "Brown", "Davis", "Wilson", "Taylor", "Clark", "Lewis", "Walker", "Hall"]
    cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Seattle", "Denver", "Miami"]

    # Start with the header row
    data = [["RollNo", "Name", "Gender", "E-Mail", "Mobile", "Age", "City"]]

    # Generate 20 dummy records
    for i in range(1, 21):
        gender = random.choice(["Male", "Female"])
        
        # Pick a name based on gender
        if gender == "Male":
            name = f"{random.choice(first_names_m)} {random.choice(last_names)}"
        else:
            name = f"{random.choice(first_names_f)} {random.choice(last_names)}"
            
        # Generate an email based on the name
        email = f"{name.replace(' ', '.').lower()}@example.com"
        
        # Generate a random 10-digit mobile number starting with 9
        mobile = f"9{random.randint(100000000, 999999999)}"
        
        # Generate an age between 18 and 25
        age = random.randint(18, 25)
        
        # Pick a random city
        city = random.choice(cities)
        
        # Add the row to our data list
        data.append([i, name, gender, email, mobile, age, city])

    # Write the data to a file
    filename = "students_data.csv"
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

    print(f"Success! '{filename}' has been created with 20 records.")
    print("You can double-click this file to open it directly in Microsoft Excel.")

# ==========================================
# EXECUTION
# ==========================================
if __name__ == "__main__":
    generate_excel_file()