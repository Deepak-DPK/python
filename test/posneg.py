numbers = [1, -2, 3, -4, 5, 0, 7, -8, 9]
"""
Filter negative numbers from a list using a loop.

This script demonstrates how to extract all negative numbers from a mixed list
of integers using Python's for loop.

Process:
1. Create a list containing positive, negative, and zero values
2. Initialize an empty list to store negative numbers
3. Use a for loop to iterate through each number
4. Check if each number is negative (num < 0) and append to result list
5. Display the negative numbers found

Expected Output:
[-2, -4, -8]

Note: Zero is not considered negative, so it won't be included in the result.
"""
negative_numbers = []
for num in numbers:
    if num < 0:
        negative_numbers.append(num)

print(negative_numbers)