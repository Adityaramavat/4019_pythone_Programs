#2.Basic Custom Exception Example
class InvalidAgeError(Exception):
    pass

# Step 2: Use the custom exception
try:
    age = int(input("Enter your age: "))
    
    if age < 18:
        raise InvalidAgeError("Age must be 18 or above.")
    
    print("You are eligible.")

except InvalidAgeError as e:
    print("Custom Exception Caught:", e)

except ValueError:
    print("Please enter a valid number.")

finally:
    print("Program ended.")
