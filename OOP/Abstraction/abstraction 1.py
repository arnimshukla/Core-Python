from abc import ABC,abstractmethod

class Shape(ABC):

    def execute(self):
        self.area()

    @abstractmethod
    def area(self):
        pass
# 
s=Shape