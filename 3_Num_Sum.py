def threeNumberSum(arr, targetSum):
    N = len(arr)
    arr.sort()
    res = []
    for i in range(1, N):
        start, end = 0, N - 1
        
        while start < i and end > i: 
            curSum = arr[start] + arr[i] + arr[end]
            
            if curSum > targetSum:
                end -= 1
            
            elif curSum < targetSum:
                start += 1
            
            else:
                temp = [arr[start], arr[i], arr[end]]
                temp.sort()
                res.append(temp)
                break
                
        return res
    
    
if __name__ == '__main__':
    arr = [12, 3, 1, 2, -6, 5, -8, 6]
    tar = 0
    print(threeNumberSum(arr, 0))

