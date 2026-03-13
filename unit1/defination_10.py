# 1. Define the 4 lambda functions for each operation
add = lambda a, b: a + b
sub = lambda a, b: a - b
mul = lambda a, b: a * b
div = lambda a, b: a / b

# 2. Take input from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

# 3. Check the operator and call the matching lambda function
if operator == '+':
    result = add(num1, num2)
elif operator == '-':
    result = sub(num1, num2)
elif operator == '*':
    result = mul(num1, num2)
elif operator == '/':
    if num2 != 0:
        result = div(num1, num2)
    else:
        result = "Error: Cannot divide by zero"
else:
    result = "Invalid Operator"
    
print(f"The answer is: {result}")
