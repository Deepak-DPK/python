# ============================================
# 1. Arithmetic Operators
# ============================================
# These operators perform mathematical calculations.

print("--- 1. Arithmetic Operators ---")
a = 2
b = 3

print(f"{a} + {b} = {a + b}")          # Addition
print(f"{a} - {b} = {a - b}")          # Subtraction
print(f"{a} * {b} = {a * b}")          # Multiplication
print(f"{a} / {b} = {a / b}")          # Division (results in a float)
print(f"{a} ** {b} = {a ** b}")         # Exponent (a to the power of b)
print(f"{a} % {b} = {a % b}")          # Modulus (remainder of a division)
print(f"{a} // {b} = {a // b}")         # Floor Division (quotient as a whole number)
print("\n") # Adds a blank line for spacing

# ============================================
# 2. Comparison Operators
# ============================================
# These operators compare two values and return a Boolean (True or False).

print("--- 2. Comparison Operators ---")
print(f"Is {a} equal to {b}? \t\t{a == b}")
print(f"Is {a} not equal to {b}? \t\t{a != b}")
print(f"Is {a} greater than {b}? \t\t{a > b}")
print(f"Is {a} less than {b}? \t\t{a < b}")
print("\n")

# ============================================
# 3. Logical Operators
# ============================================
# These operators combine conditional statements.

print("--- 3. Logical Operators ---")

# Example for 'and'
print("AND Operator Example:")
age = 20
has_license = True
if age >= 18 and has_license: # '== True' is redundant
    print("Result: You are eligible to drive.")
else:
    print("Result: You are not eligible to drive.")
print("-" * 20) # A simple separator

# Example for 'or'
print("OR Operator Example:")
day = "Sunday"
if day == "Saturday" or day == "Sunday":
    print("Result: It's the weekend! Time to relax. 🥳")
else:
    print("Result: It's a weekday. Back to work.")
print("-" * 20)

# Example for 'not'
print("NOT Operator Example:")
is_admin = False
if not is_admin:
    print("Result: Welcome, valued user! Thank you for visiting.")
else:
    print("Result: Welcome, Admin. Here is the control panel link.")
