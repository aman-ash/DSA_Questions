def topDown(s1, s2):
    n, m = len(s1), len(s2)
    ans = 0
    memo = [[0 for i in range(m + 1)] for j in range(n + 1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            if s1[i - 1] == s2[j - 1]:
                memo[i][j] = 1 + memo[i - 1][j - 1]
            else:
                memo[i][j] = 0
            ans = max(ans, memo[i][j])
    print(memo)
    return ans


if __name__ == "__main__":
    s1, s2 = 'abcdf', 'abdef'
    n, m = len(s1), len(s2)
    print(topDown(s1, s2))
