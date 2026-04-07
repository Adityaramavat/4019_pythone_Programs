class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # 1. Overload the Addition (+) Operator
    def __add__(self, other):
        # Adds the x's together and the y's together, returning a new Point
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Point(new_x, new_y)

    # 2. Overload the Subtraction (-) Operator
    def __sub__(self, other):
        # Subtracts the x's and the y's, returning a new Point
        new_x = self.x - other.x
        new_y = self.y - other.y
        return Point(new_x, new_y)

    # This magic method just makes our print() statements look nice!
    def __str__(self):
        return f"({self.x}, {self.y})"
    
# Create two Point objects
p1 = Point(5, 7)
p2 = Point(2, 3)

# Use the overloaded '+' operator
p3 = p1 + p2

# Use the overloaded '-' operator
p4 = p1 - p2

print(f"Point 1: {p1}")
print(f"Point 2: {p2}")
print("-" * 20)
print(f"Addition (p1 + p2)    : {p3}")
print(f"Subtraction (p1 - p2) : {p4}")