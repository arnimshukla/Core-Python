


class InsufficientFundException(Exception):
    def __int__(self,msg):
        super().__init__(msg)

class Account:
    def __init__(self):
        self.balance=0
        self.count=0

    def set_balance(self,balance):
        self.balance=balance
    def get_balance(self):
        return self.balance
    def deposit(self,amount):
        self.balance +=amount
        print(f"Deposite:{amount},Currebt balance{self.balance}")
    def withdraw(self,amount):
        if amount>10000:
            raise InsufficientFundException("CAN'T WITHDRAW MORE THAN 10000")
        if self.count >= 2:
            return InsufficientFundException("cant withdraw more than 3 times")
        if self.balance-amount>=200:
            self.balance-=amount
            self.count +1
            print(f"Withdraw:{amount},remanng balance:{self.balance}")
        else:
            raise InsufficientFundException("Insufficient balance. Minimum ₹2000 must remain in the account.")

acc=Account()
acc.set_balance(5000)

try:
    acc.deposit(1000)
    acc.withdraw(3500)

except InsufficientFundException as  e:
    print("exception",e)