class Dog:
    """A simple class representing a dog."""
    
    # The __init__ method initializes the object's attributes
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    # Method 1
    def bark(self):
        """Simulates the dog barking."""
        print(f"{self.name} says: Woof! Woof!")

    # Method 2
    def fetch(self, item):
        """Simulates the dog fetching an item."""
        print(f"{self.name}, the {self.breed}, excitedly runs and brings back the {item}.")
# 1. Create an object (an instance) of the Dog class
my_dog = Dog("Buddy", "Golden Retriever")

# 2. Execute the first method
my_dog.bark()

# 3. Execute the second method
my_dog.fetch("tennis ball")