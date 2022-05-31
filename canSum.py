def canSumTo(arr, k, memo={}):
    if k in memo:
        return memo[k]
    if k == 0:
        return True
    if k < 0:
        return False

    for num in arr:
        if canSumTo(arr, k - num, memo):
            memo[k] = True
            return True

    memo[k] = False
    return False


if __name__ == '__main__':
    print(canSumTo([7, 14], 3000))
