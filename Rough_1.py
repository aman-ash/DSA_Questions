def first(arr):
    arr.sort()
    pair = []
    i, j = 0, len(arr) - 1
    while i < j:
        curSum = arr[i] + arr[j]
        if curSum > 2:
            j -= 1
        
        elif curSum < 2:
            i += 1
        
        else:
            pair.append([arr[i], arr[j]])
            i += 1
            j -= 1
            
    return pair


def second(arr):
    pair = []
    A = set()
    for num in arr:
        if 2 - num in A:
            pair.append([num, 2 - num])
        A.add(num)
    return pair
            
    

arr = [-2, -1, 4, -5, 3, 7]
print(first(arr))
print(second(arr))