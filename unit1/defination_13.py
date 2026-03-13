#13.Write a program to make use of map(), filter() and reduce() functions with context to lambda functions.

from functools import reduce

# list of numbers
numbers = [1, 2, 3, 4, 5, 6]
print(f"Original List: {numbers}")

# 1. MAP: Apply a change to every item
# Goal: Square every number (x^2)
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(f"1. Map (Squared): {squared_numbers}")

# 2. FILTER: Select items based on a condition
# Goal: Keep only numbers greater than 3
big_numbers = list(filter(lambda x: x > 3, numbers))
print(f"2. Filter (> 3):  {big_numbers}")

# 3. REDUCE: Combine all items into a single result
# Goal: Multiply all numbers together (1*2*3*4*5*6)
product = reduce(lambda x, y: x * y, numbers)
print(f"3. Reduce (Product): {product}")
