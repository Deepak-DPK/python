def fibmax(maxval):
    a,b = 0, 1 
    sequence =[]
    while a <=maxval:
        sequence.append(a)
        a , b = b, a+b
    return sequence

try:
    val=int(input("enter the value : "))
    if val < 0:
        print("the value should be in positive numbers ")
    else:
        result = fibmax(val)
        print(f"the fibnocci value of {val} is {result} ")
except ValueError:
    print("Enter the whole number ")