# Write a program that prints the multiplication table of any number the user enters.

n=int(input("Enter the number: "))

for i in range(1,13):
    
    mul = i * n
    print(f"{i} * {n} = {mul}")
    