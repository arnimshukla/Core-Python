from  abc import ABC,abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class reactangle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width

    def area(self):
        return self.width*self.length

r=reactangle(5,10)
print(r.area())

shape: Shape=reactangle(5,10)
print(shape.area())