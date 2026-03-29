

# Take a string as input and print it reversed using a loop.


s = input()

res = ""

for i in range(len(s)-1,-1,-1):
    res = res + s[i]
    
print(res)