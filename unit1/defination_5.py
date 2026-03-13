# Initialize variable to store the largest odd number
largest_odd = None

print("Enter 10 numbers:")

for i in range(10):
    num = int(input(f"Number {i+1}: "))
    
    # Check if the number is odd
    if num % 2 != 0:
        if largest_odd is None or num > largest_odd:
            largest_odd = num

# Display the largest odd number
if largest_odd is not None:
    print("Largest odd number is:", largest_odd)
else:
    print("No odd number entered.")