class share:
    def __init__(self, color ,borderwidth):
        self.color=color
        self.borderwidth=borderwidth

    def geter_color(self):
        return self.color
    def set_color(self,color):
        self.color=color

    def geet_borderwidth(self):
        return self.borderwidth
    def set_borderwidth(self,borderwidth):
        self.borderwidth=borderwidth

s=share("red" , 5)
print("color", s.geter_color())
print("borderwidth" , s.geet_borderwidth())

#by set method
s.set_color("blue")
s.set_borderwidth(5)
print("color", s.geter_color())
print("borderwidth" , s.geet_borderwidth())
