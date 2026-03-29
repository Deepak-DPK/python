def fact(n):
    if n<0:
        return "enter positive number"
    elif n==0:
        return 1
    else:
        result=1
        for i in range(1,n+1):
            result =result * i
        return result

if __name__ == "__main__":
    num=int(input("Enter the number: "))
    faq = fact(num)
    print(f"the factorial of {num} is {faq}")
