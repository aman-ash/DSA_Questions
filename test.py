def solution(arr):
    n = len(arr)
    i = 0
    count = 1
    while count <= n:
        if arr[i] < 0:
            tmp = arr.pop(i)
            arr.append(tmp)
        else:
            i += 1
        count += 1
    return arr


if __name__ == '__main__':
    A = list(map(int, input().strip().split()))
    print(solution(A))
