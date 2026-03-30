class Automobile:

    NO_OF_GEAR=6

    def __init__(self):
        self.__color=None
        self.__speed=0
        self.__make=None

    def get_color(self):
        return self.__color
    def set_color(self, color):
         self.__color=color
    def get_speed(self):
        return self.__speed
    def set_speede(self, speed):
         self.__speed=speed
    def get_make(self):
        return self.make
    def set_make(self, make):
         self.__make=make


    #brek
    def  brake(self):
        if self.__speed==0:
            print("stop")
        else:
            self.__speed -= 10
            print("speed", self.__speed)

    # accelarate

    def accelarte(self):
        if self.__speed>= 200:
            print("high speed ")
        else:
            self.__speed+=10
            print(self.__speed)


    #gear method

    def gear(self,gear):
        if gear > Automobile.NO_OF_GEAR:
            print("invalid gear")
        elif gear == 1:
            print("1")
            self.__speed = 20
            print(self.__speed)

car=Automobile()
car.set_color("Red")
car.set_make("BMW")

car.accelarte()
car.brake()
car.gear(1)