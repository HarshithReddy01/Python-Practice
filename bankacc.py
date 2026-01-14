class InsufficientFundsEror(Exception):
    pass

class BankAccount:
    acc_counter = 100

    def __init__(self, name, balance=0):
        BankAccount.acc_counter += 1
        self.__acc = BankAccount.acc_counter
        self.name = name
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            raise InsufficientFundsEror("Not Enough Funds you rokiee")
        
    def get_balance(self):
        return self.__balance
    
    def details(self):
        return self.__acc, self.name, self.__balance
    


Harshith = BankAccount('Harshith', 100000)
Reddy = BankAccount('Reddy', 1000055555)
print(Harshith.details(), '\n', Reddy.details())


