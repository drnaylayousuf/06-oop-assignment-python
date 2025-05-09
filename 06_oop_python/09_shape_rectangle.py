from abc import ABC, abstractmethod

# Abstract class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass  # No body, just a rule for child classes

# Rectangle class inherits Shape
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Create object of Rectangle
rect = Rectangle(4, 5)


print("Area of rectangle:", rect.area())
