class Car:
    # A class variable to keep track of total cars
    total_cars_built = 0

    def __init__(self, brand):
        self.brand = brand  # Instance variable
        Car.total_cars_built += 1

    # 1. INSTANCE METHOD (Uses 'self')
    def drive(self):
        print(f"The {self.brand} is driving!")

    # 2. CLASS METHOD (Uses 'cls' and a decorator)
    @classmethod
    def show_total_cars(cls):
        print(f"Total cars built so far: {cls.total_cars_built}")
# Create two individual car objects
car1 = Car("Toyota")
car2 = Car("Honda")

# Call the INSTANCE method on a specific car
car1.drive() 
car2.drive()

# Call the CLASS method directly on the class itself
Car.show_total_cars()