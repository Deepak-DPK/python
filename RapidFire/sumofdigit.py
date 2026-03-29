# Write a program to calculate the sum of digits of a number (e.g., 123 → 6).
# Take a string as input and print it reversed using a loop.
# Write a program that prints the multiplication table of any number the user enters.

# total = 0
# n=int(input())
# while n != 0:
#     l = n%10
#     total+= l
#     n//=10
# print(total)


s = input()

res = ""

for i in range(len(s)-1,-1,-1):
    res = res + s[i]

print(res)