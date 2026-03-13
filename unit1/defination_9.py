def calculate(num1, num2, operator):
    # Check which operator was entered and perform the math
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        # Check to make sure we don't divide by zero
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Cannot divide by zero"
    else:
        return "Invalid Operator"
# 1. Take input from the user
number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")


answer = calculate(number1, number2, op)
print("The result is:", answer)
