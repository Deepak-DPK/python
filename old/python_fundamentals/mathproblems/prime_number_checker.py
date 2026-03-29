#Prime Number

if __name__ == "__main__":
    num=int(input('enter your number: '))

    for prime in range(2,num):
        if num % prime == 0:
            print(f"{num} is not a prime number")
            break
    else:
        print(f"{num} Is a prime number")
