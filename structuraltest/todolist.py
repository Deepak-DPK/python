# ==================================================
#                  TO-DO LIST
# ==================================================
print("-" * 100)

tasks=["email to boss", "go to gym" , "buy groceries", "call mom"]
print(f"initial list : {tasks}")

print("-" * 100)

#TASK 1 INSERTION
tasks.insert(0,"finish report")
print(f"after insert at 0th position: {tasks}")
print("-" * 100)


#TASK 2 REMOVE IT
tasks.pop(0)
print(f"after removing finish report : {tasks}")
print("-" * 100)

#Task 3 update 

tasks.pop()
tasks.append("call family")
print(f"after poping call mom and inserting call family: {tasks}")
print("-" * 100)

# ==================================================
#                   FINAL SUMMARY
# ==================================================
#final tasks 
print(f"Final updated Tasks ; {tasks}")
print(F"You have left {len(tasks)} tasks to finish")
# ==================================================
