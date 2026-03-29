# Write a program that takes a number and prints whether it's even or odd.

n = int(input("Enter a Number: "))

def oddeven(n):
    if n%2==0:
        print(f"{n} is even number")
    else:
        print(f"{n} is odd number")

oddeven(n)

