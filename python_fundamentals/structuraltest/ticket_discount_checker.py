def check_discount():
    age=int(input("Enter your age : "))
    student=input("Are you student ? : ")

    if age>61 or student=="yes":
        print("your eligible for the discount")
    else:
        print("your are not eligble")

if __name__ == '__main__':
    check_discount()
