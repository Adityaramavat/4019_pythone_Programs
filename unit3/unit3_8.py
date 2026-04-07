from abc import ABC, abstractmethod
# 1. Create the Abstract Base Class
class Shape(ABC):
    
    # 2. Define the abstract method using a decorator
    @abstractmethod
    def area(self):
        pass  # We leave this blank because child classes will fill it in!

# 3. Create a Child Class that inherits from the abstract class
class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length
        
    # 4. We MUST implement the area() method here, otherwise Python will throw an error
    def area(self):
        return self.side_length * self.side_length

# Note: If we tried to do `my_shape = Shape()`, Python would give an error!
# We have to use the child class that actually builds the method.

my_square = Square(5)
print(f"The area of the square is: {my_square.area()}")