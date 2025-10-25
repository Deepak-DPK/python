#🧩 Step 2: for Loop – The Workhorse Loop

#📘 Syntax:
"""for variable in sequence:"""
# “sequence” can be:

# a list ([1,2,3])

# a string ("hello")

# a range (range(5))


#Example 1:
#PRINT 1 TO 5

for i in range(1,6):    #it prints from 1 to 5 not includes 6
    print(f"The sequence {i} is no :  {i}") 



print("*****************************************************************************")

print("-----🧺 Example 2 Super market billing------------")
# 🧺 Example 2 – Real World: Supermarket Billing

# Let’s say a supermarket has prices of items in a list:

prices=[20,40,50,24,35]
total=0
for price in prices:
    total +=price
print(f"The total prices of the bill : {total}")




print("*****************************************************************************")

print("-----🎵 Example 3 – Sending Personalized Emails----------")

name=["Deepak","Srinath","ramesh"]
for i in name:
    print(f"hello {i} nice to meet you")




print("*****************************************************************************")
print("Print all numbers from 10 to 1 (in reverse)")

#print reverse 

num=10
for i in range(10,0,-1):
    print(f"The reverse {i}")


print("*****************************************************************************")
print("Print the square of numbers from 1 to 5.")

for i in range(1,6):
    square=i*2  # or i * i
    print(square)

