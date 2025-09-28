def return_add(a, b):
    result = a + b
    return result # Sends the result back to the code that called it

# Call the function and store the returned value
print("--- Using the return_add function ---")

r = return_add(5, 3)

# Now we can use the returned value for something else
print(f"The value of r is: {r}")
new_calculation = r * 10
print(f"We can use r in a new calculation: {r} * 10 = {new_calculation}")