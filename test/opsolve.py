"""problem statement
u have an amount add 18% gst tax to  the amount and 10 percent discount to total  amount with tax
"""

amount = 1200
tax= amount * 0.18
total = amount + tax
print(total)

if total > 1000:
    discount=total * 0.10
    total=total-discount
print(total)