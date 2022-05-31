def howSum(arr, k,):
    arr.sort(reverse=True)
    return helper(arr, k, memo={})


def helper(arr, k, memo):
    if k in memo:
        return memo[k]
    if k == 0:
        return []
    if k < 0:
        return None

    best = None
    for num in arr:
        remainder = k - num
        new = helper(arr, remainder, memo)
        if new is not None:
            current = [*new, num]
            if best is None or len(current) < len(best):
                best = current

    memo[k] = best
    return best


if __name__ == '__main__':
    test = [1, 2, 3, 4, 5, 25, 100, 1000]
    result = howSum(test, 10000)
    print(result)
    print(len(result))
