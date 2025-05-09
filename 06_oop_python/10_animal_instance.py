# Create a class Dog
class Dog:
    def __init__(self, name, breed):
        self.name = name  # Instance variable
        self.breed = breed  # Instance variable

    def bark(self):
        print(f"{self.name} says woof!")  # Instance method

# Create an object of Dog class
dog1 = Dog("Buddy", "Golden Retriever")

# Call the bark method
dog1.bark()
