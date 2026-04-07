class Phone:
    """Base Class 1"""
    def make_call(self):
        print("Making a phone call...")

class Camera:
    """Base Class 2"""
    def take_picture(self):
        print("Taking a picture...")

# The SmartPhone class inherits from BOTH Phone and Camera
class SmartPhone(Phone, Camera):
    """Derived Class"""
    def browse_internet(self):
        print("Browsing the web...")

# 1. Create the object
my_device = SmartPhone()

# 2. Use functions from all the classes
print("--- Testing Functions ---")
my_device.make_call()       # From Phone
my_device.take_picture()    # From Camera
my_device.browse_internet() # From SmartPhone

# 3. Display the MRO (Method Resolution Order)
print("\n--- Method Resolution Order (MRO) ---")

# You can use the mro() method or the __mro__ attribute
for cls in SmartPhone.mro():
    print(cls.__name__)