import matplotlib.pyplot as plt

def plot_course_pie_chart():
    """Takes course data from the user and plots a pie chart, exploding the largest slice."""
    courses = []
    students = []

    print("--- Enter Details for 5 Courses ---")
    
    # Loop 5 times to get the user input
    for i in range(5):
        course_name = input(f"Enter the name of course {i+1}: ").strip()
        
        # Ensure the user enters a valid integer for the student count
        while True:
            try:
                num_students = int(input(f"Enter the number of students in {course_name}: "))
                if num_students < 0:
                    print("Number of students cannot be negative. Try again.")
                    continue
                break
            except ValueError:
                print("Invalid input! Please enter a whole number.")
                
        courses.append(course_name)
        students.append(num_students)
        
    max_students = max(students)
    
    # 2. Find exactly which position (index) that maximum number is located at
    max_index = students.index(max_students)
    
    explode_list = []
    for i in range(len(courses)):
        if i == max_index:
            explode_list.append(0.1) # Pull out the biggest slice
        else:
            explode_list.append(0)

    plt.figure(figsize=(8, 6))
    plt.pie(students, labels=courses, explode=explode_list, autopct='%1.1f%%', 
            startangle=140, shadow=True)
    plt.title('Student Distribution by Course', fontsize=14, pad=20)
    print("\nGenerating pie chart...")
    plt.axis('equal') # This ensures the pie chart is drawn as a perfect circle, not an oval
    plt.show()

if __name__ == "__main__":
    plot_course_pie_chart()