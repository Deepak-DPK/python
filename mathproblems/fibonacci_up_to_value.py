def fibmax(maxvalue):
    a,b=0,1
    sequence=[]
    while  a<= maxvalue:
        sequence.append(a)
        a, b = b, a+b
    return sequence

if __name__ == "__main__":
    try:
        value=int(input("Enter the value to print upto the:  "))
        if value<0:
            print(f" your {value} is negative enter the only postive numbers")
        else : 
            fibanoci=fibmax(value)
            print(f"the fibanocci numbers upto your {value} is : {fibanoci}")
    except ValueError:
        print("Enter a valid whole number")
