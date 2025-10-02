def last_number(number):
    if number == 0:
        return 0
    pos_num=abs(number)
    fnum = number % 10
    return fnum
try:
    number=int(input("enter your number: "))
    res=last_number(number)
    print(f"the last digit of {number} is {res}")
except ValueError:
    print(f"enter valid whole number")