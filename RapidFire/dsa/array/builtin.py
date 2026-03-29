arr =  [30, 10, 50, 20, 40]

arr.sort()
print(arr)

arr.sort(reverse=True)
print(arr)

print(min(arr))


# Check if value exists
print(20 in arr)       # True
print(99 in arr)       # False

# Count occurrences
arr = [1, 2, 2, 3, 2]
print(arr.count(2))    # 3

# Clear list
arr.clear()
print(arr)             # []