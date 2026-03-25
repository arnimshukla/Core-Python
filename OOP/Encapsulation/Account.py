class Account:
    def __init__(self):
        self.__number = None
        self.__accunttype = None
        self.__balance = 0.0

    def get_number(self):
        return self.__number

    def set_number(self, number):
        self.__number = number

    def get_accunttype(self):
        return self.__accunttype

    def set_accunttype(self, accunttype):
        self.__accunttype = accunttype

    def get_balance(self):
        return self.__balance

    def set_balance(self, balance):
        self.__balance= balance

acc=Account()
acc.set_number("123344")
acc.set_accunttype("saving")
acc.set_balance(12345)
print(acc.get_number())
print(acc.get_accunttype())
print(acc.get_accunttype())




