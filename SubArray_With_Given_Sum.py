def MinSum(arr, N, K):
    i = 0
    res = []
    while i < N:
        newArr = arr[i:]
        N = len(newArr)
        temp = solve(arr[i:], K)
        #print(i)
        if temp == -1:
            break
        start, end = temp
        res.append(end - start + 1)
        i = end + 1
    
    if len(res) < 2:
        return -1
    print(res)
    res.sort()
    return res[-1] + res[-2]
 


def solve(arr, k):
    res = []
    curSum = arr[0]
    start = 0
    
    i = start + 1
    while i < len(arr):
        
        while curSum > k and start <i - 1:
            curSum -= arr[start]
            start += 1
            
        if curSum == k:
            res.append(i-1 - start + 1) 
            curSum = 0
        
        if i < len(arr):
            curSum += arr[i]
            i += 1
            
        print(i)
    return res


print(solve([3,2,2,4,3], 3))
            