
# Problem: Create a function that calculates the area of a rectangle 
# and then use that area 
# to determine the cost of carpeting the room.

def calculate_area(length, width):
    """Calculates the area of a rectangle."""
    area = length * width
    return area  # Send the calculated area back to the program

# --- Main part of the script ---

room_length = 12  # in feet
room_width = 10   # in feet
cost_per_sq_foot = 5  # in dollars

room_area = calculate_area(room_length, room_width)  # Call the function and store the returned value

total_cost = room_area * cost_per_sq_foot  # Use the returned value in a new calculation

print(f"The area of the room is {room_area} square feet.")  # Print the final results for the user
print(f"The total cost to carpet the room is ${total_cost}.")
