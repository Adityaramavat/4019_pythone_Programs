class Computer:
    def __init__(self, brand):
        self.brand = brand
        # We create the inner class object right inside the outer class!
        self.cpu = self.CPU() 

    def show(self):
        print(f"Computer Brand: {self.brand}")
        self.cpu.show_cpu() # Calling the inner class method

    class CPU:
        def __init__(self):
            self.model = "Intel Core i7"

        def show_cpu(self):
            print(f"CPU Model: {self.model}")

# 1. Create the outer class object
my_pc = Computer("Dell")

# 2. Call the outer class method (which also calls the inner class method!)
my_pc.show()