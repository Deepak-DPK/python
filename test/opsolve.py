"""problem statement
u have an amount discount 10 percent of the amount and gst of 18 percent to that amount 
"""

amount = 1200
tax= amount * 0.18
total = amount + tax

if total > 1000:
    discount=total * 0.10
    total=total-discount
print(total)