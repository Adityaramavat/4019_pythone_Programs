import pandas as pd
import matplotlib.pyplot as plt

def plot_gender_distribution(filename):
    """Reads a student data file and plots a bar graph of Male vs Female counts."""
    try:
        # 1. Load the data using Pandas
        df = pd.read_csv(filename)
        gender_counts = df['Gender'].value_counts()
        gender_counts = gender_counts.sort_values()
        print("--- Student Gender Counts ---")
        print(gender_counts.to_string())
        print("-----------------------------")

        # 3. Create the Bar Graph
        plt.figure(figsize=(6, 5))
        plt.bar(gender_counts.index, gender_counts.values, color=['lightcoral', 'skyblue'], edgecolor='black')
        plt.title('Number of Male and Female Students', fontsize=14)
        plt.xlabel('Gender', fontsize=12)
        plt.ylabel('Number of Students', fontsize=12)
        
        # Display the graph
        print("\nGenerating bar graph...")
        plt.tight_layout()
        plt.show()

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    plot_gender_distribution("students_data.csv")