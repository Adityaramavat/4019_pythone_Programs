# Dictionary to act as our database
# It will store data like this: {'101': {'name': 'Alice', 'course': 'Math'}}
students = {}

def display_menu():
    """Prints the main menu options."""
    print("\n" + "="*35)
    print("     STUDENT MANAGEMENT SYSTEM")
    print("="*35)
    print(" a) Add Student")
    print(" b) Search Student")
    print(" c) List All Students")
    print(" d) Update Student")
    print(" e) Delete Student")
    print(" f) Exit")
    print("="*35)

def add_student():
    """Adds a new student to the dictionary."""
    roll_no = input("Enter Roll Number: ").strip()
    
    if roll_no in students:
        print("Error: A student with this Roll Number already exists!")
    else:
        name = input("Enter Student Name: ").strip()
        course = input("Enter Course/Class: ").strip()
        
        # Add the new student to our dictionary
        students[roll_no] = {'name': name, 'course': course}
        print(f"Success! Student '{name}' added.")

def search_student():
    """Finds and displays a specific student by Roll Number."""
    roll_no = input("Enter Roll Number to search: ").strip()
    
    if roll_no in students:
        student = students[roll_no]
        print("\n--- Student Details ---")
        print(f"Roll No : {roll_no}")
        print(f"Name    : {student['name']}")
        print(f"Course  : {student['course']}")
        print("-----------------------")
    else:
        print("Error: Student not found!")

def list_all_students():
    """Displays all students currently in the system."""
    if not students:
        print("No students found. The list is empty.")
        return
    
    print("\n" + "-" * 50)
    print(f"{'Roll No':<10} | {'Student Name':<20} | {'Course'}")
    print("-" * 50)
    
    for roll_no, details in students.items():
        print(f"{roll_no:<10} | {details['name']:<20} | {details['course']}")
    print("-" * 50)

def update_student():
    """Allows updating an existing student's name or course."""
    roll_no = input("Enter Roll Number to update: ").strip()
    
    if roll_no in students:
        print("Leave the input blank and press Enter if you do not want to change a field.")
        
        current_name = students[roll_no]['name']
        current_course = students[roll_no]['course']
        
        new_name = input(f"Enter new Name (Current: {current_name}): ").strip()
        new_course = input(f"Enter new Course (Current: {current_course}): ").strip()
        
        # Only update if the user actually typed something new
        if new_name:
            students[roll_no]['name'] = new_name
        if new_course:
            students[roll_no]['course'] = new_course
            
        print("Success! Student details updated.")
    else:
        print("Error: Student not found!")

def delete_student():
    """Removes a student from the dictionary."""
    roll_no = input("Enter Roll Number to delete: ").strip()
    
    if roll_no in students:
        # pop() removes the item and returns it, so we can print the deleted name
        deleted_student = students.pop(roll_no)
        print(f"Success! Student '{deleted_student['name']}' has been deleted.")
    else:
        print("Error: Student not found!")

def main():
    """The main loop that runs the menu system."""
    while True:
        display_menu()
        choice = input("Enter your choice (a-f): ").strip().lower()
        
        if choice == 'a':
            add_student()
        elif choice == 'b':
            search_student()
        elif choice == 'c':
            list_all_students()
        elif choice == 'd':
            update_student()
        elif choice == 'e':
            delete_student()
        elif choice == 'f':
            print("Exiting program. Goodbye!")
            break  # This breaks the while loop and ends the program
        else:
            print("Invalid choice! Please type a letter between 'a' and 'f'.")

# This is the standard way to start a Python script
if __name__ == "__main__":
    main()