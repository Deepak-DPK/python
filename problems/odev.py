# using try block find odd or even

input=int(input("enter your number"))

try:
    if input%2==0:
        print(f"{input} is even number")
    else:
        print(f"{input} is odd number")

except ValueError:
    print("enter a valid number ; ")