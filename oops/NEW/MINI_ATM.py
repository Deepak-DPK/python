class ATMAccount:
    def __init__(self, name, pin, balance):
        self.name = name
        self.__pin = pin
        self.__balance = balance

    def authenticate(self, entered_pin):
        return entered_pin == self.__pin
    
    def check_balance(self):
        return self.__balance
    
    def withdraw(self, amount, entered_pin):
        if not self.authenticate(entered_pin):
            return "Invalid PIN"
        
        if amount <= self.__balance:
            self.__balance -= amount
            return "Withdraw Successful"
        else:
            return "Insufficient Balance"


# ---- Input Section ----
name = input("Enter your Name: ")
pin = int(input("Set your PIN: "))
balance = int(input("Enter initial balance: "))

# ---- Object Creation ----
s1 = ATMAccount(name, pin, balance)

# ---- Transaction ----
entered_pin = int(input("Enter PIN to withdraw: "))
amount = int(input("Enter withdraw amount: "))

print(s1.withdraw(amount, entered_pin))
print("Current Balance:", s1.check_balance())
