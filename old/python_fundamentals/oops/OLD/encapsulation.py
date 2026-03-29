#In Python:

# __var → Private (not directly accessible outside the class)

# _var → Protected (used by subclasses, not external users)


class BankAccount:
    def __init__(self,name,balance):
        self.name=name
        self.__balance=balance
    def deposit(self,amount):
        self.__balance += amount

    def withdraw(self,amount):
        if amount <=self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance")
    
    def show_balance(self):
        print(f"Account Holder Name: {self.name}, Account Balance amount: {self.__balance}")

Acc1=BankAccount("DEEPAK",25000)
Acc1.show_balance()

print("AFter deposit")
Acc1.deposit(2000)

Acc1.show_balance()


print("AFter withdrawl")

Acc1.withdraw(1200)

Acc1.show_balance()


# print(Acc1.__balance)  # IT WONT WORK BECAUSE PRIVATE WE CANT CALL DIRECTLY
