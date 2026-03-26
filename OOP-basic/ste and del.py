class Person:
    def __init__(self,name,age ):
        self.name=name
        self.age=age
    def __del__(self):
        classname=self.__class__.__name__
        print("destroy",classname)

    def __str__(self):
        return "Person:name=%s, age=%s"%(self.name,self.age)
p=Person("ABC",30)
p1=Person("asdf",2)
print(p)
print(p1)