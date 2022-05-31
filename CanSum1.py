def canSum(arr, target, n, ans):
    if n == 0:
        return

    if target == 0:
        ans[0] += 1
        return
    
    if arr[n - 1] <= target:
        canSum(arr, target - arr[n - 1], n, ans)
        canSum(arr, target ,n-1, ans)
    
    else:
        canSum(arr, target ,n-1, ans)
        
    return ans[0]




if __name__ == '__main__':
    ans = [0]
    print(canSum([1,5], 6, 2, ans))
