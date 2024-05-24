from abc import ABC, abstractmethod
import math

# Step 1: Define the Shape Abstract Class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


# Step 2: Implement Circle and Rectangle Classes
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


# Step 3: Define the shape_info Function
def shape_info(shape):
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")


# Step 4: Testing the shape_info Function
circle = Circle(5)
rectangle = Rectangle(4, 6)

print("Circle Info:")
shape_info(circle)

print("\nRectangle Info:")
shape_info(rectangle)
