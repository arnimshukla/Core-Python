class Shape():
    def execute(self):
        print("exxicute")
        self.area()
    def area(self):
        return print("shape")

class rectangle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width


    def area(self):
        rect=self.width*self.length
        print("rectangle",rect)
        return rect

class circule(Shape):
    pi=3.14

    def __init__(self,radius):
        self.radius=radius

    def area(self):
        curcle = self.radius*self.pi
        print(curcle)
        return curcle

r=rectangle(10,20)
r.execute()

c=circule(2)
c.execute()