arr = [2, 9, 5, 7, 6]
target = 8
seen = {}


for i in range(len(arr)):
    comp = target - arr[i]
    if comp in seen:
        print([seen[comp],i])
    else:
        seen[arr[i]] = i