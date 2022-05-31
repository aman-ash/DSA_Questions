def main(arr, i, j):
    memo = [[-1 for _ in range(len(arr))] for _ in range(len(arr))]
    return solve(arr, i, j, memo)


def solve(arr, i, j, memo):
    if i >= j:
        return 0
    if memo[i][j] != -1:
        return memo[i][j]

    ans = float("inf")
    for k in range(i, j):
        temp = solve(arr, i, k, memo) + solve(arr, k+1,
                                              j, memo) + (arr[i-1]*arr[k]*arr[j])
        ans = min(ans, temp)

    memo[i][j] = ans
    return memo[i][j]


if __name__ == '__main__':
    arr = [40, 20, 30, 10, 30]
    print(main(arr, 1, len(arr)-1))
