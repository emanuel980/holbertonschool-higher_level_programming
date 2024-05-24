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
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        if width < 0 or height < 0:
            raise ValueError("Width and height cannot be negative")
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
def test_circle_negative():
    try:
        circle_negative = Circle(-5)
    except ValueError as e:
        assert str(e) == "Radius cannot be negative", "Radius error message mismatch"
    else:
        assert False, "ValueError not raised for negative radius"

def test_rectangle_negative():
    try:
        rectangle_negative = Rectangle(-4, 6)
    except ValueError as e:
        assert str(e) == "Width and height cannot be negative", "Width and height error message mismatch"
    else:
        assert False, "ValueError not raised for negative width"

    try:
        rectangle_negative = Rectangle(4, -6)
    except ValueError as e:
        assert str(e) == "Width and height cannot be negative", "Width and height error message mismatch"
    else:
        assert False, "ValueError not raised for negative height"

def main():
    # Run the negative tests
    test_circle_negative()
    test_rectangle_negative()

    # Create valid shapes and display their info
    circle = Circle(5)
    rectangle = Rectangle(4, 6)

    print("Circle Info:")
    shape_info(circle)

    print("\nRectangle Info:")
    shape_info(rectangle)

if __name__ == "__main__":
    main()
