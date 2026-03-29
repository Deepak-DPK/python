# Write a program to calculate the sum of digits of a number (e.g., 123 → 6).



total = 0
n=int(input())
while n != 0:
    l = n%10
    total= total + l
    n=n//10
print(total)

