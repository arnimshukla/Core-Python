class  Shape:
    def __init__(self):
        self.color=''
        self.borderwidth=0


    def getcolor(self):
        return self.color
    def setcolor(self,color):
        self.color=color
    def getborderwidth (self):
        return self.borderwidth
    def setborderwidth(self,border):
        self.borderwidth=border

class Rectangle(Shape):
     def __init__(self):
         self.length=0
         self.width=0
     def getlength(self):
        return self.length
     def setlength(self,l):
        self.length=l
     def getwidth(self):
        return self.width
     def setwidth(self,w):
         self.width=w



r=Rectangle()
r.setlength(10)
r.setwidth=(20)
r.setcolor("black")
r.setborderwidth(11)

print(r.getlength())
print(r.getwidth())
print(r.getcolor())
print(r.getborderwidth())


