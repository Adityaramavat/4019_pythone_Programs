import matplotlib.pyplot as plt
import random

def create_age_histogram():
    """Generates 50 student ages and plots them in a grouped histogram."""
    
    # 1. Gather the Data
    # For testing, we automatically generate 50 random ages between 5 and 65
    print("Generating 50 random student ages...")
    ages = [random.randint(5, 65) for _ in range(50)]
    bin_edges = [0, 11, 21, 31, 41, 51, 61, 121]
    plt.hist(ages, bins=bin_edges, color='lightgreen', edgecolor='black')
    plt.title('Student Age Distribution (Histogram)', fontsize=14)
    plt.xlabel('Age Groups', fontsize=12)
    plt.ylabel('Number of Students', fontsize=12)
    plt.xticks(bin_edges)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    print("\nGenerating histogram...")
    plt.show()

if __name__ == "__main__":
    create_age_histogram()