def solve(arr):
    ans = [-1]
    stack = [arr[-1]]
    for i in reversed(range(len(arr) - 1)):
        flag = False
        while len(stack):
            if stack[-1] < arr[i]:
                ans.append(stack[-1])
                flag = True
                break
            else:
                stack.pop()
        if not flag:
            ans.append(-1)
        stack.append(arr[i])
    ans.reverse()
    return ans


def new(nums):
    stack = []
    n = len(nums)
    nums = nums+nums[:-1]
    res = [-1]*len(nums)
    for i, num in enumerate(nums):
        while stack and nums[stack[-1]] < num:
            res[stack.pop()] = num
        stack.append(i)
    
    d = []
    for i in range(len(nums)):
        d.append(res[i] - nums[i])
    return d[:n]

print(new([1,4,3,8]))