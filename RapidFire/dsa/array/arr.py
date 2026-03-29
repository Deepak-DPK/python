arr = [10, 20, 30, 40, 50]

# 2. Accessing Elements
print(arr[0])   # 10 → first element
print(arr[-1])  # 50 → last element
print(arr[-2])  # 40 → second from last

# 3. Slicing
print(arr[1:3])  # [20, 30] → index 1 to 2
print(arr[:3])   # [10, 20, 30] → first 3
print(arr[2:])   # [30, 40, 50] → from index 2 onwards

# 4. Modifying a List


# Change a value
arr[0] = 100
print(arr)  # [100, 20, 30, 40, 50]

# Add to end
arr.append(60)
print(arr)  # [100, 20, 30, 40, 50, 60]

# Insert at specific position
arr.insert(1, 999)
print(arr)  # [100, 999, 20, 30, 40, 50, 60]

# Remove by value
arr.remove(999)
print(arr)  # [100, 20, 30, 40, 50, 60]

# Remove by index
arr.pop(0)
print(arr)  # [20, 30, 40, 50, 60]