arr = [10,20,30,40,50]

for i in arr:
    print(i)


for i in range(len(arr)):
    print(f"INDEX {i} -> {arr[i]}")


for i,val in enumerate(arr):
    print(f"Index {i} -> {val}")