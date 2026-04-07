class Student:
    """A class to represent a student."""
    
    def __init__(self):
        # Initialize the attributes with default/empty values
        self.RollNo = ""
        self.Name = ""
        self.Age = 0
        self.Gender = ""

    def AddStudent(self):
        """Asks the user to input the student's details."""
        print("--- Enter Student Information ---")
        self.RollNo = input("Enter Roll Number: ").strip()
        self.Name = input("Enter Name: ").strip()
        self.Age = input("Enter Age: ").strip()
        self.Gender = input("Enter Gender: ").strip()
        print("Student added successfully!\n")

    def DisplayStudent(self):
        """Displays the stored student details."""
        print("--- Student Details ---")
        print(f"Roll No : {self.RollNo}")
        print(f"Name    : {self.Name}")
        print(f"Age     : {self.Age}")
        print(f"Gender  : {self.Gender}")
        print("-" * 23)

# ==========================================
# EXECUTION
# ==========================================

# 1. Create a new Student object
student1 = Student()

# 2. Call the method to add data (this will prompt you to type)
student1.AddStudent()

# 3. Call the method to display the data you just typed
student1.DisplayStudent()