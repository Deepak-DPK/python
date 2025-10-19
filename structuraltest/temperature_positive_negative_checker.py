# Simple positive/negative checker
temperatures = [25, -5, 10, -15, 0, 8, -2]

for temp in temperatures:
    if temp > 0:
        print("positive")
    elif temp < 0:
        print("negative")
    else:
        print("zero")