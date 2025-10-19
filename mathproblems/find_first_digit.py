def first_num(number):
    if number == 0 :
        return 0
    positive_number=abs(number)
    while positive_number >=10:
        positive_number=positive_number//10
    return positive_number

if __name__ == "__main__":
    try:
        num=int(input("enter the number; "))
        res=first_num(num)
        print(f"the first of the {num} is {res}")
    except ValueError:
        print(f"enter the whole number: ")
