# ===================================================================
# Example 1: `continue` - Skipping Invalid Data in a List
# ===================================================================
print("--- Example 1: Skipping Invalid Scores with `continue` ---")
scores = [85, 92, -15, 78, -10, 95]
total_score = 0

for score in scores:
    if score < 0:
        print(f"Skipping invalid score: {score}")
        continue  # Skip to the next score
    
    total_score += score
    print(f"Added score: {score}")

print(f"\nTotal score of valid entries: {total_score}\n")


# ===================================================================
# Example 2: Combining `break` and `continue` - Processing Orders
# ===================================================================
print("--- Example 2: Processing Orders with `break` and `continue` ---")
orders = ["standard", "empty", "standard", "gold", "express", "empty"]

for order in orders:
    if order == "empty":
        print("-> Skipping an empty order.")
        continue  # Go to the next order

    print(f"Processing a '{order}' order...")

    if order == "gold":
        print("! Found a high-priority 'gold' order. Stopping all processing.")
        break  # Exit the loop entirely

print("\nOrder processing has finished.\n")


# ===================================================================
# Example 3: `break` - Stopping a `while` Loop with User Input
# ===================================================================
# Note: This example is commented out because it will run an infinite
# loop and prevent the script from finishing. 
# To test it, you can uncomment the lines below and run the file.
# ===================================================================
#
print("--- Example 3: Exiting a `while` loop with `break` ---")
print("This loop will run until you type 'quit'.")

while True:
    user_input = input("Enter a command: ")
    if user_input.lower() == "quit":
        print("Exiting the program. Goodbye!")
        break
    print(f"You entered: {user_input}")