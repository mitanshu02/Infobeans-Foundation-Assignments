nums = [-1,-1,1]
k = 0
count = 0
for i in range(len(nums)):
    for j in range(i,len(nums)):
        if i == j:
            if nums[i] == k:
                count += 1
                print("i == j",i,j)
        else:
            if sum(nums[i:j+1]) == k:
                count += 1
                print(i,j)
print(count)