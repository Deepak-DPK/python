n = input()

i = 0
j = len(n) - 1

is_palindrome = True

while i < j:
    if n[i] == n[j]:
        i+=1
        j-=1
    else:
        is_palindrome = False
        break


if is_palindrome:
    print("Valid Palindrome")
else:
    print("not a valid palindrome")