# using try block find odd or even

if __name__ == "__main__":
    number=int(input("enter your number: "))

    try:
        if number%2==0:
            print(f"{number} is even number")
        else:
            print(f"{number} is odd number")
    except ValueError:
        print("enter a valid number")
