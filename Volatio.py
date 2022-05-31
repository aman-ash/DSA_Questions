def canSum(arr, K):
    if K == 0:
        return True
    
    for i in range(len(arr)):
        remain = K - arr[i]
        if canSum(arr[:i]+ arr[i+1:], remain):
            return True

    return False

def findElements(N, A):
    result = [A[0]]
    for i in range(1, N):
        if canSum(result, A[i]):
            continue
        result.append(A[i])
    return result

   

def powerOfTwo(A):
    result = 0
    low = 0
    high = A
    
    while low <= high:
        mid = (low + high) // 2
        cur = 2 ** mid
        
        if cur <= A:
            result = mid
            low = mid + 1
        
        else:
            high = mid - 1
    
    
    return result + 1 if cur * 2  <= A else result - 1 if cur > A else result


A = [1, 2, 3, 4, 5, 6, 7, 8]
print(findElements(len(A),A))