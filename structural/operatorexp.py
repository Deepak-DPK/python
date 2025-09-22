#arithmetic operators 
a=2
b=3
print(a+b) #add
print(a-b) #sub
print(a*b) #mul
print(a/b) #div  results quotient
print(a ** b)  #2*2*2
print(a  % b)  #modulus results remainder
print(a // b)  # result quotient in whole number 


print("-------------------------------------------------------------------------")

#comparison operators 

print(a == b)
print(a != b)
print(a > b)
print(a < b)

print("-------------------------------------------------------------------------")
#logical operators 
print("AND OPERATOR")
#and 
age = 20
has_license = True

# Let's check the conditions
if age >= 18 and has_license == True:
    print("You are eligible to drive.")
else:
    print("You are not eligible to drive.")

print("\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")

#or
print("OR OPERATOR")

day = "Sunday"

# Let's check if it's the weekend
if day == "Saturday" or day == "Sunday":
    print("It's the weekend! Time to relax. 🥳")
else:
    print("It's a weekday. Back to work.")

print("\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")

#not 
print("NOT OPERATOR")

is_admin = False

# The 'not' operator flips the value of is_admin
# from False to True, so the 'if' condition passes.

if not is_admin:
    print("Welcome, valued user! Thank you for visiting.")
else:
    print("Welcome, Admin. Here is the control panel link.")
