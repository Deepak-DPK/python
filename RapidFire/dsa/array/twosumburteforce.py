# # Given a list of numbers and a target, find two numbers that add up to the target and return their indices.

# Input:  arr = [2, 7, 11, 15], target = 9
# Output: [0, 1]  → because arr[0] + arr[1] = 2 + 7 = 9

# Constraints to know:

# Each input has exactly one solution
# You cannot use the same element twice

arr = [2, 7, 11, 15]
target = 9
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
            if arr[i]+arr[j]==target:
                print ([i,j])

