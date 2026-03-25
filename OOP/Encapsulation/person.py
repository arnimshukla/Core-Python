from datetime import datetime


class person:
    avg_age = 18

    def __init__(self):
        self.__name = None
        self.__dob = None
        self.__address = None

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_dob(self):
        return self.__dob

    def set_dob(self, dob):
        self.__dob = dob

    def get_address(self):
        return self.__address

    def set_address(self, address):
        self.__address = address

    def get_age(self):
        if self.__dob is None:
            return None

        now = datetime.now()
        age = now.year - self.__dob.year
        return age


p = person()
p.set_name("arnim")
p.set_dob(datetime(2020, 2, 28))
p.set_address("indore")

print("name=", p.get_name())
print("age=", p.get_age())
print("address=", p.get_address())
