# ==================================================
#           REVERSE A STRING USING SLICING 
# ==================================================

def rev_strg(s):
    return s[::-1]

org_str=input()
revstrg=rev_strg(org_str)
print(revstrg)


if org_str == revstrg:
    print(" IT IS A PALINDROME ")
else:
    print("It is not a palindrome ")

# ==================================================
#           REVERSE A STRING USING JOIN 
# ==================================================

def rev_strg(s):
    return "".join(reversed(s))
org_str=input()
res=rev_strg(org_str)
print(res)

