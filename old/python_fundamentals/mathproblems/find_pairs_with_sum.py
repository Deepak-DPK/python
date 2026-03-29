num=[2,6,4,7,9]
target=11
targeted_pairs=[]

for i in range(len(num)):
    for j in range (i+1, len(num)):
        if num[i] + num[j]==target:
            targeted_pairs.append((num[i], num[j]))

print(f"the target {target} of the pairs are {targeted_pairs}")