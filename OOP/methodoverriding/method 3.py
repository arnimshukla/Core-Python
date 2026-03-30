class Shape():
    def exicute(self):
        if self.validation():
            self.area()
        else:
            print("validation failed")

    def validation(self):
        return False
    def area(self):
        print("shape area")

class reactangle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def validation(self):
        if self.length>0  and self.width>0:
            return True
        else:
            return False
    def area(self):
        rect_area=self.length*self.width
        print(rect_area)
        return rect_area

class ciurcule(Shape):
    pi=3.14
    def __init__(self,radius):
        self.radius=radius
    def validation(self):
        if self.radius>0:
            return True
        else:
            return False
    def area(self):
        ciurcule_area=self.pi*self.radius
        print(ciurcule_area)
        return ciurcule_area

class test(Shape):
    pass

r=reactangle(10,29)
r.exicute()

c=ciurcule(2)
c.exicute()

t=test()
t.exicute()