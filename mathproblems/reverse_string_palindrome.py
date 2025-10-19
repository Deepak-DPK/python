# ==================================================
#           REVERSE A STRING USING SLICING 
# ==================================================

def rev_strg(s):
    return s[::-1]

if __name__ == "__main__":
    org_str=input("Enter a string: ")
    revstrg=rev_strg(org_str)
    print(revstrg)

    if org_str == revstrg:
        print(" IT IS A PALINDROME ")
    else:
        print("It is not a palindrome ")

    # ==================================================
    #           REVERSE A STRING USING JOIN 
    # ==================================================

    def rev_strg_join(s):
        return "".join(reversed(s))
    
    org_str2=input("Enter another string: ")
    res=rev_strg_join(org_str2)
    print(res)
