#inventory management system 
# Problem Statement: Inventory Management 🛒
# You are managing the inventory for a small electronics store. 
# Your inventory is stored in a Python list. 
# You need to perform a series of updates based on a day's transactions.

"""Tasks to Perform:

New Stock: A new shipment of "headphones" has arrived. Add this item to the end of your inventory list.

Item Sold: A customer bought the "keyboard". Remove this item from the inventory list.

Stock Check: A customer asks if you have a "monitor" in stock. Check if "monitor" is in the list and print one of the following messages:

"Yes, we have the monitor in stock."

"Sorry, the monitor is out of stock."

Final Count: At the end of the day, you need to know how many different types of items are in your inventory. 
Print a final message that says:
       "We have X items in our inventory." (where X is the total number of items).

Your goal is to write a single Python script that performs these four tasks in order and prints the required output."""


inventory = ["laptop","mouse" ,"keyboard","monitor","webcam"]

#add headphones end of the list
inventory.append("headphones")
print(f"After adding headphones: {inventory}")

#remove keyboard
inventory.remove("keyboard")
print(f"after sold item (keyboard): {inventory}")

#check stock for monitor
if "monitor" in inventory:
    print("Yes, we have the monitor in stock.")
else:
    print("SORRY , the monitor is out of stock ")

#final count 
print(f"the count of items in inventory is {len(inventory)}")

#final
print(f"we have {len(inventory)} in the inventory")