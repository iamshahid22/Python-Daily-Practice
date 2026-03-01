class Account:
    def __init__(self, balance):
        self.__balance = balance   # private variable

    def get_balance(self):
        return self.__balance

a1 = Account(10000)
print(a1.get_balance())