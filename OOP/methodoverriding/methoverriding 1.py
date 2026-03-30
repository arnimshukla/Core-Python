class Shape():
    def area(self):
        return print("hello")

class rectangle(Shape):
    def area(self):
        return print("rectangle")

r=rectangle()
r.area()

s=Shape()
s.area()

sh : Shape=rectangle()
sh.area()