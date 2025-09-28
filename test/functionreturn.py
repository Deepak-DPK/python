# Problem: Create a function that calculates 
# the area of a rectangle and 
# then use that area to determine the cost of carpeting the room.

def calculate(length, width):
    area_of_rectangle=length * width
    return area_of_rectangle
area=calculate(20,30)
room=5
print(f"area of rectange {area}")
cost_carpet=area * room
print(f"total cost of carpetin the room {room} * {area} is {cost_carpet}")
