# if elif else statemets

marks=86

if marks >90:
    print("grade A")
elif marks >80:
    print("grade B")
elif marks >70:
    print("grade c")
elif marks >60:
    print("grade d")
else:
    print("grade fail")


#nested if statement 

age=22
licensegot="yes"

if age>18:
    if licensegot=="yes":
        print("you are eligible")
    else:
        print("getlicense")
else:
    print("your are not eligble")
