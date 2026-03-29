
arr=[12, 4, -2, 99, 18, -7]

max_val = arr[0]

for num in arr:
    if num > max_val:
        max_val = num

print(max_val)


"----------------------------------------------------------------------------------------"

def highest_element(arr):
    max_val = arr[0]

    for num in arr:
        if num > max_val:
            max_val = num
    return max_val

arr=[12, 4, -2, 99, 18, -7]

print(highest_element(arr))
