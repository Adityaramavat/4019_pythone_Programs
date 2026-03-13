# 1. simple exception handling program

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    
    result = num1 / num2
    
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

except ValueError:
    print("Error: Please enter valid integers.")

else:
    # Executes if no exception occurs
    print("Result is:", result)

finally:
    # Always executes
    print("Program execution completed.")
