"""Create a class called BankAccount:

Class variable → bank_name = "SBI Bank"

Inside __init__(): take name and balance

Add:

An instance method show_details() → prints account info

A class method change_bank(cls, new_bank) → updates bank name

A static method bank_policy() → prints "Minimum balance must be ₹1000."

Create two accounts and demonstrate all three types of methods."""

class BankAccount:
    bank_name = "SBI Bank"

    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    
    def show_details(self):
        print(f"Account holder name:{self.name}, Acc Bal : {self.balance}, Bank Name : {BankAccount.bank_name}")
    
    @classmethod
    def change_bank(cls,new_bank):
        cls.bank_name=new_bank
    
    @staticmethod
    def bank_policy():
        print("Minimum balance must be  ₹1000")

acc1=BankAccount("ramesh",2000)
acc2=BankAccount("suresh",4000)

acc1.show_details()
acc2.show_details()

BankAccount.bank_policy()

print("------------After bank change----------------------")

BankAccount.change_bank("Canara Bank")

acc1.show_details()
acc2.show_details()

    