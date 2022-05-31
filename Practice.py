def main(s1, s2, n, m, memo):
    if n == 0 or m == 0:
        return 0

    if memo[n][m] != -1:
        return memo[n][m]

    if s1[n - 1] == s2[m - 1]:
        memo[n][m] = 1 + main(s1, s2, n - 1, m - 1, memo)
        return memo[n][m]
    memo[n][m] = max(main(s1, s2, n - 1, m, memo),
                     main(s1, s2, n, m - 1, memo))
    return memo[n][m]


def new(s1, s2):
    n, m = len(s1), len(s2)
    memo = [[-1 for i in range(m + 1)] for j in range(n + 1)]
    return main(s1, s2, n, m, memo)


def topDown(s1, s2):
    n, m = len(s1), len(s2)
    memo = [[0 for i in range(m + 1)] for j in range(n + 1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            if s1[i - 1] == s2[j - 1]:
                memo[i][j] = 1 + memo[i - 1][j - 1]
            else:
                memo[i][j] = max(memo[i - 1][j], memo[i][j - 1])
    return memo[n][m]


if __name__ == '__main__':
    s1, s2 = "222222222822222222222222222222433333333332", "8111111111111111142"
    print(new(s1, s2))
    print(topDown(s1, s2))
