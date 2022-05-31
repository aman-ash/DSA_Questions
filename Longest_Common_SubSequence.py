def longestCommonSubsequence(s1, s2):
    memo = {}
    ans = helper(s1, s2, memo)
    return reverse(ans)


def reverse(arr):
    i, j = 0, len(arr) - 1
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
    return arr


def helper(s1, s2, memo):
    n, m = len(s1), len(s2)
    key = str(n) + '.' + str(m)
    if key in memo:
        return memo[key]

    if n == 0 or m == 0:
        memo[key] = []
        return []

    if s1[n - 1] == s2[m - 1]:
        memo[key] = [s1[n - 1]] + helper(s1[:n - 1], s2[:m - 1], memo)
        return memo[key]
    else:
        memo[key] = max(helper(s1, s2[:m - 1], memo),
                        helper(s1[:n - 1], s2, memo))
        return memo[key]


def topDown(s1, s2):
    n, m = len(s1), len(s2)
    memo = [[0 for i in range(m + 1)] for j in range(n + 1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            if s1[i - 1] == s2[j - 1]:
                memo[i][j] = 1 + memo[i - 1][j - 1]
            else:
                memo[i][j] = max(memo[i - 1][j], memo[i][j - 1])
    return printLcs(memo, s1, s2)


def printLcs(memo, s1, s2):
    i, j = len(s1), len(s2)
    lcs = ''
    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            lcs = s1[i - 1] + lcs
            i -= 1
            j -= 1
        else:
            if memo[i - 1][j] > memo[i][j - 1]:
                i -= 1
            else:
                j -= 1
    return lcs


if __name__ == "__main__":
    s1, s2 = "abcdef", "zbfgrdhf"
    print(topDown(s1, s2))
