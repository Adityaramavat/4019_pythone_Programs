class Student:
    """The Base Class"""
    def __init__(self, rollno, name, gender, age):
        self.rollno = rollno
        self.name = name
        self.gender = gender
        self.age = age

class Course(Student):
    """The Derived Class inheriting from Student"""
    def __init__(self, rollno, name, gender, age, coursename, duration, fee):
        # super() automatically calls the __init__ of the base class (Student)
        super().__init__(rollno, name, gender, age) 
        self.coursename = coursename
        self.duration = duration
        self.fee = fee
        
    def display_details(self):
        """Prints all the combined details."""
        print("--- Student & Course Details ---")
        print(f"Roll No : {self.rollno}")
        print(f"Name    : {self.name} ({self.gender}, {self.age} years old)")
        print(f"Course  : {self.coursename} ({self.duration})")
        print(f"Fee     : ${self.fee}")
# Create an object of the DERIVED class
# Notice how we pass both the Student info AND the Course info at the same time
my_course = Course(101, "John Doe", "Male", 20, "Python Programming", "3 Months", 150)

# Display everything
my_course.display_details()