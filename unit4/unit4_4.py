import matplotlib.pyplot as plt

def plot_profit():
    """Takes 5 years of profit data from the user and plots a line graph."""
    years = []
    profits = []

    print("--- Enter Profit Details for 5 Years ---")
    
    # Loop 5 times to get the user input
    for i in range(5):
        year = input(f"Enter year {i+1} (e.g., 2019): ").strip()
        
        # We use a while loop to ensure the user types a valid number for profit
        while True:
            try:
                profit = float(input(f"Enter profit for {year}: "))
                break # Exit the while loop if conversion to float succeeds
            except ValueError:
                print("Invalid input! Please enter a numerical value for profit.")
                
        years.append(year)
        profits.append(profit)
    
    # Plot the data: marker='o' adds dots at each data point
    plt.plot(years, profits, marker='o', color='blue', linestyle='-', linewidth=2)
    
    # Add title and labels to the axes
    plt.title('Company Profit Over 5 Years', fontsize=14)
    plt.xlabel('Year', fontsize=12)
    plt.ylabel('Profit', fontsize=12)
    
    # Add a grid to make the graph easier to read
    plt.grid(True, linestyle='--', alpha=0.7)
    
    # Display the final graph on the screen
    print("\nGenerating graph...")
    plt.show()

if __name__ == "__main__":
    plot_profit()