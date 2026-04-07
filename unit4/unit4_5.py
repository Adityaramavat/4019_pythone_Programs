import matplotlib.pyplot as plt

def plot_company_employees():
    """Takes 5 companies and their employee sizes from the user and plots a bar graph."""
    companies = []
    employees = []

    print("--- Enter Details for 5 Companies ---")
    
    # Loop 5 times to get the user input
    for i in range(5):
        company = input(f"Enter the name of company {i+1}: ").strip()
        
        # We use a while loop to ensure the user types a valid integer for employees
        while True:
            try:
                emp_size = int(input(f"Enter the employee size for {company}: "))
                if emp_size < 0:
                    print("Employee size cannot be negative. Try again.")
                    continue
                break # Exit the while loop if conversion to int succeeds
            except ValueError:
                print("Invalid input! Please enter a whole number.")
                
        companies.append(company)
        employees.append(emp_size)

    combined_data = list(zip(employees, companies))
    combined_data.sort() 
    sorted_employees = [item[0] for item in combined_data]
    sorted_companies = [item[1] for item in combined_data]
    plt.bar(sorted_companies, sorted_employees, color='skyblue', edgecolor='black')
    plt.title('Employee Size by Company', fontsize=14)
    plt.xlabel('Company Name', fontsize=12)
    plt.ylabel('Number of Employees', fontsize=12)
    print("\nGenerating bar graph...")
    plt.tight_layout() 
    plt.show()
if __name__ == "__main__":
    plot_company_employees()