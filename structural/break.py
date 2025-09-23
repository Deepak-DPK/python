# A list of lottery ticket numbers to check
ticket_numbers = [101, 432, 591, 12, 988, 555, 764]
winning_number = 988

print(f"Searching for winning ticket: {winning_number}...")

# Loop through each ticket in the list
for ticket in ticket_numbers:
    print(f"Checking ticket #{ticket}...")
    
    # If the current ticket is the winner, stop the search
    if ticket == winning_number:
        print("🎉 We found the winning ticket!")
        break # Immediately exit the loop

print("\nThe search is complete.")