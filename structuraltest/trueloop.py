items=[]
while True:
    item = input("enter your items(if you added enough item please give done): ")
    if item.lower()=="done":
       break
    items.append(item)
print("\nHere are the items you entered:")
for item in items:
    print(f"- {item}")