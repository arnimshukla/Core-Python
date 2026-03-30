class student:
    def getstudent(self):
        self.name=input("Name:")
        self.gender=input("gender:")
        self.age=input("age:")


class Test(student):
    def gettest(self):
        self.getstudentclass=input("class:")
        self.english=input("english marks:")
        self.hindi=input("hindi marks:")
        self.math=input("math marks:")

class marks(Test):
    def display(self):
        print(self.name)
        print(self.age)
        print(self.gender)
        print(self.getstudentclass)
        total=self.english+self.math+self.hindi
        print(total)

m=marks()
m.getstudent()
m.gettest()
m.display()