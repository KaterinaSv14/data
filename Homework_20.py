# 1
import math


class Figure:
    def method(self):
        pass


class Rectangle(Figure):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def method(self):
        return self.length * self.width


class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius

    def method(self):
        return math.pi * self.radius ** 2


class RightTriangle(Figure):
    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2

    def method(self):
        return 0.5 * self.side1 * self.side2


class Trapezoid(Figure):
    def __init__(self, side1, side2, height):
        self.side1 = side1
        self.side2 = side2
        self.height = height

    def method(self):
        return (self.side1 + self.side2) / 2 * self.height


rectangle = Rectangle(1, 2)
area_rectangle = rectangle.method()
print('Area of rectangle:', area_rectangle)

circle = Circle(1)
area_circle = circle.method()
print('Area of circle:', area_circle)

right_triangle = RightTriangle(1, 2)
area_triangle = right_triangle.method()
print('Area of right triangle:', area_triangle)

trapezoid = Trapezoid(1, 2, 3)
area_trapezoid = trapezoid.method()
print('Area of trapezoid:', area_trapezoid)


# 2
class Figure:
    def method(self):
        pass

    def __int__(self):
        return round(self.method())

    def __str__(self):
        return 'figure'


class Rectangle(Figure):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def method(self):
        return self.length * self.width

    def __str__(self):
        return 'rectangle'


class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius

    def method(self):
        return math.pi * self.radius ** 2

    def __str__(self):
        return 'circle'


class RightTriangle(Figure):
    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2

    def method(self):
        return 0.5 * self.side1 * self.side2

    def __str__(self):
        return 'right triangle'


class Trapezoid(Figure):
    def __init__(self, side1, side2, height):
        self.side1 = side1
        self.side2 = side2
        self.height = height

    def method(self):
        return (self.side1 + self.side2) / 2 * self.height

    def __str__(self):
        return 'trapezoid'


rectangle = Rectangle(1, 2)
print('Area of', rectangle, ':', int(rectangle))

circle = Circle(1)
print('Area of', circle, ':', int(circle))

right_triangle = RightTriangle(1, 2)
print('Area of', right_triangle, ':', int(right_triangle))

trapezoid = Trapezoid(1, 2, 3)
print('Area of', trapezoid, ':', int(trapezoid))
