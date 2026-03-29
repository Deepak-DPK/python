class BankAccount:
    
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    
    def deposit(self,amount):
        self.balance = self.balance + amount
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
        else:
            print('Insufficient balance')
    
    def display(self):
        print(f"Name : {self.name}")
        print(f"Balance : {self.balance}")

name = input('Enter your Name : ')
Initial_amount = int(input("Enter your amount: "))

b1 = BankAccount(name,Initial_amount)

b1.deposit(100)
b1.withdraw(50)

b1. display()