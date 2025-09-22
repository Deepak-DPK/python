"""problem statement
u have an amount discount 18% gst tax to  the amount and 10 percent to total amount 
"""

amount = 1200
tax= amount * 0.18
total = amount + tax

if total > 1000:
    discount=total * 0.10
    total=total-discount
print(total)