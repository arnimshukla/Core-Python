from typing import List


class Shape:
    def area(self):
        print("shape area")


class reactangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        rect_area = self.width * self.length
        print(rect_area)
        return rect_area


class cicle(Shape):
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        circle_radius = self.pi * self.radius * self.radius
        print(circle_radius)
        return circle_radius

shapes: List[Shape] = [cicle(8), reactangle(10, 19)]

for shape in shapes:
    shape.area()
