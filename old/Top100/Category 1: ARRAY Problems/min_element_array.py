arr1=[12, 4, -2, 99, 18, -7]

min_value = arr1[0]

for num in arr1:
    if num < min_value:
        min_value = num

print(min_value)



"-----------------------------------------------------------------------"



def minimum_value(arr):
    min_value = arr[0]

    for num in arr:
        if num < min_value:
            min_value = num
    return min_value

arr = [2,3,4,9,6,8,3,1]
print(minimum_value(arr))



