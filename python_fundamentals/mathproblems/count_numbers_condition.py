# ==================================================
#           COUNT A NUMBER (CONDITION)
# ==================================================

numbers = [10, 55, 8, 92, 101, 43]
# Count how many numbers are greater than 50
count_over_50 = 0
for num in numbers:
    if num > 50:
        count_over_50 = count_over_50 + 1

print(f"There are {count_over_50} numbers greater than 50.")
# Output: There are 3 numbers greater than 50.

# ==================================================
#           COUNT A SPECIFIC ITEM (CONDITION)
# ==================================================

grades = ['A', 'B', 'A', 'C', 'B', 'A']
a_grades = grades.count('A')
print(f"The student received 'A' {a_grades} times.")
# Output: The student received 'A' 3 times.