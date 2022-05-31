def reverse_words(arr):
    N = len(arr)
    reverse(arr, 0, N - 1)
    startIdx = None

    for i in range(N):
        temp = arr[i].strip()
        if temp == '':
            if startIdx is not None:
                reverse(arr, startIdx,  i - 1)
                startIdx = None

        elif i == N - 1:
            if startIdx:
                reverse(arr, startIdx, i)

        else:
            if startIdx == None:
                startIdx = i

    return arr
     

def reverse(A, i, j):
    while i < j:
        A[i], A[j] = A[j], A[i]
        i += 1
        j -= 1
    return
  
if __name__ == '__main__':
    arr = [ 'p', 'e', 'r', 'f', 'e', 'c', 't', ' ',
            'm', 'a', 'k', 'e', 's', ' ',
            'p', 'r', 'a', 'c', 't', 'i', 'c', 'e' ]
    print(reverse_words(arr))

