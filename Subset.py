def subset(arr, s, n):
    if s == 0:
        return True
    if n == 0:
        return False

    if arr[n - 1] <= s:
        return subset(arr, s - arr[n - 1], n - 1) or subset(arr,  s, n - 1)

    return subset(arr,  s, n - 1)


if __name__ == '__main__':
    arr = [1, 59, 6, 8]
    s = 64
    print(subset(arr, s, len(arr)))
