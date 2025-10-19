#FIBONACCI BASED ON THE N VALUE 

def fib(n):
    if n < 0:
        return[]
    elif n == 1:
        return[0]
    sequence=[0, 1]
    a ,b= 0, 1 

    while len(sequence) < n:
        next_num=a+b
        sequence.append(next_num)
        a, b = b, next_num
    return sequence

if __name__ == "__main__":
    try:
        n= int(input("enter the number: "))
        if n < 0:
            print("enter postive number")
        else:
            res=fib(n)
            print(f"the fibonacci values of {n} is {res}")
    except ValueError:
        print("enter correct input")
