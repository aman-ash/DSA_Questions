def func(nums):
    N = len(nums)
    count = 0
    for i in range(1, N):
        if nums[i] < nums[i - 1]:
            nums[i - 1] = float("inf")
        else:
            break
            
    temp = []
    for num in nums:
        if num == float("inf"):
            continue
        temp.append(num)
        
    return temp

print(func([2,1,1,5,6,2,3,1]))